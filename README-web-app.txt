ZUNGIDILL WEB APP (zungidill.com/app)

What it is
The same ZungiDill app, running in Safari on iPhone (and any browser).
People can add it to their Home Screen: Share button, then Add to Home Screen.
Payments go through Stripe. The app never sees card numbers.

Files
app/             the web app (built from the iPhone/Android app source)
worker.js        the small Cloudflare program that talks to Stripe (/api/...)
wrangler.jsonc   tells Cloudflare to run worker.js for /api and serve the site for everything else

Prices (set in worker.js)
One letter: $4.99 through December 31, 2026, then $9.99 automatically.
ZungiDill Monthly: $39.99 a month. New subscribers get $20 off for the first 3 months ($19.99).

ONE TIME SETUP
1. Stripe account: sign up at stripe.com as Numerita LLC and finish activation
   (business details and the bank account for payouts).
2. Settings > Business > Public details: business name ZungiDill, support email
   hola.numerita@gmail.com, statement descriptor ZUNGIDILL.
3. Settings > Payments > Payment methods: turn on Apple Pay, Google Pay and Cash App Pay.
4. Settings > Billing > Customer portal: click Activate (or Save). Allow customers to cancel.
5. Developers > API keys: copy the Secret key (starts with sk_live_). Use the sk_test_ key first to test.
6. Cloudflare > Workers & Pages > zungidill-website > Settings > Variables and Secrets > Add:
   Type: Secret, Name: STRIPE_SECRET_KEY, Value: the key from step 5. Save and deploy.

Test before going live
With the sk_test_ key in step 6, open zungidill.com/app, make a letter, tap Unlock,
and pay with card 4242 4242 4242 4242, any future date, any CVC, any ZIP.
The letter should unlock. Then swap the secret to the sk_live_ key.

Web-only changes in app/index.html (keep these when copying a new app build over)
- First-use notice: "Your report is saved only in this browser..." shown once (webNotice, S.webNotice).
- Erase everything on the web clears this site's localStorage and sessionStorage and reloads (webErase).
- S.web (Stripe subscription reference) is part of the saved state, so Manage or cancel subscription works after a reload.
- SmartCredit card and More row say "We may earn a fee if you sign up."
- Server security headers for /app/ are in _headers (same set as the site, with a CSP that matches the app's own).
- The Get started renewal note (storeRenewNote) uses the Stripe wording on the web; Apple wording only shows in the iPhone app.
