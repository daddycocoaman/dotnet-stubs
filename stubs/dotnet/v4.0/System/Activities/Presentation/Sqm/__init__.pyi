from typing import Tuple, Set, Iterable, List


class IVSSqmService:
    def AddArrayToStream(self, dataPointId: int, data: Set(UInt32), count: int) -> None: ...
    def AddItemToStream(self, dataPointId: int, value: UInt32) -> None: ...
    def SetDatapoint(self, dataPointId: int, value: UInt32) -> None: ...
