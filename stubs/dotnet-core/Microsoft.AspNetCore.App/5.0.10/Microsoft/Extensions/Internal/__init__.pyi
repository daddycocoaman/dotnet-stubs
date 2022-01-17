from typing import Tuple, Set, Iterable, List


class SystemClock:
    def __init__(self): ...
    @property
    def UtcNow(self) -> DateTimeOffset: ...
