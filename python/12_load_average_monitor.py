# 12_load_average_monitor.py - Kernel Load Average Parser
import os
load_1, load_5, load_15 = os.getloadavg()
print(f"Load Average: 1m={load_1}, 5m={load_5}, 15m={load_15}")
