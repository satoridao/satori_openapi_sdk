from typing import List

from satori.api import API


class Order:
    def __init__(
            self,
            clientOrderId: str,
            isLong: bool,
            isMarket: bool,
            lever: int,
            matchType: int,
            pairName: str,
            positionType: int,
            quantity: str,
            price: str = None
    ):
        self.clientOrderId = clientOrderId
        self.isLong = isLong
        self.isMarket = isMarket
        self.lever = lever
        self.matchType = matchType
        self.pairName = pairName
        self.positionType = positionType
        self.price = price
        self.quantity = quantity

    def to_json(self):
        return self.__dict__


class OrderList:
    def __init__(self, orders: List[Order], timestamp: str):
        self.orders = orders
        self.timestamp = timestamp

    def to_json(self):
        return {
            "orders": [order.__dict__ for order in self.orders],
            "timestamp": self.timestamp
        }


class Client(API):
    def __init__(self, api_key=None, api_secret=None, api_sign_type=None, **kwargs):
        if "base_url" not in kwargs:
            kwargs["base_url"] = "https://zk-test.satori.finance"
        super().__init__(api_key, api_secret, api_sign_type, **kwargs)

    # Query
    from satori.client._get import kline
    from satori.client._get import mark_price
    from satori.client._get import index_price
    from satori.client._get import pairs
    from satori.client._get import depth
    from satori.client._get import trades
    from satori.client._get import time

    # private query
    from satori.client._private_query import balance
    from satori.client._private_query import order_list
    from satori.client._private_query import order
    from satori.client._private_query import match_result
    from satori.client._private_query import position_list

    # position
    from satori.client._position_operation import change_margin
    from satori.client._position_operation import close_position
    from satori.client._position_operation import close_position_by_direction

    # order
    from satori.client._order_operation import create_order
    from satori.client._order_operation import batch_create
    from satori.client._order_operation import cancel_order
    from satori.client._order_operation import cancel_order_by_client_id
    from satori.client._order_operation import batch_cancel
    from satori.client._order_operation import batch_cancel_by_result
    from satori.client._order_operation import cancel_all
    from satori.client._order_operation import batch_create_by_result

