import hashlib
from base64 import urlsafe_b64encode

from cryptography.fernet import Fernet


class EncyptCookies:
    def __init__(self, secret_key: str) -> None:
        key = self._transform_key(secret_key)
        self._fernet = Fernet(key)

    @staticmethod
    def _transform_key(key: str) -> bytes:
        key_hash = hashlib.md5(key.encode()).hexdigest()
        key_b64 = urlsafe_b64encode(key_hash.encode())
        return key_b64
