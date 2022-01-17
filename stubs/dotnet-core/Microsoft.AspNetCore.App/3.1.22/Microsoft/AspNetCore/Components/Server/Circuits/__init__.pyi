from typing import Tuple, Set, Iterable, List


class Circuit:
    @property
    def Id(self) -> str: ...


class CircuitHandler:
    @property
    def Order(self) -> int: ...
    def OnCircuitClosedAsync(self, circuit: Circuit, cancellationToken: CancellationToken) -> Task: ...
    def OnCircuitOpenedAsync(self, circuit: Circuit, cancellationToken: CancellationToken) -> Task: ...
    def OnConnectionDownAsync(self, circuit: Circuit, cancellationToken: CancellationToken) -> Task: ...
    def OnConnectionUpAsync(self, circuit: Circuit, cancellationToken: CancellationToken) -> Task: ...
