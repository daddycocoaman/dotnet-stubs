from typing import Tuple, Set, Iterable, List


class ToolboxItemContainer(Object):
    @overload
    def __init__(self, item: ToolboxItem): ...
    @overload
    def __init__(self, data: IDataObject): ...
    def Equals(self, obj: Object) -> bool: ...
    @property
    def IsCreated(self) -> bool: ...
    @property
    def IsTransient(self) -> bool: ...
    @property
    def ToolboxData(self) -> IDataObject: ...
    def GetFilter(self, creators: ICollection) -> ICollection: ...
    def GetHashCode(self) -> int: ...
    def GetToolboxItem(self, creators: ICollection) -> ToolboxItem: ...
    def UpdateFilter(self, item: ToolboxItem) -> None: ...