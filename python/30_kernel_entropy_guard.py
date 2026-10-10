# 30_kernel_entropy_guard.py - Audits system entropy pool for cryptographic security
def get_entropy():
    with open("/proc/sys/kernel/random/entropy_avail", "r") as f:
        return int(f.read().strip())

entropy = get_entropy()
print(f"System Available Entropy: {entropy} bits")
print(f"Cryptographic Entropy Healthy: {entropy >= 1000}")
