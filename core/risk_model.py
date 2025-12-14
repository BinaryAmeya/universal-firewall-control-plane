from core.risk_window import RiskWindow
from core.adaptive_risk import AdaptiveRisk

class RiskModel:
    def __init__(self):
        self.window = RiskWindow(seconds=120)
        self.adaptive = AdaptiveRisk()
        self.reasons = []

    def add_signal(self, weight, reason):
        self.window.add(weight)
        smoothed = self.adaptive.update(weight)
        self.reasons.append(f"{reason} (smoothed={round(smoothed,2)})")

    def final_score(self):
        return min(self.window.total(), 100)

    def explain(self):
        return list(set(self.reasons))
