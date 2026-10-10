# Day 15: Layer 2 Switching Logic & CAM Tables

## MAC Address Table Mechanics
* Switches inspect the Source MAC address of incoming frames to populate the CAM (Content Addressable Memory) table.
* The CAM table maps specific MAC addresses to physical switch ports with an aging timer (default ~300 seconds).
* Forwarding decisions:
  - Known Destination MAC: Forwarded solely to the mapped switch port (Unicast).
  - Unknown Destination MAC: Flooded out all active ports except the incoming port (Unknown Unicast Flooding).
