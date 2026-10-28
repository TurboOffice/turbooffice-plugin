---
name: termination
description: "In TurboOffice, ending a bound contract, by one party's right or by mutual release — \"the buyer is terminating during due diligence\""
---

A termination ends a bound contract. It needs that deal's bound offer: the deal's brief (`use_deal`) prints each offer's id as offer id and marks the bound contract, and `get_offer_chain` on it confirms the contract and shows what is in flight. Two instruments, and the user's words decide which: `mutual` when both parties release each other; `unilateral` when one party exercises a right it holds (name `terminatingParty`). A situation — "my buyer wants out", "the seller is walking" — is not yet a choice of instrument: ask which, and whether earnest money was delivered / how it is disbursed when that matters, before starting. Which of the two is the user's choice; a draft of the one they did not mean is paper to discard.

Three doors. `start_termination` is the paper: it mints the envelope with the request on it, and our drafter picks the state's form for the flavor, seats the signers and carries `disbursement` onto the disbursement line the paper carries. Its refusal while a draft is already in flight names that draft by the id printed as envelope id — passing it back as `reviseEnvelopeId` voids that draft and replaces it with this one, which is how a termination's terms are changed before it is signed. `record_termination` is the door for a contract the user says already ended outside the platform: it stages an approval card, and approving it runs the unwind with no instrument and no signing, and no paper on file afterward. A signed release the user brought in is neither: it is paper that came in, and recording it is the route-document skill's work. Composing is the default; take the paperless door only on the user's word that it is already done elsewhere.

Its tools: start_termination, record_termination.
