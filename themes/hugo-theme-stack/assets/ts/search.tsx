type PageType = 'post' | 'term' | 'guide';

interface PictureData {
    src: string;
    srcset: string;
    type: string;
    width: number;
    height: number;
}

interface PageData {
    title: string;
    date: string;
    permalink: string;
    content: string;
    type: PageType;
    names?: string[];
    image?: PictureData;
}

interface IndexedPage extends PageData {
    normalizedTitle: string;
    normalizedContent: string;
    normalizedNames: string[];
}

interface SearchResult {
    page: IndexedPage;
    tier: number;
    titleHits: number;
    hits: number;
}

interface SearchElements {
    form: HTMLFormElement;
    input: HTMLInputElement;
    list: HTMLDivElement;
    status: HTMLParagraphElement;
    empty: HTMLElement;
    recovery: HTMLElement;
}

function normalize(text: string): string {
    return text.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().trim().replace(/\s+/g, ' ');
}

function queryTokens(query: string): string[] {
    return Array.from(new Set(normalize(query).split(/[^\p{L}\p{N}]+/u).filter(token => Array.from(token).length > 1)));
}

/** Keep accent-insensitive matches aligned with the original, unescaped text. */
function highlight(element: HTMLElement, text: string, tokens: string[]): void {
    let folded = '';
    const starts: number[] = [], ends: number[] = [];
    let position = 0;
    for (const character of text) {
        const value = character.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
        for (let i = 0; i < value.length; i++) {
            starts.push(position);
            ends.push(position + character.length);
        }
        folded += value;
        position += character.length;
    }
    const ranges: Array<{ start: number; end: number }> = [];
    for (const token of tokens) {
        let from = 0;
        let index: number;
        while ((index = folded.indexOf(token, from)) !== -1) {
            ranges.push({ start: starts[index], end: ends[index + token.length - 1] });
            from = index + token.length;
        }
    }
    ranges.sort((a, b) => a.start - b.start);
    let cursor = 0;
    for (let i = 0; i < ranges.length; i++) {
        const range = ranges[i];
        while (i + 1 < ranges.length && ranges[i + 1].start <= range.end) {
            range.end = Math.max(range.end, ranges[++i].end);
        }
        element.append(document.createTextNode(text.slice(cursor, range.start)));
        const mark = document.createElement('mark');
        mark.textContent = text.slice(range.start, range.end);
        element.append(mark);
        cursor = range.end;
    }
    element.append(document.createTextNode(text.slice(cursor)));
}

class Search {
    private readonly elements: SearchElements;
    private dataPromise?: Promise<IndexedPage[]>;
    private revision = 0;
    private settledTimer?: number;
    private lastSettledQuery = '';

    constructor(elements: SearchElements) {
        this.elements = elements;
        elements.input.addEventListener('input', event => {
            // Do not search a partly composed IME query; still invalidate any pending result.
            if ((event as InputEvent).isComposing) {
                this.revision++;
                window.clearTimeout(this.settledTimer);
                return;
            }
            this.searchInput(false);
        });
        elements.input.addEventListener('compositionend', () => this.searchInput(false));
        elements.form.addEventListener('submit', event => {
            event.preventDefault();
            this.searchInput(true);
        });
        window.addEventListener('popstate', () => this.handleQueryString());
        if (elements.input.value.trim()) {
            void this.doSearch(elements.input.value.trim());
        } else {
            this.handleQueryString();
        }
    }

    public getData(): Promise<IndexedPage[]> {
        if (!this.dataPromise) {
            const jsonURL = this.elements.form.dataset.json;
            if (!jsonURL) return Promise.reject(new Error('Missing search index URL'));
            this.dataPromise = fetch(jsonURL).then(response => {
                if (!response.ok) throw new Error('Search index unavailable');
                return response.json() as Promise<PageData[]>;
            }).then(pages => pages.map(page => ({
                ...page,
                normalizedTitle: normalize(page.title),
                normalizedContent: normalize(page.content),
                normalizedNames: (page.names || []).map(normalize)
            })));
        }
        return this.dataPromise;
    }

    private async searchKeywords(query: string, tokens: string[]): Promise<SearchResult[]> {
        const pages = await this.getData();
        const exactQuery = normalize(query);
        const results: SearchResult[] = [];
        for (const page of pages) {
            const titleHits = tokens.filter(token => page.normalizedTitle.includes(token)).length;
            const hits = tokens.filter(token => page.normalizedTitle.includes(token) || page.normalizedContent.includes(token)).length;
            if (!hits) continue;
            const exact = page.normalizedTitle === exactQuery || page.normalizedNames.includes(exactQuery);
            const tier = exact ? 0 : titleHits === tokens.length ? 1 : hits === tokens.length ? 2 : 3;
            results.push({ page, tier, titleHits, hits });
        }
        return results.sort((a, b) => a.tier - b.tier || b.titleHits - a.titleHits || b.hits - a.hits);
    }

