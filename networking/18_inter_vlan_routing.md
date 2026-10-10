# Day 18: Inter-VLAN Routing Architectures

## Layer 3 Communication Between VLANs
* Devices in different VLANs cannot communicate at Layer 2 and require Layer 3 routing.
* Router-on-a-Stick (ROAS): Uses a single physical trunk link divided into logical sub-interfaces with 802.1Q encapsulation.
* Layer 3 Switch (Multilayer Switching): Routes traffic between VLANs internally via Switched Virtual Interfaces (SVIs) at hardware line rate.
