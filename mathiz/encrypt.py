import hashlib
from base64 import urlsafe_b64encode

from cryptography.fernet import Fernet


class EncyptCookies:
    def __init__(self, secret_key: str) -> None:
        key = self._transform_key(secret_key)
        self._fernet = Fernet(key)

    def encrypt_cookies(self, cookies: dict) -> dict:
        encrypted_cookies = {}

        for name, value in cookies.items():
            encrypted_name = self._fernet.encrypt(name.encode())
            encrypted_value = self._fernet.encrypt(value.encode())
            encrypted_name = encrypted_name.decode()
            encrypted_value = encrypted_value.decode()

            encrypted_cookies[encrypted_name] = encrypted_value

        return encrypted_cookies

    @staticmethod
    def _transform_key(key: str) -> bytes:
        key_hash = hashlib.md5(key.encode()).hexdigest()
        key_b64 = urlsafe_b64encode(key_hash.encode())
        return key_b64
