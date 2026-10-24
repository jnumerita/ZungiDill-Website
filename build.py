#!/usr/bin/env python3
"""Builds the ZungiDill website pages with one shared header and footer."""
import re, pathlib
OUT = pathlib.Path(__file__).parent
SITE = 'https://zungidill.com'
EMAIL = 'hola.numerita@gmail.com'
EFFECTIVE = 'October 14, 2026'
LASTMOD = '2026-10-22'

def page(slug, title, desc, body, current=''):
    def nav(href, label, key, cls=''):
        cur = ' aria-current="page"' if key == current else ''
        c = f' class="{cls}"' if cls else ''
        return f'<li{c}><a href="{href}"{cur}>{label}</a></li>'
    canon = SITE + ('/' if slug == 'index' else '/' + slug)
    HOMECSS = '\n<link rel="stylesheet" href="/css/home.css">' if slug == 'index' else ''
    BODYCLS = ' class="p-home"' if slug == 'index' else ''
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{'' if slug in ('thanks','404') else f'<link rel="canonical" href="{canon}">'}
<meta property="og:type" content="website">
<meta property="og:url" content="{canon}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:site_name" content="ZungiDill">
<meta property="og:image" content="{SITE}/img/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="ZungiDill app: Tired of hearing no? Check your credit report free.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}/img/og.png">{'{NOINDEX}' if slug in ('thanks','404') else ''}
<meta name="theme-color" content="#FFFFFF">
<link rel="icon" type="image/png" sizes="32x32" href="/img/icon-32.png">
<link rel="apple-touch-icon" href="/img/icon-180.png">
<link rel="preload" href="/fonts/SourceSerif4-700.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/IBMPlexSans-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/css/site.css">{HOMECSS}
</head>
<body{BODYCLS}>
<a class="skip" href="#main">Skip to content</a>
<header>
  <div class="wrap bar">
    <a class="brand" href="/" aria-label="ZungiDill home"><img src="/img/icon-72.png" alt="" width="36" height="36"><span>ZungiDill</span></a>
    <nav aria-label="Main">
      <ul>
        {nav('/#how', 'How it works', 'how', 'hide-md hide-sm')}
        {nav('/#prices', 'Prices', 'prices', 'hide-sm')}
        {nav('/learn/', 'Learn', 'learn')}
        {nav('/#questions', 'Questions', 'q', 'hide-md hide-sm')}
        {nav('/support', 'Support', 'support')}
        {nav('/#contact', 'Contact', 'contact')}
        {nav('/app/', 'Open the web app', 'app', 'navbtn hide-sm')}
      </ul>
    </nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer>
  <div class="wrap">
    <div class="grid">
      <div>
        <a class="brand" href="/" aria-label="ZungiDill home"><img src="/img/icon-72.png" alt="" width="36" height="36"><span>ZungiDill</span></a>
        <p class="made">Made by Numerita LLC, Sheridan, Wyoming.</p>
        <div class="stores">
          <a href="https://play.google.com/store/apps/details?id=com.numerita.zungidil" aria-label="Get it on Google Play"><img src="/img/badge-google-play.png" alt="Get it on Google Play" width="149" height="44"></a>
          <p class="soontxt">iPhone app coming soon. <a href="/#notify">Get notified</a></p>
        </div>
      </div>
      <div>
        <h4>Learn</h4>
        <ul>
          <li><a href="/guide">How to fix a mistake</a></li>
          <li><a href="/learn/dispute-letter">Dispute letter sample</a></li>
          <li><a href="/learn/collections">Collections</a></li>
          <li><a href="/learn/not-mine">Accounts that are not yours</a></li>
          <li><a href="/learn/mistakes">Mistakes to look for</a></li>
          <li><a href="/learn/how-long">How long items stay</a></li>
          <li><a href="/learn/">All guides</a></li>
        </ul>
      </div>
      <div>
        <h4>Legal</h4>
        <ul>
          <li><a href="/terms">Terms of Use</a></li>
          <li><a href="/privacy">Privacy Policy</a></li>
          <li><a href="/legal#disclosures">Disclosures</a></li>
          <li><a href="/legal#delete">Delete your data</a></li>
        </ul>
      </div>
      <div>
        <h4>Help</h4>
        <ul>
          <li><a href="/app/">Web app</a></li>
          <li><a href="/support">Support</a></li>
          <li><a href="/about">About</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>We reply within two business days.</li>
        </ul>
      </div>
    </div>
    <div class="disc">
      <p>ZungiDill is a self-help tool, not a credit repair organization or a law firm. It does not contact the credit bureaus for you, give legal advice, or promise results. You decide what to dispute and send your own letters.</p>
      <p>Google Play and the Google Play logo are trademarks of Google LLC. Apple, the Apple logo and App Store are trademarks of Apple Inc.</p>
      <p>© 2026 Numerita LLC</p>
    </div>
  </div>
