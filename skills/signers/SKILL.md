---
name: signers
description: "In TurboOffice, who signs and where: add, replace or remove a signer on a draft or on paper out for signatures, add a seller or buyer to a deal, take one off or put one on or off title (a listing or buyer agreement's signers follow the deal), put a draft's signing fields back to the form's own — \"add a signer to the listing agreement\", \"reset the form\""
---

`act_on_envelope({ envelopeId, action: { intent: "change_signers", change } })` adds, replaces or removes a signer on any envelope of the deal, at any stage — `envelopeId` is the id printed as envelope id (the chain receipt, `list_files`): a draft changes at once, and paper out for signatures gets an approval card. `change_parties({ change })` adds a seller or buyer to the chosen deal (`use_deal`), takes one off it, puts one on or off title, or changes one's name, email or phone, as an approval card — the door for a person who belongs on the listing or buyer agreement, whose seats follow the deal's sellers and buyers. `act_on_envelope({ envelopeId, action: { intent: "reset_layout" } })` takes every added field off a draft and puts the form's own fields back for the seated roles. A person who belongs on the listing or buyer agreement is added to the deal, never seated on the draft: its seats are the deal's sellers or buyers. Each refusal names the door that works.

Its tools: act_on_envelope, change_parties.
