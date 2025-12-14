import psutil
from streams.base_stream import RiskStream

class NetworkStream(RiskStream):
    def poll(self):
        conns = psutil.net_connections()
        outbound = [c for c in conns if c.raddr]
        if len(outbound) > 20:
            return (30, "High outbound connection volume")
        return None
