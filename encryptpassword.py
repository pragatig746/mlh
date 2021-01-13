import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
password_from_user = input("Please enter your Password: ")
password = password_from_user.encode()

mysalt = b'?\xb4\xad\xd4*\x1b\x89|\xc3\x8a\x1a\x1d\x9c\xf4\x95\xad'
kdf = PBKDF2HMAC (
    algorithm = hashes.SHA256,
    length = 32,
    salt = mysalt,
    iterations = 100000,
    backend = default_backend()
)

key = base64.urlsafe_b64encode(kdf.derive(password))
print(key.decode())
