# 04_network_socket_auditor.py - Dynamic Host Identity and Socket Audit Utility
# Evolution of 03_system_logger.py: Verifies network layer addressing and target reachability.

import socket

local_hostname = socket.gethostname()
local_ip = socket.gethostbyname(local_hostname)
target_probe_host = "8.8.8.8"
target_probe_port = 53
