# 35_pid_limit_inspector.py - Verifies system maximum PID allocation capacity
def get_pid_limits():
    with open("/proc/sys/kernel/pid_max", "r") as f:
        max_pids = int(f.read().strip())
    with open("/proc/sys/kernel/threads-max", "r") as f:
        max_threads = int(f.read().strip())
    return max_pids, max_threads

p_max, t_max = get_pid_limits()
print(f"Kernel Max PIDs:    {p_max}")
print(f"Kernel Max Threads: {t_max}")
