import json

from satori.lib.utils import hmac_hashing


def trade_data(self, pairName: str, period: str):
    time = self.get_time()
    payload = {
        "pair": pairName,
        "period": period,
        "method": self.ACTION_SUBSCRIBE,
        "event": "api_trade",
        "apiKey": self.api_key,
        "signature": self.sign(str(time)),
        "timestamp": time,
        "signType": self.api_sign_type
    }
    print("req: " + json.dumps(payload, ensure_ascii=False))
    self.send(payload)


def trade_current(self, pairName: str):
    time = self.get_time()
    payload = {
        "pair": pairName,
        "method": self.ACTION_SUBSCRIBE,
        "event": "api_spot_deals",
        "apiKey": self.api_key,
        "signature": self.sign(str(time)),
        "timestamp": time,
        "signType": self.api_sign_type
    }
    print("req: " + json.dumps(payload, ensure_ascii=False))
    self.send(payload)


def trade_immediately(self, pairName: str):
    time = self.get_time()
    payload = {
        "pair": pairName,
        "method": self.ACTION_SUBSCRIBE,
        "event": "api_deal_user",
        "apiKey": self.api_key,
        "signature": self.sign(str(time)),
        "timestamp": time,
        "signType": self.api_sign_type
    }
    print("req: " + json.dumps(payload, ensure_ascii=False))
    self.send(payload)
