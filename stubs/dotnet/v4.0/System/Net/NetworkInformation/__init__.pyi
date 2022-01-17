from typing import Tuple, Set, Iterable, List


class DuplicateAddressDetectionState:
    Invalid = 0
    Tentative = 1
    Duplicate = 2
    Deprecated = 3
    Preferred = 4


class GatewayIPAddressInformation(Object):
    @property
    def Address(self) -> IPAddress: ...


class GatewayIPAddressInformationCollection(Object):
    def Add(self, address: GatewayIPAddressInformation) -> None: ...
    def Clear(self) -> None: ...
    def Contains(self, address: GatewayIPAddressInformation) -> bool: ...
    def CopyTo(self, array: Set(GatewayIPAddressInformation), offset: int) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsReadOnly(self) -> bool: ...
    @property
    def Item(self, index: int) -> GatewayIPAddressInformation: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def Remove(self, address: GatewayIPAddressInformation) -> bool: ...


class IcmpV4Statistics(Object):
    @property
    def AddressMaskRepliesReceived(self) -> Int64: ...
    @property
    def AddressMaskRepliesSent(self) -> Int64: ...
    @property
    def AddressMaskRequestsReceived(self) -> Int64: ...
    @property
    def AddressMaskRequestsSent(self) -> Int64: ...
    @property
    def DestinationUnreachableMessagesReceived(self) -> Int64: ...
    @property
    def DestinationUnreachableMessagesSent(self) -> Int64: ...
    @property
    def EchoRepliesReceived(self) -> Int64: ...
    @property
    def EchoRepliesSent(self) -> Int64: ...
    @property
    def EchoRequestsReceived(self) -> Int64: ...
    @property
    def EchoRequestsSent(self) -> Int64: ...
    @property
    def ErrorsReceived(self) -> Int64: ...
    @property
    def ErrorsSent(self) -> Int64: ...
    @property
    def MessagesReceived(self) -> Int64: ...
    @property
    def MessagesSent(self) -> Int64: ...
    @property
    def ParameterProblemsReceived(self) -> Int64: ...
    @property
    def ParameterProblemsSent(self) -> Int64: ...
    @property
    def RedirectsReceived(self) -> Int64: ...
    @property
    def RedirectsSent(self) -> Int64: ...
    @property
    def SourceQuenchesReceived(self) -> Int64: ...
    @property
    def SourceQuenchesSent(self) -> Int64: ...
    @property
    def TimeExceededMessagesReceived(self) -> Int64: ...
    @property
    def TimeExceededMessagesSent(self) -> Int64: ...
    @property
    def TimestampRepliesReceived(self) -> Int64: ...
    @property
    def TimestampRepliesSent(self) -> Int64: ...
    @property
    def TimestampRequestsReceived(self) -> Int64: ...
    @property
    def TimestampRequestsSent(self) -> Int64: ...


