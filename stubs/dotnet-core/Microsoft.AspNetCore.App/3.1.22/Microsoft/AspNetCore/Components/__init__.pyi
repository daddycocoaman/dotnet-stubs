__all__ = ['Forms','RenderTree','Routing','Web']
from typing import Tuple, Set, Iterable, List


class BindInputElementAttribute:
    def __init__(self, type: str, suffix: str, valueAttribute: str, changeAttribute: str, isInvariantCulture: bool, format: str): ...
    @property
    def ChangeAttribute(self) -> str: ...
    @property
    def Format(self) -> str: ...
    @property
    def IsInvariantCulture(self) -> bool: ...
    @property
    def Suffix(self) -> str: ...
    @property
    def Type(self) -> str: ...
    @property
    def ValueAttribute(self) -> str: ...
