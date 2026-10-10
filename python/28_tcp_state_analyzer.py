# 28_tcp_state_analyzer.py - Audits TCP states from /proc/net/tcp
TCP_STATES = {
    "01": "ESTABLISHED", "02": "SYN_SENT", "03": "SYN_RECV",
    "04": "FIN_WAIT1", "05": "FIN_WAIT2", "06": "TIME_WAIT",
    "07": "CLOSE", "08": "CLOSE_WAIT", "09": "LAST_ACK",
    "0A": "LISTEN", "0B": "CLOSING"
}

def analyze_tcp_states():
    counts = {}
    with open("/proc/net/tcp", "r") as f:
        for line in f.readlines()[1:]:
            parts = line.split()
            if len(parts) >= 4:
                raw_state = parts[3]
                state_name = TCP_STATES.get(raw_state, "UNKNOWN")
                counts[state_name] = counts.get(state_name, 0) + 1
    return counts

for state, count in analyze_tcp_states().items():
    print(f"TCP State {state:<14}: {count}")
