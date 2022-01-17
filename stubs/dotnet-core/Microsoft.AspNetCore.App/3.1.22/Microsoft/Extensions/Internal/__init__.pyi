from typing import Tuple, Set, Iterable, List


class ISystemClock:
    @property
    def UtcNow(self) -> DateTimeOffset: ...


class SystemClock:
    def __init__(self): ...
    @property
    def UtcNow(self) -> DateTimeOffset: ...
