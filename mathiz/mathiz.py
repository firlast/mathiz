from types import FunctionType

from wsblib import route


class Mathiz:
    def __init__(self) -> None:
        self._routes = []
        self._errors_callback = []

    def route(self, path: str, method: tuple = ('GET',)) -> FunctionType:
        def decorator(func):
            _route = route.Route(func, path, method)
            self._routes.append(_route)

        return decorator
