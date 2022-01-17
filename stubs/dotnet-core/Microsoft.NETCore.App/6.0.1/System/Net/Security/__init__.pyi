from typing import Tuple, Set, Iterable, List


class NegotiateStream(AuthenticatedStream):
    @overload
    def __init__(self, innerStream: Stream): ...
    @overload
    def __init__(self, innerStream: Stream, leaveInnerStreamOpen: bool): ...
    @overload
    def AuthenticateAsClient(self) -> None: ...
    @overload
    def AuthenticateAsClient(self, credential: NetworkCredential, targetName: str) -> None: ...
    @overload
    def AuthenticateAsClient(self, credential: NetworkCredential, binding: ChannelBinding, targetName: str) -> None: ...
    @overload
    def AuthenticateAsClient(self, credential: NetworkCredential, targetName: str, requiredProtectionLevel: ProtectionLevel, allowedImpersonationLevel: TokenImpersonationLevel) -> None: ...
    @overload
    def AuthenticateAsClient(self, credential: NetworkCredential, binding: ChannelBinding, targetName: str, requiredProtectionLevel: ProtectionLevel, allowedImpersonationLevel: TokenImpersonationLevel) -> None: ...
    @overload
    def AuthenticateAsClientAsync(self) -> Task: ...
    @overload
    def AuthenticateAsClientAsync(self, credential: NetworkCredential, targetName: str) -> Task: ...
    @overload
    def AuthenticateAsClientAsync(self, credential: NetworkCredential, binding: ChannelBinding, targetName: str) -> Task: ...
    @overload
    def AuthenticateAsClientAsync(self, credential: NetworkCredential, targetName: str, requiredProtectionLevel: ProtectionLevel, allowedImpersonationLevel: TokenImpersonationLevel) -> Task: ...
    @overload
    def AuthenticateAsClientAsync(self, credential: NetworkCredential, binding: ChannelBinding, targetName: str, requiredProtectionLevel: ProtectionLevel, allowedImpersonationLevel: TokenImpersonationLevel) -> Task: ...
    @overload
    def AuthenticateAsServer(self) -> None: ...
    @overload
    def AuthenticateAsServer(self, policy: ExtendedProtectionPolicy) -> None: ...
    @overload
    def AuthenticateAsServer(self, credential: NetworkCredential, requiredProtectionLevel: ProtectionLevel, requiredImpersonationLevel: TokenImpersonationLevel) -> None: ...
    @overload
    def AuthenticateAsServer(self, credential: NetworkCredential, policy: ExtendedProtectionPolicy, requiredProtectionLevel: ProtectionLevel, requiredImpersonationLevel: TokenImpersonationLevel) -> None: ...
    @overload
    def AuthenticateAsServerAsync(self) -> Task: ...
    @overload
    def AuthenticateAsServerAsync(self, policy: ExtendedProtectionPolicy) -> Task: ...
    @overload
    def AuthenticateAsServerAsync(self, credential: NetworkCredential, requiredProtectionLevel: ProtectionLevel, requiredImpersonationLevel: TokenImpersonationLevel) -> Task: ...
    @overload
    def AuthenticateAsServerAsync(self, credential: NetworkCredential, policy: ExtendedProtectionPolicy, requiredProtectionLevel: ProtectionLevel, requiredImpersonationLevel: TokenImpersonationLevel) -> Task: ...
    @overload
    def BeginAuthenticateAsClient(self, asyncCallback: AsyncCallback, asyncState: Object) -> IAsyncResult: ...
    @overload
    def BeginAuthenticateAsClient(self, credential: NetworkCredential, targetName: str, asyncCallback: AsyncCallback, asyncState: Object) -> IAsyncResult: ...
    @overload
    def BeginAuthenticateAsClient(self, credential: NetworkCredential, binding: ChannelBinding, targetName: str, asyncCallback: AsyncCallback, asyncState: Object) -> IAsyncResult: ...
    @overload
    def BeginAuthenticateAsClient(self, credential: NetworkCredential, targetName: str, requiredProtectionLevel: ProtectionLevel, allowedImpersonationLevel: TokenImpersonationLevel, asyncCallback: AsyncCallback, asyncState: Object) -> IAsyncResult: ...
    @overload
    def BeginAuthenticateAsClient(self, credential: NetworkCredential, binding: ChannelBinding, targetName: str, requiredProtectionLevel: ProtectionLevel, allowedImpersonationLevel: TokenImpersonationLevel, asyncCallback: AsyncCallback, asyncState: Object) -> IAsyncResult: ...
    @overload
    def BeginAuthenticateAsServer(self, asyncCallback: AsyncCallback, asyncState: Object) -> IAsyncResult: ...
    @overload
    def BeginAuthenticateAsServer(self, policy: ExtendedProtectionPolicy, asyncCallback: AsyncCallback, asyncState: Object) -> IAsyncResult: ...
    @overload
    def BeginAuthenticateAsServer(self, credential: NetworkCredential, requiredProtectionLevel: ProtectionLevel, requiredImpersonationLevel: TokenImpersonationLevel, asyncCallback: AsyncCallback, asyncState: Object) -> IAsyncResult: ...
    @overload
    def BeginAuthenticateAsServer(self, credential: NetworkCredential, policy: ExtendedProtectionPolicy, requiredProtectionLevel: ProtectionLevel, requiredImpersonationLevel: TokenImpersonationLevel, asyncCallback: AsyncCallback, asyncState: Object) -> IAsyncResult: ...
    def BeginRead(self, buffer: Set(Byte), offset: int, count: int, asyncCallback: AsyncCallback, asyncState: Object) -> IAsyncResult: ...
    def BeginWrite(self, buffer: Set(Byte), offset: int, count: int, asyncCallback: AsyncCallback, asyncState: Object) -> IAsyncResult: ...
    def DisposeAsync(self) -> ValueTask: ...
    def EndAuthenticateAsClient(self, asyncResult: IAsyncResult) -> None: ...
    def EndAuthenticateAsServer(self, asyncResult: IAsyncResult) -> None: ...
    def EndRead(self, asyncResult: IAsyncResult) -> int: ...
    def EndWrite(self, asyncResult: IAsyncResult) -> None: ...
    def Flush(self) -> None: ...
    @overload
    def FlushAsync(self, cancellationToken: CancellationToken) -> Task: ...
    @property
    def CanRead(self) -> bool: ...
    @property
    def CanSeek(self) -> bool: ...
    @property
    def CanTimeout(self) -> bool: ...
    @property
    def CanWrite(self) -> bool: ...
    @property
    def ImpersonationLevel(self) -> TokenImpersonationLevel: ...
    @property
    def IsAuthenticated(self) -> bool: ...
    @property
    def IsEncrypted(self) -> bool: ...
    @property
    def IsMutuallyAuthenticated(self) -> bool: ...
    @property
    def IsServer(self) -> bool: ...
    @property
    def IsSigned(self) -> bool: ...
    @property
    def Length(self) -> Int64: ...
    @property
    def Position(self) -> Int64: ...
    @property
    def ReadTimeout(self) -> int: ...
    @property
    def RemoteIdentity(self) -> IIdentity: ...
    @property
    def WriteTimeout(self) -> int: ...
    @overload
    def Read(self, buffer: Set(Byte), offset: int, count: int) -> int: ...
    @overload
    def ReadAsync(self, buffer: Memory, cancellationToken: CancellationToken) -> ValueTask: ...
    @overload
    def ReadAsync(self, buffer: Set(Byte), offset: int, count: int, cancellationToken: CancellationToken) -> Task: ...
    def Seek(self, offset: Int64, origin: SeekOrigin) -> Int64: ...
    @Position.setter
    def Position(self, value: Int64) -> None: ...
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...
    @WriteTimeout.setter
    def WriteTimeout(self, value: int) -> None: ...
    def SetLength(self, value: Int64) -> None: ...
    @overload
    def Write(self, buffer: Set(Byte), offset: int, count: int) -> None: ...
    @overload
    def WriteAsync(self, buffer: ReadOnlyMemory, cancellationToken: CancellationToken) -> ValueTask: ...
    @overload
    def WriteAsync(self, buffer: Set(Byte), offset: int, count: int, cancellationToken: CancellationToken) -> Task: ...
