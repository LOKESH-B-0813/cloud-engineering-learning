# 23_swap_usage_analyzer.py - Evaluates Linux swap allocation from /proc/meminfo
def get_swap_metrics():
    swap_info = {}
    with open("/proc/meminfo", "r") as f:
        for line in f:
            if "SwapTotal" in line or "SwapFree" in line:
                k, v = line.split(":")
                swap_info[k.strip()] = int(v.split()[0])
    total = swap_info.get("SwapTotal", 0)
    free = swap_info.get("SwapFree", 0)
    used = total - free
    percent = round((used / total * 100), 2) if total > 0 else 0.0
    return total, used, percent

tot, usd, pct = get_swap_metrics()
print(f"Swap Total: {tot // 1024} MB | Swap Used: {usd // 1024} MB ({pct}%)")
