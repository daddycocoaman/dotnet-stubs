from typing import Tuple, Set, Iterable, List


class ThenBy(Object):
    def __init__(self): ...
    @property
    def DataField(self) -> str: ...
    @property
    def Direction(self) -> SortDirection: ...
    @DataField.setter
    def DataField(self, value: str) -> None: ...
    @Direction.setter
    def Direction(self, value: SortDirection) -> None: ...
