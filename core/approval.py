class ApprovalEngine:
    def __init__(self, required=2):
        self.required = required
        self.count = 0

    def approve(self):
        self.count += 1
        return self.count >= self.required
