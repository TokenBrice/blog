(function() {
    'use strict';

    var termsList = document.getElementById('terms-list');
    var noResults = document.getElementById('no-results');
    var searchInput = document.getElementById('glossary-search');
    var pillContainer = document.getElementById('category-pills');
    var resultCount = document.getElementById('result-count');
    var alphabetContainer = document.getElementById('alphabet-container');

    if (!termsList) return;

    var allCards = termsList.querySelectorAll('.compact-card');
    var letterSections = termsList.querySelectorAll('.letter-section');
    var activeCategory = '';
    var searchQuery = '';
    var prefersReducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    function applyFilters() {
        var visibleCount = 0;
        var query = searchQuery.toLowerCase();

        allCards.forEach(function(card) {
            var matchesCategory = !activeCategory || card.getAttribute('data-category') === activeCategory;
            var matchesSearch = true;

            if (query) {
                var termId = (card.getAttribute('data-term-id') || '').toLowerCase();
                var termName = (card.querySelector('.compact-term-name') || {}).textContent || '';
                var definition = (card.querySelector('.compact-definition') || {}).textContent || '';
                var fullTerm = (card.querySelector('.compact-full-term') || {}).textContent || '';
                var searchable = (termId + ' ' + termName + ' ' + definition + ' ' + fullTerm).toLowerCase();
                matchesSearch = searchable.indexOf(query) !== -1;
            }

            if (matchesCategory && matchesSearch) {
                card.style.display = '';
                visibleCount++;
            } else {
                card.style.display = 'none';
            }
        });

        // Hide empty letter sections
        letterSections.forEach(function(section) {
            var visibleCards = section.querySelectorAll('.compact-card:not([style*="display: none"])');
            section.style.display = visibleCards.length > 0 ? '' : 'none';
        });

        updateAlphabetNav();

        // Update result count
        if (resultCount) {
            resultCount.textContent = visibleCount;
        }

        // Show/hide no results
        if (noResults) {
            termsList.style.display = visibleCount > 0 ? '' : 'none';
            noResults.style.display = visibleCount > 0 ? 'none' : 'block';
        }
    }

    function updateAlphabetNav() {
        if (!alphabetContainer) return;
        var links = alphabetContainer.querySelectorAll('.alphabet-link');
        links.forEach(function(btn) {
            var letter = btn.getAttribute('data-letter') || btn.textContent.trim();
            var section = document.getElementById('letter-' + letter);
            if (!section) return;
            // Muted (not hidden) when current filter yields no terms for this letter
            if (section.style.display === 'none') {
                btn.classList.add('is-empty');
                btn.setAttribute('aria-disabled', 'true');
                btn.setAttribute('tabindex', '-1');
            } else {
                btn.classList.remove('is-empty');
                btn.removeAttribute('aria-disabled');
                btn.removeAttribute('tabindex');
            }
        });
    }

    // Search input handler
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            searchQuery = this.value.trim();
            applyFilters();
        });
    }

    function readCategoryFromHash() {
        var h = (window.location.hash || '').replace(/^#/, '');
        if (!h) return '';
        // Support both `#cat=risks` and `#category=risks`
        var pairs = h.split('&');
        for (var i = 0; i < pairs.length; i++) {
            var kv = pairs[i].split('=');
            if (kv[0] === 'cat' || kv[0] === 'category') {
                return decodeURIComponent(kv[1] || '');
            }
        }
        return '';
    }

    function writeCategoryToHash(cat) {
        var current = window.location.hash || '';
        var target = cat ? '#cat=' + encodeURIComponent(cat) : '';
        if (current === target) return;
        // Avoid scroll-jump by using replaceState rather than assigning location.hash
        if (window.history && window.history.replaceState) {
            var url = window.location.pathname + window.location.search + target;
            window.history.replaceState(null, '', url);
        } else {
            window.location.hash = target;
        }
    }

    function activatePill(category, opts) {
        opts = opts || {};
        activeCategory = category || '';
        if (pillContainer) {
            pillContainer.querySelectorAll('.category-pill').forEach(function(p) {
                var isMatch = (p.getAttribute('data-category') || '') === activeCategory;
                p.classList.toggle('active', isMatch);
                p.setAttribute('aria-pressed', isMatch ? 'true' : 'false');
            });
        }
        applyFilters();
        if (opts.persist !== false) writeCategoryToHash(activeCategory);
    }

    // Category pill handlers
    if (pillContainer) {
        // Initialize aria-pressed on all pills
        pillContainer.querySelectorAll('.category-pill').forEach(function(p) {
            p.setAttribute('aria-pressed', p.classList.contains('active') ? 'true' : 'false');
        });

        pillContainer.addEventListener('click', function(e) {
            var pill = e.target.closest('.category-pill');
            if (!pill) return;
            var cat = pill.getAttribute('data-category') || '';
            // Re-click active non-"All" pill resets to All
            if (cat && pill.classList.contains('active')) {
                activatePill('');
            } else {
                activatePill(cat);
            }
        });
    }

    function setActiveAlphabetLetter(letter) {
        if (!alphabetContainer) return;
        alphabetContainer.querySelectorAll('.alphabet-link').forEach(function(btn) {
            var btnLetter = btn.getAttribute('data-letter') || btn.textContent.trim();
            var isActive = btnLetter === letter;
            btn.classList.toggle('is-active', isActive);
            // Keep legacy .active class in sync for back-compat
            btn.classList.toggle('active', isActive);
            if (isActive) {
                btn.setAttribute('aria-current', 'location');
            } else {
                btn.removeAttribute('aria-current');
            }
        });
    }

    // Alphabet nav: anchor jump with reduced-motion honored
    if (alphabetContainer) {
        alphabetContainer.addEventListener('click', function(e) {
            var link = e.target.closest('.alphabet-link');
            if (!link) return;
            // Block jumps to empty letters
            if (link.classList.contains('is-empty')) {
                e.preventDefault();
                return;
            }
            var letter = link.getAttribute('data-letter') || link.textContent.trim();
            var section = document.getElementById('letter-' + letter);
            if (!section) return;
            e.preventDefault();
            var behavior = prefersReducedMotion ? 'auto' : 'smooth';
            section.scrollIntoView({ behavior: behavior, block: 'start' });
            setActiveAlphabetLetter(letter);
            // Update URL fragment without triggering native jump
            if (window.history && window.history.replaceState) {
                var hashParts = [];
                if (activeCategory) hashParts.push('cat=' + encodeURIComponent(activeCategory));
                hashParts.push('letter-' + letter);
                // Hash carries either filter or letter target; keep filter if active
                var newHash = activeCategory
                    ? '#cat=' + encodeURIComponent(activeCategory)
                    : '#letter-' + letter;
                window.history.replaceState(null, '', window.location.pathname + window.location.search + newHash);
            }
        });
    }

    // Alphabet nav scroll tracking with IntersectionObserver
    if (alphabetContainer && 'IntersectionObserver' in window) {
        var observer = new IntersectionObserver(function(entries) {
            var visible = entries.filter(function(e) { return e.isIntersecting; });
            if (!visible.length) return;
            visible.sort(function(a, b) {
                return a.boundingClientRect.top - b.boundingClientRect.top;
            });
            var letter = visible[0].target.id.replace('letter-', '');
            setActiveAlphabetLetter(letter);
        }, { rootMargin: '-100px 0px -60% 0px' });

        letterSections.forEach(function(section) {
            observer.observe(section);
        });
    }

    // Initial state: prefer URL hash, fall back to legacy `?category=` query param
    var initialCategory = readCategoryFromHash();
    if (!initialCategory) {
        var urlParams = new URLSearchParams(window.location.search);
        var urlCategory = urlParams.get('category');
        if (urlCategory) initialCategory = urlCategory;
    }
    if (initialCategory && pillContainer && pillContainer.querySelector('[data-category="' + initialCategory + '"]')) {
        activatePill(initialCategory, { persist: false });
    }

    // React to hash changes (back/forward navigation, manual edits)
    window.addEventListener('hashchange', function() {
        var cat = readCategoryFromHash();
        if (cat !== activeCategory) {
            activatePill(cat, { persist: false });
        }
    });

    // Backward compat: expose globally for category card shortcode
    window.handleCategoryFilter = function(categoryId) {
        activatePill(categoryId || '');
    };

    // Handle pending category filter
    if (window.pendingCategoryFilter) {
        window.handleCategoryFilter(window.pendingCategoryFilter);
        delete window.pendingCategoryFilter;
    }
})();
