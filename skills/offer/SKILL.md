---
name: offer
description: "In TurboOffice, an offer on a property — from our buyer, or written up on the caller's own listing — \"offer on 155 Main St, 540k, 10-day DD, close in 30\""
---

An offer on a home, from the person's buyer or written up on their own listing. It needs the home, and an address is enough: the buyer need not have a deal yet, and a new address is the usual case.

start_offer creates the offer's draft and hands it to Turbo Office's drafter with the person's request. The drafter finds the home, loads the state's forms, fills the terms the person gave and asks about the ones it still needs. Collecting missing terms is the drafter's part, so the request is best passed early and whole: `request` carries every term they stated, in their words. The start answers within about 25 seconds with the drafter's thread as it stands: often still running, sometimes already done or stopped on a question. get_thread reads on, and revise_draft carries a change, or the answer to a question the drafter asked.

`dealId` is the buyer's buy deal when they have one for this purchase, or the person's own listing when the offer is written on it; the seller is then their client, and the drafter reads the listing's documents on file. With no deal the offer starts on its own. It can still be drafted and sent, and it is recorded as an offer once its paper is on a deal: act_on_envelope `file_on_new_deal` makes a buy deal for its buyers, and revise_draft puts it on a deal that exists.

Nothing is sent by starting. When the person is ready, act_on_envelope `review_and_send` stages the send as a card. An offer's terms are read from its paper before it goes out: when they have not been read yet, the first review starts that read (two to three minutes) and stages no card, and the same call once the read has finished stages it. Someone drafting for several agents names whose paper it is with `forUserId`.

Its tools: start_offer.
