# 18_os_release_validator.py - OS Identity Parser
def read_os_release():
    os_info = {}
    with open("/etc/os-release", "r") as f:
        for line in f:
            if "=" in line:
                k, v = line.strip().split("=", 1)
                os_info[k] = v.strip('"')
    return os_info.get("PRETTY_NAME", "Unknown Linux")

print(f"Operating Platform: {read_os_release()}")
