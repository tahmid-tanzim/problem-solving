#!/usr/bin/python3
# https://www.algoexpert.io/questions/Caesar%20Cipher%20Encryptor
"""
Shift every letter in the input string by k position.
"""


# O(n) time, O(n) space
def caesarCipherEncryptor(string, key):
    encryptedStr = ""
    key %= 26
    for s in string:
        ASCII = ord(s) + key
        if ASCII > ord('z'):
            ASCII -= 26
        encryptedStr += chr(ASCII)
    return encryptedStr


if __name__ == '__main__':
    print(caesarCipherEncryptor("xyz", 2))  # zab
