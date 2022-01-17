from typing import Tuple, Set, Iterable, List


class BoundedChannelFullMode:
    Wait = 0
    DropNewest = 1
    DropOldest = 2
    DropWrite = 3


class BoundedChannelOptions(ChannelOptions):
    def __init__(self, capacity: int): ...
    @property
    def Capacity(self) -> int: ...
    @property
    def FullMode(self) -> BoundedChannelFullMode: ...
    @Capacity.setter
    def Capacity(self, value: int) -> None: ...
    @FullMode.setter
    def FullMode(self, value: BoundedChannelFullMode) -> None: ...


class Channel(Object):
    @overload
    def CreateBounded(capacity: int) -> Channel: ...
    @overload
    def CreateBounded(options: BoundedChannelOptions) -> Channel: ...
    @overload
    def CreateBounded(options: BoundedChannelOptions, itemDropped: Action) -> Channel: ...
    @overload
    def CreateUnbounded() -> Channel: ...
    @overload
    def CreateUnbounded(options: UnboundedChannelOptions) -> Channel: ...






class ChannelClosedException(InvalidOperationException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, innerException: Exception): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class ChannelOptions(Object):
    @property
    def AllowSynchronousContinuations(self) -> bool: ...
    @property
    def SingleReader(self) -> bool: ...
    @property
    def SingleWriter(self) -> bool: ...
    @AllowSynchronousContinuations.setter
    def AllowSynchronousContinuations(self, value: bool) -> None: ...
    @SingleReader.setter
    def SingleReader(self, value: bool) -> None: ...
    @SingleWriter.setter
    def SingleWriter(self, value: bool) -> None: ...






class UnboundedChannelOptions(ChannelOptions):
    def __init__(self): ...