class IcmpV6Statistics(Object):
    @property
    def DestinationUnreachableMessagesReceived(self) -> Int64: ...
    @property
    def DestinationUnreachableMessagesSent(self) -> Int64: ...
    @property
    def EchoRepliesReceived(self) -> Int64: ...
    @property
    def EchoRepliesSent(self) -> Int64: ...
    @property
    def EchoRequestsReceived(self) -> Int64: ...
    @property
    def EchoRequestsSent(self) -> Int64: ...
    @property
    def ErrorsReceived(self) -> Int64: ...
    @property
    def ErrorsSent(self) -> Int64: ...
    @property
    def MembershipQueriesReceived(self) -> Int64: ...
    @property
    def MembershipQueriesSent(self) -> Int64: ...
    @property
    def MembershipReductionsReceived(self) -> Int64: ...
    @property
    def MembershipReductionsSent(self) -> Int64: ...
    @property
    def MembershipReportsReceived(self) -> Int64: ...
    @property
    def MembershipReportsSent(self) -> Int64: ...
    @property
    def MessagesReceived(self) -> Int64: ...
    @property
    def MessagesSent(self) -> Int64: ...
    @property
    def NeighborAdvertisementsReceived(self) -> Int64: ...
    @property
    def NeighborAdvertisementsSent(self) -> Int64: ...
    @property
    def NeighborSolicitsReceived(self) -> Int64: ...
    @property
    def NeighborSolicitsSent(self) -> Int64: ...
    @property
    def PacketTooBigMessagesReceived(self) -> Int64: ...
    @property
    def PacketTooBigMessagesSent(self) -> Int64: ...
    @property
    def ParameterProblemsReceived(self) -> Int64: ...
    @property
    def ParameterProblemsSent(self) -> Int64: ...
    @property
    def RedirectsReceived(self) -> Int64: ...
    @property
    def RedirectsSent(self) -> Int64: ...
    @property
    def RouterAdvertisementsReceived(self) -> Int64: ...
    @property
    def RouterAdvertisementsSent(self) -> Int64: ...
    @property
    def RouterSolicitsReceived(self) -> Int64: ...
    @property
    def RouterSolicitsSent(self) -> Int64: ...
    @property
    def TimeExceededMessagesReceived(self) -> Int64: ...
    @property
    def TimeExceededMessagesSent(self) -> Int64: ...


class IPAddressCollection(Object):
    def Add(self, address: IPAddress) -> None: ...
    def Clear(self) -> None: ...
    def Contains(self, address: IPAddress) -> bool: ...
    def CopyTo(self, array: Set(IPAddress), offset: int) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsReadOnly(self) -> bool: ...
    @property
    def Item(self, index: int) -> IPAddress: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def Remove(self, address: IPAddress) -> bool: ...


class IPAddressInformation(Object):
    @property
    def Address(self) -> IPAddress: ...
    @property
    def IsDnsEligible(self) -> bool: ...
    @property
    def IsTransient(self) -> bool: ...


class IPAddressInformationCollection(Object):
    def Add(self, address: IPAddressInformation) -> None: ...
    def Clear(self) -> None: ...
    def Contains(self, address: IPAddressInformation) -> bool: ...
    def CopyTo(self, array: Set(IPAddressInformation), offset: int) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsReadOnly(self) -> bool: ...
    @property
    def Item(self, index: int) -> IPAddressInformation: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def Remove(self, address: IPAddressInformation) -> bool: ...


