// Email links are assembled here so the addresses are not sitting in the page source for scrapers.
(function () {
  document.querySelectorAll('a.mail').forEach(function (a) {
    var addr = a.getAttribute('data-u') + '@' + a.getAttribute('data-d');
    a.href = 'mailto:' + addr;
    if (a.getAttribute('href') !== 'contact.html') a.textContent = addr;
    else a.textContent = addr;
  });

  // Contact form: send through Web3Forms without leaving the page.
  var form = document.getElementById('contact-form');
  if (!form) return;
  var status = form.querySelector('.form-status');
  var btn = form.querySelector('button[type="submit"]');
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    status.className = 'form-status';
    if (!form.getAttribute('data-key')) {
      status.className = 'form-status err';
      status.textContent = 'The contact form is not switched on yet. Please use one of the email addresses above.';
      return;
    }
    status.textContent = 'Sending…';
    btn.disabled = true;
    fetch(form.action, {
      method: 'POST',
      headers: { 'Accept': 'application/json' },
      body: new FormData(form)
    }).then(function (r) { return r.json(); }).then(function (d) {
      if (d.success) {
        status.className = 'form-status ok';
        status.textContent = 'Thanks! Your message was sent.';
        form.reset();
      } else { throw new Error(d.message || 'failed'); }
    }).catch(function () {
      status.className = 'form-status err';
      status.textContent = 'Sorry, that didn’t go through. Please use one of the email addresses above.';
    }).then(function () { btn.disabled = false; });
  });
})();
