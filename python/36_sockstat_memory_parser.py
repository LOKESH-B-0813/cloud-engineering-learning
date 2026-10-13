# 36_sockstat_memory_parser.py - Linux /proc/net/sockstat Parser
def parse_sockstat():
    stats = {}
    with open("/proc/net/sockstat", "r") as f:
        for line in f:
            tokens = line.strip().split()
            if tokens:
                category = tokens[0][:-1]
                stats[category] = dict(zip(tokens[1::2], tokens[2::2]))
    return stats

sock_data = parse_sockstat()
print("=== KERNEL SOCKET STATISTICS ===")
for cat, values in sock_data.items():
    print(f"[{cat}] {values}")
