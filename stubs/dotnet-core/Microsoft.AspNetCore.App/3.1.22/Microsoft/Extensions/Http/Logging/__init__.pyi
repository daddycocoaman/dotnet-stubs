from typing import Tuple, Set, Iterable, List


class LoggingHttpMessageHandler:
    def __init__(self, logger: ILogger): ...


class LoggingScopeHttpMessageHandler:
    def __init__(self, logger: ILogger): ...