</footer>
<div class="mbar" aria-label="Get ZungiDill"><a class="btn" href="/app/">Check your report</a></div>
<script src="/js/site.js" defer></script>
</body>
</html>
'''

def ul():
    return '<div class="ul" aria-hidden="true"><i></i><i></i></div>'

ICON = {
 'eye': '<svg viewBox="0 0 24 24"><path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></svg>',
 'phone': '<svg viewBox="0 0 24 24"><rect x="6" y="2" width="12" height="20" rx="3"/><path d="M11 18h2"/></svg>',
 'lock': '<svg viewBox="0 0 24 24"><rect x="4" y="10" width="16" height="11" rx="3"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/></svg>',
 'free': '<svg viewBox="0 0 24 24"><path d="M20 12v9H4v-9"/><path d="M2 7h20v5H2z"/><path d="M12 21V7"/><path d="M12 7H8a2.5 2.5 0 1 1 0-5c3 0 4 5 4 5zM12 7h4a2.5 2.5 0 1 0 0-5c-3 0-4 5-4 5z"/></svg>',
 'talk': '<svg viewBox="0 0 24 24"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 21l1.9-5.4A8 8 0 1 1 21 12z"/></svg>',
 'list': '<svg viewBox="0 0 24 24"><path d="M9 6h11M9 12h11M9 18h11"/><path d="M4 6l1 1 2-2M4 12l1 1 2-2M4 18l1 1 2-2"/></svg>',
}
GOAL = {
 'car': '<svg viewBox="0 0 48 48"><path d="M8 30l4-11a4 4 0 0 1 3.8-2.7h16.4A4 4 0 0 1 36 19l4 11v8H8z"/><circle cx="15" cy="34" r="3.5" fill="#fff"/><circle cx="33" cy="34" r="3.5" fill="#fff"/></svg>',
 'home': '<svg viewBox="0 0 48 48"><path d="M8 22L24 9l16 13v17H8z"/><path d="M20 39V28h8v11" fill="#fff"/></svg>',
 'card': '<svg viewBox="0 0 48 48"><rect x="6" y="12" width="36" height="24" rx="4"/><path d="M6 20h36" /><path d="M12 29h10" stroke-width="3"/></svg>',
}

def index():
    LT = {a["slug"]: a["title"] for a in L.ARTICLES}
    LC = {a["slug"]: a["card"] for a in L.ARTICLES}
    # Icons are Fractal library icons exported from Figma (Unicons Line). The 3D objects are built in Figma and exported.
    IC = {n: (OUT / 'img' / 'icons' / f'{n}.svg').read_text(encoding='utf-8').strip().replace('<svg ', '<svg aria-hidden="true" focusable="false" ', 1) for n in ('tick', 'card', 'doc', 'plus')}
    def obj(name, w, h, cls='', lazy=True):
        l = ' loading="lazy"' if lazy else ' fetchpriority="high"'
        return f'<img class="{cls}" src="/img/3d/{name}.webp" alt="" width="{w}" height="{h}" decoding="async"{l}>'
    steps = [
        ('1', 'Add your credit report', 'Get your free report and open it in ZungiDill. A photo of a paper copy works too.', obj('step-report', 711, 846, 'h-obj rv'), obj('num-1', 220, 365, 'h-num rv')),
        ('2', 'Check each item', "Go through your report one item at a time and mark anything that isn't right.", obj('step-magnifier', 717, 602, 'h-obj rv'), obj('num-2', 255, 368, 'h-num rv')),
        ('3', 'Read and mail your letter', 'ZungiDill writes the letter from what you marked. You read it, then print and mail it.', obj('step-envelope', 804, 762, 'h-obj rv'), obj('num-3', 261, 371, 'h-num rv')),
        ('4', 'Track the 30 days', "Enter the date it was delivered. We'll remind you when the bureau's 30 days are up.", obj('step-calendar', 726, 770, 'h-obj rv'), obj('num-4', 273, 365, 'h-num rv')),
    ]
    rows = ''.join(f'''
    <li class="h-row{' h-band' if n == '3' else ''}"><div class="h-wrap h-rowin">
      <div class="h-vis" aria-hidden="true">{num}{o}</div>
      <div class="h-txt"><h3>{h}</h3><p>{t}</p></div>
    </div></li>''' for n, h, t, o, num in steps)
    li = lambda items: ''.join(f'<li>{IC["tick"]}<span>{x}</span></li>' for x in items)
    guides = ''.join(f'<li><a href="/learn/{x}"><b>{LT[x]}</b><span>{LC[x]}</span></a></li>' for x in ('dispute-letter', 'not-mine', 'collections'))
    qa = [
        ('How do I fix a mistake on my credit report?', '<p>Send the credit bureau a letter. Say which item is wrong and why, and add copies of any proof. ZungiDill writes that letter from what you mark and keeps track of the answer.</p>'),
        ('Is this credit repair?', "<p>No. ZungiDill is a tool you use yourself. Nobody does it for you, and nobody charges you every month for promises. You decide what's wrong, and you send your own letters.</p>"),
        ('Where do I get my credit report?', '<p>Free at AnnualCreditReport.com, the official site. Save each report as a PDF and open it in ZungiDill. The <a href="/support">Support page</a> walks you through it.</p>'),
        ('What does it cost?', '<p>Checking your report and writing letters is free. You pay only when a letter is ready to print, save or send. You can pay for one letter at a time or use the monthly plan. You see the price before you pay. <a href="#prices">See prices</a></p>'),
        ('Can I use it for someone else?', "<p>No. ZungiDill only works with your own credit report. If a report is in another name, the app stops and won't use it.</p>"),
        ('What if they cannot prove it?', "<p>Then it has to be fixed or taken off your report. That's the law if the company that reported it can't show it's right: <a href=\"https://www.law.cornell.edu/uscode/text/15/1681i\">15 U.S.C. 1681i(a)(5)</a>.</p>"),
        ('What if the item is mine and it is right?', "<p>ZungiDill won't tell you to call it wrong. It shows you other options instead. One is a goodwill letter, where you ask the lender to remove a late payment that really happened.</p>"),
    ]
    faq = ''.join(f'<details class="h-q"><summary><span>{q}</span>{IC["plus"]}</summary><div>{a}</div></details>' for q, a in qa)
    body = f"""
<section class="h-hero" aria-labelledby="hero-h">
  <div class="h-wrap">
    <div class="h-float" aria-hidden="true">{obj('hero-card', 1246, 1051, 'h-herocard', lazy=False)}</div>
    <h1 id="hero-h">Find mistakes on your credit report and dispute them <em>yourself.</em></h1>
    <p class="h-lede">You mark what's wrong. ZungiDill writes the letter.</p>
    <div class="h-acts">
      <a class="btn" href="/app/">Open the web app</a>
      <a class="h-badge" href="https://play.google.com/store/apps/details?id=com.numerita.zungidil" aria-label="Get it on Google Play"><img src="/img/badge-google-play.png" alt="Get it on Google Play" width="183" height="54"></a>
    </div>
    <p class="h-price"><b>Checking is free.</b> <span class="launch">A letter costs $4.99 through Dec 31, 2026.</span><span class="after" hidden>A letter costs $9.99.</span> <a href="#prices">See prices</a></p>
    <p class="h-soon">The iPhone app is coming soon. <a href="#notify">Get notified</a></p>
  </div>
</section>

<section class="h-private" aria-labelledby="private-h">
  <div class="h-wrap h-split">
    <div>
      <h2 id="private-h">Your report stays on your phone.</h2>
      <p class="h-lede">There's no account to make. We never ask for your Social Security number. You send your own letters, so you see every word.</p>
    </div>
    <div class="h-trust">
      <div class="h-tcard">{IC['card']}<p><b>Payments by Stripe</b>on the web and Google Play in the app.</p></div>
      <div class="h-tcard">{IC['doc']}<p><b>Your right to dispute:</b><a href="https://www.consumerfinance.gov/ask-cfpb/how-do-i-dispute-an-error-on-my-credit-report-en-314/">15 U.S.C. 1681i</a></p></div>
    </div>
  </div>
</section>

<section class="h-heard" aria-labelledby="heard-h">
  <div class="h-wrap">
    <h2 id="heard-h" class="h-big">When ZungiDill helps</h2>
    <div class="h-bento">
      <div><h3>You were told no, or offered a high rate</h3><p>Lenders decide from your credit report. ZungiDill shows you what they see, so you can check it for mistakes.</p></div>
      <div><h3>You paid a credit repair company and nothing changed</h3><p>You never saw what they sent. Here you read every letter before it goes out, and you mail it yourself.</p></div>
      <div><h3>You pay cash for most things</h3><p>That works until you need a lease or a loan. Your report follows you either way, so make sure it's right.</p></div>
      <div><h3>You don't know where to start</h3><p>Start with your free credit report. ZungiDill reads it with you and shows you what to look at first.</p></div>
    </div>
  </div>
</section>

<section id="how" class="h-how" aria-labelledby="how-h">
  <div class="h-wrap h-head">
    <h2 id="how-h" class="h-big">How it works</h2>
    <p>You do each step yourself, on your phone or computer. Your letters go to the credit bureaus: Equifax, Experian and TransUnion, the companies that keep your report.</p>
  </div>
  <ol class="h-rows">{rows}
  </ol>
  <div class="h-wrap"><p class="h-timing"><b>How long does it take?</b> Bureaus usually have 30 days to answer. If you're planning to apply for something, start now.</p></div>
</section>

<section id="prices" class="h-prices" aria-labelledby="prices-h">
  <div class="h-wrap">
    <div class="h-head h-head-in">
      <h2 id="prices-h" class="h-big">What it costs</h2>
      <p><b>Checking your report and writing letters is free.</b> You pay only when a letter is ready to print, save or send.</p>
    </div>
    <div class="h-plans">
      <div class="h-plan h-main">
        <h3>One letter</h3>
        <p class="h-amt"><b><span class="launch">$4.99</span><span class="after" hidden>$9.99</span></b><span>per letter</span></p>
        <p class="h-then launch">That price runs through Dec 31, 2026. After that, a letter is <b>$9.99</b>.</p>
        <ul>{li(['Pays for one finished letter you can print, save or send.', "You pay once. There's no plan."])}</ul>
        <a class="btn gold" href="/app/">Get one letter</a>
        <p class="h-terms">You see the price before you pay.</p>
      </div>
      <div class="h-plan">
        <h3>ZungiDill Monthly</h3>
        <p class="h-opt">Optional. One letter at a time works too.</p>
        <p class="h-amt"><b>$19.99</b><span>a month for your first 3 months</span></p>
        <p class="h-then">Then <b>$39.99 a month</b>. The first price is for new subscribers.</p>
        <ul>{li(['Each month you get a letter to each credit bureau, plus letters to companies.', 'It renews every month until you cancel.', 'To stop, cancel before your renewal date.'])}</ul>
        <a class="btn" href="/app/">Start Monthly</a>
        <p class="h-terms">You see the price before you pay.</p>
      </div>
    </div>
    <p class="h-fine">Prices in U.S. dollars. On the web, you pay by card through Stripe. In the Android app, you pay through Google Play. <a href="/terms#prices">Full terms</a></p>
  </div>
</section>

<section id="questions" class="h-questions" aria-labelledby="q-h">
  <div class="h-wrap h-qwrap">
    <div class="h-qside">
      <h2 id="q-h" class="h-big">Questions</h2>
      <p>Longer answers are in our guides.</p>
      <ul class="h-qlinks"><li><a href="/guide">Step by step guide</a></li><li><a href="/learn/dispute-letter">Free dispute letter sample</a></li><li><a href="/learn/collections">Collections</a></li><li><a href="/learn/">All guides</a></li></ul>
    </div>
    <div class="h-qa">{faq}</div>
  </div>
</section>

<section class="h-guides" aria-labelledby="learn-h">
  <div class="h-wrap">
    <div class="h-head h-head-in">
      <h2 id="learn-h" class="h-big">Guides</h2>
      <p>Plain answers, with the law and official sources for each rule.</p>
    </div>
    <ul class="h-glist">{guides}</ul>
    <p class="h-more"><a href="/learn/">All guides</a></p>
  </div>
</section>

<section class="h-iphone" aria-labelledby="iphone-h">
  <div class="h-wrap h-split">
    <div>
      <h2 id="iphone-h">On iPhone? Use the web app in Safari.</h2>
      <p class="h-lede">The iPhone app is coming soon. Until then, the web app works in Safari. There's nothing to download.</p>
      <div class="h-acts"><a class="btn light" href="/app/">Open the web app</a></div>
    </div>
    <form class="notify" id="notify" action="https://tally.so/r/VLR6RJ" method="get" target="_blank" rel="noopener">
      <label for="nemail"><b>Get one email when the iPhone app is ready</b></label>
      <div class="nrow"><input id="nemail" name="email" type="email" placeholder="Your email" autocomplete="email" required><button class="nbtn" type="submit">Notify me</button></div>
      <p class="nmsg" role="status" aria-live="polite" hidden></p>
      <label class="ncheck"><input type="checkbox" required><span>Email me once when the iPhone app is available. Nothing else. <a href="/privacy#launch-list">Privacy</a></span></label>
    </form>
  </div>
</section>

<section id="contact" class="h-contact" aria-labelledby="contact-h">
  <div class="h-wrap h-head">
    <div>
      <h2 id="contact-h" class="h-big">Talk to a real person</h2>
      <p>A person reads every message. We reply within two business days.</p>
    </div>
    <div class="h-cbtns">
      <a class="btn" href="https://tally.so/r/Zj479y" target="_blank" rel="noopener">Send us a message</a>
      <a class="btn quiet" href="mailto:{EMAIL}">{EMAIL}</a>
    </div>
  </div>
</section>
<script src="/js/notify.js" defer></script>
"""
    return page('index', 'Fix Your Credit Report Yourself | ZungiDill Dispute App',
        'Tired of hearing no? ZungiDill helps you check your credit report free on your phone and send your own dispute letters. No account, no Social Security number.', body)

def doc(title, meta, toc, content):
    t = ''
    import re as _re
    m = _re.search(r'<div class="short">.*?</ul></div>', content, _re.S)
    short = ''
    if m:
        short = m.group(0); content = content.replace(short, '')
    if toc:
        t = '<nav class="toc" aria-label="On this page"><b>On this page</b><ol>' + ''.join(f'<li><a href="#{a}">{l}</a></li>' for a, l in toc) + '</ol></nav>'
    return f'<div class="doc"><div class="wrap narrow"><h1>{title}</h1><p class="meta">{meta}</p>{short}{t}{content}</div></div>'

def support():
    toc = [('start','Getting started'),('letters','Letters'),('purchases','Purchases'),('data','Your data'),('help','Still need help?')]
    c = f'''
