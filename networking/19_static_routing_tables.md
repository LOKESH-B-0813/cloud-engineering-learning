# Day 19: Static Routing & Routing Table Logic

## Routing Table Lookup Mechanics
* Routers evaluate packets using the Longest Prefix Match (LPM) rule.
* Administrative Distance (AD): Determines route trustworthiness (Directly Connected = 0, Static Route = 1).
* Metric: Cost associated with the path (bandwidth, hop count, delay).

## Default Gateway / Route of Last Resort
* Destination: 0.0.0.0/0
* Next-Hop IP: Outbound router interface handling internetwork traffic.
