# Day 14: Address Resolution Protocol (ARP) & Security

## Address Resolution Workflow
* Operates between Layer 2 (Data Link) and Layer 3 (Network).
* Broadcasts Layer 2 frames (FF:FF:FF:FF:FF:FF) asking "Who owns IPv4 X.X.X.X?".
* Receiving node replies with Unicast Layer 2 frame containing its physical MAC address.

## Security Considerations
* ARP is stateless and lacks authentication.
* ARP Poisoning / Spoofing: Malicious hosts can send gratuitous ARP replies to poison CAM tables and hijack traffic.
