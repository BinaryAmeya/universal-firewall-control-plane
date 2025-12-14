from datetime import datetime

def log(entry):
    with open("audit/firewall_audit.log", "a") as f:
        f.write(f"{datetime.now()} | {entry}\n")
