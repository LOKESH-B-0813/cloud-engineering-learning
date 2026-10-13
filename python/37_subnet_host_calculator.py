# 37_subnet_host_calculator.py - Calculates Network ID, Broadcast, and Host Range
import ipaddress

def calculate_subnet_boundaries(cidr_network):
    net = ipaddress.ip_network(cidr_network, strict=False)
    hosts = list(net.hosts())
    first_host = hosts[0] if hosts else "None"
    last_host = hosts[-1] if hosts else "None"
    return {
        "network_id": net.network_address,
        "broadcast": net.broadcast_address,
        "netmask": net.netmask,
        "first_usable": first_host,
        "last_usable": last_host,
        "total_usable": len(hosts)
    }

metrics = calculate_subnet_boundaries("192.168.10.0/26")
for k, v in metrics.items():
    print(f"{k:<15}: {v}")
