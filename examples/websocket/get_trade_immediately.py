import time
from satori.websocket.client.websocket_api import WebsocketAPIClient
from examples.utils.prepare_env import get_env


def message_handler(_, message):
    print(message)


if __name__ == '__main__':
    config = get_env()
    my_client = WebsocketAPIClient(api_key=config["api_key"], on_message=message_handler,
                                   api_secret=config["api_secret"], api_sign_type=config["api_sign_type"], stream_url=config["ws_url"],
                                   proxies=config["proxies"])
    my_client.trade_immediately("ETH-USD")
    time.sleep(50)
    my_client.stop()
