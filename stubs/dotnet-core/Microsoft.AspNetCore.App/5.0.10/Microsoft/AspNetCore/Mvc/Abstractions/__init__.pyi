from typing import Tuple, Set, Iterable, List


class ParameterDescriptor:
    def __init__(self): ...
    @property
    def BindingInfo(self) -> BindingInfo: ...
    @property
    def Name(self) -> str: ...
    @property
    def ParameterType(self) -> Type: ...
    @BindingInfo.setter
    def BindingInfo(self, value: BindingInfo) -> None: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    @ParameterType.setter
    def ParameterType(self, value: Type) -> None: ...
