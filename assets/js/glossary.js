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
        pillContainer.addEventListener('click', function(e) {
            var pill = e.target.closest('.category-pill');
            if (!pill) return;
            pillContainer.querySelectorAll('.category-pill').forEach(function(p) {
                p.classList.remove('active');
            });
            pill.classList.add('active');
            activeCategory = pill.getAttribute('data-category') || '';
            applyFilters();
        });
    }

    // Alphabet nav scroll tracking with IntersectionObserver
    if (alphabetContainer && 'IntersectionObserver' in window) {
        var observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    var letter = entry.target.id.replace('letter-', '');
                    alphabetContainer.querySelectorAll('.alphabet-link').forEach(function(btn) {
                        var btnLetter = btn.getAttribute('data-letter') || btn.textContent.trim();
                        btn.classList.toggle('active', btnLetter === letter);
                    });
                }
            });
        }, { rootMargin: '-20% 0px -70% 0px' });

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
            });
            targetPill.classList.add('active');
            activeCategory = urlCategory;
            applyFilters();
        }
    }

    // Backward compat: expose globally for category card shortcode
    window.handleCategoryFilter = function(categoryId) {
        activeCategory = categoryId || '';
        if (pillContainer) {
            pillContainer.querySelectorAll('.category-pill').forEach(function(p) {
                p.classList.remove('active');
                if ((p.getAttribute('data-category') || '') === activeCategory) {
                    p.classList.add('active');
                }
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
