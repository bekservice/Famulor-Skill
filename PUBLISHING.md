# Publishing and distribution

This repository publishes Famulor's customer skill and client packaging. It does not deploy the application, publish CLI/SDK packages or register a new MCP server. The hosted server has its own registry entry; do not add a duplicate `server.json` here.

## Refresh the public contracts

Maintainers export the current canonical MCP registry, public OpenAPI document, generated CLI catalog and TypeScript operation descriptors. Pass those inputs explicitly; no credentials are required. The CLI catalog must be regenerated against the same OpenAPI version before export.

```bash
python3 scripts/sync-catalog.py /path/to/mcp-registry.json --date YYYY-MM-DD --references-only
python3 scripts/sync-api-catalog.py \
  --openapi /path/to/openapi.json \
  --cli-catalog /path/to/cli-catalog.json \
  --sdk-descriptors /path/to/operations.ts \
  --docs-dir /path/to/api-reference \
  --navigation /path/to/docs.json \
  --date YYYY-MM-DD
```

Run both commands again with `--check`. The API generator verifies the CLI's source hash and exact method/path/operation parity with the SDK. It projects public request constraints while excluding examples, defaults and response-property snapshots. Review the output for private fields and claims before publishing. Check the reviewed URL aliases in `scripts/api-doc-links.json` when endpoint summaries or routes change. The MCP generator's `--references-only` option leaves the hand-maintained entrypoint untouched; update its group counts deliberately.

The source application repository is not required to install or validate a release. Contributors can run the included fixture-based tests and offline lookup using the bundled catalog.

## Validate and release

1. Review the diff, channel-specific claims, external links and realistic evaluation scenarios. Keep upstream SDK behavior separate from capabilities exposed by Famulor.
2. Update `VERSION`, all six plugin/extension manifests, `.claude-plugin/marketplace.json`, both skill metadata versions and `CHANGELOG.md`. Update snapshot counts/dates where needed.
3. Run:

   ```bash
   python3 scripts/validate.py
   python3 -m unittest discover -s tests -v
   claude plugin validate .claude-plugin/marketplace.json --strict
   claude plugin validate .claude-plugin/plugin.json --strict
   claude plugin validate ./claude-store
   python3 scripts/package-release.py
   python3 scripts/package-release.py --check
   git diff --check
   ```

   The restricted Store manifest retains its directory-required `privacyPolicyUrl`; Claude Code can warn that it ignores that field. Review actual validator errors separately.

4. Review the archive contents. `famulor.skill` and `dist/famulor-skill.zip` contain only the portable skill directory. They are byte-identical ZIP archives. `dist/SHA256SUMS` records both asset hashes.
5. Open a pull request, wait for **Validate skill** to pass, review and merge the exact tested changes.
6. Tag the merged commit and publish a GitHub release with `famulor.skill`, `famulor-skill.zip` and `SHA256SUMS`. Confirm the release is public and the downloaded assets match the checksums.

The generator uses fixed ZIP metadata and stable ordering so packaging is reproducible. Never edit or overwrite an existing release's versioned assets silently; publish a new patch release for corrections.

## Discoverability

- Keep GitHub's description specific: Famulor voice, WhatsApp, webchat, prompts, MCP and API workflows.
- Maintain relevant topics, a clear README, working installation commands, real examples, issue templates and versioned releases.
- The [Agent Skills specification](https://agentskills.io/specification) defines the portable folder structure. The [skills installer](https://github.com/vercel-labs/skills) can install directly from this public repository.
- [skills.sh](https://skills.sh/docs) ranks skills using actual installation telemetry. Do not manufacture installs, stars or endorsements. A compatible release is not a guarantee of indexing, ranking or audience growth.
- Gemini distribution uses the root `gemini-extension.json`, GitHub tags and the `gemini-cli-extension` topic. Check the [current gallery guidance](https://geminicli.com/docs/extensions/) and verify any listing independently.
- `.claude-plugin/marketplace.json` provides a repository-hosted Claude Code marketplace. This does not claim inclusion in Anthropic's reviewed directory.

## Directory profiles and separate submissions

The root developer plugin exposes the authenticated full MCP endpoint. `claude-store/` remains a separate Assistant & History package connected to `?profile=assistant-history` with exactly 11 read tools. Never submit the full root package as though it had the restricted profile's permissions.

Public ChatGPT/Claude directory listings are separately reviewed products. Publishing this GitHub release does not update them. A marketplace listing, submission or gallery indexing must be verified in that service before claiming availability.

Additional marketplace submissions, registry uploads and promotional posts are separate actions. Follow their current publisher instructions, preserve approved capability scopes and do not imply a listing exists until confirmed.
