(function () {
  // The $4.99 launch price ends after Dec 31, 2026 (US Central), the same moment worker.js switches to $9.99.
  if (Date.now() >= Date.UTC(2027, 0, 1, 6, 0, 0)) {
    document.querySelectorAll('.launch').forEach(function (n) { n.hidden = true; });
    document.querySelectorAll('.after').forEach(function (n) { n.hidden = false; });
  }
  // Phone bottom bar: show it once the page has scrolled past the first screen.
  var bar = document.querySelector('.mbar');
  if (!bar) return;
  if (location.pathname.indexOf('/app') === 0) { bar.remove(); return; }
  // Hidden while the Prices section is on screen, so its own buttons are not doubled.
  var pricesOn = false, prices = document.getElementById('prices');
  function tick() { bar.classList.toggle('on', !pricesOn && window.scrollY > window.innerHeight * 0.8); }
  if (prices && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (e) { pricesOn = e[0].isIntersecting; tick(); }).observe(prices);
  }
  window.addEventListener('scroll', tick, { passive: true });
  tick();
})();
