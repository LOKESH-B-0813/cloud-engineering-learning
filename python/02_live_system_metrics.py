# 02_live_system_metrics.py - Live Node Metrics Engine
# Evolution of 01_system_state.py: Replaces static values with live OS calls.

import shutil
import socket

# Dynamic node identity
server_name = socket.gethostname()
ssh_port = 22
disk_limit = 80.0
is_production = True

# Query live storage metrics from the root filesystem ("/")
total, used, free = shutil.disk_usage("/")
current_disk_usage = round((used / total) * 100, 2)

# Alert logic
trigger_alert = is_production and (current_disk_usage > disk_limit)

# Formatted output report
print("--- LIVE SYSTEM DIAGNOSTIC REPORT ---")
print(f"Node: {server_name} | Port: {ssh_port}")
print(f"Live Disk Usage: {current_disk_usage}% | Threshold: {disk_limit}%")
print(f"Production Flag: {is_production}")
print(f"Alert Triggered: {trigger_alert}")
print("-------------------------------------")
