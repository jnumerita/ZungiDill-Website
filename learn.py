# Content for the Learn section of zungidill.com.
# Every fact here was checked against the source listed with the article.

UPDATED = 'October 13, 2026'
UPDATED_ISO = '2026-10-13'

SRC = {
 'ftc_dispute': ('Federal Trade Commission: Disputing errors on your credit reports', 'https://consumer.ftc.gov/articles/disputing-errors-your-credit-reports'),
 'ftc_fix': ('Federal Trade Commission: Fixing your credit FAQs', 'https://consumer.ftc.gov/articles/fixing-your-credit-faqs'),
 'ftc_freeze': ('Federal Trade Commission: Credit freeze or fraud alert', 'https://consumer.ftc.gov/articles/credit-freeze-or-fraud-alert-whats-right-your-credit-report'),
 'cfpb_dispute': ('Consumer Financial Protection Bureau: How do I dispute an error on my credit report?', 'https://www.consumerfinance.gov/ask-cfpb/how-do-i-dispute-an-error-on-my-credit-report-en-314/'),
 'cfpb_auto': ('Consumer Financial Protection Bureau: Auto loans', 'https://www.consumerfinance.gov/consumer-tools/auto-loans/'),
 'cfpb_complaint': ('Consumer Financial Protection Bureau: Submit a complaint', 'https://www.consumerfinance.gov/complaint/'),
 'idt': ('IdentityTheft.gov, run by the Federal Trade Commission', 'https://www.identitytheft.gov'),
 'acr': ('AnnualCreditReport.com, the official free credit report site', 'https://www.annualcreditreport.com'),
 'fcra_1681c': ('Fair Credit Reporting Act, 15 U.S.C. 1681c: how long items can be reported', 'https://www.law.cornell.edu/uscode/text/15/1681c'),
 'fcra_1681c2': ('Fair Credit Reporting Act, 15 U.S.C. 1681c-2: identity theft blocks', 'https://www.law.cornell.edu/uscode/text/15/1681c-2'),
 'fcra_1681i': ('Fair Credit Reporting Act, 15 U.S.C. 1681i: disputes', 'https://www.law.cornell.edu/uscode/text/15/1681i'),
 'fdcpa_1692g': ('Fair Debt Collection Practices Act, 15 U.S.C. 1692g: proof of the debt', 'https://www.law.cornell.edu/uscode/text/15/1692g'),
 'croa_1679b': ('Credit Repair Organizations Act, 15 U.S.C. 1679b: no payment before the work is done', 'https://www.law.cornell.edu/uscode/text/15/1679b'),
 'croa_1679e': ('Credit Repair Organizations Act, 15 U.S.C. 1679e: right to cancel', 'https://www.law.cornell.edu/uscode/text/15/1679e'),
 'medical_2022': ('Equifax, Experian and TransUnion: changes to medical collection debt reporting (Business Wire)', 'https://www.businesswire.com/news/home/20220318005244/en'),
 'medical_court': ('CBS News: Federal judge reverses medical debt rule', 'https://www.cbsnews.com/news/federal-judge-reverses-medical-debt-rule-credit-reports-cfpb'),
 'fico_shop': ('myFICO: How to rate shop and limit the impact on your FICO Scores (Business Wire)', 'https://www.businesswire.com/news/home/20230711822181/en/myFICO-How-to-Rate-Shop-and-Minimize-the-Impact-to-Your-FICO-Scores'),
 'cfpb_errors': ('Consumer Financial Protection Bureau: Common errors on credit reports and how to get them fixed', 'https://www.consumerfinance.gov/about-us/blog/common-errors-credit-report-and-how-get-them-fixed'),
 'ncua': ('NCUA credit union locator', 'https://mapping.ncua.gov/'),
}

