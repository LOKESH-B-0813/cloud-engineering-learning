# 34_memory_headroom_guard.py - Evaluates available memory headroom before swapping
def check_memory_headroom():
    mem = {}
    with open("/proc/meminfo", "r") as f:
        for line in f:
            k, v = line.split(":")[:2]
            mem[k.strip()] = int(v.split()[0])
    total = mem.get("MemTotal", 1)
    avail = mem.get("MemAvailable", 0)
    headroom_pct = round((avail / total) * 100, 2)
    return headroom_pct

pct = check_memory_headroom()
print(f"System Available Memory Headroom: {pct}%")
print(f"Memory Headroom Safe (> 15%): {pct > 15.0}")
