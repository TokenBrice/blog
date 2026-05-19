var trackingScript = document.querySelector('script[data-id="matomo-tracking"]');
var matomoUrl = trackingScript.getAttribute('data-matomo-tracking-url');
var matomoSiteId = trackingScript.getAttribute('data-matomo-tracking-id');

window._paq = window._paq || [];
var _paq = window._paq;

_paq.push(['disableCookies']);
_paq.push(['trackPageView']);
_paq.push(['enableLinkTracking']);

(function () {
  _paq.push(['setTrackerUrl', matomoUrl + '/piwik.php']);
  _paq.push(['setSiteId', matomoSiteId]);
  var d = document;
  var g = d.createElement('script');
  var s = d.getElementsByTagName('script')[0];
  g.type = 'text/javascript';
  g.async = true;
  g.defer = true;
  g.src = matomoUrl + '/piwik.js';
  s.parentNode.insertBefore(g, s);
})();

function trackSeoEvent(category, action, name) {
  if (!category || !action) return;
  _paq.push(['trackEvent', category, action, name || '']);
}

function externalHost(href) {
  try {
    return new URL(href, window.location.origin).hostname.replace(/^www\./, '');
  } catch (e) {
    return 'unknown';
  }
}

function searchLengthBucket(value) {
  var length = value.trim().length;
  if (length <= 10) return '1-10';
  if (length <= 30) return '11-30';
  if (length <= 60) return '31-60';
  return '61+';
}

function closestAnchor(target) {
  while (target && target !== document) {
    if (target.tagName === 'A') return target;
    target = target.parentNode;
  }
  return null;
}

document.addEventListener('click', function (event) {
  var link = closestAnchor(event.target);
  if (!link) return;

  var href = link.getAttribute('href') || '';
  var label = (link.textContent || '').trim().slice(0, 80);

  if (href.indexOf('.xml') !== -1 || href.indexOf('/index.xml') !== -1) {
    trackSeoEvent('Distribution', 'RSS click', 'feed');
  } else if (/t\.me|x\.com|twitter\.com|warpcast\.com|youtube\.com|farcaster/i.test(href)) {
    trackSeoEvent('Distribution', 'Social click', externalHost(href));
  } else if (link.hreflang || link.closest('.article-translations')) {
    trackSeoEvent('Navigation', 'Language switch', link.getAttribute('hreflang') || label);
  } else if (/\/(projects|pharos|why-polaris|defi-bullshit-detector)\//i.test(href)) {
    trackSeoEvent('Content', 'Project click', 'internal-project');
  }
});

document.addEventListener('submit', function (event) {
  var form = event.target;
  if (!form || !/search/i.test(form.getAttribute('action') || form.id || form.className || '')) return;
  var input = form.querySelector('input[type="search"], input[name="keyword"], input[name="q"]');
  if (input && input.value.trim()) {
    trackSeoEvent('Search', 'Site search', searchLengthBucket(input.value));
  }
});

document.addEventListener('change', function (event) {
  var input = event.target;
  if (!input || input.tagName !== 'INPUT' || input.type !== 'search') return;
  if (input.value.trim()) {
    trackSeoEvent('Search', 'Site search', searchLengthBucket(input.value));
  }
});
