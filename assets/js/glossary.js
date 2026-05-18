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
        var buttons = alphabetContainer.querySelectorAll('.alphabet-link');
        buttons.forEach(function(btn) {
            var letter = btn.getAttribute('data-letter') || btn.textContent.trim();
            var section = document.getElementById('letter-' + letter);
            if (section) {
                btn.style.display = section.style.display === 'none' ? 'none' : '';
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

    // Category pill handlers
    if (pillContainer) {
        // Initialize aria-pressed on all pills
        pillContainer.querySelectorAll('.category-pill').forEach(function(p) {
            p.setAttribute('aria-pressed', p.classList.contains('active') ? 'true' : 'false');
        });

        pillContainer.addEventListener('click', function(e) {
            var pill = e.target.closest('.category-pill');
            if (!pill) return;
            pillContainer.querySelectorAll('.category-pill').forEach(function(p) {
                p.classList.remove('active');
                p.setAttribute('aria-pressed', 'false');
            });
            pill.classList.add('active');
            pill.setAttribute('aria-pressed', 'true');
            activeCategory = pill.getAttribute('data-category') || '';
            applyFilters();
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

    // Alphabet nav scroll tracking with IntersectionObserver
    // Observe letter sections and highlight the link whose section heading
    // crosses the viewport top + 100px offset.
    if (alphabetContainer && 'IntersectionObserver' in window) {
        // Negative top rootMargin pushes the trigger line 100px below the viewport top.
        var observer = new IntersectionObserver(function(entries) {
            // Pick the topmost intersecting section
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

    // URL parameter support: ?category=X
    var urlParams = new URLSearchParams(window.location.search);
    var urlCategory = urlParams.get('category');
    if (urlCategory && pillContainer) {
        var targetPill = pillContainer.querySelector('[data-category="' + urlCategory + '"]');
        if (targetPill) {
            pillContainer.querySelectorAll('.category-pill').forEach(function(p) {
                p.classList.remove('active');
                p.setAttribute('aria-pressed', 'false');
            });
            targetPill.classList.add('active');
            targetPill.setAttribute('aria-pressed', 'true');
            activeCategory = urlCategory;
            applyFilters();
        }
    }

    // Backward compat: expose globally for category card shortcode
    window.handleCategoryFilter = function(categoryId) {
        activeCategory = categoryId || '';
        if (pillContainer) {
            pillContainer.querySelectorAll('.category-pill').forEach(function(p) {
                var isMatch = (p.getAttribute('data-category') || '') === activeCategory;
                p.classList.toggle('active', isMatch);
                p.setAttribute('aria-pressed', isMatch ? 'true' : 'false');
            });
        }
        applyFilters();
    };

    // Handle pending category filter
    if (window.pendingCategoryFilter) {
        window.handleCategoryFilter(window.pendingCategoryFilter);
        delete window.pendingCategoryFilter;
    }
})();
