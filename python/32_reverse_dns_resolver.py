# 32_reverse_dns_resolver.py - PTR Record IP to Hostname Resolver
import socket

test_ip = "8.8.8.8"

try:
    host_name, _, _ = socket.gethostbyaddr(test_ip)
    print(f"IPv4: {test_ip} -> PTR Hostname: {host_name}")
except socket.herror:
    print(f"IPv4: {test_ip} -> No PTR record resolved")
