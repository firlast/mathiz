from types import FunctionType

from wsblib import route
from wsblib import server


class Mathiz:
    def __init__(self) -> None:
        self._routes = []
        self._errors_callback = []

    def route(self, path: str, methods: tuple = ('GET',)) -> FunctionType:
        def decorator(func):
            _route = route.Route(func, path, methods)
            self._routes.append(_route)

        return decorator

    def run(self, host: str = '127.0.0.1', port: int = 5500) -> None:
        _server = server.Server()
        _server.start(host, port)
        
        while True:
            client = _server.wait_client()
