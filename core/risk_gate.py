class RiskGate:
    def __init__(self, min_signals=2):
        self.min_signals = min_signals

    def allowed(self, reasons):
        return len(reasons) >= self.min_signals
