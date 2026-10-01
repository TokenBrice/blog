/*!
*   Hugo Theme Stack
*
*   @author: Jimmy Cai
*   @website: https://jimmycai.com
*   @link: https://github.com/CaiJimmy/hugo-theme-stack
*/
import StackGallery from "ts/gallery";
import { getColor } from 'ts/color';
import menu from 'ts/menu';
import createElement from 'ts/createElement';
import StackColorScheme from 'ts/colorScheme';
import { setupScrollspy } from './scrollspy';
import { setupSmoothAnchors } from "ts/smoothAnchors";
import { setupReadingProgress } from './article-progress';

let Stack = {
    init: () => {
        /**
         * Bind menu event
         */
        menu();

        const articleContent = document.querySelector('.article-content') as HTMLElement;
        if (articleContent) {
            new StackGallery(articleContent);
            setupSmoothAnchors();
            setupScrollspy();
            setupReadingProgress();
        }

        /**
         * Add linear gradient background to tile style article
         */
        const articleTiles = document.querySelectorAll('.article-list--tile article.has-image');
        if (articleTiles.length && typeof IntersectionObserver !== 'undefined') {
            const observer = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (!entry.isIntersecting) return;
                    observer.unobserve(entry.target);

                    const image = entry.target.querySelector('img');
                    const articleDetails = entry.target.querySelector('.article-details') as HTMLDivElement | null;
                    if (!image || !articleDetails) return;

                    const applyPalette = async () => {
                        if (!image.naturalWidth || !image.currentSrc) return;
                        const key = image.getAttribute('data-key'),
                            hash = image.getAttribute('data-hash');
                        const colors = await getColor(key, hash, image.currentSrc);
                        articleDetails.style.background = `
                        linear-gradient(0deg,
                            rgba(${colors.DarkMuted.rgb[0]}, ${colors.DarkMuted.rgb[1]}, ${colors.DarkMuted.rgb[2]}, 0.5) 0%,
                            rgba(${colors.Vibrant.rgb[0]}, ${colors.Vibrant.rgb[1]}, ${colors.Vibrant.rgb[2]}, 0.75) 100%)`;
                    };

                    if (image.complete && image.naturalWidth) {
                        void applyPalette();
                    } else {
                        image.addEventListener('load', applyPalette, { once: true });
                    }
                });
            }, { rootMargin: '200px' });
            articleTiles.forEach(article => observer.observe(article));
        }


        /**
         * Add copy button to code block
        */
        const highlights = document.querySelectorAll('.article-content div.highlight');
        const labels = document.getElementById('stack-main-script')?.dataset;
        const copyText = labels?.codeCopy,
            copiedText = labels?.codeCopied;

        highlights.forEach(highlight => {
            if (!copyText || !copiedText) return;
            const copyButton = document.createElement('button');
            copyButton.textContent = copyText;
            copyButton.classList.add('copyCodeButton');
            highlight.appendChild(copyButton);

            const codeBlock = highlight.querySelector('code[data-lang]');
            if (!codeBlock) return;

            copyButton.addEventListener('click', () => {
                navigator.clipboard.writeText(codeBlock.textContent)
                    .then(() => {
                        copyButton.textContent = copiedText;

                        setTimeout(() => {
                            copyButton.textContent = copyText;
                        }, 1000);
                    })
                    .catch(err => {
                        console.error('Clipboard copy failed:', err);
                    });
            });
        });

        new StackColorScheme(document.getElementById('dark-mode-toggle'));
    }
}

window.addEventListener('load', () => {
    setTimeout(function () {
        Stack.init();
    }, 0);
})

declare global {
    interface Window {
        createElement: any;
        Stack: any
    }
}

window.Stack = Stack;
window.createElement = createElement;
