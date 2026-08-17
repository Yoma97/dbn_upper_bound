#!/usr/bin/env python3
"""Validate that research rounds are persistently archived and sequential.

This validator distinguishes a real round artifact from a recovery placeholder.
A round is considered archived only if at least one Markdown file in
research_lab/runs contains its round number and is not marked MISSING_SOURCE.

Usage:
    python research_lab/validate_round_archive.py
    python research_lab/validate_round_archive.py --complete-through 129 --strict
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "research_lab" / "runs"
REGISTRY = ROOT / "research_lab" / "round_registry.json"
ROUND_RE = re.compile(r"(?:^|[_-])round[_-]?(\d+)(?:[_\-.]|$)", re.IGNORECASE)


def load_registry() -> dict:
    if not REGISTRY.exists():
        raise SystemExit("ERROR: research_lab/round_registry.json is missing")
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def scan_runs() -> dict[int, list[str]]:
    rounds: dict[int, list[str]] = defaultdict(list)
    for path in sorted(RUNS.glob("*.md")):
        m = ROUND_RE.search(path.name)
        if not m:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if "MISSING_SOURCE" in text or "SOURCE_RECOVERY_REQUIRED" in text:
            # Recovery markers are visible documentation, not proof that the
            # original round content has been preserved.
            continue
        rounds[int(m.group(1))].append(str(path.relative_to(ROOT)))
    return dict(rounds)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--complete-through", type=int, default=None)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    registry = load_registry()
    archived = scan_runs()
    convo = registry.get("conversation_chronology", {})
    current_completed = int(convo.get("current_completed_round", 0))
    target = args.complete_through or current_completed

    missing = [n for n in range(1, target + 1) if n not in archived]
    duplicates = {n: files for n, files in archived.items() if len(files) > 1}
    out_of_range = sorted(n for n in archived if n > current_completed and n != current_completed + 1)

    print(f"current_completed_round={current_completed}")
    print(f"validated_complete_through={target}")
    print(f"archived_round_count={len([n for n in archived if n <= target])}")
    print(f"missing_rounds={missing}")
    print(f"multi_artifact_rounds={sorted(duplicates)}")
    print(f"unexpected_future_rounds={out_of_range}")

    # Duplicates are allowed because audit/addendum artifacts may share a
    # round number. Missing numbers are never allowed in strict mode.
    if args.strict and missing:
        print("ARCHIVE_STATUS=INCOMPLETE")
        return 1

    if args.strict and out_of_range:
        print("ARCHIVE_STATUS=NONSEQUENTIAL_FUTURE_ROUND")
        return 2

    print("ARCHIVE_STATUS=" + ("COMPLETE" if not missing else "INCOMPLETE_REPORTED"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
