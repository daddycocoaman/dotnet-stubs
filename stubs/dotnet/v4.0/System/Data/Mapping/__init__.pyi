from typing import Tuple, Set, Iterable, List


class StorageMappingItemCollection(MappingItemCollection):
    @overload
    def __init__(self, edmCollection: EdmItemCollection, storeCollection: StoreItemCollection, filePaths: Set(str)): ...
    @overload
    def __init__(self, edmCollection: EdmItemCollection, storeCollection: StoreItemCollection, xmlReaders: Iterable[XmlReader]): ...
    @property
    def MappingVersion(self) -> float: ...
