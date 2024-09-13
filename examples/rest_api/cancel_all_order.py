#!/usr/bin/env python
import json

from satori.client import Client
from examples.utils.prepare_env import get_env

if __name__ == '__main__':
    config = get_env()
    cs = Client(api_key=config["api_key"], api_secret=config["api_secret"], api_sign_type=config["api_sign_type"], base_url=config["base_url"])
    time = cs.time()["data"]
    print(json.dumps(cs.cancel_all(timestamp=time, pairName="ETH-USD", isLong=True), ensure_ascii=False))
