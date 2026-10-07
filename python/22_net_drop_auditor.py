# 22_net_drop_auditor.py - Reads /proc/net/dev to evaluate drop statistics
def audit_drops():
    drop_stats = {}
    with open("/proc/net/dev", "r") as f:
        for line in f.readlines()[2:]:
            data = line.split(":")
            if len(data) == 2:
                iface = data[0].strip()
                metrics = data[1].split()
                rx_dropped = int(metrics[3])
                tx_dropped = int(metrics[11])
                drop_stats[iface] = (rx_dropped, tx_dropped)
    return drop_stats

for iface, (rx_drop, tx_drop) in audit_drops().items():
    print(f"Interface {iface:<10} | RX Drops: {rx_drop:<5} | TX Drops: {tx_drop:<5}")
