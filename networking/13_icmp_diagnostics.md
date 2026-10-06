# Day 13: Internet Control Message Protocol (ICMP)

## Core Functions
* Operates at Layer 3 (Network Layer) alongside IPv4 and IPv6.
* Used by network devices to send error messages and operational information.
* Does not use Layer 4 port numbers; identifies packet intent via Type and Code fields.

## Primary Diagnostic Tools
* Ping: Uses ICMP Echo Request (Type 8) and Echo Reply (Type 0) to measure RTT latency.
* Traceroute: Uses ICMP Time Exceeded (Type 11) generated when TTL (Time to Live) drops to 0.