<p style="margin-top:24px">Need help? Email <a href="mailto:{EMAIL}?subject=ZungiDill%20support">{EMAIL}</a> or <a href="https://tally.so/r/Zj479y" target="_blank" rel="noopener">send us a message</a>. We reply within two business days. Please don't send your Social Security number, full account numbers or your credit report.</p>
<h2 id="start">Getting started</h2>
<h3>Where do I get my credit report?</h3>
<p>Free at <a href="https://www.annualcreditreport.com">AnnualCreditReport.com</a>, the official site. Get the report from each bureau, save each one as a PDF, then tap Import my report in ZungiDill. You can also photograph a paper copy or add items by hand.</p>
<h3>It says the report is in someone else's name</h3>
<p>ZungiDill only works with your own credit report. The first report you bring in sets the name on your file, and a report in a different name is stopped. If your own name changed, for example after marriage, open the More tab, tap Erase everything, and start again with your new report.</p>
<h3>The import missed something</h3>
<p>Every bureau's report looks a little different. Open the item to fix it, or add it by hand on the Report tab. Check every date against your report, most of all the date of the first missed payment.</p>
<h3>Which items show in red?</h3>
<p>Red means something looks wrong: you marked it as wrong, or ZungiDill found a problem worth checking, like an item listed twice or one that may be too old to report.</p>
<h2 id="letters">Letters</h2>
<h3>Mail or online?</h3>
<p>Mail gives you the best proof. Send it certified with a return receipt, keep the tracking number, and add the day it arrived on the Track tab. The bureau's time starts the day they receive it. To dispute online instead, ZungiDill copies your letter and opens the bureau's own dispute page.</p>
<h3>Why is there a blank line for my Social Security number?</h3>
<p>The bureaus use it to find your file, so you write it in by hand. ZungiDill never asks for it or keeps it. Letters to companies leave that line out.</p>
<h3>The item is mine and it is right. What can I do?</h3>
<p>ZungiDill will not help you call true information wrong, because that can get your dispute thrown out. For a late payment that really happened, it writes a goodwill letter asking the lender to remove it as a courtesy. For a collection you do not recognize, it writes a letter asking the collector to prove it.</p>
<h2 id="purchases">Purchases</h2>
<h3>What does it cost?</h3>
<p>Checking your report and drafting letters is free. You pay only to print, save or send a finished letter.</p>
<table><tr><th scope="row">One letter</th><td>$4.99 launch price through December 31, 2026, then $9.99</td></tr><tr><th scope="row">ZungiDill Monthly</th><td>$19.99 a month for your first three months as a new subscriber, then $39.99 a month. A letter to each bureau every month, plus company, validation and goodwill letters.</td></tr><tr><th scope="row">Always free</th><td>The report review, letter drafts, reading a bureau's reply, and follow-up letters</td></tr></table>
<p style="margin-top:12px">The app shows the exact price before you pay. Full price terms are in the <a href="/terms#prices">Terms of Use</a>.</p>
<h3>How do I cancel ZungiDill Monthly?</h3>
<ul><li><b>Android:</b> Google Play Store, your profile picture, Payments and subscriptions, Subscriptions, ZungiDill. Cancel before the renewal date.</li><li><b>iPhone app:</b> Settings, your name, Subscriptions, ZungiDill. Cancel at least a day before the renewal date.</li><li><b>Web app:</b> More, then Manage or cancel subscription. Cancel before the renewal date.</li></ul>
<h3>Restore a purchase on a new phone</h3>
<p>ZungiDill Monthly is tied to your Google account or Apple ID. Open the More tab and tap Restore purchases. Single letters stay on the phone where you bought them. Need help? Email us your Google Play or App Store receipt.</p>
<h3>Promo codes</h3>
<p>More tab, then Redeem a promo code. Google Play or the App Store checks the code and shows the price before you confirm.</p>
<h3>Refunds</h3>
<p>Google and Apple handle every payment, so refunds go through them: <a href="https://support.google.com/googleplay/answer/2479637">Google Play refunds</a> or <a href="https://reportaproblem.apple.com">Apple refunds</a>.</p>
<h2 id="data">Your data</h2>
<h3>Erase everything</h3>
<p>More tab, then Erase everything, or delete the app. ZungiDill never receives your app data, so it cannot be brought back after that.</p>
<h3>iPhone launch list</h3>
<p>To come off the list, email <a href="mailto:{EMAIL}">{EMAIL}</a> from the address you signed up with.</p>
<h2 id="help">Still need help?</h2>
<p>Email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
'''
    return page('support', 'ZungiDill Support: Reports, Letters and Purchases', 'Help with ZungiDill: getting your free credit report, importing it, sending your letters, purchases, cancelling a plan and deleting your data.', doc('Support', 'Real answers from a real person.', toc, c), 'support')

def terms():
    toc = [('what','What ZungiDill is'),('results','No guarantee of results'),('you','Your responsibilities'),('rights','Your free rights'),('prices','Prices and purchases'),('info','Your information'),('other','Other services'),('license','License and use'),('disclaimers','Disclaimers'),('liability','Limitation of liability'),('apple',"Apple's terms"),('google',"Google Play's terms"),('law','Governing law'),('changes','Changes'),('contact','Contact')]
    c = f'''
