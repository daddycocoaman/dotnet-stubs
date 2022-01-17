from typing import Tuple, Set, Iterable, List


class TlsHandshakeCallbackOptions:
    def __init__(self): ...
    @property
    def HandshakeTimeout(self) -> TimeSpan: ...
    @property
    def OnConnection(self) -> Func: ...
    @property
    def OnConnectionState(self) -> Object: ...
    @HandshakeTimeout.setter
    def HandshakeTimeout(self, value: TimeSpan) -> None: ...
    @OnConnection.setter
    def OnConnection(self, value: Func) -> None: ...
    @OnConnectionState.setter
    def OnConnectionState(self, value: Object) -> None: ...