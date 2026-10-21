# Worked assistant examples

Use these examples to see a complete assistant design: what the customer asks for, what belongs in each setting, how the prompt uses configured capabilities, and what a good conversation looks like. They are educational, synthetic adaptations of Famulor's demo scenarios. Their conversations and tool outcomes are illustrative, not customer transcripts or evidence of a live test.

The gallery assistants reviewed for the four scenarios below have conversation-ending capability, but no booking, ordering, order-status or CRM business tools assigned. Their business outcomes are fictional role-play. These worked examples improve that conversational inspiration into a production design with required integrations and deterministic illustrative tool fixtures. They are not clones of the gallery configuration. A polished demo conversation is not evidence that a reservation, order or CRM action happened.

## Choose one example

Read the closest example first. Load another only when it adds a behavior the task needs; do not load every example and the full API catalog together.

| You are designing | Start here | Learn from it |
| --- | --- | --- |
| Reception, accommodation enquiries or reservations | [Hotel front desk](hotel-front-desk.md) | Separate policy answers, current availability and a confirmed reservation |
| Ordering or another conversation with frequent corrections | [Drive-thru](drive-thru.md) | Maintain the customer's current choices, confirm the final request and avoid duplicate submissions |
| Customer support across voice and written channels | [Order support](order-support.md) | Retrieve the relevant facts, answer the pending question and adapt the presentation to the channel |
| A short sales discovery or qualification conversation | [Lead qualification](lead-qualification.md) | Ask relevant questions, respect a refusal and distinguish a qualified lead from a booked appointment |
| The finished proposal an agent should give the user | [Assistant deliverable](assistant-deliverable.md) | Present the prompt, settings, dependencies, expected behavior and validation state together |

The [prompt templates](../../assets/prompts/) cover additional starting points, including WhatsApp, webchat and email. Read [messaging and channels](../messaging-and-channels.md) before adapting a voice example to a written channel.

## Turn an example into the user's assistant

1. Extract the reusable behavior, such as checking availability before offering a room. Replace the fictional business, policies and sample data with the user's approved facts.
2. Read the current assistant and relevant channel configuration. Select only the capabilities the requested outcome needs.
3. Resolve the real knowledge source, integration, assigned callable names and required inputs. Do not reuse demo keys, tenant IDs, resource IDs, model choices or account data from another workspace.
4. Keep the greeting, shared system prompt, channel additions, knowledge and tool configuration in their respective places. Use the example's setting map rather than pasting the whole page into the system prompt.
5. Replace every editorial tool label or placeholder before saving. If a capability is missing, remove the claim or specify a truthful fallback. An example is not an importable assistant configuration.
6. Produce the [assistant deliverable](assistant-deliverable.md), then perform only the setup and tests the user has authorized. Report drafted, saved, tested and externally completed states separately.

## Understand the three layers

| Layer | What it means |
| --- | --- |
| Demo inspiration | A public scenario illustrates a conversational pattern. The reviewed business conversations are role-play, not evidence of connected business tools. |
| Worked example | Fictional requirements, prompts and fixed illustrative outcomes explain the desired behavior. Use the declared fixture consistently; do not invent a new result during the example. A sample successful result is not evidence that a tool ran. |
| Customer implementation | The authenticated workspace's current settings, assigned tools and actual results determine what the assistant can do. |

**Management tools and conversation tools are different.** A Famulor MCP tool that creates an assistant or reads a booking does not automatically become a callable tool inside that assistant's conversation. Assign and inspect the runtime capability separately. Map each example's tool role to the actual assigned callable name and schema before using it in a saved prompt.

Use the current workspace catalog for compatible models, voices and languages. Gallery labels are presentation choices, not API payloads. For example, Full Duplex is configured through the supported Realtime variant; do not invent a separate public engine value from a gallery label.

## What makes the result good

- The first reply addresses the customer's intent and asks only for the next missing detail.
- Short voice turns remain easy to follow; written answers use useful links and readable structure.
- Corrections update the current request without restarting intake or duplicating an action.
- Facts come from the appropriate knowledge or live tool; unsupported claims have an honest fallback.
- Success, failure and uncertain tool outcomes produce different, accurate responses.
- The final report identifies what was actually configured and verified, including any remaining dependency.

For setup detail use [assistant design](../assistant-design.md). For validation use [testing and evaluation](../testing-and-evaluation.md); an illustrative conversation is not a passed simulation, real call or delivered message.
