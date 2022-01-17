from typing import Tuple, Set, Iterable, List


class QuicTransportOptions:
    def __init__(self): ...
    @property
    def Backlog(self) -> int: ...
    @property
    def IdleTimeout(self) -> TimeSpan: ...
    @property
    def MaxBidirectionalStreamCount(self) -> UInt16: ...
    @property
    def MaxReadBufferSize(self) -> Nullable: ...
    @property
    def MaxUnidirectionalStreamCount(self) -> UInt16: ...
    @property
    def MaxWriteBufferSize(self) -> Nullable: ...
    @Backlog.setter
    def Backlog(self, value: int) -> None: ...
    @IdleTimeout.setter
    def IdleTimeout(self, value: TimeSpan) -> None: ...
    @MaxBidirectionalStreamCount.setter
    def MaxBidirectionalStreamCount(self, value: UInt16) -> None: ...
    @MaxReadBufferSize.setter
    def MaxReadBufferSize(self, value: Nullable) -> None: ...
    @MaxUnidirectionalStreamCount.setter
    def MaxUnidirectionalStreamCount(self, value: UInt16) -> None: ...
    @MaxWriteBufferSize.setter
    def MaxWriteBufferSize(self, value: Nullable) -> None: ...