class IPGlobalProperties(Object):
    def BeginGetUnicastAddresses(self, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    def EndGetUnicastAddresses(self, asyncResult: IAsyncResult) -> UnicastIPAddressInformationCollection: ...
    @property
    def DhcpScopeName(self) -> str: ...
    @property
    def DomainName(self) -> str: ...
    @property
    def HostName(self) -> str: ...
    @property
    def IsWinsProxy(self) -> bool: ...
    @property
    def NodeType(self) -> NetBiosNodeType: ...
    def GetActiveTcpConnections(self) -> Set(TcpConnectionInformation): ...
    def GetActiveTcpListeners(self) -> Set(IPEndPoint): ...
    def GetActiveUdpListeners(self) -> Set(IPEndPoint): ...
    def GetIcmpV4Statistics(self) -> IcmpV4Statistics: ...
    def GetIcmpV6Statistics(self) -> IcmpV6Statistics: ...
    def GetIPGlobalProperties() -> IPGlobalProperties: ...
    def GetIPv4GlobalStatistics(self) -> IPGlobalStatistics: ...
    def GetIPv6GlobalStatistics(self) -> IPGlobalStatistics: ...
    def GetTcpIPv4Statistics(self) -> TcpStatistics: ...
    def GetTcpIPv6Statistics(self) -> TcpStatistics: ...
    def GetUdpIPv4Statistics(self) -> UdpStatistics: ...
    def GetUdpIPv6Statistics(self) -> UdpStatistics: ...
    def GetUnicastAddresses(self) -> UnicastIPAddressInformationCollection: ...
    def GetUnicastAddressesAsync(self) -> Task: ...


class IPGlobalStatistics(Object):
    @property
    def DefaultTtl(self) -> int: ...
    @property
    def ForwardingEnabled(self) -> bool: ...
    @property
    def NumberOfInterfaces(self) -> int: ...
    @property
    def NumberOfIPAddresses(self) -> int: ...
    @property
    def NumberOfRoutes(self) -> int: ...
    @property
    def OutputPacketRequests(self) -> Int64: ...
    @property
    def OutputPacketRoutingDiscards(self) -> Int64: ...
    @property
    def OutputPacketsDiscarded(self) -> Int64: ...
    @property
    def OutputPacketsWithNoRoute(self) -> Int64: ...
    @property
    def PacketFragmentFailures(self) -> Int64: ...
    @property
    def PacketReassembliesRequired(self) -> Int64: ...
    @property
    def PacketReassemblyFailures(self) -> Int64: ...
    @property
    def PacketReassemblyTimeout(self) -> Int64: ...
    @property
    def PacketsFragmented(self) -> Int64: ...
    @property
    def PacketsReassembled(self) -> Int64: ...
    @property
    def ReceivedPackets(self) -> Int64: ...
    @property
    def ReceivedPacketsDelivered(self) -> Int64: ...
    @property
    def ReceivedPacketsDiscarded(self) -> Int64: ...
    @property
    def ReceivedPacketsForwarded(self) -> Int64: ...
    @property
    def ReceivedPacketsWithAddressErrors(self) -> Int64: ...
    @property
    def ReceivedPacketsWithHeadersErrors(self) -> Int64: ...
    @property
    def ReceivedPacketsWithUnknownProtocol(self) -> Int64: ...


class IPInterfaceProperties(Object):
    @property
    def AnycastAddresses(self) -> IPAddressInformationCollection: ...
    @property
    def DhcpServerAddresses(self) -> IPAddressCollection: ...
    @property
    def DnsAddresses(self) -> IPAddressCollection: ...
    @property
    def DnsSuffix(self) -> str: ...
    @property
    def GatewayAddresses(self) -> GatewayIPAddressInformationCollection: ...
    @property
    def IsDnsEnabled(self) -> bool: ...
    @property
    def IsDynamicDnsEnabled(self) -> bool: ...
    @property
    def MulticastAddresses(self) -> MulticastIPAddressInformationCollection: ...
    @property
    def UnicastAddresses(self) -> UnicastIPAddressInformationCollection: ...
    @property
    def WinsServersAddresses(self) -> IPAddressCollection: ...
    def GetIPv4Properties(self) -> IPv4InterfaceProperties: ...
    def GetIPv6Properties(self) -> IPv6InterfaceProperties: ...


class IPInterfaceStatistics(Object):
    @property
    def BytesReceived(self) -> Int64: ...
    @property
    def BytesSent(self) -> Int64: ...
    @property
    def IncomingPacketsDiscarded(self) -> Int64: ...
    @property
    def IncomingPacketsWithErrors(self) -> Int64: ...
    @property
    def IncomingUnknownProtocolPackets(self) -> Int64: ...
    @property
    def NonUnicastPacketsReceived(self) -> Int64: ...
    @property
    def NonUnicastPacketsSent(self) -> Int64: ...
    @property
    def OutgoingPacketsDiscarded(self) -> Int64: ...
    @property
    def OutgoingPacketsWithErrors(self) -> Int64: ...
    @property
    def OutputQueueLength(self) -> Int64: ...
    @property
    def UnicastPacketsReceived(self) -> Int64: ...
    @property
    def UnicastPacketsSent(self) -> Int64: ...


class IPStatus:
    Success = 0
    DestinationNetworkUnreachable = 11002
    DestinationHostUnreachable = 11003
    DestinationProhibited = 11004
    DestinationProtocolUnreachable = 11004
    DestinationPortUnreachable = 11005
    NoResources = 11006
    BadOption = 11007
    HardwareError = 11008
    PacketTooBig = 11009
    TimedOut = 11010
    BadRoute = 11012
    TtlExpired = 11013
    TtlReassemblyTimeExceeded = 11014
    ParameterProblem = 11015
    SourceQuench = 11016
    BadDestination = 11018
    DestinationUnreachable = 11040
    TimeExceeded = 11041
    BadHeader = 11042
    UnrecognizedNextHeader = 11043
    IcmpError = 11044
    DestinationScopeMismatch = 11045
    Unknown = -1


class IPv4InterfaceProperties(Object):
    @property
    def Index(self) -> int: ...
    @property
    def IsAutomaticPrivateAddressingActive(self) -> bool: ...
    @property
    def IsAutomaticPrivateAddressingEnabled(self) -> bool: ...
    @property
    def IsDhcpEnabled(self) -> bool: ...
    @property
    def IsForwardingEnabled(self) -> bool: ...
    @property
    def Mtu(self) -> int: ...
    @property
    def UsesWins(self) -> bool: ...


class IPv4InterfaceStatistics(Object):
    @property
    def BytesReceived(self) -> Int64: ...
    @property
    def BytesSent(self) -> Int64: ...
    @property
    def IncomingPacketsDiscarded(self) -> Int64: ...
    @property
    def IncomingPacketsWithErrors(self) -> Int64: ...
    @property
    def IncomingUnknownProtocolPackets(self) -> Int64: ...
    @property
    def NonUnicastPacketsReceived(self) -> Int64: ...
    @property
    def NonUnicastPacketsSent(self) -> Int64: ...
    @property
    def OutgoingPacketsDiscarded(self) -> Int64: ...
    @property
    def OutgoingPacketsWithErrors(self) -> Int64: ...
    @property
    def OutputQueueLength(self) -> Int64: ...
    @property
    def UnicastPacketsReceived(self) -> Int64: ...
    @property
    def UnicastPacketsSent(self) -> Int64: ...


class IPv6InterfaceProperties(Object):
    @property
    def Index(self) -> int: ...
    @property
    def Mtu(self) -> int: ...
    def GetScopeId(self, scopeLevel: ScopeLevel) -> Int64: ...


class MulticastIPAddressInformation(IPAddressInformation):
    @property
    def AddressPreferredLifetime(self) -> Int64: ...
    @property
    def AddressValidLifetime(self) -> Int64: ...
    @property
    def DhcpLeaseLifetime(self) -> Int64: ...
    @property
    def DuplicateAddressDetectionState(self) -> DuplicateAddressDetectionState: ...
    @property
    def PrefixOrigin(self) -> PrefixOrigin: ...
    @property
    def SuffixOrigin(self) -> SuffixOrigin: ...


class MulticastIPAddressInformationCollection(Object):
    def Add(self, address: MulticastIPAddressInformation) -> None: ...
    def Clear(self) -> None: ...
    def Contains(self, address: MulticastIPAddressInformation) -> bool: ...
    def CopyTo(self, array: Set(MulticastIPAddressInformation), offset: int) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsReadOnly(self) -> bool: ...
    @property
    def Item(self, index: int) -> MulticastIPAddressInformation: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def Remove(self, address: MulticastIPAddressInformation) -> bool: ...


class NetBiosNodeType:
    Unknown = 0
    Broadcast = 1
    Peer2Peer = 2
    Mixed = 4
    Hybrid = 8


class NetworkAddressChangedEventHandler(MulticastDelegate):
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, sender: Object, e: EventArgs, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: Object, e: EventArgs) -> None: ...


