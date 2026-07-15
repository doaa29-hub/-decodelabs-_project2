"""
cipher.py
----------
Core logic for the DecodeLabs Caesar Cipher (Project 2).

Simple version: two functions (encrypt and decrypt), plain logic.
"""


def encrypt(text, shift):
    """Shift every letter in text forward by `shift` positions."""
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
        elif char.islower():
            result += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
        else:
            # Leave spaces, numbers, and punctuation unchanged
            result += char

    return result


def decrypt(text, shift):
    """Reverse a Caesar cipher shift (same as encrypting with -shift)."""
    return encrypt(text, -shift)
