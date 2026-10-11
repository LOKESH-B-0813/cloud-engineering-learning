# Day 20: Dynamic Routing Protocol Classifications

## Protocol Taxonomy
* Interior Gateway Protocols (IGP): Operates within an Autonomous System (AS).
  - Distance-Vector: RIP (Hop count), EIGRP (Composite metric: Bandwidth/Delay).
  - Link-State: OSPF, IS-IS (Dijkstra Shortest Path First algorithm).
* Exterior Gateway Protocols (EGP): Operates between Autonomous Systems.
  - Path-Vector: BGP (Border Gateway Protocol) routing the global internet.
