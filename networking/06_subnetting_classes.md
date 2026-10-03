# Day 6: IPv4 Address Classes & Classful Addressing History

## The Classful Addressing Scheme (Historical)
* Class A: 1.0.0.0 to 126.255.255.255
  - Default Mask: 255.0.0.0 (/8)
  - Designed for massive networks (16M+ hosts per network)
* Class B: 128.0.0.0 to 191.255.255.255
  - Default Mask: 255.255.0.0 (/16)
  - Designed for medium networks (65,534 hosts)
* Class C: 192.0.0.0 to 223.255.255.255
  - Default Mask: 255.255.255.0 (/24)
  - Designed for small networks (254 hosts)
* Class D: 224.0.0.0 to 239.255.255.255
  - Reserved strictly for Multicast traffic
* Class E: 240.0.0.0 to 255.255.255.255
  - Reserved for experimental / future research

## The Problem With Classful Networking
Massive address waste. A company needing 300 IP addresses was forced to take a Class B block (65,534 addresses), wasting 65,000+ IPs. This led directly to the creation of CIDR (Classless Inter-Domain Routing).
