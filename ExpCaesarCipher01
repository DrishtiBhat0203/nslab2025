def caesar_encrypt(msg, shift):
    cipher_text = ""
    for ch in msg:
        if ch.isalpha():
            base = 65 if ch.isupper() else 97
            cipher_text += chr((ord(ch) - base + shift) % 26 + base)
        else:
            cipher_text += ch
    return cipher_text


def caesar_decrypt(cipher, shift):
    plain_text = ""
    for ch in cipher:
        if ch.isalpha():
            base = 65 if ch.isupper() else 97
            plain_text += chr((ord(ch) - base - shift) % 26 + base)
        else:
            plain_text += ch
    return plain_text

text = input("Enter your message: ")
key = int(input("Enter shift value: "))

encrypted_text = caesar_encrypt(text, key)
print("Encrypted Text:", encrypted_text)

decrypted_text = caesar_decrypt(encrypted_text, key)
print("Decrypted Text:", decrypted_text)
