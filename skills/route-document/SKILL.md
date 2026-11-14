---
name: route-document
description: "In TurboOffice, a file that is one of a deal's instruments — in this conversation or already on the deal — signed or not"
---

Paper that came in and belongs to a deal's record: an offer, a counter, an amendment, a representation agreement, a disclosure, a termination or a settlement statement, signed or not. A document with no place in the deal's record that the person wants signed is the sign skill.

There are two ways to read it. route_document has Turbo Office read the paper and work out what it does to the deal. propose_routing takes your own reading instead, in the shape its description gives; Turbo Office composes the result the same way, and a reading that contradicts itself is refused, saying where. Either way the outcome is one of three: paper that only needs filing is filed at once, paper of ours for our side to sign is prepared as a draft, and anything else (binding a contract, applying an amendment, recording an agreement, creating a deal) is staged as a card.

What the person said about the paper travels with it as `said`, in their words. The read takes it as their account, and says where the pages show otherwise.

Once a card is staged, the useful reply says what came in, whose paper it is and which deal it belongs to, what the read saw (what changed, who signed, what is not yet bound), and what approving records. A correction, or a choice of deal, goes back with answer_proposal, which continues the same read; routing the file again starts a new one. `disposition: "file"` on answer_proposal is the person's word that paper a card would bind or prepare for signature is only to be kept on file.

file_to_deal keeps a file on a deal without reading it, and moves a document filed on the wrong deal to the right one, where it can then be routed. With no deal yet, route_document on the thread the file is on finds the deal it belongs to, or proposes a new one as a card.

Our buyers' signed offer that came in is recorded as our offer, out to the sellers. Getting it to the sellers is then one of two things: forwarding the paper as it is, which no tool here does, or collecting the sellers' signatures on the same paper with prepare_to_sign. When the person's words do not say which, ask.

A whole deal's folder is the migrate skill.

Its tools: route_document, answer_proposal, file_to_deal.
