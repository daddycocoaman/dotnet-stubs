from typing import Tuple, Set, Iterable, List


class GeoPositionStatusChangedEventArgs(EventArgs):
    def __init__(self, status: GeoPositionStatus): ...
    @property
    def Status(self) -> GeoPositionStatus: ...
