# Day 17: Spanning Tree Protocol (IEEE 802.1D STP)

## Preventing Layer 2 Loops
* Redundant links between switches cause broadcast storms and CAM table thrashing.
* STP builds a loop-free logical topology by electing a Root Bridge and blocking redundant switch ports.
* Convergence States: Blocking -> Listening -> Learning -> Forwarding.
