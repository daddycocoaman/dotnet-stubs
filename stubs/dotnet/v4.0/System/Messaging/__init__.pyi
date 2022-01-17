__all__ = ['Design','Design']
from typing import Tuple, Set, Iterable, List


class XmlMessageFormatter(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, targetTypeNames: Set(str)): ...
    @overload
    def __init__(self, targetTypes: Set(Type)): ...
    def CanRead(self, message: Message) -> bool: ...
    def Clone(self) -> Object: ...
    @property
    def TargetTypeNames(self) -> Set(str): ...
    @property
    def TargetTypes(self) -> Set(Type): ...
    def Read(self, message: Message) -> Object: ...
    @TargetTypeNames.setter
    def TargetTypeNames(self, value: Set(str)) -> None: ...
    @TargetTypes.setter
    def TargetTypes(self, value: Set(Type)) -> None: ...
    def Write(self, message: Message, obj: Object) -> None: ...
