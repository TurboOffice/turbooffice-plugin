---
name: agreement-terms
description: "In TurboOffice, a deal's pricing and its agreement's period: move a listing or a buy deal to another pricing plan, adjust its commission or a fee, extend or shorten the listing or engagement period, or draft a new agreement rather than an amendment — \"move the Kaden listing to the 2.5% plan\", \"drop Kaden's commission to 2.75\", \"extend the listing through March\", \"the sellers want a new listing agreement, not an amendment\""
---

A deal is priced on a plan: the firm's terms for a listing or a buyer (a commission, fees, the length of the listing or engagement period), some of them adjustable. The agreement states the pricing. What is signed is what the deal records, and the plan is the starting point.

get_pricing reads what the deal is priced on, where its agreement stands, and what a change can name: the plans it can move to, each adjustable entry, and the agreement forms, with their ids. get_deal prints the current terms.

act_on_deal `pricing` changes it. `planId` moves the deal to another plan, `overrides` sets an adjustable entry's amount, `termEnd` is the day the period ends, and `formId` puts the agreement on another form; they can go together. What happens follows from where the agreement stands:

- Nothing drafted yet: the change runs at once, and it is written into the agreement when that is prepared.
- A draft, or an agreement out for signatures: a card replaces it with a new draft on the new terms, and names what is lost (edits made on the draft, signatures collected).
- Signed: a card drafts an amendment for the clients to sign, or, with `paper: "agreement"`, a new agreement that replaces the signed one once everyone signs. The signed terms stay in effect until then.

While an amendment is drafted, another change is refused, and the refusal names the amendment. The drafted paper is sent like any other, and the deal records its terms when everyone has signed.

A plan's entries are the plan's own. A flat commission where the plan states a percent, or a fee the plan does not have, is a different plan, so it helps to name the plans available. The Agreement period need opens 30 days before a signed agreement ends and stays open after it has ended; moving the end, or a new agreement, settles it once signed. Both are open to an agreement whose period is already over. The commission confirmed at a closing is recorded with the close (act_on_deal `close`), and a list price is act_on_deal `list_price`.

Its tools: act_on_deal.
