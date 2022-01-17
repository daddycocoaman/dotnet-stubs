from typing import Tuple, Set, Iterable, List


class ChangeTag:
    def __init__(self, type: ChangeTypes): ...
    @property
    def ChangeTypes(self) -> ChangeTypes: ...


class ChangeTypes:
    #None = 0
    ChangedSinceOpened = 1
    ChangedSinceSaved = 2
