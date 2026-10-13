# 39_hugepages_auditor.py - Audits kernel HugePages allocation state
def audit_hugepages():
    hp_metrics = {}
    with open("/proc/meminfo", "r") as f:
        for line in f:
            if "HugePages" in line or "Hugepagesize" in line:
                k, v = line.split(":")
                hp_metrics[k.strip()] = v.strip()
    return hp_metrics

print("=== KERNEL HUGEPAGES METRICS ===")
for k, v in audit_hugepages().items():
    print(f"{k:<20}: {v}")
