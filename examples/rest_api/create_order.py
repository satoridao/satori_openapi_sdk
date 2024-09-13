#!/usr/bin/env python
import json

from satori.client import Client,Order
from examples.utils.prepare_env import get_env

if __name__ == '__main__':
    config = get_env()
    cs = Client(api_key=config["api_key"], api_secret=config["api_secret"], api_sign_type=config["api_sign_type"], base_url=config["base_url"])
    time = cs.time()["data"]
    order1 = Order(str(time), True, False, 1, 1, "ETH-USD", 3, "0.02", "2000")
    print(json.dumps(cs.create_order(order1,str(time)), ensure_ascii=False))