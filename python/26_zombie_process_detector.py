# 26_zombie_process_detector.py - Detects lingering zombie processes in /proc
import os

zombies = []
for pid in [p for p in os.listdir("/proc") if p.isdigit()]:
    try:
        with open(f"/proc/{pid}/status", "r") as f:
            for line in f:
                if line.startswith("State:") and "Z (zombie)" in line:
                    zombies.append(pid)
    except (FileNotFoundError, PermissionError):
        continue

print(f"Detected Zombie Processes: {len(zombies)}")
if zombies:
    print(f"Zombie PIDs: {', '.join(zombies)}")
