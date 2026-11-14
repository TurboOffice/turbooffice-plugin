---
name: contract
description: "In TurboOffice, an offer that already exists, ours or theirs, and everything done to it after: a change to its terms whatever the request calls it — \"move closing on the Brooks contract to Aug 19\", \"drop Philip's price 5k and give them until Friday\" — pulling our own paper back (discard a draft, withdraw a sent offer, recall it to edit, bring back a withdrawn one, record that the other side signed it, record the contract from a file already on the deal), answering theirs (decline, set aside or accept their counter or amendment, mark the buyers' offer not accepted, record that they rejected or withdrew, undo any of those), ending a bound contract by one party's right or by mutual release — \"the buyer is terminating during due diligence\" — and fixing what the platform's RECORD of an offer says the paper contains — \"the earnest money on Philip's offer is 5k not 500\". A new offer with no paper yet is the `offer` skill"
---

Everything done to an offer that already exists, ours or theirs: changing its terms, answering the other side's paper, pulling ours back, ending a bound contract, and correcting what the record says the paper contains. A new offer with no paper yet is the offer skill. Which kind of work a request is follows from what it asks for more than from the word it uses: "amendment", "counter" and "update" can all mean a change of terms.

Start from the record. get_deal lists the deal's offers and marks the contract. get_offer_chain reads one offer: the terms on record, each piece of paper on it with its paper id and its envelope id, who has signed, what is waiting on an answer and what is in flight. read_file opens the paper itself when a request turns on its wording.

The person's account of where things stand outranks the record. When they say the other side signed something the chain shows as out for signatures, the record is behind, and recording that usually comes first (record_execution).

## A change to the terms

start_change records the change as a proposal on the offer's chain and hands the paper to the drafter. `facts` states what changes and nothing else, against the terms get_offer_chain shows. The paper it takes follows from where the deal stands: on a bound contract it is an amendment, and on an offer not yet bound (sent, countered, or expired unsigned) it is a counteroffer or modification. A counteroffer carries its own time limit to accept, so that is worth asking for when the person gave none. The answer says which paper it is.

- A counteroffer of ours replies to their pending counter. When their amendment is pending on a bound contract, `answers` says whether ours replies to it (it contends for the same terms) or stands beside it (independent terms). That is the person's call, and an amendment waits for it.
- More than one amendment of ours can be out at once, and each applies in the order it is signed. A counteroffer of ours is one at a time.
- An offer of ours that expired has two ways back. A counteroffer keeps the clients' signatures on the offer and asks them to sign one more page. withdraw_paper `recall` brings the whole offer back as a draft, to be signed again. When the person's words do not pick one, offer both.
- Different terms on an offer of ours that is still a draft, or out for signatures and not yet signed by the other side, is an edit to that offer: revise_draft on its draft, after a recall when it is out.
- When the deal has no contract recorded and the person wants to change one, the contract's own file is routed first (route_document), and the change follows once that card is approved.

## Their paper, and pulling ours back

- prepare_to_sign opens paper someone already signed as a packet for the signatures it still needs: the other side's offer, counter or amendment for the person's clients, or the person's own paper, signed outside Turbo Office, for the other side. Opening it signs and sends nothing. Their paper is accepted when the clients have signed it.
- decide_their_paper turns down their counter or amendment (`decline`), or sets aside one that was made against terms that have since changed (`set_aside`).
- end_offer ends an offer that is not bound: `rejected` when the side that received it turned it down, `withdrawn` when the side that made it took it back. reopen_offer undoes either, or a decline, at once, while the offer's paper is still in play. Ending our own offer voids its paper, so that one comes back through a recall: a fresh draft, and the offer reopens when it is sent.
- withdraw_paper pulls our paper back. `recall` returns our sent offer to an editable draft. `void` cancels a counter, an amendment or a standalone signing of ours, and start_change composes a replacement afterwards.
- record_execution records, on the person's word, that an instrument was signed outside Turbo Office. `retract` takes a recording back, and `waive_copy` stops asking for the signed copy.

Each of these except reopen_offer stages a card, and its `commits` line says what approving does. Paper the person called signed earlier in the conversation and now asks to pull back is a contradiction, and it is worth raising before any card.

## Ending a bound contract

There are two instruments, and the person's words choose between them: `mutual` when both parties release each other, `unilateral` when one exercises a right it holds. "My buyer wants out" is a situation and not yet a choice, so it is usually a question back, together with whether earnest money was delivered and how it is to be disbursed. start_termination drafts the paper, and records the request it was started with: which instrument, who is terminating, whether earnest money was delivered and how it is disbursed. A change to any of those is start_termination again with `reviseEnvelopeId`, which replaces the draft and its request together; revise_draft changes the paper's wording and leaves the recorded request as it was. record_termination is for a contract the person says already ended outside Turbo Office; approving its card unwinds the deal with no paper. A signed release the person hands over is paper that came in, which is route_document.

## Correcting the record

A correction fixes what the record says the paper contains. It does not change what the parties agreed: a price or a date they have since agreed to is a change to the terms. read_recorded_terms lists each recorded term with the key a correction names, and correct_record stages the corrections as a card. Each change says how it was checked: `verified_agrees` or `verified_contradicts` when you read the term in the paper with read_file and can quote it, `unverified` when you did not. The person is the authority on their own record. When the paper contradicts what they ask for, say what you read and ask once; if they confirm, record it as `verified_contradicts`. Not being able to check is not a reason to decline.

A refusal from any of these names the door that works, so it is usually the next step.

Its tools: start_change, withdraw_paper, record_execution, route_document, decide_their_paper, prepare_to_sign, end_offer, reopen_offer, start_termination, record_termination, read_recorded_terms, correct_record.
