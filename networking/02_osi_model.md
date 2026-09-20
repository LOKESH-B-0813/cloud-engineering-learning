# Day 2: The 7-Layer OSI Reference Framework

## Layer Hierarchy & Protocol Data Units (PDUs)
* Layer 7 (Application): Data - User interface protocols (HTTP, HTTPS, DNS, SSH)
* Layer 6 (Presentation): Data - Encryption, encoding, compression (TLS/SSL)
* Layer 5 (Session): Data - Dialog control and synchronization checkpoints
* Layer 4 (Transport): Segment/Datagram - End-to-end ports, reliability (TCP, UDP)
* Layer 3 (Network): Packet - Logical path addressing & routing (IP, ICMP)
* Layer 2 (Data Link): Frame - Physical hop delivery & error checking (MAC, Ethernet)
* Layer 1 (Physical): Bits - Electrical, optical, or radio signal transmission

## Encapsulation Pipeline
Data (L7-L5) -> Segment (+L4 Port) -> Packet (+L3 IP) -> Frame (+L2 MAC & CRC) -> Bits (L1)

## Diagnostic Rules of Thumb
* L1 Issue: Cable unplugged / link interface down (state DOWN)
* L2 Issue: Local switch forwarding or MAC table resolution failure
* L3 Issue: Default gateway unreachable / bad routing table
* L4 Issue: Firewall blocking transport port or daemon process down
* L7 Issue: Service error (HTTP 500, DNS NXDOMAIN)
