from typing import Tuple, Set, Iterable, List


class CounterSetInstanceCounterDataSet(Object):
    def Dispose(self) -> None: ...
    @property
    def Item(self, counterId: int) -> CounterData: ...
    @property
    def Item(self, counterName: str) -> CounterData: ...