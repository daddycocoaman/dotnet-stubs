from typing import Tuple, Set, Iterable, List


class FrameworkName(Object):
    @overload
    def __init__(self, frameworkName: str): ...
    @overload
    def __init__(self, identifier: str, version: Version): ...
    @overload
    def __init__(self, identifier: str, version: Version, profile: str): ...
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    def Equals(self, other: FrameworkName) -> bool: ...
    @property
    def FullName(self) -> str: ...
    @property
    def Identifier(self) -> str: ...
    @property
    def Profile(self) -> str: ...
    @property
    def Version(self) -> Version: ...
    def GetHashCode(self) -> int: ...
    def op_Equality(left: FrameworkName, right: FrameworkName) -> bool: ...
    def op_Inequality(left: FrameworkName, right: FrameworkName) -> bool: ...
    def ToString(self) -> str: ...