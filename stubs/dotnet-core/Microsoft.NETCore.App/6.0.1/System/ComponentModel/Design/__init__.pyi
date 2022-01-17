__all__ = ['Serialization','Serialization','Serialization','Serialization','Serialization','Serialization','Serialization','Serialization','Serialization','Serialization','Serialization','Serialization','Serialization','Serialization','Serialization','Serialization','Serialization','Serialization']
from typing import Tuple, Set, Iterable, List


class TypeDescriptionProviderService(Object):
    @overload
    def GetProvider(self, instance: Object) -> TypeDescriptionProvider: ...
    @overload
    def GetProvider(self, type: Type) -> TypeDescriptionProvider: ...
