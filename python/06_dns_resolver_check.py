# 06_dns_resolver_check.py - Transport & Application Layer DNS Resolution Check
# Evolution of 05_ipv4_validator.py: Resolves FQDN domain names to Layer 3 IPv4 addresses.

import socket

domains = ["google.com", "github.com", "localhost"]

print("=== DNS TO LAYER 3 ADDRESS RESOLUTION ===")
for domain in domains:
    try:
        resolved_ip = socket.gethostbyname(domain)
        print(f"Domain: {domain:<15} -> IPv4: {resolved_ip}")
    except socket.gaierror as e:
        print(f"Domain: {domain:<15} -> FAILED: {e}")
print("=========================================")
