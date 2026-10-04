# 10_uptime_scanner.py - Host Uptime Diagnostic
def audit_uptime():
    with open("/proc/uptime", "r") as f:
        uptime_seconds = float(f.readline().split()[0])
    return round(uptime_seconds / 3600, 2)

print(f"System Uptime: {audit_uptime()} hours")
