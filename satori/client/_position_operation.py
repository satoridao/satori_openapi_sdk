from satori.api import API


def change_margin(self: API, positionId: int, call: bool, marginAmount: str, timestamp: str):
    url_path = "/api/third/order/callMarginAmount"
    params = {"call": call, "marginAmount": marginAmount, "positionId": positionId, "timestamp": timestamp}
    return self.sign_request("POST", url_path, params)


def close_position(self: API, contractPositionId: int, price: str, isMarket: bool, quantity: str, timestamp: str,
                   clientOrderId: str = None):
    url_path = "/api/third/hot/order/closeOrder"
    params = {
        "clientOrderId": clientOrderId,
        "contractPositionId": contractPositionId,
        "isMarket": isMarket,
        "price": price,
        "quantity": quantity,
        "timestamp": timestamp
    }
    return self.sign_request("POST", url_path, params)


def close_position_by_direction(self: API,
                                pairName: str,
                                quantity: str,
                                isLong: bool,
                                timestamp: str,
                                isMarket: bool,
                                price: str,
                                matchType: int = None):
    url_path = "/api/third/order/closeOrderByDirection"
    params = {
        "isLong": isLong,
        "isMarket": isMarket,
        "matchType": matchType,
        "pairName": pairName,
        "price": price,
        "quantity": quantity,
        "timestamp": timestamp
    }
    return self.sign_request("POST", url_path, params)
