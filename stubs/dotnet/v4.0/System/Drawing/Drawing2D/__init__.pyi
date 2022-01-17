from typing import Tuple, Set, Iterable, List


class RegionData(Object):
    @property
    def Data(self) -> Set(Byte): ...
    @Data.setter
    def Data(self, value: Set(Byte)) -> None: ...
