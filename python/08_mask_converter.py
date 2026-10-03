# 08_mask_converter.py - Subnet Mask to CIDR Prefix Length Converter
# Evolution of 07_memory_guard.py: Converts dotted-decimal masks to CIDR slash notation.

def mask_to_cidr(mask_str):
    octets = [int(x) for x in mask_str.split(".")]
    binary_str = "".join([f"{bin(octet)[2:]:0>8}" for octet in octets])
    return binary_str.count("1")

test_masks = [
    "255.255.255.0",
    "255.255.255.128",
    "255.255.255.192",
    "255.255.255.252"
]

print("=== SUBNET MASK TO CIDR NOTATION ===")
for m in test_masks:
    print(f"Mask: {m:<16} -> Prefix: /{mask_to_cidr(m)}")
print("====================================")
