(function () {
  function show() {
    if (window.Tally && Tally.loadEmbeds) { Tally.loadEmbeds(); return; }
    document.querySelectorAll('iframe[data-tally-src]:not([src])').forEach(function (f) { f.src = f.dataset.tallySrc; });
  }
  // The "Loading the form" line stays until the form has really loaded, so the box is never empty.
  document.querySelectorAll('iframe.tally').forEach(function (f) {
    f.addEventListener('load', function () {
      if (!f.getAttribute('src')) return;
      var w = f.parentNode.querySelector('.formwait');
      if (w) w.hidden = true;
    });
  });
  var tries = 0;
  (function wait() {
    if (window.Tally || tries++ > 20) show(); else setTimeout(wait, 150);
  })();
})();
