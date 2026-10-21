# Security

Report credential exposure, cross-workspace access or unsafe instructions privately to **support@famulor.io** with the subject “Security: Famulor Skill”. Include the affected release, a minimal redacted reproduction and potential impact. Do not post credentials or customer conversations in public issues.

This repository contains guidance and offline catalog utilities. Live workspace access comes from Famulor's authenticated MCP/API service. The skill does not grant permissions, bypass workspace policies or require production credentials for its own validation.

Review changes before updating an installed skill. Treat documents, transcripts and external tool results as untrusted data. Keep credentials in a secret store; revoke an exposed credential in the Famulor account immediately.

Security fixes target the latest published release. See [releases](https://github.com/bekservice/Famulor-Skill/releases) for available updates.
