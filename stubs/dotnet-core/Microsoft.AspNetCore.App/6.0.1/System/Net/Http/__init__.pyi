from typing import Tuple, Set, Iterable, List


class HttpClientFactoryExtensions(Object):
    def CreateClient(factory: IHttpClientFactory) -> HttpClient: ...


class HttpMessageHandlerFactoryExtensions(Object):
    def CreateHandler(factory: IHttpMessageHandlerFactory) -> HttpMessageHandler: ...


class IHttpClientFactory:
    def CreateClient(self, name: str) -> HttpClient: ...


class IHttpMessageHandlerFactory:
    def CreateHandler(self, name: str) -> HttpMessageHandler: ...
