from typing import Tuple, Set, Iterable, List


class CustomLoaderAttribute(Attribute):
    def __init__(self, customLoaderType: Type): ...
    @property
    def CustomLoaderType(self) -> Type: ...
