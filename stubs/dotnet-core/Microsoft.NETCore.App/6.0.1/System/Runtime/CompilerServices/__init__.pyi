from typing import Tuple, Set, Iterable, List


class IUnknownConstantAttribute(CustomConstantAttribute):
    def __init__(self): ...
    @property
    def Value(self) -> Object: ...
