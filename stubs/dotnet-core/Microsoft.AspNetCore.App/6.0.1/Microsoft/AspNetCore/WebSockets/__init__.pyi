from typing import Tuple, Set, Iterable, List


class WebSocketMiddleware:
    def __init__(self, next: RequestDelegate, options: IOptions, loggerFactory: ILoggerFactory): ...
    def Invoke(self, context: HttpContext) -> Task: ...


class WebSocketsDependencyInjectionExtensions:
    def AddWebSockets(services: IServiceCollection, configure: Action) -> IServiceCollection: ...
