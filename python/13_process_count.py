# 13_process_count.py - Active Process Counter via /proc
import os
pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
print(f"Total Running Process Threads: {len(pids)}")
