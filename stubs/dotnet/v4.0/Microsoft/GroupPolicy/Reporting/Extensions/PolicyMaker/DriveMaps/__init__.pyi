from typing import Tuple, Set, Iterable, List


class DriveMapGPOSettings(PolicyMakerElement):
    def __init__(self): ...
    @property
    def DriveMappings(self) -> List: ...
    @DriveMappings.setter
    def DriveMappings(self, value: List) -> None: ...
