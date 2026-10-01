var trackingScript = document.querySelector('script[data-id="matomo-tracking"]');
var matomoUrl = (trackingScript.getAttribute('data-matomo-tracking-url') || '').replace(/\/+$/, '');
var matomoSiteId = trackingScript.getAttribute('data-matomo-tracking-id');

window._paq = window._paq || [];
var _paq = window._paq;

_paq.push(['disableCookies']);
// Pageviews must not disclose search text or other URL parameters.
_paq.push(['setCustomUrl', window.location.origin + window.location.pathname]);
if (document.referrer) {
  try {
    var referrer = new URL(document.referrer);
    if (referrer.origin === window.location.origin) {
      _paq.push(['setReferrerUrl', referrer.origin + referrer.pathname]);
    }
  } catch (e) {
    // Ignore an invalid referrer; browsers normally supply an absolute URL.
  }
}
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

  var placement = link.getAttribute('data-placement');
  var purpose = link.getAttribute('data-purpose');
  if (['sidebar', 'post-end', 'subscribe', 'footer', 'home'].indexOf(placement) !== -1 &&
      ['rss', 'announcements', 'follow', 'watch', 'contact'].indexOf(purpose) !== -1) {
    trackSeoEvent('Distribution', purpose, placement);
    return;
  }
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

document.addEventListener('tb:search-settled', function (event) {
  var detail = event.detail || {};
  // Only the documented vocabulary is accepted, never raw input or result titles.
  if (['1-10', '11-30', '31-60', '61+'].indexOf(detail.lengthBucket) === -1 ||
      ['0', '1-5', '6-20', '21+'].indexOf(detail.resultBucket) === -1) return;
  trackSeoEvent('Search', 'Site search', detail.lengthBucket + ' / ' + detail.resultBucket);
});

document.addEventListener('change', function (event) {
  var select = event.target;
  if (!select || select.tagName !== 'SELECT' || !select.closest('#i18n-switch')) return;
  var option = select.options[select.selectedIndex];
  if (option) {
    trackSeoEvent('Navigation', 'Language switch', (option.label || option.textContent || '').trim());
  }
});
