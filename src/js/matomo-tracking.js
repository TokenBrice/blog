const matomoUrl = document
  .querySelector('script[data-id="matomo-tracking"]')
  .getAttribute('data-matomo-tracking-url');
const matomoSiteId = document
  .querySelector('script[data-id="matomo-tracking"]')
  .getAttribute('data-matomo-tracking-id');

var _paq = _paq || [];

_paq.push([function() { 
  var self = this; 
  function getOriginalVisitorCookieTimeout() {
    var now = new Date(),
    nowTs = Math.round(now.getTime() / 1000),
    visitorInfo = self.getVisitorInfo();
    var createTs = parseInt(visitorInfo[2]);
    var cookieTimeout = 33696000; // 13 mois en secondes        
    var originalTimeout = createTs + cookieTimeout - nowTs;        return originalTimeout;  }  
    this.setVisitorCookieTimeout( getOriginalVisitorCookieTimeout() );  }]);
/* tracker methods like "setCustomDimension" should be called before "trackPageView" */
_paq.push(['disableCookies']);
_paq.push(['trackPageView']);
_paq.push(['enableLinkTracking']);
(function() {
  _paq.push(['setTrackerUrl', `${matomoUrl}/piwik.php`]);
  _paq.push(['setSiteId', matomoSiteId]);

  const d = document;
  const g = d.createElement('script');
  const s = d.getElementsByTagName('script')[0];

  g.type = 'text/javascript';
  g.defer = true;
  g.src = `${matomoUrl}/piwik.js`;
  s.parentNode.insertBefore(g, s);
})();
