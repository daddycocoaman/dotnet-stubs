from typing import Tuple, Set, Iterable, List


class CounterFileInfo:
    @property
    def NewestRecord(self) -> DateTime: ...
    @property
    def OldestRecord(self) -> DateTime: ...
    @property
    def SampleCount(self) -> UInt32: ...
