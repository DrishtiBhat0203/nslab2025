import hashlib

def generate_sha256(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest

original_text = input("Enter the original message: ").strip()
altered_text = input("Enter the tampered text: ").strip()

hash_original = generate_sha256(original_text)
hash_altered = generate_sha256(altered_text)


print(f"\nOriginal Text: {original_text}")
print(f"Tampered Text: {altered_text}")
print(f"Original Hash: {hash_original}")
print(f"Tampered Hash: {hash_altered}")

if hash_original == hash_altered:
    print("\n Data integrity verified (no tampering)")
else:
    print("\n Warning: Data has been tampered (hashes differ).")
