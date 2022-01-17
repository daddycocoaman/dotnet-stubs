from typing import Tuple, Set, Iterable, List


class NullLogger:
    def BeginScope(self, state: TState) -> IDisposable: ...
    @property
    def Instance() -> NullLogger: ...
    def IsEnabled(self, logLevel: LogLevel) -> bool: ...
    def Log(self, logLevel: LogLevel, eventId: EventId, state: TState, exception: Exception, formatter: Func`3) -> None: ...




class NullLoggerFactory:
    def __init__(self): ...
    def AddProvider(self, provider: ILoggerProvider) -> None: ...
    def CreateLogger(self, name: str) -> ILogger: ...
    def Dispose(self) -> None: ...


class NullLoggerProvider:
    def CreateLogger(self, categoryName: str) -> ILogger: ...
    def Dispose(self) -> None: ...
    @property
    def Instance() -> NullLoggerProvider: ...
