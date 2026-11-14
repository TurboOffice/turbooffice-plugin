---
name: signers
description: "In TurboOffice, who signs and where: add, replace or remove a signer on a draft or on paper out for signatures, add a seller or buyer to a deal, take one off or put one on or off title (a listing or buyer agreement's signers follow the deal), add, move or remove a draft's signing fields, put them back to the form's own — \"add a signer to the listing agreement\", \"Jordan's signature is on the wrong line\", \"reset the form\""
---

Who signs a piece of paper, and where on it.

read_document shows one document of an envelope as it stands: each page's rows, the blanks, the fields already there with who owns each, and any ink, with the ids a change names. Naming a `page` returns its picture with the fields drawn on it. It is the usual first step before adding or moving a field.

act_on_envelope does the work on one envelope:

- `change_signers` adds, replaces or removes a signer. On a draft it runs at once; on paper out for signatures it stages a card.
- `change_fields` adds, moves, removes or re-assigns a draft's signing fields, every change of a request in one call. A field that overlaps another field or a mark on the page still lands, and the answer says by how much. Whether a line is already signed is yours to read from the page.
- `reset_layout` puts a draft's fields back to the form's own.
- `signing_order` sets who is asked to sign first.
- `move` puts a signing envelope on another deal, or off its deal.
- `review_and_send` stages the send as a card.

A listing or buyer agreement takes its client seats from the deal's sellers or buyers. A person who belongs on that paper is added to the deal with change_parties, and the draft reseats itself. change_parties also takes a seller or buyer off a deal, puts one on or off title, or corrects a name, email or phone; each is a card that says who is emailed and what paper is voided, redrawn or sent again.

The form's roles are the seats by default. A person the form has no line for can still be seated by role, and a field placed for that role gives the seat its line; a seat with no line when the draft is sent is left off. A seat that has already signed is not changed in place: the paper is pulled back and prepared again.

Its tools: act_on_envelope, read_document, change_parties.
