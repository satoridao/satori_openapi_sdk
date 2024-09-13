#!/usr/bin/env python
import json

from satori.client import Client


client = Client()

if __name__ == '__main__':
    client = Client()
    print(json.dumps(client.index_price("ETH-USD"), ensure_ascii=False))
    print(json.dumps(client.index_price("BTC-USD"), ensure_ascii=False))
