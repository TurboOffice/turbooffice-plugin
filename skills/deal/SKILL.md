---
name: deal
description: "In TurboOffice, the deal itself, its clients or its photos: archive a deal or take it out of the archive, move it between the stages before a contract, change a listing's list price, add, reorder, caption or download a listing's photos or pick its cover, close a deal (one whose contract was signed outside the app too) or correct a closed deal's price, day or commission, move a contract's closing date, share uploaded files with the clients, correct a seller's or buyer's name, email or phone, add someone from the brokerage to the deal's team or take them off it — \"add Jed to the Brooks deal\", \"archive the old Kaden deal\", \"send the inspection to the sellers for their records\", \"Kaden's email is wrong, it's kaden@gmail.com\", \"we're live, mark it listed\", \"drop the list price to 425\", \"it closed Oct 7 at 262k\", and a sale that already closed off the platform, recorded so it counts in the agent's closed numbers — \"add my closing on 4 Elm St from March, 412k, 3%\""
---

The deal itself: its stage, team, clients, list price, dates, close and photos.

act_on_deal acts on one deal, and its description says which actions run at once and which stage a card. In practice:

- Status and team changes (`stage`, `list_price`, `go_live`, `unarchive`, `add_teammate`, `remove_teammate`) run at once, and the answer says what changed. A teammate's user id comes from find_teammates, and nobody is emailed.
- `archive` runs at once on a deal with nothing out for signatures. With paper out it is a card, because archiving voids that paper and tells its signers.
- `close` records the closing with its day, its price and, when the person stated one, the commission. It also corrects a close already on record, and `close_commission` changes the commission alone.
- `contract_date` moves a date on the contract that the parties moved without papering it. A date the record got wrong is a correction, and a move the parties still have to sign is an amendment; both are the contract skill's.
- `share_documents` emails the deal's clients that files are on their deal page. `send_contract_copy` emails the signed copy of a contract that was recorded as signed outside Turbo Office. `contact_clients` turns on the emails Turbo Office sends a deal's clients on its own, which a deal created from paper starts without.
- Pricing, commission and the agreement's period are the agreement-terms skill.

Which deal is meant is the person's to say. search_deals finds it by address or client, and "the old one" or "the one with the wrong email" is read against what get_deal shows. A deal's stages under contract come from its paper: the signed contract puts it under contract, and a termination ends it (the contract skill).

change_parties `contact` corrects a seller's or buyer's details on every deal they are on, as a card. An email the client already signs in with is changed by support, and the refusal says where to reach them.

record_closed_deal records a sale that closed outside Turbo Office as a new deal, already closed, from the price, day and commission the person stated; one they did not give is worth asking for. A sale on a deal the person already has is that deal's `close`.

A listing's photos are its gallery: the cover first, then the rest in the agent's order. list_photos reads it. act_on_photos adds images from a thread (attach_file), removes one, reorders them, picks the cover, writes a caption or gives download links, each at once. A photo of a document is a file to read and not a gallery photo, and nothing here edits a photo.

Its tools: act_on_deal, change_parties, record_closed_deal.
