---
name: people
description: "In TurboOffice, the firm's people and their pay: bringing an agent on, who works where, an agent's pay terms — \"we're bringing on Michael, prep his agreement\", \"record Dana's split\""
---

The firm's own people: who works in which unit, a person the firm is bringing on, and what the firm and an agent agreed about the agent's pay. The tools answer for what the person may do. get_people reads the units they administer, the people in them and the people being added, and says so when they administer none. Recording pay terms takes the permission to set pay in that unit.

Bringing a person on has two states.

**Being added.** start_adding_person records who they are and the address paper for them goes to, at once. They are not on staff: nobody is emailed, and they have no sign-in and no seat. The firm's agreement with them is paper they sign. A copy nobody has signed is prepared and sent as any paper on no deal is (the sign skill: attach_file, start_signing with no `dealId`, act_on_envelope for its signers and fields and then `review_and_send`), with them as a signer at that address beside whoever signs for the firm. get_people then reads where the agreement stands (drafted, out for signatures, signed) from the signings sent to that address, and prints the signed copy's file id. stop_adding_person ends it.

**On staff.** add_person_to_staff stages a card that puts a person on the firm's staff. Approving it gives them a sign-in, takes a seat where the firm's plan counts seats, and emails their invitation at their work email, which is often not the address their agreement went to. `additionId` names the person being added it finishes. With `terms` the card also records their pay terms.

So what the person hands over decides the step. An agreement nobody has signed is prepared for signature, and the person is recorded as being added. A signed agreement is what the card's terms are read from.

**Pay terms.** get_agent_pay prints an agent's terms in force, each closing in the days asked for with how its commission divides, a month's pay for an agent paid monthly, and the units the person sets terms for, each with its standard terms. A unit's standard terms are what an agent there with no terms of their own is on: "our normal split". A person added with no `terms` is on them, and they are what a blank agreement's pay section is filled from when the person says the terms are the usual ones. record_agent_terms records an agent's terms at once, or a unit's standard terms with `agentUserId` null. Terms for a start day already on record correct that record.

Terms are lines, read in order. Each `take` line pays someone a percent or an amount out of what the lines before it left, and `rest` names who keeps what is left after the last line: the `agent` on a split, the `firm` when the agent is paid a salary or an amount a closing. Order records "off the top" and "after the split": a cut off the top is a line placed first with `of: "commission"`, and the same cut after the firm's split is that line placed after the firm's.

- `to`: `firm`, `agent`, or `other` with a `name` (a franchise, a team lead). On a firm or agent line `name` is what the agreement calls the charge.
- `feeType` and `amount`: `PERCENT` (20 means 20%) or `FLAT` dollars. `of` says what a percent is of: `rest`, what is left when the line runs, or `commission`, the whole of it.
- `yearlyLimit`: the most the line takes in a cap year, which starts on `capYearStart` (MM-DD). A cap on what the firm keeps is a limit on the firm's line. Give that line an `id` so another line can refer to it.
- `when`: the line runs only when every condition stated holds. `source` is who supplied the deal's client (`firm`, `team`, `own`). `afterLimitOf` and `untilLimitOf` name a line's `id` whose yearly limit has, or has not, been reached. `fromGross` and `untilGross` are the year's commission so far.
- Beside the lines: `base_pay`, dollars a month the firm pays the agent, with `commission` `higher` when a month pays the base or the commission, whichever is more, and `plus` when it pays both; `monthly_fee`, dollars a month the agent pays the firm; and `other`, a term the lines cannot say, kept in the agreement's words and not applied by the numbers.

Three agreements as terms:

An 80/20 split until the firm has kept $16,000 in a year starting January 1, then the agent keeps it all less $250 a closing:
`{"capYearStart":"01-01","rest":"agent","entries":[{"kind":"take","to":"firm","name":"Split","feeType":"PERCENT","amount":20,"id":"split","yearlyLimit":16000},{"kind":"take","to":"firm","name":"Transaction fee","feeType":"FLAT","amount":250,"when":{"afterLimitOf":"split"}}]}`
The first $10,000 closing of a cap year: $8,000 to the agent, $2,000 to the firm. A $10,000 closing after $80,000 of commission that year: $9,750 to the agent, $250 to the firm.

A 6% franchise royalty off the top, then 70/30:
`{"capYearStart":"01-01","rest":"agent","entries":[{"kind":"take","to":"other","name":"Franchise royalty","feeType":"PERCENT","amount":6,"of":"commission"},{"kind":"take","to":"firm","name":"Split","feeType":"PERCENT","amount":30}]}`
The first $10,000 closing of a cap year: $600 to Franchise royalty, $6,580 to the agent, $2,820 to the firm.

A salary of $4,000 a month and $500 for each closing:
`{"capYearStart":"01-01","rest":"firm","entries":[{"kind":"base_pay","amount":4000,"commission":"plus"},{"kind":"take","to":"agent","name":"Closing bonus","feeType":"FLAT","amount":500}]}`
The first $10,000 closing of a cap year: $500 to the agent, $9,500 to the firm. A month with that one closing: the firm pays the agent $4,500.

An agreement is recorded from what its pages state: each term as its own entry in the order the agreement applies them, and the file's id as `artifactId`, which ties the terms to that paper. A blank the agreement leaves empty states nothing. The start day is the agreement's effective date; with none stated, it is a question for the person.

The answer to a recording, and the card's `commits` line, say the terms back in dollars on a $10,000 closing. Those dollars are worth reading against the agreement before the person sees them: a figure the agreement would not pay is a misreading, corrected by recording the terms again.

Its tools: get_people, start_adding_person, stop_adding_person, add_person_to_staff, get_agent_pay, record_agent_terms.