<div class="short"><h2>The short version</h2><ul><li>ZungiDill is a tool you use yourself. It is not credit repair and not a law firm.</li><li>Nobody can promise a score or a removal. The bureaus decide.</li><li>Checking and drafting are free. You pay only to send a letter, or with Monthly if you choose it.</li><li>Use it only for your own credit report, and only dispute what you believe is wrong.</li><li>Cancel Monthly any time in Google Play or your iPhone settings, or in the web app under More, then Manage or cancel subscription.</li></ul></div>
<p style="margin-top:24px">These terms cover the ZungiDill app for Android and iPhone and the website zungidill.com, made by Numerita LLC. By using the app you agree to them.</p>
<h2 id="what">What ZungiDill is</h2>
<ul><li>Self-help software for reviewing your own credit reports, deciding what you believe is inaccurate, and drafting letters you send yourself.</li><li>Not a credit repair organization, credit counseling service or law firm. It does not give legal, financial or credit advice.</li><li>It does not contact credit bureaus, creditors, debt collectors or government agencies for you, and it never sends anything on your behalf.</li><li>The free review points out items worth checking against federal reporting rules. You decide what is wrong.</li><li>Letters are built from set wording plus your answers. Read every letter and change anything that is not true for you.</li></ul>
<h2 id="results">No guarantee of results</h2>
<p>Credit bureaus and the companies that report to them decide every dispute. No outcome, removal or score change is promised. Accurate, current information cannot lawfully be removed. Removing inaccurate or outdated negative items may help a score, but no change can be guaranteed.</p>
<h2 id="you">Your responsibilities</h2>
<ul><li>You must be at least 18 and live in the United States.</li><li>Use ZungiDill only for your own credit file. A report in another person's name is not accepted.</li><li>Dispute only items you believe in good faith are wrong, incomplete, outdated or not yours. Disputing accurate items can get a dispute rejected as frivolous.</li><li>Use identity theft letters only if you are a real victim. A false identity theft report is a crime.</li><li>Keep copies of everything you send, and send copies of documents, never originals.</li></ul>
<h2 id="rights">Your free rights</h2>
<p>You can dispute directly with the credit bureaus and the companies that report to them for free, without ZungiDill. Free credit reports are at <a href="https://www.annualcreditreport.com">AnnualCreditReport.com</a>. Credit freezes are free under federal law.</p>
<h2 id="prices">Prices and purchases</h2>
<p>Downloading the app, the credit report review and letter drafting are free. You pay only to print, save or send a finished letter. Prices are shown in the app and by your store, or at checkout on the web, before you pay. Current U.S. prices:</p>
<table><tr><th scope="row">Credit report review</th><td>Free</td></tr><tr><th scope="row">Letter drafting, reading replies, follow-up letters</th><td>Free</td></tr><tr><th scope="row">One letter, one-time purchase</th><td>$4.99 launch price through December 31, 2026, then $9.99</td></tr><tr><th scope="row">ZungiDill Monthly, auto-renewing</th><td>$39.99 a month. New subscribers pay $19.99 a month for the first three months, then $39.99 a month.</td></tr></table>
<p style="margin-top:12px">You pay the price your store shows when you confirm. A price change applies only to later purchases or renewals. Your store tells you before a subscription renews at a higher price.</p>
<h3>One letter</h3>
<p>A one-time purchase that unlocks one finished letter to print, save and share on the phone where you bought it. One letter covers every item you dispute at one bureau.</p>
<h3>ZungiDill Monthly</h3>
<ul><li>Each month includes one round: a letter to each credit bureau, plus letters to the companies that reported the items, debt validation letters and goodwill letters.</li><li>In the apps, payment is charged to your Google Play account or Apple ID when you confirm. In the web app, payment is charged to your card through Stripe when you confirm.</li><li>It renews every month at the price shown until you cancel.</li><li>iPhone: cancel at least 24 hours before the period ends. The renewal is charged within 24 hours before the end of the period.</li><li>Android: cancel before the renewal date in Google Play.</li><li>To cancel on Android: Play Store, your profile picture, Payments and subscriptions, Subscriptions. On iPhone: Settings, your name, Subscriptions.</li><li>Cancelling stops future renewals. You keep access until the paid period ends.</li></ul>
<h3>Buying in the web app</h3>
<ul><li>The web app at zungidill.com/app takes payment through Stripe Checkout. You see the price before you pay.</li><li>A letter you buy in the web app unlocks in the browser on the device where you bought it.</li><li>To cancel ZungiDill Monthly in the web app: open More, then Manage or cancel subscription. Cancelling stops future renewals, and you keep access until the paid period ends.</li><li>The introductory price is for new subscribers.</li></ul>
<h3>Launch prices, introductory prices and promo codes</h3>
<p>Launch prices last for a limited time. Introductory prices, like the three month offer, are for new subscribers who have not subscribed before, one time per account, as decided by your store. The regular price applies after. Promo codes are redeemed through your store, which decides if a code is valid. Codes have no cash value, usually cannot be combined, and may expire.</p>
<h3>Refunds</h3>
<p>In the apps, Google and Apple handle payments, receipts and refunds under their own terms: <a href="https://support.google.com/googleplay/answer/2479637">Google Play refunds</a>, <a href="https://reportaproblem.apple.com">Apple refunds</a>. For purchases in the web app, email <a href="mailto:{EMAIL}">{EMAIL}</a> with your Stripe receipt. We refund charges made in error and letters that did not unlock. Reading a bureau reply and follow-up letters are always free.</p>
<h2 id="info">Your information</h2>
<p>What you enter in the app is stored only on your phone. Numerita LLC does not have a copy. Deleting the app or erasing its data is permanent and cannot be undone. See the <a href="/privacy">Privacy Policy</a>.</p>
<h2 id="other">Other services</h2>
<p>The app links to other websites, such as the credit bureaus, AnnualCreditReport.com, the CFPB and SmartCredit. Numerita LLC does not control them and is not responsible for them. SmartCredit is optional, priced separately, has its own terms, and is not part of ZungiDill Monthly. Numerita LLC may earn a commission if you sign up through the link.</p>
<h2 id="license">License and acceptable use</h2>
<p>You get a personal license to use the app on devices you own or control, under your store's rules. It cannot be transferred. You may not copy, resell or reverse engineer the app, or use it to run a paid dispute service for other people. The app, its design and its text belong to Numerita LLC.</p>
<h2 id="disclaimers">Disclaimers</h2>
<p>The app is provided as is and as available. To the extent the law allows, all implied warranties are disclaimed. We do not promise the app is free of errors, or that the laws, addresses or bureau procedures it refers to are current when you use it.</p>
<h2 id="liability">Limitation of liability</h2>
<p>To the extent the law allows, Numerita LLC is not liable for indirect, incidental, special or consequential damages, or for decisions made by credit bureaus, creditors, collectors or lenders. Our total liability for any claim is limited to what you paid for the app in the twelve months before the claim. Some states do not allow these limits. Consumer protection rights that cannot be waived are not affected.</p>
<h2 id="apple">Apple's terms</h2>
<ul><li>If you got the app from the App Store, this agreement is between you and Numerita LLC, not Apple. Apple is not responsible for the app, its content, maintenance or support.</li><li>If the app fails to meet a warranty, you may tell Apple and Apple may refund the purchase price. Apple has no other warranty obligation.</li><li>Apple is not responsible for product liability, legal or regulatory compliance, or consumer protection claims. Numerita LLC handles any claim that the app infringes someone's intellectual property.</li><li>You confirm you are not in a country under a U.S. embargo or named as supporting terrorism, and you are not on a U.S. list of prohibited or restricted parties.</li><li>Apple and its subsidiaries are third party beneficiaries of these terms and may enforce them.</li><li>You may use the app only on Apple devices you own or control, under the App Store Usage Rules.</li></ul>
<h2 id="google">Google Play's terms</h2>
<p>If you got the app from Google Play, this agreement is between you and Numerita LLC, not Google. The Google Play Terms of Service also apply.</p>
<h2 id="law">Governing law</h2>
<p>These terms are governed by the laws of Wyoming and applicable federal law, without regard to conflict of laws rules. This does not take away protections you have under the laws of your home state.</p>
<h2 id="changes">Changes</h2>
<p>We post updated terms on this page with a new effective date, and note big changes in the app's update notes. Using the app after a change means you accept it.</p>
<h2 id="contact">Contact</h2>
<p>Numerita LLC, Sheridan, Wyoming<br>Email <a href="mailto:{EMAIL}">{EMAIL}</a></p>
'''
    return page('terms', 'Terms of Use | ZungiDill', 'The ZungiDill Terms of Use: what the app does and does not do, prices, subscriptions, refunds, cancelling, and your part when you send letters.', doc('Terms of Use', 'Effective ' + EFFECTIVE, toc, c))

def privacy():
    toc = [('never','What the app never asks for'),('phone','What stays on your phone'),('report','Your report and replies'),('diagnostics','Diagnostics on Android'),('reminders','Reminders'),('purchases','Purchases'),('links','Links to other sites'),('launch-list','The iPhone launch list'),('contact','Messages you send us'),('website','This website'),('delete','Deleting your information'),('rights','Your privacy rights'),('children','Children'),('security','Security'),('changes','Changes'),('reach','Contact')]
    c = f'''
