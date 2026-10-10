# 24_context_switch_auditor.py - Kernel Context Switch & Fork Counter
def parse_stat_metrics():
    metrics = {}
    with open("/proc/stat", "r") as f:
        for line in f:
            parts = line.split()
            if parts[0] in ["ctxt", "processes", "procs_running"]:
                metrics[parts[0]] = int(parts[1])
    return metrics

data = parse_stat_metrics()
print(f"Total Context Switches: {data.get('ctxt', 0):,}")
print(f"Total Process Forks:    {data.get('processes', 0):,}")
print(f"Currently Running:      {data.get('procs_running', 0)}")
