__all__ = ['Metadata','Metadata','Metadata','Metadata','Metadata','Metadata','Metadata','Metadata']
from typing import Tuple, Set, Iterable, List


class ReferenceResolver(Object):
    def AddReference(self, referenceId: str, value: Object) -> None: ...
    def GetReference(self, value: Object) -> Tuple[str, bool]: ...
    def ResolveReference(self, referenceId: str) -> Object: ...