<div class="short"><h2>The short version</h2><ul><li>Your report and letters stay on your phone. We never get them.</li><li>No account, and we never ask for your Social Security number.</li><li>We never sell your information.</li><li>If you email us or join the iPhone list, we use your email only to answer you.</li><li>Erase everything any time from the More tab.</li></ul></div>
<p style="margin-top:24px">This policy covers the ZungiDill app for Android and iPhone and the website zungidill.com, made by Numerita LLC.</p>
<h2 id="never">What the app never asks for</h2>
<p>Your Social Security number, date of birth, passwords, or bank or card details. Letters to the bureaus have blank lines where you write your Social Security number and birth date by hand. The app does not keep them.</p>
<h2 id="phone">What stays on your phone</h2>
<p>Your name and mailing address, report items (company names, the last four digits of account numbers, balances, dates, statuses and personal details from your report), your answers and dispute choices, drafted letters, mailing and arrival dates, tracking numbers, results you record, photos of proof or bureau replies, and your settings.</p>
<p>This is kept in the app's private storage on your phone. It is not sent to Numerita LLC or anyone else. It may be included in your phone's own backup (iCloud or your computer on iPhone, your Google account on Android), which you, Apple and Google control.</p>
<h2 id="report">Your report and bureau replies</h2>
<p>Report files and photos you bring in are read on your phone, using Apple's Vision on iPhone and Google's ML Kit on Android. Only the items you choose are saved. The report file and the text read from it are not kept, and nothing is uploaded. The app checks that a report is in the same name as your file, on your phone, so it is used only for your own report.</p>
<h2 id="diagnostics">Diagnostics on Android</h2>
<p>Google's ML Kit, which reads text on Android, may send Google basic diagnostics: device model, Android version, app name and version, an installation identifier, performance timings and error codes. It does not include your documents, photos or the text read from them. Numerita LLC does not receive this information.</p>
<h2 id="reminders">Reminders</h2>
<p>Deadline and monthly reminders are scheduled on your phone as local notifications. Nothing is sent to a server.</p>
<h2 id="purchases">Purchases</h2>
<p>In the Android and iPhone apps, Google Play and the App Store handle all payments. The app only checks with your store whether a purchase or subscription is active.</p>
<p>In the web app at zungidill.com/app, payments are handled by Stripe, our payment processor. Stripe collects your card details and the email address for your receipt. Numerita LLC never receives your full card number. We can see in our Stripe account the email address, the amount, the date and whether a subscription is active, and we use this only to provide what you bought, answer billing questions and meet legal and tax duties. The web app keeps a reference to your purchase in your browser on your device so it can unlock your letters. <a href="https://stripe.com/privacy">Stripe Privacy Policy</a></p>
<h2 id="links">Links to other sites</h2>
<p>The app links to sites such as AnnualCreditReport.com, the credit bureaus, IdentityTheft.gov, the CFPB, OptOutPrescreen.com and SmartCredit. Their own privacy policies apply. Nothing you enter in ZungiDill is passed to them. SmartCredit is an optional affiliate: Numerita LLC may earn a commission through the link, and no user information is shared with SmartCredit.</p>
<h2 id="launch-list">The iPhone launch list</h2>
<p>When you sign up on our website, your email address is sent to us by FormSubmit, an email delivery service. If you use our Tally form instead, Tally (Tally BV) stores it and sends it to us. We keep your email address and the date you signed up. We use it only to email you when the iPhone app launches. It is never sold, rented, shared or added to another list. We delete the list after the launch email goes out. To be removed sooner, email <a href="mailto:{EMAIL}">{EMAIL}</a> from the address you signed up with, or reply to the launch email.</p>
<h2 id="contact">Messages you send us</h2>
<p>When you use our contact form or email us, we receive your email address and what you tell us. The contact form is run by Tally (Tally BV), which stores what you enter and sends it to us. We use this only to answer you. We delete messages within twelve months of your last contact, or sooner if you ask. Please do not send your Social Security number, full account numbers or your credit report.</p>
<h2 id="website">This website</h2>
<p>This website has no ads and no tracking cookies. We use Cloudflare Web Analytics to count page visits. It does not use cookies or local storage and does not follow you across sites or over time. Cloudflare, Inc., our website host, processes technical information like IP addresses and browser type to deliver pages and prevent abuse.</p>
<h2 id="delete">Deleting your information</h2>
<p>In the app: tap Erase everything on the More tab, or delete the app. We cannot see, restore or delete app data for you because we never have it. For the launch list, messages or emails: email <a href="mailto:{EMAIL}">{EMAIL}</a> and we will delete it within 30 days.</p>
<h2 id="rights">Your privacy rights</h2>
<p>We do not sell or share personal information for targeted advertising, and we do not profile users. Depending on your state, you may have the right to know, access, correct or delete information we hold about you. For launch list and message information, email us and we will respond within 45 days. We will not treat you differently for using these rights.</p>
<h2 id="children">Children</h2>
<p>ZungiDill is for adults in the United States. It is not meant for anyone under 18, and we do not knowingly collect information from children.</p>
<h2 id="security">Security</h2>
<p>The biggest protection is that the app keeps your information on your phone, with no account and no server. Use a passcode or screen lock on your phone. Launch list and support emails are kept in our email account.</p>
<h2 id="changes">Changes</h2>
<p>We post any update on this page with a new effective date. Changes to how the app handles your information are also noted in the app's update notes.</p>
<h2 id="reach">Contact</h2>
<p>Numerita LLC, Sheridan, Wyoming<br>Email <a href="mailto:{EMAIL}">{EMAIL}</a></p>
'''
    return page('privacy', 'Privacy Policy | ZungiDill', 'How ZungiDill handles your information: your report stays on your phone, there is no account, we never ask for your Social Security number and never sell data.', doc('Privacy Policy', 'Effective ' + EFFECTIVE, toc, c))

def legal():
    c = f'''
<p style="margin-top:24px">Everything legal in one place: the <a href="/terms">Terms of Use</a>, the <a href="/privacy">Privacy Policy</a>, the disclosures below, and how to delete your data.</p>
<h2 id="disclosures">Disclosures</h2>
<h3>Self-help software</h3>
<p>ZungiDill is self-help software made by Numerita LLC. It is not a credit repair organization, a credit counseling service or a law firm, and it does not give legal, financial or credit advice. It does not contact credit bureaus, creditors, collectors or agencies for you and never sends anything on your behalf. You decide what to dispute, and you send your own letters.</p>
<h3>Your rights</h3>
<p>You can dispute inaccurate or incomplete information directly with the credit bureaus and the companies that report it, for free, without this app. Free reports are at <a href="https://www.annualcreditreport.com">AnnualCreditReport.com</a>, and credit freezes are free. No one can lawfully remove accurate, current information from a credit report.</p>
<h3>No guarantee</h3>
<p>The credit bureaus and reporting companies decide every dispute. ZungiDill cannot promise corrections, removals or score changes.</p>
<h3>Your own report only</h3>
<p>ZungiDill is for your own credit report. A report in another person's name is not accepted.</p>
<h3>Laws the app uses</h3>
<p>Letters and checks are based on the Fair Credit Reporting Act, the Fair Debt Collection Practices Act, Regulation V and the FTC's sample dispute letters. Laws and bureau procedures can change, and the app does not replace advice from a lawyer.</p>
<h3>Affiliate disclosure</h3>
<p>The app links to SmartCredit, an optional credit monitoring service run by a separate company with its own prices and terms. Numerita LLC may earn a commission if you join through the link. You pay nothing extra, SmartCredit is not part of ZungiDill Monthly, nothing you enter in ZungiDill is shared with it, and you never need it to use ZungiDill.</p>
<h3>Example content</h3>
<p>Screenshots on this website and in the app stores use a made-up credit report. The names, accounts and addresses are not real.</p>
<h3>Trademarks</h3>
<p>Google Play, Apple, iPhone, App Store, Equifax, Experian and TransUnion are trademarks of their owners. ZungiDill is not affiliated with or endorsed by any of them.</p>
<h2 id="delete">Delete your data</h2>
<ul><li>ZungiDill has no accounts. Everything you enter stays on your phone.</li><li>To erase it, open the More tab and tap Erase everything, or delete the app.</li><li>For the iPhone launch list or emails you sent us, write to <a href="mailto:{EMAIL}">{EMAIL}</a> from the address you used. We delete it within 30 days.</li><li>Purchase records are kept by Google Play or the App Store under their own policies.</li></ul>
<h2 id="contact">Contact</h2>
<p>Numerita LLC, Sheridan, Wyoming<br>Email <a href="mailto:{EMAIL}">{EMAIL}</a></p>
'''
    return page('legal', 'Legal Disclosures | ZungiDill', 'ZungiDill legal disclosures: not a credit repair company or a law firm, your rights, our affiliate disclosure and how to delete your data.', doc('Legal', 'Terms, privacy, disclosures and your data.', [], c))

def guide():
    toc = [('reports','Get your free reports'),('look','Look for what is wrong'),('theft','If someone used your name'),('send','Send your dispute'),('next','What happens next'),('stays','If they say it stays'),('right','If it is yours and it is right'),('repair','About credit repair companies'),('sources','Where this comes from')]
    c = f'''
