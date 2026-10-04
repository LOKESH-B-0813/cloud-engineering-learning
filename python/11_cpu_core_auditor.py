# 11_cpu_core_auditor.py - Hardware CPU Core Counter
import os
cores = os.cpu_count()
print(f"Total Available Hardware Threads: {cores}")
