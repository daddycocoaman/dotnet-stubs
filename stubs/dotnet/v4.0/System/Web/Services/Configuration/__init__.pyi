from typing import Tuple, Set, Iterable, List


class XmlFormatExtensionPrefixAttribute(Attribute):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, prefix: str, ns: str): ...
    @property
    def Namespace(self) -> str: ...
    @property
    def Prefix(self) -> str: ...
    @Namespace.setter
    def Namespace(self, value: str) -> None: ...
    @Prefix.setter
    def Prefix(self, value: str) -> None: ...