<div class="short"><h2>The short version</h2><ul><li>Get your free reports from all three credit bureaus.</li><li>Find what is wrong and write down why.</li><li>Send a dispute to each bureau that shows it, with copies of your proof.</li><li>They usually have 30 days to check it, and they must send you the results in writing.</li></ul></div>
<h2 id="reports">Get your free reports</h2>
<p>Go to <a href="https://www.annualcreditreport.com">AnnualCreditReport.com</a>, the official site. Your reports from Equifax, Experian and TransUnion are free there every week. Get all three, because a mistake can show on one and not the others.</p>
<h2 id="look">Look for what is wrong</h2>
<ul><li>An account you never opened</li><li>A late payment you paid on time</li><li>A balance or credit limit that is wrong</li><li>The same account listed twice with a balance owed on both</li><li>An old debt that should have dropped off</li><li>A name, address or employer that is not yours</li></ul>
<p>Write down each item and what is wrong with it. Find any proof you have, like a bank statement, a receipt or a letter.</p>
<h2 id="theft">If someone used your name</h2>
<p>If someone else opened an account in your name, report it at <a href="https://www.identitytheft.gov">IdentityTheft.gov</a> first. Send that report to the credit bureaus with proof of who you are and ask them to block the accounts. They must block them within four business days, which is faster than a regular dispute.</p>
<h2 id="send">Send your dispute</h2>
<p>Dispute with each credit bureau that shows the mistake. You can do it online, by phone or by mail. Mail gives you the best record.</p>
<ul><li>Say who you are and which item is wrong.</li><li>Say what is wrong and why.</li><li>Ask them to fix it or take it off.</li><li>Add copies of your proof. Never send originals.</li><li>Keep a copy of everything you send.</li></ul>
<p>If you mail it, use certified mail with a return receipt, so you can prove the day it arrived. You can also dispute with the company that reported the item, like the bank or the collection agency.</p>
<h2 id="next">What happens next</h2>
<p>The credit bureau sends your dispute and your proof to the company that reported the item. The bureau usually has 30 days to finish. If that company cannot show the item is right, it has to be fixed or taken off.</p>
<p>The bureau must send you the results in writing. If anything changed, you also get a free copy of your report.</p>
<h2 id="stays">If they say it stays</h2>
<ul><li>Ask the credit bureau how they checked it.</li><li>Send new proof if you find more.</li><li>Dispute with the company that reported it.</li><li>Ask the bureau to add a short statement about your dispute to your report.</li><li>File a complaint with the Consumer Financial Protection Bureau at <a href="https://www.consumerfinance.gov/complaint/">consumerfinance.gov/complaint</a>.</li></ul>
<h2 id="right">If it is yours and it is right</h2>
<p>A dispute is for mistakes. It will not take off something that is true, and anyone who promises that is not being straight with you. Most late payments and collections drop off after seven years. Bankruptcy can stay for ten.</p>
<p>You can still write a goodwill letter asking the lender to remove a late payment that really happened. Some lenders say yes, mostly when the rest of your history is good.</p>
<h2 id="repair">About credit repair companies</h2>
<p>You do not need to pay anyone to dispute for you. Everything they do, you can do yourself for free. By law, a credit repair company cannot charge you before it finishes the work it promised. If one asks for money up front, walk away.</p>
<div class="cta"><h3>Do it on your phone</h3><p>ZungiDill walks you through each step above. Open your report and mark what's wrong. It writes the letter and reminds you when the answer is due.</p><div class="stores"><a class="btn" href="/app/">Check your report</a><a href="https://play.google.com/store/apps/details?id=com.numerita.zungidil" aria-label="Get it on Google Play"><img src="/img/badge-google-play.png" alt="Get it on Google Play" width="176" height="52"></a></div></div>
<h2 id="sources">Where this comes from</h2>
<ul><li><a href="https://consumer.ftc.gov/articles/disputing-errors-your-credit-reports">Federal Trade Commission: Disputing errors on your credit reports</a></li><li><a href="https://www.consumerfinance.gov/ask-cfpb/how-do-i-dispute-an-error-on-my-credit-report-en-314/">Consumer Financial Protection Bureau: How do I dispute an error on my credit report?</a></li><li><a href="https://www.identitytheft.gov">IdentityTheft.gov</a></li><li><a href="https://www.annualcreditreport.com">AnnualCreditReport.com</a></li></ul>
<p class="fine" style="margin-top:16px">This guide is general information, not legal advice.</p>
'''
    return page('guide', 'How to Fix Your Credit Report Yourself | ZungiDill', 'A free do it yourself guide to fixing mistakes on your credit report: get your reports, spot errors, send your dispute and know what happens next.', doc('How to fix a mistake on your credit report', 'Last updated ' + L.UPDATED + ' · Checked against official FTC and CFPB sources', toc, c), 'learn')

import learn as L
LBY={a['slug']:a for a in L.ARTICLES}
def src_list(keys):
    return '<ol class="sources">'+''.join(f'<li><a href="{L.SRC[k][1]}">{L.SRC[k][0]}</a></li>' for k in keys)+'</ol>'
CTA='<div class="cta"><h3>Do it on your phone</h3><p>Open your report in ZungiDill and mark what\'s wrong. It writes the letter and reminds you when the answer is due.</p><div class="stores"><a class="btn" href="/app/">Check your report</a><a href="https://play.google.com/store/apps/details?id=com.numerita.zungidil" aria-label="Get it on Google Play"><img src="/img/badge-google-play.png" alt="Get it on Google Play" width="176" height="52" loading="lazy"></a></div></div>'
def article(a):
    toc=[(i,h) for i,h,_ in a['sections']]+[('faq','Common questions'),('sources','Sources')]
    body=''.join(f'<h2 id="{i}">{h}</h2>\n{html}\n' for i,h,html in a['sections'])
    faq='<h2 id="faq">Common questions</h2>\n'+''.join(f'<h3>{q}</h3><p>{ans}</p>\n' for q,ans in a['faqs'])
    rel=''.join(f'<li><a href="/learn/{r}"><b>{LBY[r]["title"]}</b><span>{LBY[r]["card"]}</span></a></li>' for r in a['related'])
    t='<nav class="toc" aria-label="On this page"><b>On this page</b><ol>'+''.join(f'<li><a href="#{x}">{l}</a></li>' for x,l in toc)+'</ol></nav>'
    c=f"""<div class="doc art"><div class="wrap narrow">
<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> <span aria-hidden="true">›</span> <a href="/learn/">Learn</a> <span aria-hidden="true">›</span> <span>{a['title']}</span></nav>
<h1>{a['title']}</h1>
<p class="meta">Last updated {L.UPDATED} · Checked against official sources</p>
<div class="short answer"><h2>The quick answer</h2><p>{a['answer']}</p></div>
{t}
{body}{faq}{CTA}
<h2 id="sources">Sources</h2>
{src_list(a['sources'])}
<p class="fine" style="margin-top:14px">General information, not legal advice.</p>
<div class="related"><h2>Keep reading</h2><ul class="cards">{rel}</ul></div>
</div></div>"""
    return page('learn/'+a['slug'], a['seo'], a['desc'], c, 'learn')
def learn_hub():
    items=[('/guide','How to fix a mistake on your credit report','The full step by step guide. Start here.')]+[(f"/learn/{a['slug']}",a['title'],a['card']) for a in L.ARTICLES]
    cards=''.join(f'<li><a href="{u}"><b>{t}</b><span>{d}</span></a></li>' for u,t,d in items)
    c=f"""<div class="doc"><div class="wrap">
<div class="narrow" style="padding:0"><h1>Learn</h1>
<p class="lede" style="margin-top:14px">Plain answers about fixing your credit report yourself, for free. Every guide is checked against federal law and official pages from the FTC and the CFPB, and each one lists its sources.</p></div>
<ul class="cards hub">{cards}</ul>
<p class="fine" style="margin-top:24px">Last updated {L.UPDATED}. General information, not legal advice.</p>
</div></div>"""
    return page('learn/', 'Free Credit Report Guides: Do It Yourself | ZungiDill', 'Free plain language guides to fixing your credit report yourself: dispute letters, collections, identity theft, late payments and car loans.', c, 'learn')

def about():
    c = f"""<div class="doc"><div class="wrap narrow">
<h1>About ZungiDill</h1>
<p class="lede" style="margin-top:16px">ZungiDill helps you check your own credit report and send your own dispute letters. You don't have to pay anyone every month. It's made by Numerita LLC, a small software company in Sheridan, Wyoming.</p>
<h2 id="why">Why it exists</h2>
<p>Credit repair companies charge every month for letters you have the right to send yourself, and most people never see what was sent. ZungiDill puts that work in your hands. You read every letter, and you decide what goes out.</p>
<h2 id="honest">How the app stays honest</h2>
<ul><li>Your report stays on your phone. We never see it.</li><li>There is no account, and the app never asks for your Social Security number.</li><li>It only works with your own credit report.</li><li>It will not tell you to call something wrong when it is right.</li></ul>
<h2 id="guides">How we write our guides</h2>
<p>Every page in <a href="/learn/">Learn</a> is checked against federal law and official pages from the Federal Trade Commission and the Consumer Financial Protection Bureau. Each one lists its sources and the date it was last checked, and we update them when the rules change. They are general information, not legal advice.</p>
<h2 id="reach">Reach us</h2>
<p>Numerita LLC, Sheridan, Wyoming<br>Email <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</div></div>"""
    return page('about', 'About ZungiDill and Numerita LLC', 'ZungiDill is a do it yourself credit report app from Numerita LLC in Wyoming. Why we built it, how the app protects you and how we check our guides.', c)

def thanks():
    c = f'''<div class="doc"><div class="wrap narrow" style="text-align:left"><h1>Got it. Thank you.</h1><p class="lede" style="margin-top:20px">Your message reached us. A real person will get back to you within two business days. If you joined the iPhone list, you will hear from us once, when the app is out.</p><p style="margin-top:28px"><a class="btn" href="/">Back to ZungiDill</a></p></div></div>'''
    return page('thanks', 'Thank you · ZungiDill', 'Your message reached ZungiDill.', c)

def notfound():
    c = f'''<div class="doc"><div class="wrap narrow"><h1>That page is not here.</h1><p class="lede" style="margin-top:20px">The link may be old. Everything you need is one tap away.</p><p style="margin-top:28px"><a class="btn" href="/">Go to the home page</a></p></div></div>'''
    return page('404', 'Page not found · ZungiDill', 'Page not found.', c)

files = {'index.html': index(), 'guide.html': guide(), 'learn/index.html': learn_hub(), **{f"learn/{a['slug']}.html": article(a) for a in L.ARTICLES}, 'support.html': support(), 'about.html': about(), 'terms.html': terms(), 'privacy.html': privacy(), 'legal.html': legal(), 'thanks.html': thanks(), '404.html': notfound()}
def rel(html):
    def fix(m):
        attr,path=m.group(1),m.group(2)
        base,_,frag=path.partition('#')
        if base=='':target='index.html'
        elif base.startswith(('img/','css/','fonts/')) or '.' in base.split('/')[-1]:target=base
        else:target=base+'.html'
        return f'{attr}="{target}'+('#'+frag if frag else '')+'"'
    return re.sub(r'(href|src|action)="/(?!/)([^"]*)"',fix,html)

import json, html as _h
PLAY='https://play.google.com/store/apps/details?id=com.numerita.zungidil'
def strip(x): return _h.unescape(re.sub(r'<[^>]+>','',x)).strip()
def ld(obj): return '<script type="application/ld+json">'+json.dumps(obj,ensure_ascii=False,separators=(',',':'))+'</script>'
org={'@type':'Organization','@id':SITE+'/#org','name':'Numerita LLC','url':SITE+'/','logo':SITE+'/img/icon-512.png','email':EMAIL,
     'address':{'@type':'PostalAddress','addressLocality':'Sheridan','addressRegion':'WY','addressCountry':'US'},
     'sameAs':[PLAY],'contactPoint':{'@type':'ContactPoint','contactType':'customer support','email':EMAIL,'availableLanguage':'English'}}
web={'@type':'WebSite','@id':SITE+'/#site','name':'ZungiDill','url':SITE+'/','publisher':{'@id':SITE+'/#org'},'inLanguage':'en-US'}
OFFERS=[{'@type':'Offer','name':'Credit report check and letter drafting','price':'0','priceCurrency':'USD'},
 {'@type':'Offer','name':'One letter, launch price','price':'4.99','priceCurrency':'USD','priceValidUntil':'2026-12-31'},
 {'@type':'Offer','name':'One letter','price':'9.99','priceCurrency':'USD','validFrom':'2027-01-01'},
 {'@type':'Offer','name':'ZungiDill Monthly, first 3 months for new subscribers','description':'$19.99 a month for the first 3 months, then $39.99 a month','priceCurrency':'USD','price':'19.99','priceSpecification':{'@type':'UnitPriceSpecification','price':'19.99','priceCurrency':'USD','unitCode':'MON','billingDuration':3}},
 {'@type':'Offer','name':'ZungiDill Monthly','price':'39.99','priceCurrency':'USD','priceSpecification':{'@type':'UnitPriceSpecification','price':'39.99','priceCurrency':'USD','unitCode':'MON'}}]
app={'@type':'MobileApplication','@id':SITE+'/#app','name':'ZungiDill','operatingSystem':'Android','applicationCategory':'FinanceApplication',
     'description':'Check your own credit report on your phone, mark what is wrong, and send your own dispute letters. No account and no Social Security number.',
     'url':SITE+'/','downloadUrl':PLAY,'installUrl':PLAY,'publisher':{'@id':SITE+'/#org'},'image':SITE+'/img/og.png','offers':OFFERS}
webapp={'@type':'WebApplication','@id':SITE+'/#webapp','name':'ZungiDill web app','url':SITE+'/app/','applicationCategory':'FinanceApplication','operatingSystem':'iOS, Android, Windows, macOS','browserRequirements':'Works in Safari on iPhone and in any modern browser.',
     'description':'The ZungiDill app in your browser. Check your own credit report, mark what is wrong, and send your own dispute letters. Works on iPhone in Safari.','publisher':{'@id':SITE+'/#org'},'image':SITE+'/img/og.png','offers':OFFERS}
qa=re.findall(r'<details class="h-q"><summary><span>(.*?)</span>.*?</summary><div>(.*?)</div></details>',files['index.html'],re.S)
faq={'@type':'FAQPage','@id':SITE+'/#faq','mainEntity':[{'@type':'Question','name':strip(q),'acceptedAnswer':{'@type':'Answer','text':strip(a)}} for q,a in qa]}
assert len(qa)>=3
home=ld({'@context':'https://schema.org','@graph':[org,web,app,webapp,faq]})
def crumbs(items): return {'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':i+1,'name':n,'item':u} for i,(n,u) in enumerate(items)]}
def faqld(pairs): return {'@type':'FAQPage','mainEntity':[{'@type':'Question','name':strip(q),'acceptedAnswer':{'@type':'Answer','text':strip(a)}} for q,a in pairs]}
def artld(url,headline,desc,cites,about):
    return {'@type':'Article','@id':url+'#article','headline':headline,'description':desc,'datePublished':L.PUBLISHED_ISO,'dateModified':L.UPDATED_ISO,
      'author':{'@id':SITE+'/#org'},'publisher':{'@id':SITE+'/#org'},'mainEntityOfPage':url,'image':SITE+'/img/og.png','inLanguage':'en-US',
      'isPartOf':{'@id':SITE+'/#site'},'about':about,'citation':cites}
names={'about.html':'About ZungiDill','support.html':'Support','terms.html':'Terms of Use','privacy.html':'Privacy Policy','legal.html':'Legal'}
for k in list(files):
    v=files[k]; g=None
    if k=='index.html': v=v.replace('</head>',home+'\n</head>',1)
    elif k=='guide.html':
        u=SITE+'/guide'
        cites=[L.SRC[x][1] for x in ('ftc_dispute','cfpb_dispute','idt','acr','fcra_1681i','fcra_1681c2','croa_1679b')]
        g=[artld(u,'How to fix a mistake on your credit report','A plain step by step guide to disputing a mistake on your credit report yourself, for free.',cites,'Disputing credit report errors'),
           crumbs([('Home',SITE+'/'),('Learn',SITE+'/learn/'),('How to fix a mistake on your credit report',u)])]
    elif k=='learn/index.html':
        u=SITE+'/learn/'
        g=[{'@type':'CollectionPage','@id':u,'name':'Learn','url':u,'isPartOf':{'@id':SITE+'/#site'},'publisher':{'@id':SITE+'/#org'},
            'mainEntity':{'@type':'ItemList','itemListElement':[{'@type':'ListItem','position':1,'url':SITE+'/guide'}]+[{'@type':'ListItem','position':i+2,'url':f"{SITE}/learn/{a['slug']}"} for i,a in enumerate(L.ARTICLES)]}},
           crumbs([('Home',SITE+'/'),('Learn',u)])]
    elif k.startswith('learn/'):
        a=LBY[k[6:-5]]; u=f"{SITE}/learn/{a['slug']}"
        g=[artld(u,a['title'],a['desc'],[L.SRC[x][1] for x in a['sources']],a['title']),
           crumbs([('Home',SITE+'/'),('Learn',SITE+'/learn/'),(a['title'],u)]), faqld(a['faqs'])]
    elif k in names:
        slug=k[:-5]
        g=[{'@type':'WebPage','name':names[k],'url':f'{SITE}/{slug}','isPartOf':{'@id':SITE+'/#site'},'publisher':{'@id':SITE+'/#org'}},
           crumbs([('Home',SITE+'/'),(names[k],f'{SITE}/{slug}')])]
    if g: v=v.replace('</head>',ld({'@context':'https://schema.org','@graph':g})+'\n</head>',1)
    v=v.replace('{NOINDEX}','\n<meta name="robots" content="noindex">')
    files[k]=v

import hashlib
_vh={}
def _ver(path):
    if path not in _vh:
        fp=OUT/path
        _vh[path]=hashlib.md5(fp.read_bytes()).hexdigest()[:8] if fp.exists() else None
    return _vh[path]
def bust(html):
    def f(m):
        attr,path=m.group(1),m.group(2)
        v=_ver(path)
        return f'{attr}="/{path}?v={v}"' if v else m.group(0)
    return re.sub(r'(src|href)="/((?:css|js|img|fonts)/[^"?#]+)"',f,html)
files={k:bust(v) for k,v in files.items()}
for name, html in files.items():
    if re.search('[–—]', html):
        raise SystemExit('dash found in ' + name)
    (OUT / name).parent.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(html, encoding='utf-8')
pages=['/','/app/','/guide','/learn/']+[f"/learn/{a['slug']}" for a in L.ARTICLES]+['/about','/support','/terms','/privacy','/legal']
(OUT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{SITE}{u}</loc><lastmod>{LASTMOD}</lastmod></url>\n' for u in pages)+'</urlset>\n',encoding='utf-8')
bots=['GPTBot','OAI-SearchBot','ChatGPT-User','PerplexityBot','Perplexity-User','ClaudeBot','Claude-SearchBot','Claude-User','Google-Extended','Applebot-Extended','Bingbot','Googlebot']
(OUT/'robots.txt').write_text('User-agent: *\nAllow: /\n\n'+''.join(f'User-agent: {b}\nAllow: /\n\n' for b in bots)+f'Sitemap: {SITE}/sitemap.xml\n',encoding='utf-8')
GUIDES="\n".join([f"- [How to fix a mistake on your credit report]({SITE}/guide): The full step by step guide to disputing credit report errors yourself, for free"]+[f"- [{x['title']}]({SITE}/learn/{x['slug']}): {x['answer']}" for x in L.ARTICLES])
llms=f"""# ZungiDill

> ZungiDill is a phone and web app for people who want to fix mistakes on their own credit report themselves. You open your free credit report in the app, answer one question per account (not mine, I do not recognize it, mine but something is wrong, or mine and right), and ZungiDill writes the dispute letters for you to send to the credit bureaus. It is a self-help tool, not a credit repair organization or a law firm, and it does not promise results. It has no account and never asks for a Social Security number. Your report stays on your phone. Made by Numerita LLC in Sheridan, Wyoming.

- Use it now in any browser, including Safari on iPhone: {SITE}/app/ (no download).
- Android app on Google Play: {PLAY}
- iPhone app: coming soon to the App Store.
- Web app purchases are paid by card through Stripe. App purchases go through Google Play or the App Store.
- Checking your report and drafting letters is free. You pay only when a letter is ready to print, save or send.
- One letter: $4.99 through December 31, 2026, then $9.99.
- ZungiDill Monthly (optional): $19.99 a month for the first 3 months for new subscribers, then $39.99 a month. Renews until you cancel. Full terms: {SITE}/terms#prices
- Works only with your own credit report. A report in another person's name is stopped.
- Where to get a free report: AnnualCreditReport.com, the official site.

## Guides

{GUIDES}

## Pages

- [Home]({SITE}/): What ZungiDill does, how it works and common questions
- [Web app]({SITE}/app/): Use ZungiDill in your browser, including on iPhone
- [About]({SITE}/about): Who makes ZungiDill and how the guides are checked
- [Support]({SITE}/support): Getting your report, sending letters, purchases, cancelling and deleting your data
- [Terms of Use]({SITE}/terms): Prices, subscriptions, refunds and your responsibilities
- [Privacy Policy]({SITE}/privacy): What stays on your phone and what we never collect
- [Legal]({SITE}/legal): Disclosures and your rights

## Contact

- Email: {EMAIL}
"""
(OUT/'llms.txt').write_text(llms+f"\n## Full text\n\n- [All guides as plain text]({SITE}/llms-full.txt)\n",encoding='utf-8')
def plain(h):
    h=re.sub(r'<(script|nav|style)[^>]*>.*?</\1>','',h,flags=re.S)
    h=re.sub(r'<h1[^>]*>(.*?)</h1>',r'\n# \1\n',h,flags=re.S); h=re.sub(r'<h2[^>]*>(.*?)</h2>',r'\n## \1\n',h,flags=re.S); h=re.sub(r'<h3[^>]*>(.*?)</h3>',r'\n### \1\n',h,flags=re.S)
    h=re.sub(r'<li[^>]*>',r'\n- ',h); h=re.sub(r'<tr[^>]*>',r'\n',h); h=re.sub(r'</t[dh]>',' | ',h); h=re.sub(r'<(p|br|pre|div)[^>]*>',r'\n',h)
    h=_h.unescape(re.sub(r'<[^>]+>','',h)); h=re.sub(r'[ \t]+\n','\n',h); return re.sub(r'\n{3,}','\n\n',h).strip()
full=['# ZungiDill guides, full text\n\nSource: '+SITE+'/learn/ . Updated '+L.UPDATED_ISO+'. General information, not legal advice.']
for k in ['guide.html']+[f"learn/{x['slug']}.html" for x in L.ARTICLES]:
    m=re.search(r'<main id="main">(.*?)</main>',files[k],re.S)
    url=SITE+'/'+k[:-5]
    full.append('URL: '+url+'\n\n'+plain(m.group(1).split('<div class="related">')[0]))
(OUT/'llms-full.txt').write_text('\n\n---\n\n'.join(full)+'\n',encoding='utf-8')
for n in ('sitemap.xml','robots.txt','llms.txt','llms-full.txt'):
    if re.search('[–—]',(OUT/n).read_text()): raise SystemExit('dash in '+n)
print('built', ', '.join(files), '+ sitemap.xml robots.txt llms.txt')
