def apply(action):
    if action == "restrict_outbound":
        print("[macOS] DRY-RUN: pfctl rule would be applied")
    elif action == "monitor_only":
        print("[macOS] Monitoring only")
    else:
        print("[macOS] No firewall action")
