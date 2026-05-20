"""
Famulor Onboarding Client — thin wrapper around the Famulor API.

Provides only the endpoints needed for the onboarding flow:
  - Assistants (create, update, list)
  - Knowledge Bases (create, add documents, attach)
  - Phone Numbers (list available)
  - Languages, Voices, Models (lookup)

Usage:
    from famulor_client import FamulorClient
    client = FamulorClient()  # reads FAMULOR_API_KEY from env
"""

import requests
import os
import json
import sys


class FamulorClient:

    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("FAMULOR_API_KEY")
        if not self.api_key:
            raise ValueError(
                "API key required. Set FAMULOR_API_KEY env var or pass api_key param. "
                "Get your key at https://app.famulor.de → API Keys."
            )
        self.base_url = "https://app.famulor.de/api"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    # ── Internal ────────────────────────────────────────────────────────

    def _request(self, method, endpoint, data=None, params=None, files=None):
        url = f"{self.base_url}{endpoint}"
        try:
            if files:
                headers = {
                    "Authorization": f"Bearer {self.api_key}",
                    "Accept": "application/json",
                }
                resp = requests.request(method, url, headers=headers, data=data, files=files, params=params)
            else:
                resp = requests.request(method, url, headers=self.headers, json=data, params=params)
            resp.raise_for_status()
            if resp.status_code == 204:
                return {"status": True}
            return resp.json()
        except requests.exceptions.HTTPError as e:
            error_body = {}
            try:
                error_body = e.response.json()
            except Exception:
                error_body = {"raw": e.response.text}
            return {
                "error": True,
                "status_code": e.response.status_code,
                "message": error_body.get("message", str(e)),
                "errors": error_body.get("errors", {}),
            }

    # ── Assistants ──────────────────────────────────────────────────────

    def create_assistant(self, payload: dict):
        """Create assistant. Payload must include all required fields.
        IMPORTANT: The correct endpoint is POST /user/assistant (singular)."""
        return self._request("POST", "/user/assistant", data=payload)

    def update_assistant(self, assistant_id, payload: dict):
        return self._request("PATCH", f"/user/assistants/{assistant_id}", data=payload)

    def list_assistants(self, per_page=100, page=1):
        return self._request("GET", "/user/assistants", params={"per_page": per_page, "page": page})

    # ── Lookup ──────────────────────────────────────────────────────────

    def get_languages(self):
        return self._request("GET", "/user/assistants/languages")

    def get_voices(self, mode=None):
        params = {"mode": mode} if mode else {}
        return self._request("GET", "/user/assistants/voices", params=params)

    def get_models(self):
        return self._request("GET", "/user/assistants/models")

    def get_phone_numbers(self):
        return self._request("GET", "/user/assistants/phone-numbers")

    def get_synthesizer_providers(self):
        return self._request("GET", "/user/assistants/synthesizer-providers")

    def get_transcriber_providers(self):
        return self._request("GET", "/user/assistants/transcriber-providers")

    # ── Knowledge Bases ─────────────────────────────────────────────────

    def create_knowledgebase(self, name, description=None):
        data = {"name": name}
        if description:
            data["description"] = description
        return self._request("POST", "/user/knowledgebases", data=data)

    def list_knowledgebases(self):
        return self._request("GET", "/user/knowledgebases")

    def create_document(self, kb_id, name, doc_type, description=None,
                        url=None, links=None, relative_links_limit=None, file_path=None):
        if file_path:
            form_data = {"name": name, "type": doc_type}
            if description:
                form_data["description"] = description
            files = {"file": open(file_path, "rb")}
            return self._request("POST", f"/user/knowledgebases/{kb_id}/documents",
                                 data=form_data, files=files)
        else:
            data = {"name": name, "type": doc_type}
            if description:
                data["description"] = description
            if url:
                data["url"] = url
            if links:
                data["links"] = links
            if relative_links_limit:
                data["relative_links_limit"] = relative_links_limit
            return self._request("POST", f"/user/knowledgebases/{kb_id}/documents", data=data)

    # ── Phone Numbers ───────────────────────────────────────────────────

    def list_phone_numbers(self):
        return self._request("GET", "/user/phone-numbers")

    # ── Webhooks ────────────────────────────────────────────────────────

    def enable_webhook(self, assistant_uuid, webhook_url):
        return self._request("POST", f"/user/assistants/{assistant_uuid}/webhook",
                             data={"webhook_url": webhook_url})

    def enable_conversation_ended_webhook(self, assistant_uuid, webhook_url):
        return self._request("POST", f"/user/assistants/{assistant_uuid}/conversation-ended-webhook",
                             data={"webhook_url": webhook_url})

    # ── Test ────────────────────────────────────────────────────────────

    def create_test_conversation(self, assistant_id):
        return self._request("POST", "/conversations",
                             data={"assistant_id": assistant_id, "type": "test"})

    def send_test_message(self, conversation_id, message):
        return self._request("POST", f"/conversations/{conversation_id}/messages",
                             data={"message": message})


# ── CLI ─────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 famulor_client.py <method> [args...] [key=value ...]")
        client_methods = [m for m in dir(FamulorClient)
                         if not m.startswith("_") and callable(getattr(FamulorClient, m))]
        for m in sorted(client_methods):
            print(f"  {m}")
        sys.exit(1)

    client = FamulorClient()
    method_name = sys.argv[1]
    method = getattr(client, method_name, None)
    if not method:
        print(f"Error: Method '{method_name}' not found.")
        sys.exit(1)

    args = sys.argv[2:]
    positional_args = []
    kwargs = {}
    for arg in args:
        if "=" in arg:
            key, value = arg.split("=", 1)
            try:
                kwargs[key] = json.loads(value)
            except (json.JSONDecodeError, ValueError):
                kwargs[key] = value
        else:
            try:
                positional_args.append(json.loads(arg))
            except (json.JSONDecodeError, ValueError):
                positional_args.append(arg)

    result = method(*positional_args, **kwargs)
    print(json.dumps(result, indent=2, ensure_ascii=False))