    private searchInput(submitted: boolean): void {
        const query = this.elements.input.value.trim();
        Search.updateQueryString(query, !submitted);
        void this.doSearch(query, submitted);
    }

    private async doSearch(query: string, submitted = false): Promise<void> {
        const revision = ++this.revision;
        window.clearTimeout(this.settledTimer);
        const tokens = queryTokens(query);
        const { list, status, empty, recovery } = this.elements;
        list.replaceChildren();
        recovery.hidden = true;
        empty.hidden = tokens.length > 0;
        if (!tokens.length) {
            status.textContent = '';
            this.lastSettledQuery = '';
            list.removeAttribute('aria-busy');
            return;
        }
        list.setAttribute('aria-busy', 'true');
        status.textContent = this.elements.form.dataset.loading || '';
        try {
            const results = await this.searchKeywords(query, tokens);
            // A slow index request must never render or measure an older input value.
            if (revision !== this.revision) return;
            const fragment = document.createDocumentFragment();
            for (const result of results) {
                fragment.append(Search.render(result.page, tokens, this.elements.form.dataset[`type${result.page.type[0].toUpperCase()}${result.page.type.slice(1)}`] || ''));
            }
            list.replaceChildren(fragment);
            list.removeAttribute('aria-busy');
            const template = results.length === 1 ? this.elements.form.dataset.countOne : this.elements.form.dataset.countMany;
            status.textContent = (template || '').replace('#COUNT', String(results.length));
            recovery.hidden = results.length > 0;
            if (submitted) {
                this.dispatchSettled(query, results.length);
            } else {
                this.settledTimer = window.setTimeout(() => {
                    if (revision === this.revision) this.dispatchSettled(query, results.length);
                }, 800);
            }
        } catch {
            if (revision !== this.revision) return;
            this.dataPromise = undefined;
            list.removeAttribute('aria-busy');
            status.textContent = this.elements.form.dataset.unavailable || '';
            recovery.hidden = false;
        }
    }

    private dispatchSettled(query: string, resultCount: number): void {
        const key = normalize(query);
        if (key === this.lastSettledQuery) return;
        this.lastSettledQuery = key;
        const length = Array.from(query).length;
        const lengthBucket = length <= 10 ? '1-10' : length <= 30 ? '11-30' : length <= 60 ? '31-60' : '61+';
        const resultBucket = resultCount === 0 ? '0' : resultCount <= 5 ? '1-5' : resultCount <= 20 ? '6-20' : '21+';
        document.dispatchEvent(new CustomEvent('tb:search-settled', { detail: { lengthBucket, resultBucket } }));
    }

    private handleQueryString(): void {
        const query = new URL(window.location.href).searchParams.get('keyword') || '';
        this.elements.input.value = query;
        void this.doSearch(query.trim());
    }

    private static updateQueryString(query: string, replaceState: boolean): void {
        const url = new URL(window.location.href);
        if (query) url.searchParams.set('keyword', query);
        else url.searchParams.delete('keyword');
        if (replaceState) window.history.replaceState(null, '', url);
        else window.history.pushState(null, '', url);
    }

    public static render(page: IndexedPage, tokens: string[], typeLabel: string): HTMLElement {
        const article = document.createElement('article');
        const link = document.createElement('a');
        link.href = page.permalink;
        const details = document.createElement('div');
        details.className = 'article-details';
        const type = document.createElement('span');
        type.className = 'search-result--type';
        type.textContent = typeLabel;
        const title = document.createElement('h2');
        title.className = 'article-title';
        highlight(title, page.title, tokens);
        const preview = document.createElement('p');
        preview.className = 'article-preview';
        // Terms lead with their short definition. Other records retain the compact excerpt.
        const excerpt = page.content.slice(0, 180);
        highlight(preview, excerpt + (page.content.length > 180 ? '…' : ''), tokens);
        details.append(type, title, preview);
        link.append(details);
        if (page.image) {
            const wrapper = document.createElement('div');
            wrapper.className = 'article-image';
            const image = document.createElement('img');
            image.src = page.image.src;
            if (page.image.srcset) image.srcset = page.image.srcset;
            image.sizes = '(max-width: 767px) 72px, 120px';
            if (page.image.width > 0) image.width = page.image.width;
            if (page.image.height > 0) image.height = page.image.height;
            image.alt = '';
            image.loading = 'lazy';
            image.decoding = 'async';
            wrapper.append(image);
            link.append(wrapper);
        }
        article.append(link);
        return article;
    }
}

window.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector<HTMLFormElement>('.search-page-form');
    const input = form?.querySelector<HTMLInputElement>('input[type="search"]');
    const list = document.querySelector<HTMLDivElement>('.search-result--list');
    const status = document.querySelector<HTMLParagraphElement>('.search-result--title');
    const empty = document.querySelector<HTMLElement>('.search-empty');
    const recovery = document.querySelector<HTMLElement>('.search-recovery');
    if (form && input && list && status && empty && recovery) {
        new Search({ form, input, list, status, empty, recovery });
    }
});

export default Search;
