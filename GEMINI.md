# Famulor.io Skill Context

This repository ships the Famulor skill following the [Open Plugins](https://open-plugins.com) layout.

When users ask to build or manage Famulor resources, prioritize:

1. Valid API configuration (`FAMULOR_API_KEY` environment variable)
2. Correct resource type selection (assistant, campaign, knowledge base, messaging)
3. Safe iterative setup with test runs before production use

Primary skill entry point:

- `skills/famulor-skill/SKILL.md` — full instructions and onboarding flow
- `skills/famulor-skill/references/nischen_intelligenz.md` — niche/branche-specific intelligence
- `skills/famulor-skill/scripts/famulor_client.py` — Python API client
