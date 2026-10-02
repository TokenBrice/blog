// Implements smooth scrolling when clicking on an anchor link.
// This is required instead of using modern CSS because Chromium does not currently support scrolling
// one element with scrollTo while another element is scrolled because of a click on a link. This would
// thus not work with the ToC scrollspy and e.g. footnotes.

// Here are additional links about this issue:
// - https://stackoverflow.com/questions/49318497/google-chrome-simultaneously-smooth-scrollintoview-with-more-elements-doesn
// - https://stackoverflow.com/questions/57214373/scrollintoview-using-smooth-function-on-multiple-elements-in-chrome
// - https://bugs.chromium.org/p/chromium/issues/detail?id=833617
// - https://bugs.chromium.org/p/chromium/issues/detail?id=1043933
// - https://bugs.chromium.org/p/chromium/issues/detail?id=1121151

const anchorLinksQuery = "a[href]";

function setupSmoothAnchors() {
    document.querySelectorAll<HTMLAnchorElement>(anchorLinksQuery).forEach(aElement => {
        const href = aElement.getAttribute("href");
        // Glossary alphabet navigation owns its category-preserving history.
        if (!href || !href.startsWith("#") || aElement.classList.contains("alphabet-link")) {
            return;
        }
        aElement.addEventListener("click", clickEvent => {
            // Preserve new-tab/window gestures and other components' handlers.
            if (clickEvent.defaultPrevented || clickEvent.button !== 0 || clickEvent.metaKey || clickEvent.ctrlKey || clickEvent.shiftKey || clickEvent.altKey || aElement.target === "_blank") {
                return;
            }

            let targetId: string;
            try {
                targetId = decodeURIComponent(href.substring(1));
            } catch {
                return;
            }
            const target = document.getElementById(targetId);
            if (!target) return;

            clickEvent.preventDefault();
            const offset = target.getBoundingClientRect().top - document.documentElement.getBoundingClientRect().top;

            window.history.pushState({}, "", href);
            // A scroll-only jump strands keyboard users at the originating link.
            // Temporarily make headings/sections focusable without adding a tab stop.
            const hadTabindex = target.hasAttribute("tabindex");
            if (!hadTabindex) target.setAttribute("tabindex", "-1");
            target.focus({ preventScroll: true });
            if (!hadTabindex) {
                target.addEventListener("blur", () => target.removeAttribute("tabindex"), { once: true });
            }
            scrollTo({
                top: offset,
                behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth'
            });
        });
    });
}

export { setupSmoothAnchors };
