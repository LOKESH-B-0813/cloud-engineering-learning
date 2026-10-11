# 33_softirq_auditor.py - Kernel Softirq Event Metrics Parser
def audit_softirqs():
    with open("/proc/softirqs", "r") as f:
        lines = f.readlines()
    header = lines[0].split()
    net_rx = [line for line in lines if line.strip().startswith("NET_RX")]
    print(f"Active Softirq Cores: {len(header)}")
    if net_rx:
        print(f"Network RX Softirq Summary: {net_rx[0].strip()}")

audit_softirqs()
