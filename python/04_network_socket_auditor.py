# 04_network_socket_auditor.py - Dynamic Host Identity and Socket Audit Utility
# Evolution of 03_system_logger.py: Verifies network layer addressing and target reachability.

import socket

local_hostname = socket.gethostname()
local_ip = socket.gethostbyname(local_hostname)
target_probe_host = "8.8.8.8"
target_probe_port = 53

def probe_tcp_port(host, port, timeout_sec=2.0):
    """Probes whether a remote target port is reachable via L4 TCP handshake."""
    probe_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    probe_socket.settimeout(timeout_sec)
    try:
        probe_socket.connect((host, port))
        probe_socket.close()
        return True
    except (socket.timeout, socket.error):
        return False

is_service_reachable = probe_tcp_port(target_probe_host, target_probe_port)

print("========================================")
print("NETWORK LAYER 3 / 4 AUDIT REPORT")
print("========================================")
print(f"Local Host     : {local_hostname}")
print(f"Local IP (L3)  : {local_ip}")
print(f"Target Probe   : {target_probe_host}:{target_probe_port}")
print(f"Port Reachable : {is_service_reachable}")
print("========================================")
