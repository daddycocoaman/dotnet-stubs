from typing import Tuple, Set, Iterable, List


class EventSourceLoggerProvider:
    def __init__(self, eventSource: LoggingEventSource): ...
    def CreateLogger(self, categoryName: str) -> ILogger: ...
    def Dispose(self) -> None: ...


class Keywords:
    pass


class LoggingEventSource:
    pass
