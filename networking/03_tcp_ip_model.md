# Day 3: TCP/IP 4-Layer Model Architecture

## Model Layers
* Layer 4: Application (HTTP, HTTPS, DNS, SSH, TLS) - Consolidates OSI L7, L6, L5
* Layer 3: Transport (TCP, UDP) - End-to-end ports and delivery control
* Layer 2: Internet (IPv4, IPv6, ICMP, ARP) - Logical packet routing across subnets
* Layer 1: Network Access (Ethernet, Wi-Fi, MAC) - Physical framing and wire transmission

## Transport Mechanics
* TCP: 3-Way Handshake (SYN -> SYN-ACK -> ACK), reliable retransmissions, ordered delivery.
* UDP: Connectionless, lightweight fire-and-forget, low latency for DNS and streaming.

## Network Socket Definition
Socket = IP Address (Layer 3) + Port Number (Layer 4) (e.g., 192.168.1.50:443)
