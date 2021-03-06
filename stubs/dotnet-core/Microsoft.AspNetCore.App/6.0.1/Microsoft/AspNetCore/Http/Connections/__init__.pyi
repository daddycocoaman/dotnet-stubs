__all__ = ['Features']
from typing import Tuple, Set, Iterable, List


class ConnectionOptions:
    def __init__(self): ...
    @property
    def DisconnectTimeout(self) -> Nullable: ...
    @DisconnectTimeout.setter
    def DisconnectTimeout(self, value: Nullable) -> None: ...


class ConnectionOptionsSetup:
    def __init__(self): ...
    def Configure(self, options: ConnectionOptions) -> None: ...


class HttpConnectionContextExtensions:
    def GetHttpContext(connection: ConnectionContext) -> HttpContext: ...


class HttpConnectionDispatcherOptions:
    def __init__(self): ...
    @property
    def ApplicationMaxBufferSize(self) -> Int64: ...
    @property
    def AuthorizationData(self) -> List[IAuthorizeData]: ...
    @property
    def CloseOnAuthenticationExpiration(self) -> bool: ...
    @property
    def LongPolling(self) -> LongPollingOptions: ...
    @property
    def MinimumProtocolVersion(self) -> int: ...
    @property
    def TransportMaxBufferSize(self) -> Int64: ...
    @property
    def Transports(self) -> HttpTransportType: ...
    @property
    def TransportSendTimeout(self) -> TimeSpan: ...
    @property
    def WebSockets(self) -> WebSocketOptions: ...
    @ApplicationMaxBufferSize.setter
    def ApplicationMaxBufferSize(self, value: Int64) -> None: ...
    @CloseOnAuthenticationExpiration.setter
    def CloseOnAuthenticationExpiration(self, value: bool) -> None: ...
    @MinimumProtocolVersion.setter
    def MinimumProtocolVersion(self, value: int) -> None: ...
    @TransportMaxBufferSize.setter
    def TransportMaxBufferSize(self, value: Int64) -> None: ...
    @Transports.setter
    def Transports(self, value: HttpTransportType) -> None: ...
    @TransportSendTimeout.setter
    def TransportSendTimeout(self, value: TimeSpan) -> None: ...


class LongPollingOptions:
    def __init__(self): ...
    @property
    def PollTimeout(self) -> TimeSpan: ...
    @PollTimeout.setter
    def PollTimeout(self, value: TimeSpan) -> None: ...


class NegotiateMetadata:
    def __init__(self): ...


class WebSocketOptions:
    def __init__(self): ...
    @property
    def CloseTimeout(self) -> TimeSpan: ...
    @property
    def SubProtocolSelector(self) -> Func: ...
    @CloseTimeout.setter
    def CloseTimeout(self, value: TimeSpan) -> None: ...
    @SubProtocolSelector.setter
    def SubProtocolSelector(self, value: Func) -> None: ...
