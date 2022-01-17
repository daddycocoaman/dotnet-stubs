from typing import Tuple, Set, Iterable, List


class DataServiceKeyAttribute(Attribute):
    @overload
    def __init__(self, keyName: str): ...
    @overload
    def __init__(self, keyNames: Set(str)): ...
    @property
    def KeyNames(self) -> ReadOnlyCollection: ...
