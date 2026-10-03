# 07_memory_guard.py - System RAM and Swap Usage Diagnostic
# Evolution of 06_dns_resolver_check.py: Audits Linux /proc/meminfo memory utilization.

def get_memory_usage():
    mem_info = {}
    with open("/proc/meminfo", "r") as f:
        for line in f:
            parts = line.split(":")
            if len(parts) == 2:
                mem_info[parts[0].strip()] = int(parts[1].split()[0])
    
    total = mem_info.get("MemTotal", 1)
    free = mem_info.get("MemAvailable", 0)
    used = total - free
    usage_percent = round((used / total) * 100, 2)
    return usage_percent

usage = get_memory_usage()
print(f"Current System Memory Utilization: {usage}%")
print(f"Memory Alert Triggered: {usage > 85.0}")
