__all__ = ['Circuits']
from typing import Tuple, Set, Iterable, List


class CircuitOptions:
    def __init__(self): ...
    @property
    def DetailedErrors(self) -> bool: ...
    @property
    def DisconnectedCircuitMaxRetained(self) -> int: ...
    @property
    def DisconnectedCircuitRetentionPeriod(self) -> TimeSpan: ...
    @property
    def JSInteropDefaultCallTimeout(self) -> TimeSpan: ...
    @property
    def MaxBufferedUnacknowledgedRenderBatches(self) -> int: ...
    @DetailedErrors.setter
    def DetailedErrors(self, value: bool) -> None: ...
    @DisconnectedCircuitMaxRetained.setter
    def DisconnectedCircuitMaxRetained(self, value: int) -> None: ...
    @DisconnectedCircuitRetentionPeriod.setter
    def DisconnectedCircuitRetentionPeriod(self, value: TimeSpan) -> None: ...
    @JSInteropDefaultCallTimeout.setter
    def JSInteropDefaultCallTimeout(self, value: TimeSpan) -> None: ...
    @MaxBufferedUnacknowledgedRenderBatches.setter
    def MaxBufferedUnacknowledgedRenderBatches(self, value: int) -> None: ...


class RevalidatingServerAuthenticationStateProvider(ServerAuthenticationStateProvider):
    def __init__(self, loggerFactory: ILoggerFactory): ...


class ServerAuthenticationStateProvider(AuthenticationStateProvider):
    def __init__(self): ...
    def GetAuthenticationStateAsync(self) -> Task: ...
    def SetAuthenticationState(self, authenticationStateTask: Task) -> None: ...
