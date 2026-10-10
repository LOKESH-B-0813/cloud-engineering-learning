# 29_disk_io_stat_reader.py - Evaluates disk read/write sector counts from /proc/diskstats
def parse_disk_stats():
    stats = {}
    with open("/proc/diskstats", "r") as f:
        for line in f:
            parts = line.split()
            if len(parts) >= 14 and not parts[2].startswith("loop"):
                device = parts[2]
                reads_completed = int(parts[3])
                writes_completed = int(parts[7])
                stats[device] = (reads_completed, writes_completed)
    return stats

for dev, (r, w) in parse_disk_stats().items():
    print(f"Block Device: {dev:<10} | Reads: {r:<8} | Writes: {w:<8}")
