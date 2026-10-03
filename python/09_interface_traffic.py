# 09_interface_traffic.py - Linux Network Device RX/TX Packet Counter
# Evolution of 08_mask_converter.py: Parses /proc/net/dev to audit byte throughput.

print("=== INTERFACE THROUGHPUT DUMP (/proc/net/dev) ===")
with open("/proc/net/dev", "r") as dev_file:
    lines = dev_file.readlines()[2:]  # Skip header rows
    for line in lines:
        data = line.split(":")
        if len(data) == 2:
            iface = data[0].strip()
            metrics = data[1].split()
            rx_bytes = int(metrics[0])
            tx_bytes = int(metrics[8])
            print(f"Interface: {iface:<10} | RX: {rx_bytes / (1024*1024):.2f} MB | TX: {tx_bytes / (1024*1024):.2f} MB")
print("==================================================")
