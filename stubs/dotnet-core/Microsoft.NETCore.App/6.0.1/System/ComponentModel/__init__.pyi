from typing import Tuple, Set, Iterable, List


class TypeDescriptionProviderAttribute(Attribute):
    @overload
    def __init__(self, typeName: str): ...
    @overload
    def __init__(self, type: Type): ...
    @property
    def TypeName(self) -> str: ...
