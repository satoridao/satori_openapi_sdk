from satori.api import API


def balance(self: API, symbol: str, timestamp: str):
    url_path = "/api/third/hot/order/balance"
    params = {"symbol": symbol, "timestamp": timestamp}
    return self.sign_request("POST", url_path, params)


def order_list(self: API, pairName: str, timestamp: str, pageNo: int = None, pageSize: int = None):
    url_path = "/api/third/order/selectContractCurrentEntrustList"
    params = {"pageNo": pageNo, "pageSize": pageSize, "pairName": pairName, "timestamp": timestamp}
    return self.sign_request("POST", url_path, params)


def order(self: API, entrustId: int, timestamp: str):
    url_path = "/api/third/order/queryOrder"
    params = {"entrustId": entrustId, "timestamp": timestamp}
    return self.sign_request("POST", url_path, params)


def match_result(self: API, pairName: str,  timestamp: str, matchId: int = None, pageNo: int = None,
                 pageSize: int = None):
    url_path = "/api/third/order/selectContractMatchPairList"
    params = {"matchId": matchId, "pageNo": pageNo, "pageSize": pageSize, "pairName": pairName, "timestamp": timestamp}
    return self.sign_request("POST", url_path, params)


def position_list(self: API, pairName: str, timestamp: str,  pageNo: int = None, pageSize: int = None):
    url_path = "/api/third/hot/order/selectContractPositionList"
    params = {"pageNo": pageNo, "pageSize": pageSize, "pairName": pairName, "timestamp": timestamp}
    return self.sign_request("POST", url_path, params)