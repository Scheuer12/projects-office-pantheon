#!/usr/bin/env python3
"""IDs determinísticos de perguntas — Papiro (não altera documento-fonte)."""
from __future__ import annotations

import hashlib
import re
from typing import Any


def _slug(text: str) -> str:
    t = text.strip().lower()
    repl = {
        "ç": "c",
        "ã": "a",
        "á": "a",
        "à": "a",
        "â": "a",
        "é": "e",
        "ê": "e",
        "í": "i",
        "ó": "o",
        "ô": "o",
        "õ": "o",
        "ú": "u",
        "&": "e",
    }
    for a, b in repl.items():
        t = t.replace(a, b)
    t = re.sub(r"[^a-z0-9]+", "_", t)
    return t.strip("_") or "sec"


def source_hash(content: bytes | str) -> str:
    if isinstance(content, str):
        content = content.encode("utf-8")
    return hashlib.sha256(content).hexdigest()


def make_question_id(
    profile: str,
    section: str,
    position: int,
    source_hash_hex: str,
) -> str:
    if position < 1:
        raise ValueError("position must be 1-based >= 1")
    h12 = source_hash_hex.lower()[:12]
    if len(h12) < 12:
        raise ValueError("source_hash must have at least 12 hex chars")
    return f"Q-{_slug(profile)}-{_slug(section)}-p{position}-{h12}"


def register_source_version_change(
    *,
    profile: str,
    section: str,
    position: int,
    old_source_hash: str,
    new_source_hash: str,
    previous_id: str | None = None,
    safe_correspondence: bool = False,
) -> dict[str, Any]:
    """Quando o documento muda, emite novo ID e opcionalmente alias do anterior."""
    new_id = make_question_id(profile, section, position, new_source_hash)
    old_id = previous_id or make_question_id(profile, section, position, old_source_hash)
    record: dict[str, Any] = {
        "id": new_id,
        "source_hash": new_source_hash.lower(),
        "previous_source_hash": old_source_hash.lower(),
        "id_version": 2,
        "id_aliases": [],
        "collision_with_previous": new_id == old_id,
    }
    if safe_correspondence and old_id != new_id:
        record["id_aliases"].append(old_id)
    return record
