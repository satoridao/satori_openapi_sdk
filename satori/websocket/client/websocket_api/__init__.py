from typing import Optional
from satori.client import Client
from satori.lib.authentication import sign_with_type
from satori.websocket.websocket_client import SatoriWebsocketClient


class WebsocketAPIClient(SatoriWebsocketClient):
    def __init__(
            self,
            stream_url="wss://zk-test.satori.finance/api/market/ws",
            api_key=None,
            api_secret=None,
            api_sign_type=None,
            on_message=None,
            on_open=None,
            on_close=None,
            on_error=None,
            on_ping=None,
            on_pong=None,
            timeout=None,
            logger=None,
            proxies: Optional[dict] = None,
    ):
        self.api_key = api_key
        self.api_secret = api_secret
        self.api_sign_type = api_sign_type
        self.proxies = proxies
        super().__init__(
            stream_url,
            on_message=on_message,
            on_open=on_open,
            on_close=on_close,
            on_error=on_error,
            on_ping=on_ping,
            on_pong=on_pong,
            logger=logger,
            timeout=timeout,
            proxies=proxies,
        )

    def get_time(self):
        cs = Client(api_key=self.api_key, api_secret=self.api_secret, proxies=self.proxies)
        return cs.time()["data"]
    def sign(self, payload):
        return sign_with_type(self.api_sign_type, self.api_secret, payload)

    # Account
    from satori.websocket.client.websocket_api._account import account

    # Market
    from satori.websocket.client.websocket_api._market import order
    from satori.websocket.client.websocket_api._market import order_book
    from satori.websocket.client.websocket_api._market import position
    from satori.websocket.client.websocket_api._market import kline

    # Trade
    from satori.websocket.client.websocket_api._trade import trade_data
    from satori.websocket.client.websocket_api._trade import trade_current
    from satori.websocket.client.websocket_api._trade import trade_immediately
