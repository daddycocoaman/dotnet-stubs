from typing import Tuple, Set, Iterable, List


class SnapLine(Object):
    @overload
    def __init__(self, type: SnapLineType, offset: int): ...
    @overload
    def __init__(self, type: SnapLineType, offset: int, filter: str): ...
    @overload
    def __init__(self, type: SnapLineType, offset: int, priority: SnapLinePriority): ...
    @overload
    def __init__(self, type: SnapLineType, offset: int, filter: str, priority: SnapLinePriority): ...
    def AdjustOffset(self, adjustment: int) -> None: ...
    @property
    def Filter(self) -> str: ...
    @property
    def IsHorizontal(self) -> bool: ...
    @property
    def IsVertical(self) -> bool: ...
    @property
    def Offset(self) -> int: ...
    @property
    def Priority(self) -> SnapLinePriority: ...
    @property
    def SnapLineType(self) -> SnapLineType: ...
    def ShouldSnap(line1: SnapLine, line2: SnapLine) -> bool: ...
    def ToString(self) -> str: ...
