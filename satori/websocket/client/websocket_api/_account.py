import json

from satori.lib.utils import hmac_hashing


def account(self, symbol: str):
    time = self.get_time()
    payload = {
        "symbol": symbol,
        "method": self.ACTION_SUBSCRIBE,
        "event": "api_account",
        "apiKey": self.api_key,
        "signature": self.sign(str(time)),
        "timestamp": time,
        "signType": self.api_sign_type
    }
    print("req: " + json.dumps(payload, ensure_ascii=False))
    self.send(payload)


