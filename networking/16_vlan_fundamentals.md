# Day 16: Virtual Local Area Networks (VLANs) & Trunking

## Segmentation at Layer 2
* VLANs divide a single physical switch into multiple isolated broadcast domains.
* Access Ports: Carry untagged traffic assigned to a single specific VLAN.
* Trunk Ports: Carry traffic for multiple VLANs across switches using IEEE 802.1Q encapsulation (inserts a 4-byte VLAN tag into the Ethernet frame header).
