import json

from satori.lib.utils import hmac_hashing


def order(self, pairName: str):
    time = self.get_time()
    payload = {
        "pair": pairName,
        "method": self.ACTION_SUBSCRIBE,
        "event": "api_entrust",
        "apiKey": self.api_key,
        "signature": self.sign(str(time)),
        "timestamp": time,
        "signType": self.api_sign_type
    }
    print("req: " + json.dumps(payload, ensure_ascii=False))
    self.send(payload)


def position(self, pairName: str):
    time = self.get_time()
    payload = {
        "pair": pairName,
        "method": self.ACTION_SUBSCRIBE,
        "event": "api_position",
        "apiKey": self.api_key,
        "signature": self.sign(str(time)),
        "timestamp": time,
        "signType": self.api_sign_type
    }
    print("req: " + json.dumps(payload, ensure_ascii=False))
    self.send(payload)


def kline(self, pairName: str, period: str):
    time = self.get_time()
    payload = {
        "pair": pairName,
        "period": period,
        "method": self.ACTION_SUBSCRIBE,
        "event": "api_kline",
        "apiKey": self.api_key,
        "signature": self.sign(str(time)),
        "timestamp": time,
        "signType": self.api_sign_type
    }
    print("req: " + json.dumps(payload, ensure_ascii=False))
    self.send(payload)


def order_book(self, pairName: str):
    time = self.get_time()
    payload = {
        "pair": pairName,
        "method": self.ACTION_SUBSCRIBE,
        "event": "api_depth",
        "apiKey": self.api_key,
        "signature": self.sign(str(time)),
        "timestamp": time,
        "signType": self.api_sign_type
    }
    print("req: " + json.dumps(payload, ensure_ascii=False))
    self.send(payload)
