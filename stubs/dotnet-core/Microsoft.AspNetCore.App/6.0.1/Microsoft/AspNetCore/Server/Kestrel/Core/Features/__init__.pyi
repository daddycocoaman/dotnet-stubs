from typing import Tuple, Set, Iterable, List


class IConnectionTimeoutFeature:
    def CancelTimeout(self) -> None: ...
    def ResetTimeout(self, timeSpan: TimeSpan) -> None: ...
    def SetTimeout(self, timeSpan: TimeSpan) -> None: ...


class IDecrementConcurrentConnectionCountFeature:
    def ReleaseConnection(self) -> None: ...


class IHttp2StreamIdFeature:
    @property
    def StreamId(self) -> int: ...


class IHttpMinRequestBodyDataRateFeature:
    @property
    def MinDataRate(self) -> MinDataRate: ...
    @MinDataRate.setter
    def MinDataRate(self, value: MinDataRate) -> None: ...


class IHttpMinResponseDataRateFeature:
    @property
    def MinDataRate(self) -> MinDataRate: ...
    @MinDataRate.setter
    def MinDataRate(self, value: MinDataRate) -> None: ...


class ITlsApplicationProtocolFeature:
    @property
    def ApplicationProtocol(self) -> ReadOnlyMemory: ...
