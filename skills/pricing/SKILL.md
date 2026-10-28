---
name: pricing
description: "In TurboOffice, a deal's pricing and its agreement's period: move a listing or a buy deal to another pricing plan, adjust its commission or a fee, extend or shorten the listing or engagement period, or draft a new agreement rather than an amendment — \"move the Kaden listing to the 2.5% plan\", \"drop Kaden's commission to 2.75\", \"extend the listing through March\", \"the sellers want a new listing agreement, not an amendment\""
---

A deal is priced on a plan: the firm's terms for a listing or a buyer (a commission, fees, the length of the listing or engagement period), some of them adjustable. The deal brief's Pricing block prints the plan the deal is on, its terms, where the agreement stands, and the plans the lead can price on, each with its planId= and each adjustable entry with its entry=. The agreement states the pricing: what is signed is what the deal records, and the plan is only the starting point.

`act_on_deal({ action: { intent: "pricing", ... } })` changes it, on a listing or a buy deal: `planId` moves the deal to another plan, starting from that plan's own amounts; `overrides` sets an adjustable entry's `amount` by its `entryId`, and the adjustments already made carry; `termEnd` is the day the listing or engagement period ends (YYYY-MM-DD); `formId` puts the agreement on another form, one the brief lists under Pricing with its formId= (a firm's own listing agreement rather than the association's, say), and otherwise the form follows the plan. Any of them may go together. What it does follows where the agreement stands:
- no agreement drafted yet: it runs at once, and the terms are written in when the agreement is prepared;
- a draft, or an agreement out for signatures: an approval card replaces it with a new draft on the new terms, and the card names what is lost (edits made on the draft, signatures collected);
- signed: an approval card drafts an amendment the clients sign, or with `paper: "agreement"` a whole new agreement beside the signed one, which replaces it once everyone signs. The signed terms stay in effect until then, and an amendment that only moves the period changes no pricing. A form names the agreement a change drafts, so on a signed agreement it goes with a new agreement; an amendment is drafted on its own form.
Nothing changes until the user approves the card, and its line says what approving drafts, withdraws or emails. While an amendment is drafted, another change is refused and the refusal names it: it is finished or voided on the deal's Documents card. The drafted amendment or agreement is then prepared and sent from the Documents card like any paper, and the deal records its terms when everyone signs.

The Agreement period need opens 30 days before a signed agreement's period ends and stays after the end; an amendment moving the end, or a new agreement, retires it once signed.

A plan's entries and fee types are the plan's: a flat commission where the plan states a percent, or a fee the plan does not have, is another plan, so name the plans the lead has. The commission confirmed at a closing is recorded with the close (the deal skill's `act_on_deal` `close`), and a listing's list price is the deal skill's `list_price`.

Its tools: act_on_deal.
