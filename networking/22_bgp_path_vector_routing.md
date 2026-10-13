# Day 22: Border Gateway Protocol (BGP) Architecture

## The Core Routing Engine of the Internet
* Type: Exterior Gateway Protocol (EGP), Path-Vector protocol.
* Operates over reliable Layer 4 TCP transport on port 179.
* Autonomous System (AS): Collection of IP networks under a single administrative domain using globally unique ASN numbers.

## BGP Flavors & Attributes
* eBGP (External BGP): Exchanges prefixes between distinct Autonomous Systems.
* iBGP (Internal BGP): Propagates external routing prefixes inside the same Autonomous System.
* Path Attributes for Route Selection: Weight (Cisco local) -> Local Preference -> AS-Path Length -> Origin -> MED (Multi-Exit Discriminator).
