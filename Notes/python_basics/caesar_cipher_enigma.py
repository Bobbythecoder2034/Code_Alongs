import math
import random

def cipher_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or not
            base = ord("A") if char.isupper() else ord('a')
            # Perform the shift ensuring it wraps around the alphabet
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            # Non-alphabet characters remain unchanged
            encrypted += char 

    return encrypted

name = "Ana"
done = cipher_encrypt(name, 5)
print(done)


def cipher_decrypt(encrypted_text, unshift):
    # Decrypt is simply encryption with the negative of the shift
    return cipher_encrypt(encrypted_text, unshift)

print(cipher_decrypt(done, -5))
print(cipher_encrypt(name, 5))