# 16_file_descriptor_audit.py - Linux File Descriptor Usage Audit
def audit_system_file_descriptors():
    with open("/proc/sys/fs/file-nr", "r") as f:
        allocated, _, maximum = f.readline().split()
    return int(allocated), int(maximum)

alloc, max_fd = audit_system_file_descriptors()
percentage = round((alloc / max_fd) * 100, 4)
print(f"Allocated FDs: {alloc} / {max_fd} ({percentage}%)")