class NetworkAvailabilityChangedEventHandler(MulticastDelegate):
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, sender: Object, e: NetworkAvailabilityEventArgs, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: Object, e: NetworkAvailabilityEventArgs) -> None: ...


class NetworkAvailabilityEventArgs(EventArgs):
    @property
    def IsAvailable(self) -> bool: ...


class NetworkChange(Object):
    def __init__(self): ...
    def add_NetworkAddressChanged(value: NetworkAddressChangedEventHandler) -> None: ...
    def add_NetworkAvailabilityChanged(value: NetworkAvailabilityChangedEventHandler) -> None: ...
    def remove_NetworkAddressChanged(value: NetworkAddressChangedEventHandler) -> None: ...
    def remove_NetworkAvailabilityChanged(value: NetworkAvailabilityChangedEventHandler) -> None: ...


class NetworkInformationAccess:
    #None = 0
    Read = 1
    Ping = 4


class NetworkInformationException(Win32Exception):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, errorCode: int): ...
    @property
    def ErrorCode(self) -> int: ...


class NetworkInformationPermission(CodeAccessPermission):
    @overload
    def __init__(self, state: PermissionState): ...
    @overload
    def __init__(self, access: NetworkInformationAccess): ...
    def AddPermission(self, access: NetworkInformationAccess) -> None: ...
    def Copy(self) -> IPermission: ...
    def FromXml(self, securityElement: SecurityElement) -> None: ...
    @property
    def Access(self) -> NetworkInformationAccess: ...
    def Intersect(self, target: IPermission) -> IPermission: ...
    def IsSubsetOf(self, target: IPermission) -> bool: ...
    def IsUnrestricted(self) -> bool: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, target: IPermission) -> IPermission: ...


