# 19_arp_table_audit.py - Linux ARP Cache Parser (/proc/net/arp)
def audit_arp_cache():
    entries = []
    with open("/proc/net/arp", "r") as f:
        lines = f.readlines()[1:]
        for line in lines:
            parts = line.split()
            if len(parts) >= 6:
                entries.append({"ip": parts[0], "mac": parts[3], "iface": parts[5]})
    return entries

for entry in audit_arp_cache():
    print(f"IP: {entry['ip']:<15} -> MAC: {entry['mac']} on {entry['iface']}")
