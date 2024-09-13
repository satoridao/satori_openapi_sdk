#!/usr/bin/env python
import json

from satori.client import Client
from examples.utils.prepare_env import get_env

if __name__ == '__main__':
    config = get_env()
    cs = Client(api_key=config["api_key"], api_secret=config["api_secret"], api_sign_type=config["api_sign_type"], base_url=config["base_url"])
    time = cs.time()["data"]
    # print(cs.order_list("ETH-USD",time))
    print(json.dumps(cs.cancel_order(entrustId=178790278,timestamp=str(time)), ensure_ascii=False))