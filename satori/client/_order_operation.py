from typing import List
import json
from satori.api import API
from satori.client import Order, OrderList


def create_order(self: API, order: Order, timestamp: str):
    url_path = "/api/third/hot/order/create"
    params = order.to_json()
    params["timestamp"] = timestamp
    return self.sign_request("POST", url_path, params)


def batch_create(self: API, orders: OrderList):
    url_path = "/api/third/hot/order/batchCreate"
    url = self.base_url + url_path
    params = json.dumps(orders.to_json(), separators=(',', ':'))
    self.session.headers.update({
        "signature": self._get_sign(params),
        "Content-Type": "application/json",
    })
    response = self.session.request("POST", url=url, data=params, proxies=self.proxies)
    try:
        data = response.json()
    except ValueError:
        data = response.text
    result = {}

    if self.show_header:
        result["header"] = response.headers

    if len(result) != 0:
        result["data"] = data
        return result

    return data


def batch_create_by_result(self: API, orders: OrderList, language_CN: bool = False):
    url_path = "/api/third/hot/order/batchCreateWithRes"
    url = self.base_url + url_path
    if language_CN:
        language = "zh-CN"
    else:
        language = "zh-CN"
    params = json.dumps(orders.to_json(), separators=(',', ':'))
    self.session.headers.update({
        "signature": self._get_sign(params),
        "Content-Type": "application/json",
        "Accept-Language": language
    })
    response = self.session.request("POST", url=url, data=params, proxies=self.proxies)
    try:
        data = response.json()
    except ValueError:
        data = response.text
    result = {}

    if self.show_header:
        result["header"] = response.headers

    if len(result) != 0:
        result["data"] = data
        return result

    return data


def cancel_order(self: API, entrustId: int, timestamp: str):
    url_path = "/api/third/order/cancelEntrust"
    params = {"entrustId": {entrustId}, "timestamp": timestamp}
    return self.sign_request("POST", url_path, params)


def cancel_order_by_client_id(self: API, clientOrderId: str, timestamp: str):
    url_path = "/api/third/order/cancelEntrustByCli"
    params = {"clientOrderId": {clientOrderId}, "timestamp": timestamp}
    return self.sign_request("POST", url_path, params)


def batch_cancel(self: API, entrustIds: List[int], timestamp: str):
    url_path = "/api/third/order/batchCancelEntrust"
    ids = ','.join(map(str, entrustIds))
    params = {"entrustIds": ids, "timestamp": timestamp}
    return self.sign_request("POST", url_path, params)


def batch_cancel_by_result(self: API, entrustIds: List[int], timestamp: str):
    url_path = "/api/third/order/batchCancelWithRes"
    ids = ','.join(map(str, entrustIds))
    params = {"entrustIds": ids, "timestamp": timestamp}
    return self.sign_request("POST", url_path, params)


def cancel_all(self: API, timestamp: int, pairName: str = None, isLong: bool = None):
    url_path = "/api/third/order/cancelAll"
    params = {"isLong": isLong, "pairName": pairName, "timestamp": timestamp}
    return self.sign_request("POST", url_path, params)