class NetworkInformationPermissionAttribute(CodeAccessSecurityAttribute):
    def __init__(self, action: SecurityAction): ...
    def CreatePermission(self) -> IPermission: ...
    @property
    def Access(self) -> str: ...
    @Access.setter
    def Access(self, value: str) -> None: ...


class NetworkInterface(Object):
    @property
    def Description(self) -> str: ...
    @property
    def Id(self) -> str: ...
    @property
    def IPv6LoopbackInterfaceIndex() -> int: ...
    @property
    def IsReceiveOnly(self) -> bool: ...
    @property
    def LoopbackInterfaceIndex() -> int: ...
    @property
    def Name(self) -> str: ...
    @property
    def NetworkInterfaceType(self) -> NetworkInterfaceType: ...
    @property
    def OperationalStatus(self) -> OperationalStatus: ...
    @property
    def Speed(self) -> Int64: ...
    @property
    def SupportsMulticast(self) -> bool: ...
    def GetAllNetworkInterfaces() -> Set(NetworkInterface): ...
    def GetIPProperties(self) -> IPInterfaceProperties: ...
    def GetIPStatistics(self) -> IPInterfaceStatistics: ...
    def GetIPv4Statistics(self) -> IPv4InterfaceStatistics: ...
    def GetIsNetworkAvailable() -> bool: ...
    def GetPhysicalAddress(self) -> PhysicalAddress: ...
    def Supports(self, networkInterfaceComponent: NetworkInterfaceComponent) -> bool: ...


class NetworkInterfaceComponent:
    IPv4 = 0
    IPv6 = 1


class NetworkInterfaceType:
    Unknown = 1
    Ethernet = 6
    TokenRing = 9
    Fddi = 15
    BasicIsdn = 20
    PrimaryIsdn = 21
    Ppp = 23
    Loopback = 24
    Ethernet3Megabit = 26
    Slip = 28
    Atm = 37
    GenericModem = 48
    FastEthernetT = 62
    Isdn = 63
    FastEthernetFx = 69
    Wireless80211 = 71
    AsymmetricDsl = 94
    RateAdaptDsl = 95
    SymmetricDsl = 96
    VeryHighSpeedDsl = 97
    IPOverAtm = 114
    GigabitEthernet = 117
    Tunnel = 131
    MultiRateSymmetricDsl = 143
    HighPerformanceSerialBus = 144
    Wman = 237
    Wwanpp = 243
    Wwanpp2 = 244


class OperationalStatus:
    Up = 1
    Down = 2
    Testing = 3
    Unknown = 4
    Dormant = 5
    NotPresent = 6
    LowerLayerDown = 7


