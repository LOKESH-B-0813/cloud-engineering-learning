# Day 7: RFC 1918 Private IP Address Allocations

## The 3 Private IP Ranges (Non-Routable on Public Internet)
1. Class A Private:
   - Range: 10.0.0.0 to 10.255.255.255
   - Prefix: 10.0.0.0/8
   - Total Addresses: 16,777,216

2. Class B Private:
   - Range: 172.16.0.0 to 172.31.255.255
   - Prefix: 172.16.0.0/12
   - Total Addresses: 1,048,576

3. Class C Private:
   - Range: 192.168.0.0 to 192.168.255.255
   - Prefix: 192.168.0.0/16
   - Total Addresses: 65,536

## Why RFC 1918 Exists
Private IPs allow thousands of local devices (homes, data centers, office buildings) to share the same address spaces internally without collisions. Outbound traffic is converted to a single public IP using NAT (Network Address Translation).
