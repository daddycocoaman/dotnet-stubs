from typing import Tuple, Set, Iterable, List


class CapSettings(GPOExtension):
    def __init__(self): ...
    @property
    def Caps(self) -> List: ...
    def Initialize(self, context: ReportingContext) -> None: ...
    @Caps.setter
    def Caps(self, value: List) -> None: ...