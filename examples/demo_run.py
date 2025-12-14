import sys, os, time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.risk_model import RiskModel
from core.decision_engine import decide
from core.risk_gate import RiskGate
from core.confidence import confidence_level
from core.two_phase import TwoPhaseEnforcer
from core.approval import ApprovalEngine
from core.scope import scoped_action
from core.rollback import RollbackEngine
from core.cooldown import Cooldown
from core.fail_mode import DEFAULT_MODE, FAIL_OPEN
from core.sla import sla_allows

from streams.stream_manager import StreamManager
from adapters.windows_firewall import WindowsFirewall
from audit.event_logger import log_event
from resilience.safe_executor import safe_call

risk = RiskModel()
gate = RiskGate(min_signals=2)
approvals = ApprovalEngine(required=2)
two_phase = TwoPhaseEnforcer()
rollback = RollbackEngine()
cooldown = Cooldown(seconds=20)

streams = StreamManager()
fw = WindowsFirewall()

print("🏦 BANK-GRADE FIREWALL CONTROL PLANE — HARDENED")

for cycle in range(10):
    print(f"\n--- Cycle {cycle} ---")

    signals = safe_call(streams.poll_all, fallback=[])

    for weight, reason in signals:
        risk.add_signal(weight, reason)
        log_event(reason)

    score = risk.final_score()
    reasons = risk.explain()

    print("Risk:", score)
    print("Signals:", reasons)

    if not gate.allowed(reasons):
        print("[GATE] Blocked — insufficient evidence")
        time.sleep(2)
        continue

    decision = decide(score, reasons)
    confidence = confidence_level(score, reasons)

    print("Decision:", decision)
    print("Confidence:", confidence)

    if confidence != "HIGH":
        print("[POLICY] Human approval required")

    if not cooldown.allowed():
        print("[COOLDOWN] Enforcement paused")
        continue

    if approvals.approve():
        two_phase.dry_run(decision)
        action = two_phase.commit()
        action = scoped_action(action)

        if not sla_allows(action):
            print("[SLA] Action blocked — critical system")
            continue

        fw.apply(action)
    else:
        print("[APPROVAL] Waiting for quorum")

    time.sleep(2)
