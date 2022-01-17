from typing import Tuple, Set, Iterable, List


class CounterSetInstance(Object):
    def Dispose(self) -> None: ...
    @property
    def Counters(self) -> CounterSetInstanceCounterDataSet: ...
