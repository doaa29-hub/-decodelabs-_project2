"""
main.py
--------
Simple command-line tool for encrypting and decrypting text
with a Caesar cipher.

Usage:
    python main.py
"""

from cipher import encrypt, decrypt


def main():
    print("=== DecodeLabs Caesar Cipher ===")
    print("Type 'quit' at any time to exit.\n")

    while True:
        choice = input("Encrypt or decrypt? (e/d): ").strip().lower()

        if choice == "quit":
            print("Goodbye!")
            break

        if choice not in ("e", "d"):
            print("Please type 'e' for encrypt, 'd' for decrypt, or 'quit'.\n")
            continue

        text = input("Enter your text: ")
        if text.lower() == "quit":
            print("Goodbye!")
            break

        shift_input = input("Enter shift key (a whole number): ")
        if shift_input.lower() == "quit":
            print("Goodbye!")
            break

        if not shift_input.lstrip("-").isdigit():
            print("Shift key must be a number.\n")
            continue

        shift = int(shift_input)

        if choice == "e":
            print(f"\nEncrypted text: {encrypt(text, shift)}\n")
        else:
            print(f"\nDecrypted text: {decrypt(text, shift)}\n")


if __name__ == "__main__":
    main()
