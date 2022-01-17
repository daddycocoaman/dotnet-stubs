from typing import Tuple, Set, Iterable, List


class ParallelLoopResult(ValueType):
    @property
    def IsCompleted(self) -> bool: ...
    @property
    def LowestBreakIteration(self) -> Nullable: ...
