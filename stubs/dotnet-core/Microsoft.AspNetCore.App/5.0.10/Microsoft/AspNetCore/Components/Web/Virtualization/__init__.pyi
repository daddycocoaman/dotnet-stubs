from typing import Tuple, Set, Iterable, List




class ItemsProviderRequest:
    def __init__(self, startIndex: int, count: int, cancellationToken: CancellationToken): ...
    @property
    def CancellationToken(self) -> CancellationToken: ...
    @property
    def Count(self) -> int: ...
    @property
    def StartIndex(self) -> int: ...




class PlaceholderContext:
    def __init__(self, index: int, size: Single): ...
    @property
    def Index(self) -> int: ...
    @property
    def Size(self) -> Single: ...


