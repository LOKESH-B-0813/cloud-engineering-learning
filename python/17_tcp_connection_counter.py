# 17_tcp_connection_counter.py - TCP Socket Connection Summary
def count_tcp_connections():
    with open("/proc/net/tcp", "r") as f:
        lines = f.readlines()[1:]
    return len(lines)

print(f"Active TCP Sockets in Kernel Pool: {count_tcp_connections()}")
