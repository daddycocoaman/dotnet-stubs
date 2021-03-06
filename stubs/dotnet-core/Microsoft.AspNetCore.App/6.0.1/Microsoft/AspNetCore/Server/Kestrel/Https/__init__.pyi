from typing import Tuple, Set, Iterable, List


class CertificateLoader:
    def LoadFromStoreCert(subject: str, storeName: str, storeLocation: StoreLocation, allowInvalid: bool) -> X509Certificate2: ...


class ClientCertificateMode:
    NoCertificate = 0
    AllowCertificate = 1
    RequireCertificate = 2
    DelayCertificate = 3


class HttpsConnectionAdapterOptions:
    def __init__(self): ...
    def AllowAnyClientCertificate(self) -> None: ...
    @property
    def CheckCertificateRevocation(self) -> bool: ...
    @property
    def ClientCertificateMode(self) -> ClientCertificateMode: ...
    @property
    def ClientCertificateValidation(self) -> Func`4: ...
    @property
    def HandshakeTimeout(self) -> TimeSpan: ...
    @property
    def OnAuthenticate(self) -> Action: ...
    @property
    def ServerCertificate(self) -> X509Certificate2: ...
    @property
    def ServerCertificateSelector(self) -> Func`3: ...
    @property
    def SslProtocols(self) -> SslProtocols: ...
    @CheckCertificateRevocation.setter
    def CheckCertificateRevocation(self, value: bool) -> None: ...
    @ClientCertificateMode.setter
    def ClientCertificateMode(self, value: ClientCertificateMode) -> None: ...
    @ClientCertificateValidation.setter
    def ClientCertificateValidation(self, value: Func`4) -> None: ...
    @HandshakeTimeout.setter
    def HandshakeTimeout(self, value: TimeSpan) -> None: ...
    @OnAuthenticate.setter
    def OnAuthenticate(self, value: Action) -> None: ...
    @ServerCertificate.setter
    def ServerCertificate(self, value: X509Certificate2) -> None: ...
    @ServerCertificateSelector.setter
    def ServerCertificateSelector(self, value: Func`3) -> None: ...
    @SslProtocols.setter
    def SslProtocols(self, value: SslProtocols) -> None: ...


class TlsHandshakeCallbackContext:
    def __init__(self): ...
    @property
    def AllowDelayedClientCertificateNegotation(self) -> bool: ...
    @property
    def CancellationToken(self) -> CancellationToken: ...
    @property
    def ClientHelloInfo(self) -> SslClientHelloInfo: ...
    @property
    def Connection(self) -> ConnectionContext: ...
    @property
    def SslStream(self) -> SslStream: ...
    @property
    def State(self) -> Object: ...
    @AllowDelayedClientCertificateNegotation.setter
    def AllowDelayedClientCertificateNegotation(self, value: bool) -> None: ...


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
