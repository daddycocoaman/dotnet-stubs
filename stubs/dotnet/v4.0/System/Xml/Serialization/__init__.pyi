__all__ = ['Advanced','Advanced','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration']
from typing import Tuple, Set, Iterable, List


class UnreferencedObjectEventArgs(EventArgs):
    def __init__(self, o: Object, id: str): ...
    @property
    def UnreferencedId(self) -> str: ...
    @property
    def UnreferencedObject(self) -> Object: ...
