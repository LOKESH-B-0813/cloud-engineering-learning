# 01_system_state.py - Infrastructure Node Health Check

# Server identity and port configuration
instance_id = "prod-srv-01"
ssh_port = 22
disk_usage_pct = 82.5
is_production = True
disk_threshold = 80.0

# Logic check: evaluate if action is required
needs_alert = is_production and (disk_usage_pct > disk_threshold)

# Formatted output log
print("========================================")
print(f"HOST: {instance_id} | PORT: {ssh_port}")
print(f"ENVIRONMENT: {'PRODUCTION' if is_production else 'NON-PROD'}")
print(f"CURRENT USAGE: {disk_usage_pct}% (LIMIT: {disk_threshold}%)")
print(f"ALERT TRIGGERED: {needs_alert}")
print("========================================")
