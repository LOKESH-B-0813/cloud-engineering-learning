# 14_network_interfaces.py - NIC Interface Enumerator
import os
interfaces = os.listdir('/sys/class/net')
print(f"Detected Network Interfaces: {', '.join(interfaces)}")
