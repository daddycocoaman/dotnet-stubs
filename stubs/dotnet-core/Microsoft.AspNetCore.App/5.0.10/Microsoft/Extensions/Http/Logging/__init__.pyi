from typing import Tuple, Set, Iterable, List


class LoggingScopeHttpMessageHandler:
    @overload
    def __init__(self, logger: ILogger): ...
    @overload
    def __init__(self, logger: ILogger, options: HttpClientFactoryOptions): ...
