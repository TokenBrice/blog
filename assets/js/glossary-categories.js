(function() {
    function getCategoryColor(categoryId) {
        var colors = {
            'yields': '#10B981',
            'rendements': '#10B981',
            'risks': '#EF4444',
            'risques': '#EF4444',
            'strategies': '#8B5CF6',
            'stratégies': '#8B5CF6',
            'protocols': '#3B82F6',
            'protocoles': '#3B82F6',
            'tokens': '#F59E0B',
            'technical': '#6B7280',
            'technique': '#6B7280',
            'trading': '#06B6D4',
            'governance': '#EC4899',
            'gouvernance': '#EC4899',
            'defi-protocols': '#3B82F6',
            'trading-amms': '#06B6D4',
            'governance-daos': '#EC4899',
            'technical-concepts': '#6366F1',
            'lending-borrowing': '#059669',
            'stablecoins': '#F97316',
            'yield-farming': '#10B981'
        };
        return colors[categoryId] || '#6B7280';
    }

    function hexToRgb(hex) {
        var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
        return result ? {
            r: parseInt(result[1], 16),
            g: parseInt(result[2], 16),
            b: parseInt(result[3], 16)
        } : null;
    }

    function shouldUseDarkText(hexColor) {
        var rgb = hexToRgb(hexColor);
        if (!rgb) return false;
        var luminance = (0.299 * rgb.r + 0.587 * rgb.g + 0.114 * rgb.b) / 255;
        return luminance > 0.5;
    }

    function getCategoryIcon(categoryId) {
        var icons = {
            'yields': '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20m5-5l-5 5-5-5"/></svg>',
            'rendements': '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20m5-5l-5 5-5-5"/></svg>',
            'risks': '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
            'risques': '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
            'strategies': '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>',
            'stratégies': '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>',
            'protocols': '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>',
            'protocoles': '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>',
            'tokens': '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8"/><path d="M15 9.354a4 4 0 1 0 0 5.292"/></svg>',
            'technical': '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M12 1v6m0 6v6m11-7h-6m-6 0H1m15.5-6.5l-4.24 4.24m-6.36 0L1.66 5.34M18.34 18.66l-4.24-4.24m-6.36 0L3.5 18.5"/></svg>',
            'technique': '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M12 1v6m0 6v6m11-7h-6m-6 0H1m15.5-6.5l-4.24 4.24m-6.36 0L1.66 5.34M18.34 18.66l-4.24-4.24m-6.36 0L3.5 18.5"/></svg>',
            'trading': '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22,6 13.5,14.5 8.5,9.5 2,16"/><polyline points="16,6 22,6 22,12"/></svg>',
            'governance': '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.29 1.51 4.04 3 5.5l7 7z"/></svg>',
            'gouvernance': '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.29 1.51 4.04 3 5.5l7 7z"/></svg>'
        };
        return icons[categoryId] || '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14,2 14,8 20,8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10,9 9,9 8,9"/></svg>';
    }

    function handleCategoryClick(categoryId) {
        if (typeof window.handleCategoryFilter === 'function') {
            window.handleCategoryFilter(categoryId);
        } else {
            var glossaryApp = document.getElementById('glossary-app');
            if (glossaryApp) {
                glossaryApp.scrollIntoView({ behavior: 'smooth' });
                window.pendingCategoryFilter = categoryId;
            }
        }
    }

    document.addEventListener('DOMContentLoaded', function() {
        var categoryCards = document.querySelectorAll('.category-card[data-category-id]');
        categoryCards.forEach(function(card) {
            var categoryId = card.getAttribute('data-category-id');
            var color = getCategoryColor(categoryId);
            var icon = getCategoryIcon(categoryId);
            var countSpan = card.querySelector('.category-count');
            var iconElement = card.querySelector('.category-icon');

            card.style.borderLeftColor = color;

            if (countSpan) {
                countSpan.style.backgroundColor = color;
                countSpan.style.color = shouldUseDarkText(color) ? '#1a1a1a' : '#ffffff';
            }

            var rgb = hexToRgb(color);
            if (rgb) {
                card.style.setProperty('--category-color-rgb', rgb.r + ', ' + rgb.g + ', ' + rgb.b);
            }

            card.style.setProperty('--category-color', color);

            if (iconElement) {
                iconElement.innerHTML = icon;
                iconElement.style.color = color;
            }

            card.addEventListener('click', function(e) {
                e.preventDefault();
                handleCategoryClick(categoryId);
            });

            card.addEventListener('keydown', function(e) {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    handleCategoryClick(categoryId);
                }
            });
        });
    });
})();
