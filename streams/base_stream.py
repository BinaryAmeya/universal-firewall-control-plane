class RiskStream:
    def poll(self):
        """
        Returns:
            (weight:int, reason:str) OR None
        """
        raise NotImplementedError
