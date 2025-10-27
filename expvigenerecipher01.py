def vigenere_encrypt(plain_text, key):
    result = []
    key = key.upper()
    k = 0
    for ch in plain_text:
        if ch.isalpha():
            shift = ord(key[k % len(key)]) - 65
            base = 65 if ch.isupper() else 97
            result.append(chr((ord(ch) - base + shift) % 26 + base))
            k += 1
        else:
            result.append(ch)
    return ''.join(result)


def vigenere_decrypt(cipher_text, key):
    result = []
    key = key.upper()
    k = 0
    for ch in cipher_text:
        if ch.isalpha():
            shift = ord(key[k % len(key)]) - 65
            base = 65 if ch.isupper() else 97
            result.append(chr((ord(ch) - base - shift) % 26 + base))
            k += 1
        else:
            result.append(ch)
    return ''.join(result)

message = input("Enter message: ")
key = input("Enter key: ")

enc = vigenere_encrypt(message, key)
print("Encrypted Text:", enc)

dec = vigenere_decrypt(enc, key)
print("Decrypted Text:", dec)
