# 38_udp_socket_counter.py - Audits active UDP sockets from /proc/net/udp
def count_udp_sockets():
    with open("/proc/net/udp", "r") as f:
        return len(f.readlines()) - 1

active_udp = count_udp_sockets()
print(f"Active UDP Sockets in Kernel Pool: {active_udp}")
