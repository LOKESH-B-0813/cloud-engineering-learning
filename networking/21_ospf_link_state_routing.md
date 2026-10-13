# Day 21: Open Shortest Path First (OSPF) Protocol

## Architecture & Operation
* Type: Interior Gateway Protocol (IGP), Link-State routing protocol.
* Algorithm: Dijkstra's Shortest Path First (SPF) algorithm.
* Metric: Cost based on reference bandwidth ($10^8 / \text{Bandwidth in bps}$).
* Hierarchical Design:
  - Backbone Area (Area 0): Central transit hub through which all inter-area traffic must pass.
  - Non-Backbone Areas: Connect directly to Area 0 via Area Border Routers (ABRs).

## Packet Exchange & Adjacency
* Hello packets discover neighbors and maintain keepalives (Multicast 224.0.0.5 / 224.0.0.6).
* Adjacency States: Down -> Init -> 2-Way -> ExStart -> Exchange -> Loading -> Full.
* Link-State Advertisements (LSAs) flood topological state across the link-state database (LSDB).
