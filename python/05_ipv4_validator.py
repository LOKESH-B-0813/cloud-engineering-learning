# 05_ipv4_validator.py - IPv4 Address Format & Scope Validation Utility
# Evolution of 04_network_socket_auditor.py: Parses raw string addresses into Layer 3 octets.

import ipaddress

test_ips = [
    "192.168.1.1",
    "127.0.0.1",
    "8.8.8.8",
    "169.254.10.5",
    "999.1.1.1"  # Invalid intentionally
]

print("=== LAYER 3 IPv4 VALIDATION ENGINE ===")

for ip_str in test_ips:
    try:
        obj = ipaddress.ip_address(ip_str)
        print(f"IP: {ip_str:<15} | Valid: True  | Private: {obj.is_private!s:<5} | Loopback: {obj.is_loopback!s:<5}")
    except ValueError:
        print(f"IP: {ip_str:<15} | Valid: False | [MALFORMED IPv4 ADDRESS]")

print("======================================")
