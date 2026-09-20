# 01_system_state.py - Node State Evaluation Engine

server_name = "web-prod-node-01"
ssh_port = 22
current_disk_usage = 84.6
disk_limit = 80.0
is_production = True
# Evaluates true only if node is production AND storage exceeds safety margin
trigger_alert = is_production and (current_disk_usage > disk_limit)

print("--- SYSTEM DIAGNOSTIC REPORT ---")
print(f"Node: {server_name} | Management Port: {ssh_port}")
print(f"Current Usage: {current_disk_usage}% | Max Limit: {disk_limit}%")
print(f"Production Environment: {is_production}")
print(f"Alert Triggered: {trigger_alert}")
print("--------------------------------")
