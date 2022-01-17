__all__ = ['Symbol','Symbol','Symbol']
from typing import Tuple, Set, Iterable, List


class SourceLocationFoundEventArgs(EventArgs):
    def __init__(self, target: Object, sourceLocation: SourceLocation): ...
    @property
    def SourceLocation(self) -> SourceLocation: ...
    @property
    def Target(self) -> Object: ...
