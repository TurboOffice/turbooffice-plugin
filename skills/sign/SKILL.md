---
name: sign
description: "In TurboOffice, a document to send out for signature that is not one of the deal's instruments — \"get the attorney's signature on this exhibit\", \"prep this affidavit to sign\""
---

A document that needs signatures and is not one of the deal's instruments: an exhibit, an affidavit, a brokerage's own form. Paper that is one of the deal's instruments (a representation agreement, an offer, a counter, an amendment, a termination) goes to route_document whatever its signatures, so that the deal learns of it; a standalone envelope would be signed without the deal knowing.

It needs the PDF. attach_file puts a file on a thread, and start_signing builds a signing envelope from the files named: one document per form it recognizes, with a field for each signer role the form carries, less any line that is already signed. A photo of a page is an image and is refused by name. Each call is one envelope, and `envelopeId` adds paper to a draft already started. `dealId` says where the envelope lives; leave it off for paper on no deal.

Paper that matches no form arrives with no signing fields. When the person asked to get it signed, place them (the signers skill). When they only handed it over, say it has none.

The answer names the roles that still need a signer. Third parties are added with act_on_envelope `change_signers`, from the name and email the person gives. Nothing is sent until act_on_envelope `review_and_send` stages the send as a card and the person approves it.

Its tools: start_signing, act_on_envelope.
