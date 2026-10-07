# 21_tcp_port_range_scanner.py - Probes standard management ports on a target
import socket

target = "127.0.0.1"
target_ports = [22, 80, 443, 8080]

print(f"=== SCANNING LOCAL MANAGEMENT PORTS ON {target} ===")
for port in target_ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    status = "OPEN" if result == 0 else "CLOSED/FILTERED"
    print(f"Port {port:<5} : {status}")
    s.close()
