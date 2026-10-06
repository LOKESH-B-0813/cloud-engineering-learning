# 15_icmp_ping_tester.py - Layer 3 ICMP Echo Probe
import subprocess

target_host = "1.1.1.1"

def check_host_reachability(host):
    res = subprocess.run(["ping", "-c", "2", "-W", "2", host], stdout=subprocess.DEVNULL)
    return res.returncode == 0

status = "REACHABLE" if check_host_reachability(target_host) else "UNREACHABLE"
print(f"Target {target_host} is {status}")
