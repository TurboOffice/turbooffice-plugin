---
name: cma
description: "In TurboOffice, a CMA — pricing a home from the sales around it — \"run a CMA on 117 Terrace Dr\", \"what should we list the Loridans house at?\""
---

A CMA prices one home from the nearby sales, on its own page, where Turbo chooses the sales a buyer would also tour, places the home among them and says why. It needs the home: a listing deal on your roster (its dealId), or the home's address, which `work_on` looks up in the MLS. `request` is Turbo's first message on the CMA: the user's ask in their own words, with everything they told you about the home (its condition, what was updated, the price they have in mind) — Turbo sees nothing else from this chat, and adds nothing you did not hear. A start opens the CMA page and Turbo is already working there, so start it and say where it is. An address that matches several homes is refused with the list: ask which one and pass it as `mls`. A home that is neither in the MLS nor a listing on your roster cannot have a CMA yet; say so.

Its work runs in Turbo Office's own assistant, not here: hand it to `work_on` with the person's words and what you know (`request`; `dealId` when you know the deal; `threadId` to say more on a thread it started). Where this guide names `work_on` with arguments, put them in the request's words.
