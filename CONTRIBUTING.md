# Contributing

Help improve real Famulor workflows: a clearer installation step, a reproducible channel failure, a corrected endpoint mapping or a useful test case.

1. Open an issue describing the task, expected result and observed result. Redact credentials, customer identities, phone numbers and conversation content.
2. Keep the main `SKILL.md` concise. Put conditional guidance in a linked reference, and templates in the skill's `assets/` directory so portable installs include them.
3. Verify behavior against the current customer-facing contract. A capability in an upstream SDK does not establish that Famulor exposes it.
4. Add or adapt a realistic evaluation when behavior changes. Scripts should have deterministic tests and must not require production credentials.
5. Run the checks below and describe what you verified in your pull request.

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/package-release.py
python3 scripts/package-release.py --check
git diff --check
```

Generated catalogs are maintained from the canonical contract; do not hand-edit endpoint names to hide drift. See [PUBLISHING.md](PUBLISHING.md). Live schemas remain authoritative; capability snapshots have dates.

Do not include internal infrastructure, deployment configuration, credentials, private logs or customer data. Use fictional business placeholders in examples. For sensitive findings, follow [SECURITY.md](SECURITY.md).
