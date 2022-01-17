from typing import Tuple, Set, Iterable, List


class KnownTypeAttribute(Attribute):
    @overload
    def __init__(self, type: Type): ...
    @overload
    def __init__(self, methodName: str): ...
    @property
    def MethodName(self) -> str: ...
    @property
    def Type(self) -> Type: ...