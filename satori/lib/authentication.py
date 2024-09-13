import hmac
import hashlib
from eth_account import Account
from eth_account.messages import encode_defunct
from base64 import b64encode
from Crypto.PublicKey import RSA, ECC
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15, eddsa


def hmac_hashing(api_secret, payload):
    m = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), hashlib.sha256)
    return m.hexdigest()


def rsa_signature(private_key, payload, private_key_pass=None):
    private_key = RSA.import_key(private_key, passphrase=private_key_pass)
    h = SHA256.new(payload.encode("utf-8"))
    signature = pkcs1_15.new(private_key).sign(h)
    return b64encode(signature)


def ed25519_signature(private_key, payload, private_key_pass=None):
    private_key = ECC.import_key(private_key, passphrase=private_key_pass)
    signer = eddsa.new(private_key, "rfc8032")
    signature = signer.sign(payload.encode("utf-8"))
    return b64encode(signature)

def secp256k1_signature(private_key, payload, private_key_pass=None):
    account = Account.from_key(private_key)
    signed_message = account.sign_message(encode_defunct(text=payload))
    return "0x" + hex(signed_message.r)[2:].zfill(64) + hex(signed_message.s)[2:].zfill(64) + hex(signed_message.v)[2:]

def sign_with_type(api_sign_type, api_secret, payload, private_key_pass=None):
    if api_sign_type is None:
        api_sign_type = 1
    if int(api_sign_type) == 1:
        return hmac_hashing(api_secret, payload)
    elif int(api_sign_type) == 2:
        print("payload: " + str(payload))
        sign = secp256k1_signature(
            api_secret, payload, private_key_pass
        )
        print("sign: " + sign)
        return sign
    elif int(api_sign_type) == 3:
        try:
            return ed25519_signature(
                api_secret, payload, private_key_pass
            )
        except ValueError:
            return rsa_signature(api_secret, payload, private_key_pass)
    else:
        return hmac_hashing(api_secret, payload)