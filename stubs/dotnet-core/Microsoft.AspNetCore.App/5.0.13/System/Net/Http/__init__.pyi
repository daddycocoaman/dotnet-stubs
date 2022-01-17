from typing import Tuple, Set, Iterable, List


class IHttpMessageHandlerFactory:
    def CreateHandler(self, name: str) -> HttpMessageHandler: ...
