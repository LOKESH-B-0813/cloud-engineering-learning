# 31_kernel_route_parser.py - Linux Kernel IPv4 Route Parser (/proc/net/route)
def parse_kernel_routes():
    routes = []
    with open("/proc/net/route", "r") as f:
        lines = f.readlines()[1:]
        for line in lines:
            parts = line.split()
            if len(parts) >= 8:
                iface = parts[0]
                dest_hex = parts[1]
                routes.append((iface, dest_hex))
    return routes

print(f"Total Active Kernel Route Entries: {len(parse_kernel_routes())}")
