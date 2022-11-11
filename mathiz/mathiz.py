from types import FunctionType
from threading import Thread

from wsblib import route
from wsblib import server
from wsblib import request

from http_pyparser import response


class Mathiz:
    def __init__(self) -> None:
        self._routes = []
        self._errors_callback = []
        self._process_request: request.ProcessRequest = None

    def route(self, path: str, methods: tuple = ('GET',)) -> FunctionType:
        def decorator(func):
            _route = route.Route(func, path, methods)
            self._routes.append(_route)

        return decorator

    def _process(self, client: server.Client) -> None:
        result = self._process_request.process(client)

        if result:
            _response, _request = result
            final_response = response.make_response(_response)

            client.send_message(final_response)
            client.destroy()

    def run(self, host: str = '127.0.0.1', port: int = 5500) -> None:
        _server = server.Server()
        _server.start(host, port)

        self._process_request = request.ProcessRequest(
            self._routes, self._errors_callback
        )
        
        while True:
            client = _server.wait_client()
            th = Thread(target=self._process, args=(client,))
            th.start()