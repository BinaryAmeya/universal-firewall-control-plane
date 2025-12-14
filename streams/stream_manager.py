from streams.process_stream import ProcessStream
from streams.network_stream import NetworkStream
from streams.log_stream import LogStream
from streams.auth_stream import AuthStream
from streams.cloud_stream import CloudStream

from resilience.safe_executor import safely

class StreamManager:
    def __init__(self):
        self.streams = [
            ProcessStream(),
            NetworkStream(),
            LogStream(),
            AuthStream(),
            CloudStream()
        ]

    def poll_all(self):
        signals = []
        for stream in self.streams:
            result = safely(stream.poll)
            if result:
                signals.append(result)
        return signals
