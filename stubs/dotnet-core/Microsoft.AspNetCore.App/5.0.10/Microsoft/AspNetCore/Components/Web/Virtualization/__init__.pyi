from typing import Tuple, Set, Iterable, List


class PlaceholderContext:
    def __init__(self, index: int, size: Single): ...
    @property
    def Index(self) -> int: ...
    @property
    def Size(self) -> Single: ...
