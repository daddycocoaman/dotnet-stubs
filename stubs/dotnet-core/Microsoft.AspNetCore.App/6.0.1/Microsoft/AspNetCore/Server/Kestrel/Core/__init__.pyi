__all__ = ['Features','Features','Features','Features','Features','Features']
from typing import Tuple, Set, Iterable, List


class MinDataRate:
    def __init__(self, bytesPerSecond: float, gracePeriod: TimeSpan): ...
    @property
    def BytesPerSecond(self) -> float: ...
    @property
    def GracePeriod(self) -> TimeSpan: ...
    def ToString(self) -> str: ...
