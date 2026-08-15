from __future__ import annotations

from dataclasses import dataclass

from agents import ModelSettings
from openai.types.shared import Reasoning


@dataclass(frozen=True)
class RoleModelPolicy:
    effort: str
    mode: str = "pro"
    context: str = "current_turn"
    verbosity: str = "medium"


# Search/invention gets enough depth to be creative without spending the most
# expensive reasoning budget on every speculative idea. Certification is the
# quality-first stage and therefore receives maximum reasoning effort.
ROLE_MODEL_POLICIES: dict[str, RoleModelPolicy] = {
    "frontier_curator": RoleModelPolicy("high", verbosity="low"),

    "obstruction_analyst": RoleModelPolicy("xhigh"),
    "constraint_hunter": RoleModelPolicy("xhigh"),
    "violation_amplifier": RoleModelPolicy("xhigh"),
    "structural_mutator": RoleModelPolicy("high"),
    "object_inventor": RoleModelPolicy("high"),
    "identity_invariant_hunter": RoleModelPolicy("xhigh"),
    "bridge_builder": RoleModelPolicy("xhigh"),
    "definition_inventor": RoleModelPolicy("high"),
    "theory_builder": RoleModelPolicy("xhigh"),

    "destroyer": RoleModelPolicy("max", context="all_turns", verbosity="high"),
    "equivalence_auditor": RoleModelPolicy("max", context="all_turns", verbosity="high"),
    "mathematical_legitimacy_auditor": RoleModelPolicy("max", context="all_turns", verbosity="high"),
    "exclusion_completeness_auditor": RoleModelPolicy("max", context="all_turns", verbosity="high"),
    "independent_referee": RoleModelPolicy("max", context="all_turns", verbosity="high"),

    "synthesis": RoleModelPolicy("xhigh", verbosity="high"),
    "proof_reconstructor": RoleModelPolicy("max", context="all_turns", verbosity="high"),
}


DEFAULT_POLICY = RoleModelPolicy("high")


def policy_for(role_key: str) -> RoleModelPolicy:
    return ROLE_MODEL_POLICIES.get(role_key, DEFAULT_POLICY)


def model_settings_for(role_key: str) -> ModelSettings:
    p = policy_for(role_key)
    return ModelSettings(
        reasoning=Reasoning(
            mode=p.mode,
            effort=p.effort,
            context=p.context,
        ),
        verbosity=p.verbosity,
        truncation="auto",
    )
