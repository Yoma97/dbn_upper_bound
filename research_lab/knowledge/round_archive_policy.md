# Canonical Round Archive Policy

## Purpose

Every research round must remain recoverable even if it is exploratory, rejected, audited, superseded, or frozen. A round is a historical research object, not merely a theorem milestone.

## Canonical rule

For every integer `N >= 1`, at least one authentic Markdown artifact must exist in `research_lab/runs/` whose filename contains `roundN`.

A round may have multiple artifacts (main run, hostile audit, correction, addendum). Multiple artifacts do not create new round numbers.

## Mandatory state labels for new/backfilled rounds

Each newly archived or recovered round should state one of:

- `WORKING` — active exploratory mathematics; not frozen.
- `FROZEN` — accepted as the authoritative state carried forward.
- `AUDIT` — adversarial/source/dependency/convention verification.
- `ADDENDUM` — correction or extension attached to the same round.
- `REFUTED` — preserved failed route/dead end.

A round is preserved regardless of status. `WORKING` content must not disappear merely because a later round supersedes it.

## Recovery rule

A placeholder labelled `MISSING_SOURCE` or `SOURCE_RECOVERY_REQUIRED` is useful as an alarm but **does not count as an archived round**. The strict validator ignores such placeholders.

Backfilling must use the authentic prior output/transcript/commit. Do not reconstruct mathematical statements from memory when the exact source is unavailable.

## Sequencing rule

Before beginning active Round `N+1`, strict CI must verify that authentic round artifacts exist for every integer `1..N`.

Historical references such as “from Round 99” are dependency citations only and must never reset the active round counter.

## Freeze rule

When a round is frozen, its file remains immutable as historical evidence. Later corrections are stored as a new round or an explicit addendum/correction artifact; the old file is not silently rewritten.

## Current recovery state (2026-08-17)

The active project chronology reports Round 129 completed and Round 130 next. The connected GitHub archive, however, authenticates run artifacts only through Round 88, with no standalone Round 62 artifact and no authentic run files for Rounds 89–129.

Therefore the archive is currently `INCOMPLETE` and Round 130 should be treated as **start-locked for mathematical execution** until the missing authentic source rounds are recovered or an explicit governance decision documents that they never existed as standalone rounds.

The machine-readable authority is `research_lab/round_registry.json`; the validator is `research_lab/validate_round_archive.py`.
