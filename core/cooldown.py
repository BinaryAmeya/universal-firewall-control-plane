import time

class Cooldown:
    def __init__(self, seconds=30):
        self.seconds = seconds
        self.last = 0

    def allowed(self):
        now = time.time()
        if now - self.last >= self.seconds:
            self.last = now
            return True
        return False