class PhysicalAddress(Object):
    def __init__(self, address: Set(Byte)): ...
    def Equals(self, comparand: Object) -> bool: ...
    def GetAddressBytes(self) -> Set(Byte): ...
    def GetHashCode(self) -> int: ...
    def Parse(address: str) -> PhysicalAddress: ...
    def ToString(self) -> str: ...


class Ping(Component):
    def __init__(self): ...
    def add_PingCompleted(self, value: PingCompletedEventHandler) -> None: ...
    def remove_PingCompleted(self, value: PingCompletedEventHandler) -> None: ...
    @overload
    def Send(self, address: IPAddress) -> PingReply: ...
    @overload
    def Send(self, hostNameOrAddress: str) -> PingReply: ...
    @overload
    def Send(self, address: IPAddress, timeout: int) -> PingReply: ...
    @overload
    def Send(self, hostNameOrAddress: str, timeout: int) -> PingReply: ...
    @overload
    def Send(self, hostNameOrAddress: str, timeout: int, buffer: Set(Byte)) -> PingReply: ...
    @overload
    def Send(self, address: IPAddress, timeout: int, buffer: Set(Byte)) -> PingReply: ...
    @overload
    def Send(self, hostNameOrAddress: str, timeout: int, buffer: Set(Byte), options: PingOptions) -> PingReply: ...
    @overload
    def Send(self, address: IPAddress, timeout: int, buffer: Set(Byte), options: PingOptions) -> PingReply: ...
    @overload
    def SendAsync(self, address: IPAddress, userToken: Object) -> None: ...
    @overload
    def SendAsync(self, hostNameOrAddress: str, userToken: Object) -> None: ...
    @overload
    def SendAsync(self, address: IPAddress, timeout: int, userToken: Object) -> None: ...
    @overload
    def SendAsync(self, hostNameOrAddress: str, timeout: int, userToken: Object) -> None: ...
    @overload
    def SendAsync(self, address: IPAddress, timeout: int, buffer: Set(Byte), userToken: Object) -> None: ...
    @overload
    def SendAsync(self, hostNameOrAddress: str, timeout: int, buffer: Set(Byte), userToken: Object) -> None: ...
    @overload
    def SendAsync(self, hostNameOrAddress: str, timeout: int, buffer: Set(Byte), options: PingOptions, userToken: Object) -> None: ...
    @overload
    def SendAsync(self, address: IPAddress, timeout: int, buffer: Set(Byte), options: PingOptions, userToken: Object) -> None: ...
    def SendAsyncCancel(self) -> None: ...
    @overload
    def SendPingAsync(self, address: IPAddress) -> Task: ...
    @overload
    def SendPingAsync(self, hostNameOrAddress: str) -> Task: ...
    @overload
    def SendPingAsync(self, hostNameOrAddress: str, timeout: int) -> Task: ...
    @overload
    def SendPingAsync(self, address: IPAddress, timeout: int) -> Task: ...
    @overload
    def SendPingAsync(self, address: IPAddress, timeout: int, buffer: Set(Byte)) -> Task: ...
    @overload
    def SendPingAsync(self, hostNameOrAddress: str, timeout: int, buffer: Set(Byte)) -> Task: ...
    @overload
    def SendPingAsync(self, hostNameOrAddress: str, timeout: int, buffer: Set(Byte), options: PingOptions) -> Task: ...
    @overload
    def SendPingAsync(self, address: IPAddress, timeout: int, buffer: Set(Byte), options: PingOptions) -> Task: ...


class PingCompletedEventArgs(AsyncCompletedEventArgs):
    @property
    def Reply(self) -> PingReply: ...


class PingCompletedEventHandler(MulticastDelegate):
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, sender: Object, e: PingCompletedEventArgs, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: Object, e: PingCompletedEventArgs) -> None: ...


class PingException(InvalidOperationException):
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class PingOptions(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, ttl: int, dontFragment: bool): ...
    @property
    def DontFragment(self) -> bool: ...
    @property
    def Ttl(self) -> int: ...
    @DontFragment.setter
    def DontFragment(self, value: bool) -> None: ...
    @Ttl.setter
    def Ttl(self, value: int) -> None: ...


