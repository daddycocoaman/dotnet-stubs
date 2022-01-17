__all__ = ['Internal','Internal','Internal']
from typing import Tuple, Set, Iterable, List


class HostOptions:
    def __init__(self): ...
    @property
    def BackgroundServiceExceptionBehavior(self) -> BackgroundServiceExceptionBehavior: ...
    @property
    def ShutdownTimeout(self) -> TimeSpan: ...
    @BackgroundServiceExceptionBehavior.setter
    def BackgroundServiceExceptionBehavior(self, value: BackgroundServiceExceptionBehavior) -> None: ...
    @ShutdownTimeout.setter
    def ShutdownTimeout(self, value: TimeSpan) -> None: ...
