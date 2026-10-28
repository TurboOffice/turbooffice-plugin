---
name: closed-deal
description: "In TurboOffice, a sale that already closed off the platform, recorded so it counts in the agent's closed numbers — an off-market deal, a closing from before the agent joined — \"add my closing on 4 Elm St from March, 412k, 3%\""
---

A record of the past: `record_closed_deal` creates a new deal already closed from what the user stated, and nothing is drafted or sent. A sale on a deal the person already has (their listing or buy deal at that address) is never recorded here: find that deal among theirs by the address, and close it with the `deal` skill's `act_on_deal` `close`. `record_closed_deal` refuses such a sale and names the deal.

Its tools: record_closed_deal.
