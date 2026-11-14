---
name: forms
description: "In TurboOffice, a form from the brokerage's library that no other skill composes — a disclosure, an addendum, a repair request, a touring or agency agreement, the brokerage's own form — the paper a deal still owes (its listing or buyer agreement, the seller's disclosure), and a new buyer client started on their representation agreement — \"start a touring agreement for Dana\", \"draft the listing agreement on Wren Hollow\""
---

The brokerage's library of standing forms and agreements, the paper a deal still owes, and a new buyer client's representation agreement. An offer, a change of terms and a termination each have their own skill, which knows the deal and the offer's chain; a blank copy of the same form would skip both.

The library is read by Turbo Office's own assistant, not from here. start_form takes the form in the person's words (`request`), and the assistant finds it in the library of the deal's state, or of the state the person is licensed in. When the words fit more than one form the answer asks which, and the next call names it. The form starts blank, as a draft: revise_draft has the drafter fill it, or the person fills it in Turbo Office.

Paper a deal still owes is a need on the deal: its listing or buyer agreement, the seller's disclosure. get_deal lists the needs with their keys. draft_need prepares that need's own paper with the deal's form, terms and signers, where a blank copy from the library would meet nothing; start_form names the need when it is asked for one. A listing agreement is prepared on a listing that has a list price, which `listPrice` records first. A seller's disclosure whose questionnaire still has open questions answers with what its packet holds and what is open. The sellers are invited to answer it themselves, and answers the person gives can go back as `answers`.

start_buyer_engagement starts a new buyer client: it creates the buy deal and prepares the agreement on it. The commission is the one the person stated, so when they gave none it is a question back. A choice they have not made (which brokerage, which of two agreements, a second engagement for a buyer who is already a client) comes back as a question, and the next call carries their answer. A deal that already owes the agreement uses draft_need, and an agreement the person uploaded is read with route_document.

Its tools: start_form, draft_need, start_buyer_engagement.
