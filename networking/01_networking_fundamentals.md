# Day 1: Networking Fundamentals

## Traffic Flow Architecture
`Host (PC/Server)` -> `Switch (Layer 2 - MAC Table)` -> `Firewall (Stateful Inspection)` -> `Router (Layer 3 - IP Routing)` -> `Internet/WAN`

## Hardware Roles
* **Hub (L1):** Dumb electrical repeater; broadcasts frames blindly to all ports; high collisions.
* **Switch (L2):** Intelligent local forwarder; maintains MAC Address Table to direct frames to specific ports.
* **Router (L3):** Forwards packets across different subnets/networks based on IP routing tables.
* **Firewall (L3-L7):** Inspects packet states and drops unauthorized connections via security policies.

## Key Performance Indicators
* **Bandwidth:** Theoretical maximum data rate of a medium (e.g., 1 Gbps).
* **Throughput:** Actual measured data transferred over time.
* **Latency:** Delay for a packet to travel source to destination (ms).
* **Jitter:** Fluctuation in latency over time (critical for real-time traffic).
* **Duplex:** Half-Duplex (one direction at a time, e.g., Wi-Fi) vs Full-Duplex (simultaneous send/receive, e.g., switched Ethernet).
