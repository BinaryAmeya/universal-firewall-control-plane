CRITICAL_SYSTEMS = ["core_banking", "payment_gateway"]

def sla_allows(action):
    # In real banks this checks asset inventory
    if action and "restrict" in action:
        return False
    return True
