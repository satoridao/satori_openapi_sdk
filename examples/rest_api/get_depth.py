#!/usr/bin/env python
import json

from satori.client import Client


client = Client()

if __name__ == '__main__':
    client = Client()
    print(json.dumps(client.depth("ETH-USD",page_size= 2), ensure_ascii=False))
    print(json.dumps(client.depth("ETH-USD"), ensure_ascii=False))



