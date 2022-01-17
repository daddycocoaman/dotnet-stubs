from typing import Tuple, Set, Iterable, List


class LoggingHttpMessageHandler:
    @overload
    def __init__(self, logger: ILogger): ...
    @overload
    def __init__(self, logger: ILogger, options: HttpClientFactoryOptions): ...


class LoggingScopeHttpMessageHandler:
    @overload
    def __init__(self, logger: ILogger): ...
    @overload
    def __init__(self, logger: ILogger, options: HttpClientFactoryOptions): ...
