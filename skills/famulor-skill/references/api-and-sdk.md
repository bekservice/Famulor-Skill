# REST API, CLI, SDK and MCP

Use the interface already connected to the user's workspace. MCP fits interactive AI work; the CLI fits terminal work; the TypeScript SDK fits a server application; REST fits other languages. They share workspace resources, but authentication grants, availability and schemas must be checked for the chosen interface.

## Find any endpoint

The [complete operation index](api/index.md) covers **487 public REST operations across 40 areas**, reviewed on 2026-10-21. Every entry maps the public operation ID to its HTTP method/path, actual generated CLI command and `client.api` SDK method. The [MCP references](toolsets/assistants.md) separately cover the MCP tools; counts and names differ because some capabilities use several tools or an action selector.

For exact request shapes without loading the entire catalog:

```bash
python3 skills/famulor-skill/scripts/find-operation.py --search assistant
python3 skills/famulor-skill/scripts/find-operation.py createAssistant
python3 skills/famulor-skill/scripts/find-operation.py update-whatsapp-sender-profile
```

From an installed skill folder, shorten the path to `scripts/find-operation.py`. Output includes path/query/header parameters, required fields, type and enum constraints, request content types, actual CLI flags, response status/media types and only the reachable schema definitions. This is a dated discovery aid, not a validator. Business rules and permissions remain enforced by the server. Check the [current API reference](https://docs.famulor.io/api-reference/introduction), live MCP schema or installed client help before execution. Request examples, default values, descriptive prose and response property schemas are intentionally absent from the bundled JSON.

Do not infer MCP arguments from REST parameters or convert an SDK method into a tool name. For example, an action endpoint may correspond to several MCP tools. Discover the tool's actual input schema.

## Connect to the correct workspace

- **MCP:** use `https://app.famulor.io/mcp`, or the customer's own domain, and complete the client's OAuth sign-in. The workspace needs **Connect AI / MCP**. Filter discovery with `?toolsets=assistants,calls` when useful; this does not extend the credential's permissions.
- **REST, CLI and SDK:** use the public API at `https://app.famulor.io/api/v1` or `https://YOUR_DOMAIN/api/v1`. Ordinary API access requires **API Access**. Approved billing recovery operations have their own documented exception.
- **Workspace credentials:** an API key belongs to one workspace. Keep separate CLI profiles or SDK clients for separate workspaces. Never change a workspace identifier to bypass a key's boundary.
- **Secrets:** use the client's OAuth flow, the CLI's interactive login, or a server-side secret store. Do not request secrets in chat, put them in a prompt, publish them in a repository, or embed them in a website/mobile bundle. Public request fields that accept a secret are input contracts, not permission to expose its value.
- **Browser steps:** account consent, channel authorization and payment completion can require the user in a browser. Creating an authorization or checkout link is not completion.

The [MCP connection guide](https://docs.famulor.io/mcp/overview) explains full custom connections and the limited read-only directory profile. Installing this skill does not upgrade a limited connector or grant access to additional operations.

## CLI workflow

Requires Node.js 22 or newer. Install and authenticate in the intended workspace:

```bash
npm install --global famulor
famulor auth login
famulor auth whoami
famulor commands assistant
famulor create-assistant --help --output json
famulor list-assistants --limit 10 --output table
```

Path parameters are positional. Query and top-level body fields become flags; nested objects/arrays accept JSON or files. Exact flag names are in help and the bundled lookup, including flags renamed to avoid global-option collisions.

```bash
# Inspect the existing assistant first.
famulor get-assistant ASSISTANT_ID

# Preview an authorized prompt update without sending it.
famulor update-assistant ASSISTANT_ID --system-prompt @prompt.md --dry-run

# After the requested content is ready, save and read back.
famulor update-assistant ASSISTANT_ID --system-prompt @prompt.md
famulor get-assistant ASSISTANT_ID
```

Replace `ASSISTANT_ID` with an ID returned by the current workspace. File input is supported for full JSON bodies with `--input request.json`. On updates, a supplied object or array can replace the stored collection: merge deliberately and preserve entries outside the requested change.

`--dry-run` sends no API request. It can still print sensitive request-body content, so inspect output privately and avoid sharing it unredacted. Some destructive commands require `--yes` in automation; the flag supplies client confirmation, not user authorization. Outbound calls and campaign starts can execute without an interactive prompt, so do not rely on the CLI to decide whether outreach was requested.

Use `--all` for supported paginated lists, `--output jsonl` for pipelines and `--output-file` for binary output. Four browser-oriented operations are deliberately hidden from the normal command interface in this snapshot; their index entries identify a browser/raw-API route instead of advertising a direct command. Read [the CLI guide](https://docs.famulor.io/cli/overview) for profiles, output and login details.

## TypeScript SDK workflow

The `famulor-sdk` package is the customer-facing **server SDK**. It is different from a model-provider AI SDK. It manages Famulor resources through the public API; it does not implement a browser chat transport.

```bash
npm install famulor-sdk
```

```typescript
import { Famulor } from 'famulor-sdk';

const client = new Famulor({
  apiKey: process.env.FAMULOR_API_KEY,
});

const { data: assistants } = await client.assistants.list({ limit: 10 });
console.log(assistants.map(({ id, name }) => ({ id, name })));
```

The application supplies credentials explicitly; the SDK does not load `.env` files, select a workspace or run an OAuth consent flow. For a white-label workspace, supply its full HTTPS API base URL. For OAuth, supply `accessToken` instead of `apiKey`, never both. A token callback can retrieve the current token from your server's token store; your application owns refresh.

Every indexed operation is available through the generated `client.api` surface in the corresponding SDK contract. Resource aliases are convenient, but do not invent an alias when one does not exist:

```typescript
const { data: assistant } = await client.api.getAssistant({
  path: { id: assistantId },
});

// Only the user's requested field is included in this authorized update.
await client.api.updateAssistant({
  path: { id: assistant.id },
  body: { system_prompt: approvedPrompt },
});

const verified = await client.api.getAssistant({
  path: { id: assistant.id },
});
```

Inputs are grouped into `path`, `query`, `body` and `headers`; request controls are the second argument. An installed older SDK may lack a newer operation: inspect its types/version and update the package or use the documented REST operation, rather than guessing a method.

JSON responses preserve `{ data, meta? }`. Binary operations return `ArrayBuffer`; multipart uploads use `FormData`. Omitted fields differ from explicit `null`. For supported resource iterators, `limit` is a page size and stopping iteration stops further fetching. See [SDK usage](https://docs.famulor.io/sdk/usage) and [SDK configuration](https://docs.famulor.io/sdk/reference).

## Direct REST workflow

Keep authentication server-side. This read-only example reads a credential from the server environment without embedding it in a command or source file:

```javascript
const response = await fetch('https://app.famulor.io/api/v1/assistants?limit=10', {
  headers: { Authorization: `Bearer ${process.env.FAMULOR_API_KEY}` },
});
const result = await response.json();
if (!response.ok) throw new Error(result.error?.message ?? `HTTP ${response.status}`);
console.log(result.data.map(({ id, name }) => ({ id, name })));
```

Discover `limit`/`offset` support per operation; do not assume every list uses the same pagination or that a list is a stable snapshot. Follow response metadata. Use the documented multipart or binary format rather than JSON-encoding file bytes when the endpoint expects a file.

## Verify outcomes and handle uncertainty

For writes, read current state, execute the authorized action once, retain the returned resource/task ID, and read back or follow the documented status. A queued job, created call, approved template, sent request and delivered message are different states. Run or send actions can incur usage even when they are called a test.

The SDK retries eligible GET/HEAD requests after certain transport errors and HTTP 429/502/503/504; it never automatically retries writes. A timeout, cancelled wait or unreadable successful response can leave a write's outcome unknown. Inspect `mayHaveExecuted` on applicable SDK errors and reconcile using state/history/webhooks before retrying. An arbitrary idempotency header does not make an operation idempotent.

Use returned error codes and recovery guidance: reconnect on authentication failure; resolve scope/role/plan restrictions without bypassing them; check resource visibility on not-found errors; read fresh state after conflicts; respect retry delays. Do not switch from MCP to REST to escape a denial. CLI retry behavior differs from the SDK, so inspect the selected client's documented behavior when writing automation.

## Recipes by task

| Task | Start with | Verify with |
| --- | --- | --- |
| Build or refine an assistant | [Assistant design](assistant-design.md), [Assistants API](api/assistants.md), [Catalog API](api/catalog.md) | Read back prompt/configuration; run appropriate [evaluations](testing-and-evaluation.md) |
| Connect tools or booking | [Tools](api/tools.md), [Integrations](api/integrations.md), [Bookings](api/bookings.md) | Assigned tools, actual schema, confirmed availability/result |
| WhatsApp, email or social channels | [Channel guide](messaging-and-channels.md), [Messaging API](api/messaging.md) | Connector state and conversation details/delivery state |
| Add website voice/chat | [Widgets API](api/widgets.md), [Channel guide](messaging-and-channels.md) | Real widget conversation and history |
| Start authorized outreach | [Campaigns](api/campaigns.md), [Calls](api/calls.md), [Suppression](api/suppression.md) | Consent, target list, run status and settled results |
| Add knowledge | [Knowledge Bases](api/knowledge-bases.md) | Index readiness and a source-grounded answer |
| Review conversations | [History](api/history.md), [Calls](api/calls.md), [QA](api/qa.md) | Complete channel-specific detail, not only a preview |
| Automate a workflow | [Automations](api/automations.md), [Missions](api/milian-missions.md), [Webhooks](api/webhook-subscriptions.md) | Reviewed scope, run status and resulting resources |
| Manage telephony, teams or billing | [All API areas](api/index.md) | Explicit target/workspace, allowed operation and resulting state |
