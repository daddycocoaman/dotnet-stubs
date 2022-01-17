from typing import Tuple, Set, Iterable, List


class WebSocketsDependencyInjectionExtensions:
    def AddWebSockets(services: IServiceCollection, configure: Action) -> IServiceCollection: ...
