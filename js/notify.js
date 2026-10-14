(function () {
  var f = document.getElementById('notify');
  if (!f || !window.fetch) return;
  var msg = f.querySelector('.nmsg');
  var btn = f.querySelector('.nbtn');
  f.addEventListener('submit', function (e) {
    e.preventDefault();
    var email = f.querySelector('input[type=email]').value.trim();
    btn.disabled = true; btn.textContent = 'Sending...';
    fetch('https://formsubmit.co/ajax/hola.numerita@gmail.com', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify({ email: email, list: 'ZungiDill iPhone launch list', _subject: 'New iPhone launch list signup', _template: 'table', _captcha: 'false' })
    }).then(function (r) { return r.json(); }).then(function (d) {
      if (String(d.success) !== 'true') throw new Error(d.message || 'failed');
      f.innerHTML = '<p class="ndone"><b>You are on the list.</b> We will email you once, when ZungiDill is on the App Store. Nothing else.</p>';
    }).catch(function () {
      btn.disabled = false; btn.textContent = 'Notify me';
      msg.hidden = false;
      msg.innerHTML = 'That did not go through. Please try again, or <a href="https://tally.so/r/VLR6RJ" target="_blank" rel="noopener">use this form</a>.';
    });
  });
})();