ARTICLES = [
# ------------------------------------------------------------------
dict(
 slug='mistakes',
 title='Credit report mistakes to look for',
 seo='Credit Report Mistakes to Look For | ZungiDill',
 desc='The most common credit report mistakes, from wrong names and accounts that are not yours to late payments, balances and dates, and how to spot each one.',
 card='The errors that show up most, and how to spot them.',
 answer='The most common credit report mistakes are wrong personal details, accounts that belong to someone else, late payments you paid on time, wrong balances or limits, the same debt listed twice and wrong dates. Check each account on all three reports, because a mistake can show on one and not the others.',
 sections=[
  ('you','Mistakes about you','''<ul>
<li>A name, address or phone number that is not yours</li>
<li>Accounts from someone with a name like yours</li>
<li>Accounts opened by someone who stole your identity. See <a href="/learn/not-mine">accounts that are not yours</a>.</li>
</ul>'''),
  ('status','Mistakes in how an account is reported','''<ul>
<li>An account you closed shows as open.</li>
<li>You are listed as the owner when you were only an authorized user.</li>
<li>A payment you made on time shows as late.</li>
<li>The date of your last payment, the date the account opened or the date you first fell behind is wrong.</li>
<li>The same debt is listed more than once.</li>
</ul>
<p>The date you first fell behind matters most. It decides <a href="/learn/how-long">how long a negative item can stay</a>, so a wrong date can keep it on your report too long.</p>'''),
  ('balance','Wrong balances and limits','''<ul>
<li>A balance that is higher than what you owe</li>
<li>A paid account that still shows a balance</li>
<li>A credit limit that is lower than your real limit, which can make your card look maxed out</li>
</ul>'''),
  ('data','Mistakes that come back','''<ul>
<li>A mistake that was fixed and then shows up again</li>
<li>The same account showing several times under different company names</li>
</ul>
<p>A deleted item can only come back if the company certifies it is accurate, and the credit bureau has to tell you in writing within five business days.</p>'''),
  ('check','How to check your report','''<ol class="list">
<li>Get all three reports free at <a href="https://www.annualcreditreport.com">AnnualCreditReport.com</a>.</li>
<li>Go account by account. Compare each one with your own records, like statements and receipts.</li>
<li>Write down every mistake and what is wrong with it.</li>
<li>Dispute each one with every bureau that shows it. Use our <a href="/learn/dispute-letter">sample dispute letter</a>.</li>
</ol>'''),
 ],
 faqs=[
  ('Should I check accounts that look fine?','Yes. A wrong balance, limit or date on a good account can still hurt your score.'),
  ('Can I dispute a mistake on just one report?','Yes. Dispute it with each bureau that shows it. The others do not need a letter.'),
 ],
 sources=['cfpb_errors','ftc_dispute','fcra_1681i','acr'],
 related=['dispute-letter','not-mine','how-long'],
),
# ------------------------------------------------------------------
dict(
 slug='dispute-letter',
 title='Credit dispute letter: a free sample you can copy',
 seo='Credit Dispute Letter Sample: Free Template | ZungiDill',
 desc='A free credit dispute letter you can copy, what to put in it, where to mail it for Equifax, Experian and TransUnion, and what happens after you send it.',
 card='A sample letter, what to put in it and where to mail it.',
 answer='A credit dispute letter tells a credit bureau which item on your report is wrong, why it is wrong and what you want done. Send one to each bureau that shows the mistake, add copies of your proof and keep a copy for yourself. The bureau usually has 30 days to look into it.',
 sections=[
  ('what','What goes in the letter','''<ul>
<li>Your full name, current address and date of birth, so they can find your file.</li>
<li>The company name and the account number shown on your report for each item. The last four digits are enough.</li>
<li>What is wrong, in one or two plain sentences.</li>
<li>What you want: fix it or take it off.</li>
<li>A list of the copies you are sending.</li>
</ul>
<p>The bureaus' own forms also ask for your Social Security number to find your file. If you choose to include it, write it in by hand after you print. ZungiDill never asks for it.</p>'''),
  ('sample','Sample dispute letter','''<p>Copy this, fill in the parts in brackets and delete what you do not need.</p>
<pre class="letter">[Your full name]
[Street address]
[City, State ZIP]
Date of birth: [month day, year]

[Today's date]

[Credit bureau name]
[Bureau mailing address]

Re: Dispute of information on my credit report

I am writing to dispute the information below. Each item is also circled on the attached copy of my report.

1. [Company name], account ending in [last four digits]
What is wrong: [For example: I never opened this account.]
What I want: Please delete this account from my report.

2. [Company name], account ending in [last four digits]
What is wrong: [For example: I paid on time in March. My bank statement is attached.]
What I want: Please remove the late payment.

Please investigate these items and correct or delete anything that is inaccurate, incomplete or cannot be verified. Please send me the results in writing.

Enclosed:
Copy of my ID
Copy of a bill or bank statement showing my address
[Your proof for each item]

Sincerely,
[Your signature]
[Your printed name]</pre>'''),
  ('where','Where to mail it','''<table>
<tr><th>Bureau</th><th>Mail disputes to</th><th>Online</th></tr>
<tr><td>Equifax</td><td>Equifax Information Services LLC<br>P.O. Box 740256<br>Atlanta, GA 30374</td><td><a href="https://www.equifax.com/personal/credit-report-services/credit-dispute/">equifax.com</a></td></tr>
<tr><td>Experian</td><td>Experian<br>P.O. Box 4500<br>Allen, TX 75013</td><td><a href="https://www.experian.com/disputes/main.html">experian.com</a></td></tr>
<tr><td>TransUnion</td><td>TransUnion LLC<br>Consumer Dispute Center<br>P.O. Box 2000<br>Chester, PA 19016</td><td><a href="https://www.transunion.com/credit-disputes/dispute-your-credit">transunion.com</a></td></tr>
</table>
<p>Check the address on the bureau's website before you mail, in case it changed. Use certified mail with a return receipt so you can prove the day it arrived.</p>'''),
  ('proof','What proof to send','''<ul>
<li>A copy of your ID and a bill or statement that shows your address.</li>
<li>Bank statements or receipts that show you paid on time.</li>
<li>Letters from the lender that say the account is paid, closed or settled.</li>
<li>An identity theft report from IdentityTheft.gov if the account is not yours.</li>
</ul>
<p>Send copies only. Never mail your originals.</p>'''),
  ('after','What happens after you mail it','''<p>The bureau sends your dispute and your proof to the company that reported the item. It usually has 30 days to finish, and up to 45 if you send more information while it is checking. If the item is wrong, incomplete or cannot be verified, it has to be fixed or deleted.</p>
<p>When they finish, the bureau has five business days to send you the results in writing. If anything changed, you also get a free copy of your report. If they say it stays, see <a href="/guide#stays">what to do next</a>.</p>'''),
 ],
 faqs=[
  ('Should I dispute online or by mail?','Both work. Online is faster. Mail gives you proof of what you sent and the day it arrived, which helps if you need to dispute again or file a complaint.'),
  ('Do I need a letter for each credit bureau?','Yes. Each bureau keeps its own file, so send a letter to every bureau that shows the mistake.'),
  ('Can I dispute more than one item in one letter?','Yes. List each item on its own with what is wrong with it and what you want done.'),
 ],
 sources=['ftc_dispute','cfpb_dispute','fcra_1681i'],
 related=['collections','not-mine','how-long'],
),
# ------------------------------------------------------------------
dict(
 slug='collections',
 title='How to get a collection off your credit report',
 seo='Remove a Collection From Your Credit Report | ZungiDill',
 desc='How to get a collection off your credit report: check it, make the collector prove it, dispute it, and what to do if the debt is really yours.',
 card='Check it, make them prove it, and what to do if it is yours.',
 answer='If a collection is wrong, dispute it with the credit bureaus and ask the collector to prove the debt. If it cannot be verified, it has to come off. If it is yours and correct, it can stay for about seven and a half years from the first missed payment that led to it, but you can still ask the collector to remove it.',
 sections=[
  ('check','First, check if it is really yours','''<ul>
<li>Do you know the original company, like the phone company, the hospital or the landlord?</li>
<li>Is the amount right?</li>
<li>Is the same debt listed twice with a balance owed on both, once by the lender and once by the collector?</li>
<li>Is the date of the first missed payment right? A newer date can keep it on your report longer than allowed.</li>
<li>Did someone else open it? Then follow the steps for <a href="/learn/not-mine">accounts that are not yours</a>.</li>
</ul>'''),
  ('prove','Make the collector prove it','''<p>When a debt collector first contacts you, it has to send you a notice about the debt. You have 30 days after you get that notice to dispute it in writing. If you do, the collector has to stop collecting until it sends you proof of the debt or the name and address of the original company.</p>
<p>Send your letter by certified mail and keep a copy. A collector that cannot prove the debt should not be reporting it.</p>'''),
  ('dispute','Dispute it with the credit bureaus','''<p>Send a dispute to each bureau that shows the collection. Say what is wrong and add your proof. Our <a href="/learn/dispute-letter">sample dispute letter</a> shows you how. If the collector cannot show the item is right, the bureau has to fix it or delete it.</p>
<p>If a deleted collection comes back, the collector has to certify it is accurate first, and the bureau has to tell you in writing within five business days.</p>'''),
  ('medical','Medical collections','''<p>Equifax, Experian and TransUnion no longer show paid medical collections, medical collections under $500, or unpaid medical collections until they are a year old. A federal rule that would have taken all medical debt off credit reports was struck down by a court in 2025, so larger unpaid medical collections can still show.</p>
<p>If a medical collection on your report is paid, under $500 or less than a year old, dispute it.</p>'''),
  ('yours','If it is yours and it is right','''<ul>
<li><b>Ask for a pay for delete.</b> Offer to pay in exchange for removing it from your report. The collector does not have to agree. Get the deal in writing before you pay.</li>
<li><b>Pay it.</b> It will show as paid. Some newer credit scores ignore paid collections, but many lenders still use older scores that do not.</li>
<li><b>Ask for a goodwill removal.</b> See our <a href="/learn/goodwill-letter">goodwill letter</a>.</li>
<li><b>Wait it out.</b> It comes off on its own when the time is up.</li>
</ul>'''),
  ('old','Very old debts','''<p>A collection can be reported for seven years, counted from 180 days after you first fell behind. Paying it does not restart that clock.</p>
<p>The time a collector has to sue you is a different clock set by each state. In some states, paying or promising to pay an old debt can restart it. If a debt is very old, read your state's rules before you pay or promise anything.</p>'''),
 ],
 faqs=[
  ('Does paying a collection take it off my report?','Not by itself. Paying changes it to paid, and it can stay until its time is up, unless it was a mistake, it is a medical collection, or the collector agrees to remove it.'),
  ('Can a deleted collection come back?','Only if the company certifies that it is accurate, and the credit bureau has to tell you in writing within five business days.'),
  ('Should I talk to the collector on the phone?','Writing is safer. A letter gives you a record of what you said and when, and some rights only apply to disputes made in writing.'),
 ],
 sources=['fdcpa_1692g','fcra_1681i','fcra_1681c','medical_2022','medical_court','ftc_dispute'],
 related=['dispute-letter','goodwill-letter','how-long'],
),
# ------------------------------------------------------------------
dict(
 slug='not-mine',
 title='Accounts on your credit report that are not yours',
 seo='Accounts on Your Credit Report That Are Not Yours',
 desc='Accounts on your credit report you never opened? Tell a mix up from identity theft, block the accounts in four business days and freeze your credit.',
 card='Mix up or identity theft, and how to block the accounts.',
 answer='If an account on your report is not yours, first figure out if it is a mix up or identity theft. For identity theft, report it at IdentityTheft.gov, then send that report to each credit bureau and ask them to block the accounts. They must block them within four business days. For a mix up, send a regular dispute.',
 sections=[
  ('which','Mix up or identity theft?','''<p>A mix up happens when someone with a name like yours gets mixed into your file. You will usually see their address or their accounts, but nobody applied for credit as you. Fix it with a regular <a href="/learn/dispute-letter">dispute letter</a>.</p>
<p>Identity theft looks like accounts you never opened, credit checks you never asked for, addresses you never lived at, or calls about debts you never had.</p>'''),
  ('steps','Steps for identity theft','''<ol class="list">
<li><b>Report it at <a href="https://www.identitytheft.gov">IdentityTheft.gov</a>.</b> You get an Identity Theft Report and a recovery plan with letters already written for you.</li>
<li><b>Place a fraud alert.</b> Contact one credit bureau and it tells the other two. It lasts one year. With your Identity Theft Report you can get an extended alert that lasts seven years.</li>
<li><b>Freeze your credit.</b> A freeze is free and stops new accounts from being opened in your name. You have to contact all three bureaus.</li>
<li><b>Ask each bureau to block the accounts.</b> Send your Identity Theft Report, proof of who you are, the accounts that are not yours, and a statement that you did not open them. They must block them within four business days.</li>
<li><b>Contact each company.</b> Call the fraud department of every business where an account was opened. Ask them to close it and stop reporting it, and send them your Identity Theft Report.</li>
</ol>'''),
  ('alert','Fraud alert or credit freeze?','''<table>
<tr><th></th><th>Fraud alert</th><th>Credit freeze</th></tr>
<tr><td>What it does</td><td>Lenders have to check it is really you</td><td>Lenders cannot see your report at all</td></tr>
<tr><td>Cost</td><td>Free</td><td>Free</td></tr>
<tr><td>How long</td><td>One year, or seven with an Identity Theft Report</td><td>Until you lift it</td></tr>
<tr><td>Who to contact</td><td>One bureau</td><td>All three bureaus</td></tr>
</table>
<p>Lift a freeze for a short time when you apply for a car, an apartment or a card, then put it back.</p>'''),
 ],
 faqs=[
  ('Does a credit freeze hurt my score?','No. It does not change your score, and you can keep using the accounts you already have.'),
  ('Do I need a police report?','Usually the Identity Theft Report from IdentityTheft.gov is enough. Some companies also ask for a police report.'),
  ('How is a block different from a dispute?','A block is for identity theft and has to happen within four business days. A dispute is for mistakes and usually takes up to 30 days.'),
 ],
 sources=['idt','fcra_1681c2','ftc_freeze','ftc_dispute'],
 related=['dispute-letter','collections','how-long'],
),
# ------------------------------------------------------------------
dict(
 slug='how-long',
 title='How long things stay on your credit report',
 seo='How Long Do Negative Items Stay on Your Credit Report?',
 desc='How long late payments, collections, charge offs, bankruptcy and credit checks stay on your credit report, and what to do if one stays too long.',
 card='Late payments, collections, bankruptcy and when they drop off.',
 answer='Most negative items, like late payments, collections and charge offs, can stay on your credit report for seven years. Bankruptcy can stay for ten. Hard credit checks stay for two years. When the time is up, the item should come off on its own, and if it does not, you can dispute it.',
 sections=[
  ('table','How long each item stays','''<table>
<tr><th>Item</th><th>How long</th><th>When the clock starts</th></tr>
<tr><td>Late payment</td><td>7 years</td><td>The date of the late payment</td></tr>
<tr><td>Collection account</td><td>7 years</td><td>180 days after you first fell behind on that debt</td></tr>
<tr><td>Charge off</td><td>7 years</td><td>180 days after you first fell behind on that debt</td></tr>
<tr><td>Bankruptcy</td><td>Up to 10 years</td><td>The date the case was filed</td></tr>
<tr><td>Hard credit check</td><td>2 years on your report, and FICO scores only count it for 1</td><td>The date of the check</td></tr>
<tr><td>Medical collection</td><td>Not shown if it is paid, under $500 or less than a year old</td><td>Not reported until it is a year old</td></tr>
</table>'''),
  ('reset','What does not restart the clock','''<p>Paying a debt, disputing it, or a new collector buying it does not restart the seven years. The date that counts is when you first fell behind with the original company.</p>
<p>If a collection shows a newer date than your first missed payment, it can stay on your report too long. That is a mistake you can <a href="/learn/dispute-letter">dispute</a>.</p>'''),
  ('lawsuit','Credit report time is not lawsuit time','''<p>How long something stays on your report is set by federal law. How long a collector can sue you is set by your state, and the two are different. In some states, paying or promising to pay an old debt can restart the time to sue. Read your state's rules before you pay a very old debt.</p>'''),
  ('sooner','Can it come off sooner?','''<ul>
<li>If it is wrong, dispute it. See the <a href="/guide">step by step guide</a>.</li>
<li>If it is a late payment that really happened, try a <a href="/learn/goodwill-letter">goodwill letter</a>.</li>
<li>If it is a collection, ask for a <a href="/learn/collections#yours">pay for delete</a>.</li>
</ul>'''),
 ],
 faqs=[
  ('Does paying a debt reset the seven years?','No. The clock is based on when you first fell behind, and paying does not change that date.'),
  ('Do old items still hurt my score?','Less over time. Older items count less than new ones, even before they come off.'),
  ('What if an item is past its time and still there?','Dispute it with each credit bureau that shows it and point to the date you first fell behind.'),
 ],
 sources=['fcra_1681c','ftc_dispute','fico_shop','medical_2022'],
 related=['collections','goodwill-letter','dispute-letter'],
),
# ------------------------------------------------------------------
dict(
 slug='goodwill-letter',
 title='Goodwill letter for a late payment: a free sample',
 seo='Remove a Late Payment: Goodwill Letter Sample | ZungiDill',
 desc='A free goodwill letter sample to ask a lender to remove a late payment that really happened, when it works, when it does not, and who to send it to.',
 card='Ask a lender to remove a late payment that really happened.',
 answer='A goodwill letter asks a lender to remove a late payment that really happened, as a favor. They do not have to say yes. It works best when the late payment was a one time slip, your account is current now and the rest of your history is good. It costs nothing to ask.',
 sections=[
  ('when','When it makes sense','''<ul>
<li>One or two late payments on an account that is otherwise on time</li>
<li>The account is paid up now</li>
<li>There was a real reason, like a job loss, a hospital stay, a move or an autopay change</li>
</ul>
<p>It is less likely to work for an account that is still behind, a long run of missed payments, or a debt that was sold to a collector.</p>'''),
  ('dispute','Goodwill letter or dispute?','''<p>A dispute says the item is wrong. A goodwill letter says the item is right and asks for a favor. If the late payment did not really happen, send a <a href="/learn/dispute-letter">dispute letter</a> instead. Never claim something is wrong when it is not.</p>'''),
  ('sample','Sample goodwill letter','''<pre class="letter">[Your full name]
[Street address]
[City, State ZIP]

[Today's date]

[Lender name]
[Customer service or credit reporting address]

Re: Goodwill request for account ending in [last four digits]

I have been a customer since [year]. In [month and year] I missed a payment because [one honest sentence, for example: I lost my job for two months]. I caught up as soon as I could, and my account has been paid on time since then.

That one late payment is now holding me back as I try to [buy a car, rent an apartment, get a better rate]. I am asking you, as a goodwill gesture, to remove the late payment from my credit reports.

Thank you for considering this.

Sincerely,
[Your signature]
[Your printed name]</pre>'''),
  ('send','Who to send it to','''<p>Send it to the lender, not the credit bureaus. Look for a credit reporting or customer service address on your statement or the lender's website. You can also call and ask for a goodwill adjustment. If the answer is no, you can try again later, after more months of on time payments.</p>'''),
 ],
 faqs=[
  ('Does a goodwill letter hurt my credit?','No. Asking does not change your report. The worst answer is no.'),
  ('Can I send a goodwill letter to a collection agency?','You can, but with collections a pay for delete offer usually gets further. See how to get a collection off your report.'),
 ],
 sources=['ftc_fix','ftc_dispute'],
 related=['collections','how-long','dispute-letter'],
),
# ------------------------------------------------------------------
dict(
 slug='car-loan',
 title='Car loan with bad credit: check your report before you shop',
 seo='Bad Credit Car Loan? Check Your Report First | ZungiDill',
 desc='Getting a car with bad credit? Fix mistakes on your credit report first, get preapproved by a credit union and know what to ask before you sign.',
 card='Fix your report, get preapproved and know what to ask.',
 answer='Before you shop for a car with bad credit, get your free credit reports and dispute anything wrong, then get preapproved by a bank or credit union so you know your rate before you walk in. A mistake on your report can cost you a higher rate for the whole loan.',
 sections=[
  ('why','Why your report matters at the lot','''<p>The lender sets your rate from your credit. A collection that is not yours or a late payment that never happened can push you into a higher rate, a bigger down payment or a buy here pay here lot. Fixing a mistake before you apply is the cheapest way to lower your payment.</p>'''),
  ('early','Start a month or two early','''<p>A dispute usually takes about 30 days. Get your free reports at <a href="https://www.annualcreditreport.com">AnnualCreditReport.com</a>, dispute anything wrong and give it time to clear before you apply. The <a href="/guide">step by step guide</a> walks you through it.</p>'''),
  ('preapproved','Get preapproved first','''<p>Apply with your bank or a credit union before you go to the dealer. Credit unions often work with members whose credit is not perfect. A preapproval tells you your rate and how much you can borrow, so you can compare it with anything the dealer offers. Find one near you with the <a href="https://mapping.ncua.gov/">credit union locator</a>.</p>'''),
  ('shopping','Shopping for rates will not wreck your score','''<p>FICO scores count several auto loan checks made close together as one. Older versions give you a 14 day window and newer ones give you 45. Keep your shopping to about two weeks to be safe.</p>'''),
  ('bhph','Buy here pay here lots','''<p>Some buy here pay here lots do not report your on time payments to the credit bureaus, so the loan may not help you build credit. Ask before you sign.</p>'''),
  ('ask','Ask before you sign','''<ul>
<li>What is the total price and the interest rate?</li>
<li>Do you report my payments to all three credit bureaus?</li>
<li>Is there a penalty for paying it off early?</li>
<li>What add ons are in the price, like a warranty or GAP coverage, and can I say no to them?</li>
<li>Is this rate final, or can it change after I drive off?</li>
</ul>'''),
 ],
 faqs=[
  ('Does a bigger down payment help?','Usually. A bigger down payment means a smaller loan, which can help you get approved and lower your payment.'),
  ('Will checking my own credit report lower my score?','No. Checking your own report never hurts your score.'),
 ],
 sources=['cfpb_auto','fico_shop','ncua','acr'],
 related=['dispute-letter','collections','credit-repair'],
),
# ------------------------------------------------------------------
dict(
 slug='credit-repair',
 title='Credit repair companies: what they can and cannot do',
 seo='Is Credit Repair Worth It? What the Law Says | ZungiDill',
 desc='What credit repair companies can legally do, what they cannot, the red flags of a scam, and how to do the same thing yourself for free in the same time.',
 card='What the law allows, red flags, and doing it yourself.',
 answer='A credit repair company can only do what you can do yourself for free: dispute mistakes on your credit report. By law it cannot charge you before the work is done, it has to give you a written contract, and you can cancel within three business days. Nobody can remove true information from your report.',
 sections=[
  ('law','What the law says','''<ul>
<li>They cannot charge you before they finish the work they promised.</li>
<li>They have to give you a written contract that spells out the work, the cost and how long it takes.</li>
<li>You can cancel within three business days of signing, for free.</li>
<li>They cannot tell you to lie on a credit application or to the credit bureaus.</li>
</ul>'''),
  ('flags','Red flags','''<ul>
<li>They want money up front.</li>
<li>They promise to remove everything, even items that are true.</li>
<li>They tell you not to contact the credit bureaus yourself.</li>
<li>They offer a new credit identity or a CPN. That is a scam, and using one can be a crime.</li>
<li>They dispute everything on your report, true or not.</li>
</ul>'''),
  ('compare','Doing it yourself','''<table>
<tr><th></th><th>Credit repair company</th><th>Doing it yourself</th></tr>
<tr><td>Cost</td><td>Often a monthly fee</td><td>Free</td></tr>
<tr><td>Who sees the letters</td><td>Often only them</td><td>You read every one</td></tr>
<tr><td>How long the bureaus take</td><td>Usually 30 days</td><td>Usually 30 days</td></tr>
<tr><td>Can remove true items</td><td>No</td><td>No</td></tr>
</table>
<p>The <a href="/guide">step by step guide</a> covers everything a credit repair company would do.</p>'''),
 ],
 faqs=[
  ('Is credit repair worth it?','For most people, no. Everything they can legally do, you can do yourself for free in about the same time.'),
  ('What is a CPN?','A credit privacy number, sold as a way to get a fresh credit file. It is a scam, and using one to apply for credit can be a federal crime.'),
  ('Is ZungiDill a credit repair company?','No. ZungiDill is a tool you use yourself. You decide what is wrong and you send your own letters.'),
 ],
 sources=['croa_1679b','croa_1679e','ftc_fix'],
 related=['dispute-letter','collections','not-mine'],
),
]
