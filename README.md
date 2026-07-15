# -decodelabs-_project2
# 🔒 Caesar Cipher — Encryption & Decryption

**DecodeLabs Industrial Training Kit — Cyber Security Track, Project 2**

A simple command-line tool that encrypts and decrypts text using a
Caesar cipher (a classic "shift" cipher).

## How it works

Each letter is shifted forward in the alphabet by a chosen number
(the "key" or "shift"), wrapping back to `A` after `Z`:

```
E(x) = (x + shift) % 26      -> encrypt
D(x) = (x - shift) % 26      -> decrypt
```

Example with shift = 3:

```
Plaintext:  HELLO
Encrypted:  KHOOR
```

Spaces, numbers, and punctuation are left unchanged. Uppercase and
lowercase letters keep their case.

## Files

```
caesar_cipher/
├── cipher.py         # encrypt() and decrypt() functions
├── main.py             # Run this to use the tool
├── test_cipher.py       # Tests
└── README.md
```

## How to run it

```bash
python main.py
```

Example session:

```
=== DecodeLabs Caesar Cipher ===
Type 'quit' at any time to exit.

Encrypt or decrypt? (e/d): e
Enter your text: Hello, World!
Enter shift key (a whole number): 3

Encrypted text: Khoor, Zruog!

Encrypt or decrypt? (e/d): d
Enter your text: Khoor, Zruog!
Enter shift key (a whole number): 3

Decrypted text: Hello, World!

Encrypt or decrypt? (e/d): quit
Goodbye!
```

## Running the tests

```bash
python -m unittest test_cipher.py -v
```

## Using it in your own code

```python
from cipher import encrypt, decrypt

secret = encrypt("Attack at dawn", 5)
print(secret)              # "Fyyfhp fy ifbs"
print(decrypt(secret, 5))  # "Attack at dawn"
```

## Why this cipher isn't real-world secure

- **Tiny key space** — only 25 possible shifts, so it can be
  brute-forced instantly.
- **Pattern preservation** — the cipher doesn't change how often each
  letter appears, so it can be broken with frequency analysis.

This is why real systems use much stronger algorithms like AES, which
combine many rounds of substitution and mixing instead of a single
fixed shift.

## Ideas to extend it

- Let the user pick the shift with a `-shift` random key option
- Detect the shift automatically using letter-frequency analysis
- Implement a Vigenère cipher (a multi-letter keyword version of this same idea)
