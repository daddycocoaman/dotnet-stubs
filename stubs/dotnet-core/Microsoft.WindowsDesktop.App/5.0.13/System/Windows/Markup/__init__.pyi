from typing import Tuple, Set, Iterable, List


class RuntimeNamePropertyAttribute(Attribute):
    def __init__(self, name: str): ...
    @property
    def Name(self) -> str: ...
