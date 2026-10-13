(function () {
  function show() {
    if (window.Tally && Tally.loadEmbeds) { Tally.loadEmbeds(); return; }
    document.querySelectorAll('iframe[data-tally-src]:not([src])').forEach(function (f) { f.src = f.dataset.tallySrc; });
  }
  var tries = 0;
  (function wait() {
    if (window.Tally || tries++ > 20) show(); else setTimeout(wait, 150);
  })();
})();
