# Day 4: Layer 2 MAC Addressing & Ethernet Frames

## MAC Structure (48 Bits / 6 Bytes)
* First 24 Bits: Organizationally Unique Identifier (OUI - Hardware Manufacturer)[cite: 4]
* Last 24 Bits: Device Serial Identifier assigned by vendor[cite: 4]
* Addressing Types: Unicast, Multicast, Broadcast (FF:FF:FF:FF:FF:FF)[cite: 4]

## Ethernet Frame Layout (IEEE 802.3)
Preamble (7B) -> SFD (1B) -> Dest MAC (6B) -> Src MAC (6B) -> EtherType (2B) -> Payload (46-1500B MTU) -> FCS (4B)[cite: 4]

## Switching Logic
* Switches learn incoming Source MACs and map them to physical ingress ports.
* Switches forward frames out the specific egress port matching the Destination MAC.
* Unknown Destination MACs trigger local segment flooding.
