from typing import Tuple, Set, Iterable, List


class IDataStorage:
    def TryGetItemValue(self, itemKey: str) -> Tuple[bool, ResourceDictionary]: ...


class IDataStorageService:
    def GetDataStorage(self, storageKey: str) -> IDataStorage: ...
