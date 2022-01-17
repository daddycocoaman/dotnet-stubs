from typing import Tuple, Set, Iterable, List


class XsltSettings(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, enableDocumentFunction: bool, enableScript: bool): ...
    @property
    def Default() -> XsltSettings: ...
    @property
    def EnableDocumentFunction(self) -> bool: ...
    @property
    def EnableScript(self) -> bool: ...
    @property
    def TrustedXslt() -> XsltSettings: ...
    @EnableDocumentFunction.setter
    def EnableDocumentFunction(self, value: bool) -> None: ...
    @EnableScript.setter
    def EnableScript(self, value: bool) -> None: ...
