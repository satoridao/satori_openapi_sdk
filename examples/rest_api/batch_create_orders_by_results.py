#!/usr/bin/env python
import json

from satori.client import Client, Order, OrderList
from examples.utils.prepare_env import get_env

if __name__ == '__main__':
    config = get_env()
    cs = Client(api_key=config["api_key"], api_secret=config["api_secret"], api_sign_type=config["api_sign_type"], base_url=config["base_url"])
    time = cs.time()["data"]
    order1 = Order(str(time), True, False, 1, 1, "ETH-USD", 3, "0.02", "2000")
    order2 = Order(str(time), False, False, 1, 1, "ETH-USD", 3, "0.02", "3500")
    order3 = Order(str(time), False, False, 1, 1, "ETH-USD", 3, "0.02", "3500")
    orders = [order1, order2, order3]
    order_list = OrderList(orders, str(time))
    print(json.dumps(cs.batch_create_by_result(order_list), ensure_ascii=False))
