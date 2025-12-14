class TwoPhaseEnforcer:
    def __init__(self):
        self.pending = None

    def dry_run(self, decision):
        self.pending = decision
        return "DRY_RUN_COMPLETE"

    def commit(self):
        if self.pending:
            action = self.pending.get("action")
            self.pending = None
            return action
        return None
