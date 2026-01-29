(function() {
    'use strict';

    // Data variables
    let glossaryData, categories, lang, sitePages;

    // DOM elements
    let termsList, noResults, alphabetContainer;

    // Current state
    let currentTerms = [];

    // Wait for Stack theme to fully initialize
    function waitForStackTheme() {
        // Check if Stack theme has initialized
        if (window.Stack && document.readyState === 'complete') {
            // Give Stack a moment to finish its initialization
            setTimeout(initializeGlossary, 100);
        } else {
            // Keep checking
            setTimeout(waitForStackTheme, 100);
        }
    }

    // Start checking for Stack initialization after page load
    window.addEventListener('load', function() {
        // Give Stack theme priority to initialize first
        setTimeout(waitForStackTheme, 200);
    });

    function initializeGlossary() {
        try {
            // Load data from Hugo-injected config
            var config = window.glossaryConfig;
            if (!config) {
                return;
            }

            lang = config.lang;
            glossaryData = config.glossaryData;
            categories = config.categories;
            sitePages = config.sitePages;

            // Get DOM elements
            termsList = document.getElementById('terms-list');
            noResults = document.getElementById('no-results');
            alphabetContainer = document.getElementById('alphabet-container');

            if (!termsList || !noResults || !alphabetContainer) {
                return;
            }

            // Initialize current terms
            currentTerms = glossaryData.terms || [];

            if (currentTerms.length === 0) {
                return;
            }

            // Initialize everything
            init();

            // Check for pending category filter
            if (window.pendingCategoryFilter) {
                handleCategoryFilter(window.pendingCategoryFilter);
                delete window.pendingCategoryFilter;
            }
        } catch (error) {
            // Initialization failed silently
        }
    }
    function init() {
        createAlphabetNavigation();
        renderTerms(currentTerms);

        // Make existing category cards clickable
        setupCategoryCardListeners();
    }


    function setupCategoryCardListeners() {
        // Find existing category cards in the page content and make them clickable
        // Only add event listener to the glossary content area, not the entire document
        const glossaryApp = document.getElementById('glossary-app');
        if (glossaryApp) {
            glossaryApp.addEventListener('click', (e) => {
                // Only handle clicks within the glossary app, not navigation elements
                const clickedElement = e.target;

                // Skip if clicked on navigation elements
                if (clickedElement.closest('.sidebar, .hamburger, #main-menu, #toggle-menu')) {
                    return; // Let the theme handle navigation clicks
                }

                // IMPORTANT: Skip if clicked on article links - let them work normally
                if (clickedElement.closest('.related-articles-list a, .related-articles-list article')) {
                    return; // Let article links work normally
                }

                // Check if clicked element or its parent is a category card
                let currentElement = clickedElement;

                // Traverse up to find a category card (look for elements with category info)
                while (currentElement && currentElement !== glossaryApp) {
                    // Look for category-related elements based on text content or structure
                    const textContent = currentElement.textContent;

                    // Map category names to IDs
                    const categoryMap = {
                        'Yields & Returns': 'yields',
                        'Rendements et Retours': 'rendements',
                        'Risks & Security': 'risks',
                        'Risques et Sécurité': 'risques',
                        'Strategies': 'strategies',
                        'Stratégies': 'stratégies',
                        'Protocols & Platforms': 'protocols',
                        'Protocoles et Plateformes': 'protocoles',
                        'Tokens & Assets': 'tokens',
                        'Technical Concepts': 'technical',
                        'Concepts Techniques': 'technique'
                    };

                    // Check if this element represents a category
                    for (const [categoryName, categoryId] of Object.entries(categoryMap)) {
                        if (textContent && textContent.includes(categoryName)) {
                            handleCategoryFilter(categoryId);
                            e.preventDefault();
                            e.stopPropagation();
                            return;
                        }
                    }

                    currentElement = currentElement.parentElement;
                }
            });
        }
    }


    function createAlphabetNavigation() {
        const letters = [...new Set(currentTerms.map(term => term.term.charAt(0).toUpperCase()))].sort();

        // Clear existing buttons
        alphabetContainer.innerHTML = '';

        letters.forEach(letter => {
            const link = document.createElement('button');
            link.textContent = letter;
            link.className = 'alphabet-link';
            link.onclick = () => scrollToLetter(letter);
            alphabetContainer.appendChild(link);
        });
    }

    function renderTerms(terms) {
        if (terms.length === 0) {
            termsList.style.display = 'none';
            noResults.style.display = 'block';
            return;
        }

        termsList.style.display = 'block';
        noResults.style.display = 'none';

        // Group terms by first letter
        const groupedTerms = {};
        terms.forEach(term => {
            const letter = term.term.charAt(0).toUpperCase();
            if (!groupedTerms[letter]) groupedTerms[letter] = [];
            groupedTerms[letter].push(term);
        });

        // Render grouped terms
        let html = '';
        Object.keys(groupedTerms).sort().forEach(letter => {
            html += `<div class="letter-section" id="letter-${letter}">`;
            html += `<h2 class="letter-heading">${letter}</h2>`;

            groupedTerms[letter].forEach(term => {
                html += renderTerm(term);
            });

            html += '</div>';
        });

        termsList.innerHTML = html;

        // Update alphabet navigation for filtered results
        createAlphabetNavigation();
    }

    function renderTerm(term) {
        const safeHtml = (str) => str ? str.replace(/[<>&"']/g, (m) => ({
            '<': '&lt;', '>': '&gt;', '&': '&amp;', '"': '&quot;', "'": '&#39;'
        }[m])) : '';

        const relatedLinks = (term.related_terms || []).map(relatedId => {
            const relatedTerm = currentTerms.find(t => t.id === relatedId);
            return relatedTerm ? `<a href="#${relatedId}" class="related-link">${safeHtml(relatedTerm.term)}</a>` : '';
        }).filter(Boolean).join(', ');

        const risks = (term.risks || []).map(risk => `<li>${safeHtml(risk)}</li>`).join('');
        const questions = (term.common_questions || []).map(qa => `
            <div class="faq-item">
                <h5 class="faq-question">${safeHtml(qa.question)}</h5>
                <p class="faq-answer">${safeHtml(qa.answer)}</p>
            </div>
        `).join('');

        return `
        <div class="term-card" id="${term.id}" style="border-left-color: ${getCategoryColor(term.category)}">
            <div class="term-category-header" style="background-color: ${getCategoryColor(term.category)}; color: white;">
                ${safeHtml(getCategoryName(term.category)).toUpperCase()}
            </div>
            <div class="term-header">
                <div class="term-icon" style="background-color: ${getCategoryColor(term.category)}">
                    ${getCategoryIcon(term.category)}
                </div>
                <div class="term-title-group">
                    <h3 class="term-title">
                        <span class="term-name">${safeHtml(term.term)}</span>
                        ${term.full_term !== term.term ? `<span class="full-term">(${safeHtml(term.full_term)})</span>` : ''}
                    </h3>
                </div>
            </div>

            <div class="term-body" style="padding: 0 var(--card-padding) var(--card-padding);">
                <p class="term-definition">${safeHtml(term.definition)}</p>

                ${term.example ? `
                <div class="term-example">
                    <div class="example-header">
                        <span class="example-icon">💡</span>
                        <strong>${lang === 'fr' ? 'Exemple' : 'Example'}</strong>
                    </div>
                    <p>${safeHtml(term.example)}</p>
                </div>` : ''}

                ${(risks || relatedLinks) ? `
                <div class="term-secondary-info">
                    ${risks ? `
                    <div class="term-risks">
                        <div class="risks-header">
                            <span class="risks-icon">⚠️</span>
                            <strong>${lang === 'fr' ? 'Risques à considérer' : 'Risks to Consider'}</strong>
                        </div>
                        <ul>${risks}</ul>
                    </div>` : ''}

                    ${relatedLinks ? `
                    <div class="term-related">
                        <strong>${lang === 'fr' ? 'Termes liés :' : 'Related Terms:'}</strong>
                        <p>${relatedLinks}</p>
                    </div>` : ''}
                </div>` : ''}

                ${questions ? `
                <div class="term-faqs">
                    <div class="faq-header">
                        <span class="faq-icon">❓</span>
                        <h4>${lang === 'fr' ? 'Questions fréquentes' : 'Common Questions'}</h4>
                    </div>
                    <div class="faq-container">
                        ${questions}
                    </div>
                </div>` : ''}

                ${term.related_articles && term.related_articles.length > 0 ? `
                <div class="term-articles">
                    <h4>${lang === 'fr' ? 'Articles connexes' : 'Related Articles'}</h4>
                    <div class="related-articles-list article-list--compact">
                        ${term.related_articles.slice(0, 3).map(article => renderRelatedArticle(article)).join('')}
                    </div>
                </div>` : ''}
            </div>
        </div>`;
    }

    function renderRelatedArticle(article) {
        const safeHtml = (str) => str ? str.replace(/[<>&"']/g, (m) => ({
            '<': '&lt;', '>': '&gt;', '&': '&amp;', '"': '&quot;', "'": '&#39;'
        }[m])) : '';

        // Get the correct URL and image from sitePages lookup
        const pageInfo = getArticleInfo(article.url);
        const actualUrl = pageInfo ? pageInfo.url : article.url;
        const articleImage = pageInfo ? pageInfo.image : '';

        return `
            <article>
                <a href="${safeHtml(actualUrl)}">
                    <div class="article-details">
                        <h2 class="article-title">${safeHtml(article.title)}</h2>
                        <section class="article-preview">${safeHtml(article.description)}</section>
                    </div>
                    ${articleImage ? `
                    <div class="article-image">
                        <img src="${safeHtml(articleImage)}" loading="lazy" alt="${safeHtml(article.title)}" onerror="handleImageError(this)"/>
                    </div>` : ''}
                </a>
            </article>`;
    }

    function getCategoryName(categoryId) {
        const category = categories.find(cat => cat.id === categoryId);
        return category ? category.name : categoryId;
    }

    function getCategoryColor(categoryId) {
        const colors = {
            'yields': '#10B981',      // Green - for earning/returns
            'rendements': '#10B981',  // Green (French)
            'risks': '#EF4444',       // Red - for risks/security
            'risques': '#EF4444',     // Red (French)
            'strategies': '#8B5CF6',  // Purple - for strategies
            'stratégies': '#8B5CF6',  // Purple (French)
            'protocols': '#3B82F6',   // Blue - for protocols/platforms
            'protocoles': '#3B82F6',  // Blue (French)
            'tokens': '#F59E0B',      // Amber - for tokens/assets
            'technical': '#6B7280',   // Gray - for technical concepts
            'technique': '#6B7280',   // Gray (French)
            'trading': '#06B6D4',     // Cyan - for trading/AMMs
            'governance': '#EC4899',  // Pink - for governance/DAOs
            'gouvernance': '#EC4899', // Pink (French)
            // Additional unique colors for overlapping categories
            'defi-protocols': '#3B82F6',      // Keep blue for DeFi Protocols
            'trading-amms': '#06B6D4',        // Keep cyan for Trading & AMMs
            'governance-daos': '#EC4899',     // Keep pink for Governance & DAOs
            'technical-concepts': '#6366F1',  // Indigo - distinct from gray
            'lending-borrowing': '#059669',   // Emerald - distinct from green
            'stablecoins': '#F97316',         // Orange - distinct from amber
            'yield-farming': '#10B981'        // Green - same as yields
        };
        return colors[categoryId] || '#6B7280'; // Default to gray
    }

    function getCategoryIcon(categoryId) {
        // Use emoji or text characters for simplicity
        const icons = {
            'yields': '💰',     // Money bag for yields/returns
            'rendements': '💰', // Same for French
            'risks': '⚠️',      // Warning for risks
            'risques': '⚠️',    // Same for French
            'strategies': '🧩', // Puzzle piece for strategies
            'stratégies': '🧩', // Same for French
            'protocols': '🔄',  // Arrows for protocols/platforms
            'protocoles': '🔄', // Same for French
            'tokens': '🪙',     // Coin for tokens/assets
            'technical': '⚙️',  // Gear for technical concepts
            'technique': '⚙️',  // Same for French
            'trading': '📊',    // Chart for trading/AMMs
            'governance': '🗳️', // Ballot box for governance/DAOs
            'gouvernance': '🗳️' // Same for French
        };
        return icons[categoryId] || '📄'; // Default to document icon
    }

    function getArticleImage(url) {
        // Use the site pages data built from front matter
        if (sitePages[url] && sitePages[url].image) {
            return sitePages[url].image;
        }
        // If no image found in mapping, hide the image container
        return '';
    }

    function getArticleInfo(url) {
        // Try exact match first
        if (sitePages[url]) {
            return sitePages[url];
        }

        // Try with trailing slash
        const urlWithSlash = url.endsWith('/') ? url : url + '/';
        if (sitePages[urlWithSlash]) {
            return sitePages[urlWithSlash];
        }

        // Try without trailing slash
        const urlWithoutSlash = url.endsWith('/') ? url.slice(0, -1) : url;
        if (sitePages[urlWithoutSlash]) {
            return sitePages[urlWithoutSlash];
        }

        // Search through all entries to find a match by key or URL
        for (const [key, pageInfo] of Object.entries(sitePages)) {
            if (key.includes(url.replace(/\//g, '')) || pageInfo.url === url || key === url) {
                return pageInfo;
            }
        }

        return null;
    }

    function handleImageError(img) {
        // If the front matter image fails to load, hide the image container
        img.parentNode.style.display = 'none';
    }

    function handleCategoryFilter(categoryValue) {
        // Filter terms
        let filteredTerms = glossaryData.terms || [];

        if (categoryValue) {
            filteredTerms = filteredTerms.filter(term => term.category === categoryValue);
        }

        currentTerms = filteredTerms;
        renderTerms(filteredTerms);

        // Scroll to glossary section
        document.getElementById('glossary-app').scrollIntoView({ behavior: 'smooth' });
    }

    // Expose the function globally so category cards can use it
    window.handleCategoryFilter = handleCategoryFilter;

    function scrollToLetter(letter) {
        const element = document.getElementById(`letter-${letter}`);
        if (element) {
            element.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    }
})();
