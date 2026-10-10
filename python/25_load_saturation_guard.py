# 25_load_saturation_guard.py - Evaluates CPU saturation relative to hardware threads
import os

load_1m, _, _ = os.getloadavg()
cpu_count = os.cpu_count() or 1
saturation_ratio = round((load_1m / cpu_count) * 100, 2)

print(f"1-Minute Load Average: {load_1m} across {cpu_count} CPU cores")
print(f"CPU Thread Saturation: {saturation_ratio}%")
print(f"System Overloaded:     {saturation_ratio > 100.0}")
