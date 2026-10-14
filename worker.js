// ZungiDill web payments. Runs on Cloudflare in front of the static site.
// Only /api/* comes here. Everything else is served from the static files.
// Needs one secret in Cloudflare: STRIPE_SECRET_KEY (Settings > Variables and Secrets).
// The app never sees card details. Stripe Checkout handles the card. This file only
// starts a checkout, confirms a payment, and checks whether a subscription is active.

const LAUNCH_ENDS = '2026-12-31';                 // launch price for one letter ends after this day (US Central)
const LETTER = { launch: 499, regular: 999 };      // cents
const MONTHLY = 3999;                              // cents per month
const INTRO = { off: 2000, months: 3, id: 'ZD_INTRO_3' }; // $20 off for the first 3 months = $19.99
const STRIPE = 'https://api.stripe.com/v1';

function json(d, status = 200) {
  return new Response(JSON.stringify(d), {
    status,
    headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store', 'X-Content-Type-Options': 'nosniff' }
  });
}
function money(c) { return '$' + (c / 100).toFixed(2); }
function launchOn() {
  const now = new Date(new Date().toLocaleString('en-US', { timeZone: 'America/Chicago' }));
  return now <= new Date(LAUNCH_ENDS + 'T23:59:59');
}
function form(obj, prefix = '', out = []) {
  for (const [k, v] of Object.entries(obj)) {
    if (v === undefined || v === null) continue;
    const key = prefix ? `${prefix}[${k}]` : k;
    if (typeof v === 'object') form(v, key, out);
    else out.push(encodeURIComponent(key) + '=' + encodeURIComponent(String(v)));
  }
  return out.join('&');
}
async function stripe(env, method, path, body) {
  const r = await fetch(STRIPE + path, {
    method,
    headers: {
      Authorization: 'Bearer ' + env.STRIPE_SECRET_KEY,
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: body ? form(body) : undefined
  });
  const d = await r.json();
  if (!r.ok) { const e = new Error((d.error && d.error.message) || 'stripe error'); e.status = r.status; e.code = d.error && d.error.code; throw e; }
  return d;
}
async function ensureIntroCoupon(env) {
  try { return (await stripe(env, 'GET', '/coupons/' + INTRO.id)).id; }
  catch (e) {
    if (e.status !== 404) throw e;
    const c = await stripe(env, 'POST', '/coupons', {
      id: INTRO.id, name: 'New subscriber price, first 3 months', amount_off: INTRO.off, currency: 'usd',
      duration: 'repeating', duration_in_months: INTRO.months
    });
    return c.id;
  }
}
function periodEnd(sub) {
  const item = sub.items && sub.items.data && sub.items.data[0];
  return ((item && item.current_period_end) || sub.current_period_end || 0) * 1000;
}
const ACTIVE = { active: 1, trialing: 1 };
function newKey() { const a = new Uint8Array(24); crypto.getRandomValues(a); return Array.from(a, b => b.toString(16).padStart(2, '0')).join(''); }
function keyOk(sub, k) { const want = sub.metadata && sub.metadata.zd_key; if (!want || typeof k !== 'string' || k.length !== want.length) return false; let d = 0; for (let i = 0; i < k.length; i++) d |= k.charCodeAt(i) ^ want.charCodeAt(i); return d === 0; }
const okId = (s, p) => typeof s === 'string' && s.startsWith(p) && /^[A-Za-z0-9_]{8,255}$/.test(s);

async function api(request, env, url) {
  if (!env.STRIPE_SECRET_KEY) return json({ error: 'payments are not set up yet' }, 503);
  const path = url.pathname.replace(/^\/api\//, '');

  if (path === 'prices' && request.method === 'GET') {
    const letter = launchOn() ? LETTER.launch : LETTER.regular;
    return json({
      letter: { str: money(letter), num: letter / 100 },
      sub: { str: money(MONTHLY), num: MONTHLY / 100 },
      intro: { str: money(MONTHLY - INTRO.off), num: (MONTHLY - INTRO.off) / 100, periods: INTRO.months }
    });
  }

  if (path === 'checkout' && request.method === 'POST') {
    let b = {};
    try { b = await request.json(); } catch (e) {}
    const kind = b.kind === 'sub' ? 'sub' : b.kind === 'letter' ? 'letter' : null;
    if (!kind) return json({ error: 'bad request' }, 400);
    const letterId = typeof b.letter === 'string' ? b.letter.slice(0, 80).replace(/[^A-Za-z0-9_:.-]/g, '') : '';
    const back = new URL('/app/', url.origin).href;
    const common = {
      success_url: back + '?checkout=done&session_id={CHECKOUT_SESSION_ID}',
      cancel_url: back + '?checkout=cancel',
      metadata: { app: 'zungidill-web', kind, letter: letterId }
    };
    let params;
    if (kind === 'letter') {
      const amount = launchOn() ? LETTER.launch : LETTER.regular;
      params = {
        ...common, mode: 'payment', allow_promotion_codes: 'true',
        line_items: { 0: { quantity: 1, price_data: { currency: 'usd', unit_amount: amount, product_data: { name: 'ZungiDill letter', description: 'Unlocks one finished dispute letter to print, save or send.' } } } },
        payment_intent_data: { description: 'ZungiDill letter', metadata: { app: 'zungidill-web', letter: letterId } }
      };
    } else {
      params = {
        ...common, mode: 'subscription',
        line_items: { 0: { quantity: 1, price_data: { currency: 'usd', unit_amount: MONTHLY, recurring: { interval: 'month' }, product_data: { name: 'ZungiDill Monthly', description: 'One round each month: a letter to each credit bureau, plus company letters.' } } } },
        subscription_data: { description: 'ZungiDill Monthly', metadata: { app: 'zungidill-web', zd_key: newKey() } }
      };
      if (b.intro !== false) params.discounts = { 0: { coupon: await ensureIntroCoupon(env) } };
      else params.allow_promotion_codes = 'true';
    }
    const s = await stripe(env, 'POST', '/checkout/sessions', params);
    return json({ url: s.url });
  }

  if (path === 'verify' && request.method === 'GET') {
    const id = url.searchParams.get('session_id');
    if (!okId(id, 'cs_')) return json({ error: 'bad request' }, 400);
    const s = await stripe(env, 'GET', '/checkout/sessions/' + encodeURIComponent(id) + '?expand[]=payment_intent&expand[]=subscription');
    if (!s.metadata || s.metadata.app !== 'zungidill-web') return json({ error: 'not found' }, 404);
    if (s.mode === 'subscription') {
      const sub = s.subscription;
      if (!sub || !ACTIVE[sub.status]) return json({ error: 'not paid' }, 402);
      return json({ kind: 'sub', sub: sub.id, key: (sub.metadata && sub.metadata.zd_key) || '', expires: periodEnd(sub) });
    }
    if (s.payment_status !== 'paid' || !s.payment_intent) return json({ error: 'not paid' }, 402);
    const pi = s.payment_intent;
    if (pi.metadata && pi.metadata.zd_used) return json({ error: 'used' }, 409);
    await stripe(env, 'POST', '/payment_intents/' + pi.id, { metadata: { zd_used: new Date().toISOString() } });
    return json({ kind: 'letter', letter: (s.metadata && s.metadata.letter) || '' });
  }

  if (path === 'sub' && request.method === 'GET') {
    const id = url.searchParams.get('id');
    if (!okId(id, 'sub_')) return json({ error: 'bad request' }, 400);
    try {
      const sub = await stripe(env, 'GET', '/subscriptions/' + encodeURIComponent(id));
      if (!sub.metadata || sub.metadata.app !== 'zungidill-web' || !keyOk(sub, url.searchParams.get('key'))) return json({ active: false });
      return json({ active: !!ACTIVE[sub.status], expires: periodEnd(sub), cancelAt: (sub.cancel_at || 0) * 1000 });
    } catch (e) { if (e.status === 404) return json({ active: false }); throw e; }
  }

  if (path === 'portal' && request.method === 'GET') {
    const id = url.searchParams.get('sub');
    if (!okId(id, 'sub_')) return json({ error: 'bad request' }, 400);
    const sub = await stripe(env, 'GET', '/subscriptions/' + encodeURIComponent(id));
    if (!sub.metadata || sub.metadata.app !== 'zungidill-web' || !keyOk(sub, url.searchParams.get('key'))) return json({ error: 'not found' }, 404);
    const p = await stripe(env, 'POST', '/billing_portal/sessions', { customer: sub.customer, return_url: new URL('/app/', url.origin).href });
    return json({ url: p.url });
  }

  return json({ error: 'not found' }, 404);
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname.startsWith('/api/')) {
      try { return await api(request, env, url); }
      catch (e) { return json({ error: 'payment service error' }, 502); }
    }
    return env.ASSETS.fetch(request);
  }
};
