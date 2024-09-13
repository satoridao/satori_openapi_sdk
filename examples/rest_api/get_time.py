#!/usr/bin/env python
import json

from satori.client import Client


client = Client()

if __name__ == '__main__':
    client = Client()
    print(json.dumps(client.time(), ensure_ascii=False))
