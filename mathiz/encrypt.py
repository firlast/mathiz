import hashlib
from base64 import urlsafe_b64encode


def _transform_key(key: str) -> bytes:
    key_hash = hashlib.md5(key.encode()).hexdigest()
    key_b64 = urlsafe_b64encode(key_hash.encode())
    return key_b64
