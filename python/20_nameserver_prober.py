# 20_nameserver_prober.py - Parses /etc/resolv.conf and probes nameserver port 53
import socket

def get_nameservers():
    ns_list = []
    with open("/etc/resolv.conf", "r") as f:
        for line in f:
            if line.startswith("nameserver"):
                ns_list.append(line.split()[1])
    return ns_list

def test_dns_port(ns):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(2.0)
    try:
        sock.connect((ns, 53))
        sock.close()
        return True
    except Exception:
        return False

for ns in get_nameservers():
    print(f"Nameserver: {ns:<15} | Port 53 UDP Reachable: {test_dns_port(ns)}")
