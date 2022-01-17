from typing import Tuple, Set, Iterable, List


class LdapSessionOptions(Object):
    def FastConcurrentBind(self) -> None: ...
    @property
    def AutoReconnect(self) -> bool: ...
    @property
    def DomainName(self) -> str: ...
    @property
    def HostName(self) -> str: ...
    @property
    def HostReachable(self) -> bool: ...
    @property
    def LocatorFlag(self) -> LocatorFlags: ...
    @property
    def PingKeepAliveTimeout(self) -> TimeSpan: ...
    @property
    def PingLimit(self) -> int: ...
    @property
    def PingWaitTimeout(self) -> TimeSpan: ...
    @property
    def ProtocolVersion(self) -> int: ...
    @property
    def QueryClientCertificate(self) -> QueryClientCertificateCallback: ...
    @property
    def ReferralCallback(self) -> ReferralCallback: ...
    @property
    def ReferralChasing(self) -> ReferralChasingOptions: ...
    @property
    def ReferralHopLimit(self) -> int: ...
    @property
    def RootDseCache(self) -> bool: ...
    @property
    def SaslMethod(self) -> str: ...
    @property
    def Sealing(self) -> bool: ...
    @property
    def SecureSocketLayer(self) -> bool: ...
    @property
    def SecurityContext(self) -> Object: ...
    @property
    def SendTimeout(self) -> TimeSpan: ...
    @property
    def Signing(self) -> bool: ...
    @property
    def SslInformation(self) -> SecurityPackageContextConnectionInformation: ...
    @property
    def SspiFlag(self) -> int: ...
    @property
    def TcpKeepAlive(self) -> bool: ...
    @property
    def VerifyServerCertificate(self) -> VerifyServerCertificateCallback: ...
    @AutoReconnect.setter
    def AutoReconnect(self, value: bool) -> None: ...
    @DomainName.setter
    def DomainName(self, value: str) -> None: ...
    @HostName.setter
    def HostName(self, value: str) -> None: ...
    @LocatorFlag.setter
    def LocatorFlag(self, value: LocatorFlags) -> None: ...
    @PingKeepAliveTimeout.setter
    def PingKeepAliveTimeout(self, value: TimeSpan) -> None: ...
    @PingLimit.setter
    def PingLimit(self, value: int) -> None: ...
    @PingWaitTimeout.setter
    def PingWaitTimeout(self, value: TimeSpan) -> None: ...
    @ProtocolVersion.setter
    def ProtocolVersion(self, value: int) -> None: ...
    @QueryClientCertificate.setter
    def QueryClientCertificate(self, value: QueryClientCertificateCallback) -> None: ...
    @ReferralCallback.setter
    def ReferralCallback(self, value: ReferralCallback) -> None: ...
    @ReferralChasing.setter
    def ReferralChasing(self, value: ReferralChasingOptions) -> None: ...
    @ReferralHopLimit.setter
    def ReferralHopLimit(self, value: int) -> None: ...
    @RootDseCache.setter
    def RootDseCache(self, value: bool) -> None: ...
    @SaslMethod.setter
    def SaslMethod(self, value: str) -> None: ...
    @Sealing.setter
    def Sealing(self, value: bool) -> None: ...
    @SecureSocketLayer.setter
    def SecureSocketLayer(self, value: bool) -> None: ...
    @SendTimeout.setter
    def SendTimeout(self, value: TimeSpan) -> None: ...
    @Signing.setter
    def Signing(self, value: bool) -> None: ...
    @SspiFlag.setter
    def SspiFlag(self, value: int) -> None: ...
    @TcpKeepAlive.setter
    def TcpKeepAlive(self, value: bool) -> None: ...
    @VerifyServerCertificate.setter
    def VerifyServerCertificate(self, value: VerifyServerCertificateCallback) -> None: ...
    def StartTransportLayerSecurity(self, controls: DirectoryControlCollection) -> None: ...
    def StopTransportLayerSecurity(self) -> None: ...