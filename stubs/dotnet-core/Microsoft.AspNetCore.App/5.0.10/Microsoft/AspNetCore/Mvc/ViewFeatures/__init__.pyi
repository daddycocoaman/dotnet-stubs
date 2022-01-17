__all__ = ['Buffers','Buffers','Infrastructure']
from typing import Tuple, Set, Iterable, List


class Enumerator:
    def __init__(self, attributes: AttributeDictionary): ...
    def Dispose(self) -> None: ...
    @property
    def Current(self) -> KeyValuePair: ...
    def MoveNext(self) -> bool: ...
    def Reset(self) -> None: ...