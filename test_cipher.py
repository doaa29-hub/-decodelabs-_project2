"""
test_cipher.py
----------------
Simple tests for cipher.py. Run with:

    python -m unittest test_cipher.py
"""

import unittest
from cipher import encrypt, decrypt


class TestCaesarCipher(unittest.TestCase):

    def test_encrypt_basic_shift(self):
        self.assertEqual(encrypt("A", 3), "D")

    def test_encrypt_wraps_around(self):
        self.assertEqual(encrypt("Y", 3), "B")

    def test_encrypt_keeps_case(self):
        self.assertEqual(encrypt("Hello", 3), "Khoor")

    def test_encrypt_leaves_non_letters(self):
        self.assertEqual(encrypt("Hi, 123!", 3), "Kl, 123!")

    def test_decrypt_reverses_encrypt(self):
        original = "Attack at dawn!"
        shift = 7
        ciphertext = encrypt(original, shift)
        self.assertEqual(decrypt(ciphertext, shift), original)


if __name__ == "__main__":
    unittest.main()
