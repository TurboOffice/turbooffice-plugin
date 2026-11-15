---
name: migrate
description: "In TurboOffice, a whole deal coming over from another system with its paper, live or already over — \"here is the Dotloop folder for 12 Oak St, bring it over\""
---

A deal arriving with its paper from another system: a Dotloop loop, another platform's export, a folder of PDFs.

A good migration starts with the whole pile. Gather every file for the deal (attach_file puts each on a thread), and ask for more when the pile points at paper it does not hold. Then sort it: the representation agreement, the operative contract, its amendments, a termination or a withdrawal, offers that died and counters a later one replaced, duplicates, supporting paper, and paper that belongs to another deal. Reading as far as it takes to say what each one is is usually enough. From the sorted paper it follows whether the deal is over (closed, terminated, withdrawn, expired) or still in play.

Before anything is committed, tell the person the plan: the deal it goes on (one of theirs, or a new one), the paper it commits and in what order, and what the deal will still owe afterwards, naming what this pile cannot meet. Where the paper and the person disagree, that is a question for them. Commit after their yes.

propose_routing takes the whole plan in one call: `instruments` in the order the paper was signed (the agreement, the contract packet with its counters and addenda, each executed amendment, a termination), each with its files and your reading, and `supporting` for the rest. One card says what approving does to each piece. route_document is the same door with Turbo Office reading one paper at a time. A card whose reading differs from the plan is the place to stop and say how, and the person's correction goes back with answer_proposal.

- A sale that already closed is record_closed_deal, with the price, day and commission from the paper; one the paper does not state is asked for. A sale on a deal the person already has is that deal's close.
- An offer that died, or a counter a later one replaced, is filed with file_to_deal and not routed: it does nothing to the deal.
- A deal that ended without a sale has no door of its own. It can come over on the person's word as a live deal and then be archived.
- An agreement in the pile that nobody signed is history, filed as supporting paper.

Paper coming over is sent to no one. A deal created from paper keeps Turbo Office's own emails to its clients off until the person turns them on (act_on_deal `contact_clients`), and a deal that already exists keeps the setting it has. Paper the person sends for signatures reaches its signers either way.

Its tools: route_document, answer_proposal, file_to_deal, record_closed_deal, act_on_deal.
