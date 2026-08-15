from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum
from pathlib import Path
import json
import uuid


class NumericalRole(str, Enum):
    REFUTE = "REFUTE"
    DISCOVER = "DISCOVER"
    FINITE_CERTIFY = "FINITE_CERTIFY"


class ArbCapability(str, Enum):
    SQRT = "sqrt"
    RIEMANN_ZETA = "riemann_zeta"
    ZETA_ZERO = "zeta_zero"
    XI = "xi"
    XI_DERIVATIVE = "xi_derivative"
    H_T = "H_t"
    H_T_DERIVATIVE = "H_t_derivative"
    LAGUERRE = "laguerre"
    INTERVAL_INTEGRAL = "interval_integral"
    INTERVAL_EXTREMUM = "interval_extremum"
    MATRIX_INERTIA = "matrix_inertia"
    INTERVAL_NEWTON = "interval_newton"


# This must reflect the connector that is actually exposed, not desired future tools.
CURRENTLY_CONNECTED = {
    ArbCapability.SQRT,
    ArbCapability.RIEMANN_ZETA,
    ArbCapability.ZETA_ZERO,
}


@dataclass
class ArbJob:
    title: str
    role: NumericalRole
    capability: ArbCapability
    mathematical_quantity: str
    inputs: dict
    certified_domain: str
    analytic_reduction: str = ""
    logically_necessary: bool = False
    job_id: str = ""

    def __post_init__(self) -> None:
        if not self.job_id:
            self.job_id = str(uuid.uuid4())


@dataclass
class ArbGateResult:
    job_id: str
    runnable_now: bool
    status: str
    reason: str


def gate_job(job: ArbJob) -> ArbGateResult:
    if job.capability not in CURRENTLY_CONNECTED:
        return ArbGateResult(
            job_id=job.job_id,
            runnable_now=False,
            status="ARB_CAPABILITY_MISSING",
            reason=(
                f"Required rigorous capability '{job.capability.value}' is not "
                "currently exposed by Arb_Riemann_Lab. Do not substitute floating point."
            ),
        )

    if job.role == NumericalRole.FINITE_CERTIFY and not job.certified_domain.strip():
        return ArbGateResult(
            job_id=job.job_id,
            runnable_now=False,
            status="REJECT",
            reason="Finite certification requires an explicit certified domain.",
        )

    if job.logically_necessary and not job.analytic_reduction.strip():
        return ArbGateResult(
            job_id=job.job_id,
            runnable_now=False,
            status="REPAIR",
            reason=(
                "A logically necessary numerical step must state the analytic "
                "reduction showing why a finite certificate suffices."
            ),
        )

    return ArbGateResult(
        job_id=job.job_id,
        runnable_now=True,
        status="READY_FOR_ARB",
        reason="Requested capability is currently exposed and the job is well specified.",
    )


def append_job(root: Path, job: ArbJob) -> ArbGateResult:
    root.mkdir(parents=True, exist_ok=True)
    gate = gate_job(job)
    with (root / "arb_jobs.jsonl").open("a", encoding="utf-8") as fh:
        payload = {"job": asdict(job), "gate": asdict(gate)}
        payload["job"]["role"] = job.role.value
        payload["job"]["capability"] = job.capability.value
        fh.write(json.dumps(payload, ensure_ascii=False) + "\n")
    return gate


def universal_claim_warning() -> str:
    return (
        "Arb may refute a universal claim with one rigorous counterexample, or "
        "certify a finite subproblem. It may enter a global theorem only after "
        "an independently proved analytic reduction to finitely many certified cases."
    )
