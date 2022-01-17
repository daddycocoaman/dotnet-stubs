from typing import Tuple, Set, Iterable, List


class IDataStorageService:
    def GetDataStorage(self, storageKey: str) -> IDataStorage: ...