class PingReply(Object):
    @property
    def Address(self) -> IPAddress: ...
    @property
    def Buffer(self) -> Set(Byte): ...
    @property
    def Options(self) -> PingOptions: ...
    @property
    def RoundtripTime(self) -> Int64: ...
    @property
    def Status(self) -> IPStatus: ...


class PrefixOrigin:
    Other = 0
    Manual = 1
    WellKnown = 2
    Dhcp = 3
    RouterAdvertisement = 4


class ScopeLevel:
    #None = 0
    Interface = 1
    Link = 2
    Subnet = 3
    Admin = 4
    Site = 5
    Organization = 8
    Global = 14


class SuffixOrigin:
    Other = 0
    Manual = 1
    WellKnown = 2
    OriginDhcp = 3
    LinkLayerAddress = 4
    Random = 5


class TcpConnectionInformation(Object):
    @property
    def LocalEndPoint(self) -> IPEndPoint: ...
    @property
    def RemoteEndPoint(self) -> IPEndPoint: ...
    @property
    def State(self) -> TcpState: ...


class TcpState:
    Unknown = 0
    Closed = 1
    Listen = 2
    SynSent = 3
    SynReceived = 4
    Established = 5
    FinWait1 = 6
    FinWait2 = 7
    CloseWait = 8
    Closing = 9
    LastAck = 10
    TimeWait = 11
    DeleteTcb = 12


class TcpStatistics(Object):
    @property
    def ConnectionsAccepted(self) -> Int64: ...
    @property
    def ConnectionsInitiated(self) -> Int64: ...
    @property
    def CumulativeConnections(self) -> Int64: ...
    @property
    def CurrentConnections(self) -> Int64: ...
    @property
    def ErrorsReceived(self) -> Int64: ...
    @property
    def FailedConnectionAttempts(self) -> Int64: ...
    @property
    def MaximumConnections(self) -> Int64: ...
    @property
    def MaximumTransmissionTimeout(self) -> Int64: ...
    @property
    def MinimumTransmissionTimeout(self) -> Int64: ...
    @property
    def ResetConnections(self) -> Int64: ...
    @property
    def ResetsSent(self) -> Int64: ...
    @property
    def SegmentsReceived(self) -> Int64: ...
    @property
    def SegmentsResent(self) -> Int64: ...
    @property
    def SegmentsSent(self) -> Int64: ...


class UdpStatistics(Object):
    @property
    def DatagramsReceived(self) -> Int64: ...
    @property
    def DatagramsSent(self) -> Int64: ...
    @property
    def IncomingDatagramsDiscarded(self) -> Int64: ...
    @property
    def IncomingDatagramsWithErrors(self) -> Int64: ...
    @property
    def UdpListeners(self) -> int: ...


class UnicastIPAddressInformation(IPAddressInformation):
    @property
    def AddressPreferredLifetime(self) -> Int64: ...
    @property
    def AddressValidLifetime(self) -> Int64: ...
    @property
    def DhcpLeaseLifetime(self) -> Int64: ...
    @property
    def DuplicateAddressDetectionState(self) -> DuplicateAddressDetectionState: ...
    @property
    def IPv4Mask(self) -> IPAddress: ...
    @property
    def PrefixLength(self) -> int: ...
    @property
    def PrefixOrigin(self) -> PrefixOrigin: ...
    @property
    def SuffixOrigin(self) -> SuffixOrigin: ...


class UnicastIPAddressInformationCollection(Object):
    def Add(self, address: UnicastIPAddressInformation) -> None: ...
    def Clear(self) -> None: ...
    def Contains(self, address: UnicastIPAddressInformation) -> bool: ...
    def CopyTo(self, array: Set(UnicastIPAddressInformation), offset: int) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsReadOnly(self) -> bool: ...
    @property
    def Item(self, index: int) -> UnicastIPAddressInformation: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def Remove(self, address: UnicastIPAddressInformation) -> bool: ...
