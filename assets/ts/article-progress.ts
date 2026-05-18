/**
 * Reading-progress bar for article pages.
 * Gated on .article-content existing (uniquely identifies an article single page).
 * Honours prefers-reduced-motion. CSS lives in custom.scss as .reading-progress
 * (added by Zone H).
 */
function setupReadingProgress() {
    if (!document.querySelector('.article-content')) return;
    const mq = window.matchMedia('(prefers-reduced-motion: reduce)');
    if (mq.matches) return;

    const bar = document.createElement('div');
    bar.className = 'reading-progress';
    bar.setAttribute('aria-hidden', 'true');
    document.body.prepend(bar);

    let ticking = false;
    const update = () => {
        const h = document.documentElement;
        const scrollable = h.scrollHeight - h.clientHeight;
        const pct = scrollable > 0 ? (h.scrollTop / scrollable) : 0;
        bar.style.transform = `scaleX(${Math.min(Math.max(pct, 0), 1)})`;
        ticking = false;
    };
    const onScroll = () => {
        if (!ticking) {
            window.requestAnimationFrame(update);
            ticking = true;
        }
    };

    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll, { passive: true });
    update();
}

export { setupReadingProgress };
