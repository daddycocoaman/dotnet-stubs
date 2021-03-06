from typing import Tuple, Set, Iterable, List


class DynamicClass(Object):
    def ToString(self) -> str: ...


class ParseException(Exception):
    def __init__(self, message: str, position: int): ...
    @property
    def Position(self) -> int: ...
    def ToString(self) -> str: ...
