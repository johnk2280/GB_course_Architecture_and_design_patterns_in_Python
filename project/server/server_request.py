class Request:

    method: str
    route: str
    version: str
    headers: dict

    def __init__(self, method, route, version, headers):
        self.method = method
        self.route = route
        self.version = version
        self.headers = headers
