__all__ = ['Mail','NetworkInformation','PeerToPeer']
from typing import Tuple, Set, Iterable, List


class EndpointPermission(Object):
    def Equals(self, obj: Object) -> bool: ...
    @property
    def Hostname(self) -> str: ...
    @property
    def Port(self) -> int: ...
    @property
    def Transport(self) -> TransportType: ...
    def GetHashCode(self) -> int: ...


class NetworkAccess:
    Connect = 64
    Accept = 128


class TransportType:
    Udp = 1
    Connectionless = 1
    ConnectionOriented = 2
    Tcp = 2
    All = 3
