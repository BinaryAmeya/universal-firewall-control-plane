import psutil
from streams.base_stream import RiskStream

class ProcessStream(RiskStream):
    def poll(self):
        for p in psutil.process_iter(['cpu_percent', 'name']):
            try:
                if p.info['cpu_percent'] and p.info['cpu_percent'] > 50:
                    return (25, f"High CPU usage by process {p.info['name']}")
            except:
                pass
        return None
