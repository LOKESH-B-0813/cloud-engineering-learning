# Day 5: IPv4 Logical Addressing & Binary Structure

## Address Format
* 32 Bits total split into 4 decimal octets separated by dots (0-255 per octet)[cite: 3].
* Address Space: 2^32 ≈ 4.29 Billion distinct addresses[cite: 3].

## Logical Subdivision
* [ Network Bits ] determines subnet routing identity[cite: 3].
* [ Host Bits ] determines host assignment on the subnet[cite: 3].
* Subnet Mask defines the boundary separating network bits from host bits[cite: 3].

## Reserved IP Ranges
* 127.0.0.1: Loopback local system interface[cite: 3]
* 0.0.0.0: Default route / unspecified wildcard[cite: 3]
* 255.255.255.255: Local broadcast address[cite: 3]
* 169.254.0.0/16: APIPA auto-assignment fallback[cite: 3]
