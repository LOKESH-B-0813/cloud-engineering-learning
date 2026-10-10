# 27_interface_mtu_inspector.py - Audits MTU and link operational state from /sys/class/net
import os

def audit_interfaces():
    base_path = "/sys/class/net"
    results = {}
    for iface in os.listdir(base_path):
        try:
            with open(f"{base_path}/{iface}/mtu", "r") as f_mtu:
                mtu = f_mtu.read().strip()
            with open(f"{base_path}/{iface}/operstate", "r") as f_state:
                state = f_state.read().strip()
            results[iface] = (mtu, state)
        except (FileNotFoundError, PermissionError):
            continue
    return results

for iface, (mtu, state) in audit_interfaces().items():
    print(f"Interface: {iface:<12} | State: {state:<6} | MTU: {mtu}")
