def time(self):
    """Query system time"""
    url_path = "/api/third/info/time"
    return self.query(url_path)


def index_price(self, pair: str):
    """Query current index price"""
    url_path = "/api/third/info/indexPrice"
    params = {"pairName": pair}
    return self.query(url_path, params)


def mark_price(self, pair_name: str):
    """Query the current mark price"""
    url_path = "/api/third/info/markPrice"
    params = {"pairName": pair_name}
    return self.query(url_path, params)


def trades(self, pair_name: str, page_size: int = None):
    """Query last trade"""
    url_path = "/api/third/info/trades"
    params = {"pairName": pair_name, "limit": page_size}
    return self.query(url_path, params)


def pairs(self):
    """Get pair list"""
    url_path = "/api/third/info/pairs"
    return self.query(url_path)


def depth(self, pair_name: str, page_size: int = None):
    """query the orderbook depth"""
    url_path = "/api/third/info/depth"
    params = {"pairName": pair_name, "limit": page_size}
    return self.query(url_path, params)


def kline(self, pair_name: str, period: str, end_time: int = None, page_size: int = None):
    """Kline"""
    url_path = "/api/third/info/kline"
    params = {"pairName": pair_name, "period": period, "end_time": end_time, "limit": page_size}
    return self.query(url_path, params)
