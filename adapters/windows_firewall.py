from adapters.base import FirewallAdapter

class WindowsFirewall(FirewallAdapter):
    def apply(self, action):
        if action == "restrict_outbound":
            print("[Windows] DRY-RUN: outbound firewall rule would be applied")
        elif action == "monitor_only":
            print("[Windows] Monitoring only (no enforcement)")
        else:
            print("[Windows] No firewall action")
