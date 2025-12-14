class CircuitBreaker:
    def __init__(self, max_failures=3):
        self.failures = 0
        self.max_failures = max_failures
        self.open = False

    def record_success(self):
        self.failures = 0

    def record_failure(self):
        self.failures += 1
        if self.failures >= self.max_failures:
            self.open = True
