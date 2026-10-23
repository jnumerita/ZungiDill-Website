(function () {
  var f = document.getElementById('notify');
  if (!f || !window.fetch) return;
  var msg = f.querySelector('.nmsg');
  var btn = f.querySelector('.nbtn');
  f.addEventListener('submit', function (e) {
    e.preventDefault();
    var email = f.querySelector('input[type=email]').value.trim();
    btn.disabled = true; btn.textContent = 'Sending...';
    msg.hidden = true;
    // Never hang: after 10 seconds without an answer, stop and show the error.
    var done = false;
    var ctl = window.AbortController ? new AbortController() : null;
    var timer = setTimeout(function () { if (ctl) ctl.abort(); fail(); }, 10000);
    function fail() {
      if (done) return; done = true; clearTimeout(timer);
      btn.disabled = false; btn.textContent = 'Notify me';
      msg.hidden = false;
      msg.textContent = "That didn't go through. Please try again.";
    }
    fetch('https://formsubmit.co/ajax/hola.numerita@gmail.com', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify({ email: email, list: 'ZungiDill iPhone launch list', _subject: 'New iPhone launch list signup', _template: 'table', _captcha: 'false' }),
      signal: ctl ? ctl.signal : undefined
    }).then(function (r) {
      if (!r.ok) throw new Error('HTTP ' + r.status);
      return r.json();
    }).then(function (d) {
      if (String(d.success) !== 'true') throw new Error(d.message || 'failed');
      if (done) return; done = true; clearTimeout(timer);
      f.innerHTML = '<p class="ndone"><b>You\'re on the list.</b> We\'ll email you once when the iPhone app is ready.</p>';
    }).catch(fail);
  });
})();
