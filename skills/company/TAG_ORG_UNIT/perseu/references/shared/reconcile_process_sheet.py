#!/usr/bin/env python3
"""Reconcilia schema provisório de ficha de processo com campos do template oficial.

Não renomeia nem migra automaticamente. Produz relatório para aceite humano.
Autoridade: operacional interna — não normativa.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


def _norm(s: str) -> str:
    s = s.strip().lower()
    s = s.replace("ç", "c").replace("ã", "a").replace("á", "a").replace("à", "a")
    s = s.replace("â", "a").replace("é", "e").replace("ê", "e").replace("í", "i")
    s = s.replace("ó", "o").replace("ô", "o").replace("õ", "o").replace("ú", "u")
    s = re.sub(r"[^a-z0-9]+", "_", s)
    return s.strip("_")


def load_provisional_fields(schema_path: Path) -> list[dict[str, str]]:
    text = schema_path.read_text(encoding="utf-8")
    fields: list[dict[str, str]] = []
    current: dict[str, str] = {}
    in_fields = False
    for line in text.splitlines():
        if line.startswith("fields:"):
            in_fields = True
            continue
        if in_fields and line.startswith("header_fields:"):
            break
        if not in_fields:
            continue
        if line.strip().startswith("- id:"):
            if current:
                fields.append(current)
            current = {"id": line.split(":", 1)[1].strip()}
        elif "name:" in line and current is not None:
            current["name"] = line.split(":", 1)[1].strip()
        elif "label:" in line and current is not None:
            current["label"] = line.split(":", 1)[1].strip()
    if current:
        fields.append(current)
    return fields


def reconcile(
    provisional_fields: list[dict[str, str]],
    official_fields: list[dict[str, str]],
    mapping_hints: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Compara listas de campos {id?, name, label}.

    mapping_hints: optional provisional_name -> official_name (humano), nunca norma.
    """
    hints = mapping_hints or {}
    prov_by_name = {_norm(f["name"]): f for f in provisional_fields}
    off_by_name = {_norm(f.get("name") or f.get("label", "")): f for f in official_fields}
    off_by_label = {_norm(f.get("label") or f.get("name", "")): f for f in official_fields}

    coincident: list[dict[str, Any]] = []
    equivalent: list[dict[str, Any]] = []
    matched_off: set[str] = set()
    matched_prov: set[str] = set()

    for pname, pf in prov_by_name.items():
        # 1) coincident by name
        if pname in off_by_name:
            of = off_by_name[pname]
            oname = _norm(of.get("name") or of.get("label", ""))
            if _norm(pf.get("label", "")) == _norm(of.get("label") or of.get("name", "")):
                coincident.append({"provisional": pf, "official": of})
            else:
                equivalent.append(
                    {
                        "provisional": pf,
                        "official": of,
                        "reason": "same_name_different_label",
                    }
                )
            matched_prov.add(pname)
            matched_off.add(oname)
            continue
        # 2) human hint
        hint = hints.get(pf["name"]) or hints.get(pname)
        if hint and _norm(hint) in off_by_name:
            of = off_by_name[_norm(hint)]
            equivalent.append(
                {
                    "provisional": pf,
                    "official": of,
                    "reason": "human_mapping_hint",
                }
            )
            matched_prov.add(pname)
            matched_off.add(_norm(of.get("name") or of.get("label", "")))
            continue
        # 3) label-only soft match (reported as equivalent candidate, not auto-applied)
        plab = _norm(pf.get("label", ""))
        if plab in off_by_label and plab not in matched_off:
            of = off_by_label[plab]
            equivalent.append(
                {
                    "provisional": pf,
                    "official": of,
                    "reason": "same_label_different_name_candidate",
                    "requires_human_confirmation": True,
                }
            )
            matched_prov.add(pname)
            matched_off.add(_norm(of.get("name") or of.get("label", "")))

    missing = [prov_by_name[k] for k in prov_by_name if k not in matched_prov]
    extra = [off_by_name[k] for k in off_by_name if k not in matched_off]

    breaking: list[dict[str, Any]] = []
    if missing:
        breaking.append(
            {
                "type": "provisional_fields_absent_in_official",
                "fields": missing,
                "severity": "requires_human_decision",
            }
        )
    if extra:
        breaking.append(
            {
                "type": "official_fields_absent_in_provisional",
                "fields": extra,
                "severity": "requires_human_decision",
            }
        )

    return {
        "authority": "internal_operational",
        "normative": False,
        "auto_rename_applied": False,
        "coincident_fields": coincident,
        "equivalent_fields_different_labels": equivalent,
        "missing_fields": missing,
        "extra_fields": extra,
        "breaking_changes": breaking,
        "migration_recommendation": {
            "status": "pending_human_acceptance",
            "actions_suggested": [
                "keep_provisional_ids_stable",
                "map_labels_only_after_acceptance",
                "open_gap_for_unmatched",
            ],
            "forbidden_until_acceptance": [
                "auto_rename_provisional_fields",
                "claim_as_official_pop_fields",
                "silent_schema_migration",
            ],
        },
        "human_acceptance_required": True,
        "prohibit_silent_apply": True,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Reconcile provisional process sheet vs template fields")
    parser.add_argument(
        "--provisional",
        type=Path,
        default=Path(__file__).with_name("asis-process-sheet.schema.yaml"),
    )
    parser.add_argument(
        "--official-json",
        type=Path,
        required=True,
        help="JSON list of official fields [{id?, name, label}, ...] extracted from template",
    )
    parser.add_argument("--hints-json", type=Path, default=None)
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args(argv)

    provisional = load_provisional_fields(args.provisional)
    official = json.loads(args.official_json.read_text(encoding="utf-8"))
    hints = None
    if args.hints_json:
        hints = json.loads(args.hints_json.read_text(encoding="utf-8"))
    report = reconcile(provisional, official, hints)
    text = json.dumps(report, ensure_ascii=False, indent=2)
    if args.out:
        args.out.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
