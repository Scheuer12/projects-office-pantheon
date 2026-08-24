"""
Sanitized external-query skill stub.

The original implementation contained integration-specific request construction,
authentication flow, [REDACTED_ENDPOINT] handling, and payload details. Those details were
removed for portfolio publication.

This file preserves the engineering shape:
- validate a complete caller payload
- normalize bounded context
- enforce one scoped question per execution
- return a structured result object
- fail honestly when private runtime configuration is absent
"""

from __future__ import annotations

import argparse
import json
import sys
import uuid

REDACTED_RUNTIME_ERROR = (
    "[REDACTED_RUNTIME_INTEGRATION] is not available in the sanitized portfolio export."
)


def _first(*values):
    for value in values:
        if value is None:
            continue
        if isinstance(value, str) and not value.strip():
            continue
        return value
    return None


def _parse_context(context):
    if context is None:
        return []
    if isinstance(context, str):
        try:
            context = json.loads(context)
        except json.JSONDecodeError:
            context = [context]
    if not isinstance(context, list):
        raise ValueError("context must be a list of strings.")
    return [str(item) for item in context[-12:]]


def consultar(*, subject_id: str, subject_name: str, scope: str, question: str, session_id: str | None = None, context=None) -> dict:
    required = {
        "subject_id": subject_id,
        "subject_name": subject_name,
        "scope": scope,
        "question": question,
    }
    missing = [key for key, value in required.items() if value in (None, "")]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")

    return {
        "ok": False,
        "status": "SANITIZED_STUB",
        "error": REDACTED_RUNTIME_ERROR,
        "sessionId": session_id or str(uuid.uuid4()),
        "request_shape": {
            "subject_id": "[REDACTED_IDENTIFIER]",
            "subject_name": "[PERSON_NAME]",
            "scope": "[CLIENT_OR_SYSTEM_SCOPE]",
            "question": question[:240],
            "context_items": len(_parse_context(context)),
        },
    }


def _inputs_from_globals() -> dict | None:
    raw_subject = _first(globals().get("subject_id"), globals().get("id"))
    if raw_subject is None and not any(globals().get(k) for k in ("subject_name", "scope", "question")):
        return None
    return {
        "subject_id": str(raw_subject) if raw_subject is not None else None,
        "subject_name": _first(globals().get("subject_name"), globals().get("name")),
        "scope": _first(globals().get("scope"), globals().get("client_scope")),
        "question": _first(globals().get("question"), globals().get("chat_input")),
        "session_id": _first(globals().get("session_id"), globals().get("sessionId")),
        "context": globals().get("context"),
    }


def _inputs_from_cli(argv: list[str] | None = None) -> dict:
    parser = argparse.ArgumentParser(description="Run sanitized external-query skill stub")
    parser.add_argument("--subject-id", required=True)
    parser.add_argument("--subject-name", required=True)
    parser.add_argument("--scope", required=True)
    parser.add_argument("--question", required=True)
    parser.add_argument("--session-id", default=None)
    parser.add_argument("--context", default="[]")
    args = parser.parse_args(argv)
    return vars(args)


def main(argv: list[str] | None = None) -> int:
    embedded = _inputs_from_globals()
    inputs = embedded if embedded else _inputs_from_cli(argv)
    result = consultar(**inputs)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        raise SystemExit(1) from exc


_embedded = _inputs_from_globals()
if _embedded and __name__ != "__main__":
    output = consultar(**_embedded)