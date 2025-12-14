def apply(action):
    if action == "restrict_outbound":
        print("[Linux] DRY-RUN: iptables/nftables rule would be applied")
    elif action == "monitor_only":
        print("[Linux] Monitoring only")
    else:
        print("[Linux] No firewall action")
