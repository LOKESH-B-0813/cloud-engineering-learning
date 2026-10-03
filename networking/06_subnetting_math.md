# Day 6: Subnetting Mathematical Foundations

## The Rule of Powers of 2
Subnetting relies on binary place values:
* 2^1 = 2
* 2^2 = 4
* 2^3 = 8
* 2^4 = 16
* 2^5 = 32
* 2^6 = 64
* 2^7 = 128
* 2^8 = 256

## Host Formula
* Number of usable hosts = 2^H - 2
* H = Number of host bits (0s in the subnet mask).
* The "- 2" subtracts:
  1. The Network ID (first address, all host bits 0)
  2. The Broadcast address (last address, all host bits 1)

## CIDR Prefix Quick Lookup (/24 to /30)
* /24: 256 Total IPs -> 254 Usable Hosts (Mask: 255.255.255.0)
* /25: 128 Total IPs -> 126 Usable Hosts (Mask: 255.255.255.128)
* /26: 64 Total IPs  -> 62 Usable Hosts  (Mask: 255.255.255.192)
* /27: 32 Total IPs  -> 30 Usable Hosts  (Mask: 255.255.255.224)
* /28: 16 Total IPs  -> 14 Usable Hosts  (Mask: 255.255.255.240)
* /29: 8 Total IPs   -> 6 Usable Hosts   (Mask: 255.255.255.248)
* /30: 4 Total IPs   -> 2 Usable Hosts   (Mask: 255.255.255.252 - Point-to-Point links)
