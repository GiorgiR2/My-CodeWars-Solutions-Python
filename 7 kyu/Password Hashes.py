# https://www.codewars.com/kata/password-hashes/train/python
import hashlib

def pass_hash(str):
    crypt = hashlib.md5()
    crypt.update(str.encode())
    return crypt.hexdigest()
