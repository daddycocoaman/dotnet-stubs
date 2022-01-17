from typing import Tuple, Set, Iterable, List


class ChangeTag:
    def __init__(self, type: ChangeTypes): ...
    @property
    def ChangeTypes(self) -> ChangeTypes: ...
