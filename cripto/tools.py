import hashlib
import hmac


def create_sha256_signature(key, message):
    byte_key = bytes(key, 'UTF-8')
    message = message.encode()
    return hmac.new(byte_key, message, hashlib.sha256).hexdigest().upper()


def is_valid_binance_api(api, secret_key):
    from cripto.binance import account_status

    if account_status(api, secret_key):
        return True
    else:
        return False
