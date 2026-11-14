---
name: cma
description: "In TurboOffice, a CMA — pricing a home from the sales around it — \"run a CMA on 117 Terrace Dr\", \"what should we list the Loridans house at?\""
---

A CMA prices one home from the sales around it. Turbo, Turbo Office's pricing agent, chooses the sales a buyer would also tour, places the home among them and says why, on a page of its own.

It needs the home: a listing deal (its `dealId`), a buy deal with the `address` its buyers are after, or an `address` on no deal. An address is looked up in the brokerage's MLS data and, when the MLS has no record of it, in the county's public record. `request` is the person's ask in their words, with what they said about the home (its condition, what was updated, the price they have in mind): Turbo sees nothing else from this conversation.

start_cma answers with the CMA's thread and its link. Pricing usually takes one to two minutes. get_thread reads where it stands, and revise_cma asks Turbo for a change, a note, or the client report's link. An address that matches several homes is refused with the list: ask which one, and pass it as `mls`. A CMA needs the brokerage's MLS data connected, which whoami says.

Its tools: start_cma.
