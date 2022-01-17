__all__ = ['Collaboration']
from typing import Tuple, Set, Iterable, List


class Cloud(Object):
    @overload
    def Equals(self, other: Cloud) -> bool: ...
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @property
    def Global() -> Cloud: ...
    @property
    def Name(self) -> str: ...
    @property
    def Scope(self) -> PnrpScope: ...
    @property
    def ScopeId(self) -> int: ...
    def GetAvailableClouds() -> CloudCollection: ...
    def GetCloudByName(cloudName: str) -> Cloud: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...


class CloudCollection:
    def __init__(self): ...


class PeerName(Object):
    @overload
    def __init__(self, remotePeerName: str): ...
    @overload
    def __init__(self, classifier: str, peerNameType: PeerNameType): ...
    def CreateFromPeerHostName(peerHostName: str) -> PeerName: ...
    def CreateRelativePeerName(peerName: PeerName, classifier: str) -> PeerName: ...
    @overload
    def Equals(self, other: PeerName) -> bool: ...
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @property
    def Authority(self) -> str: ...
    @property
    def Classifier(self) -> str: ...
    @property
    def IsSecured(self) -> bool: ...
    @property
    def PeerHostName(self) -> str: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...


class PeerNameRecord(Object):
    def __init__(self): ...
    @property
    def Comment(self) -> str: ...
    @property
    def Data(self) -> Set(Byte): ...
    @property
    def EndPointCollection(self) -> IPEndPointCollection: ...
    @property
    def PeerName(self) -> PeerName: ...
    @Comment.setter
    def Comment(self, value: str) -> None: ...
    @Data.setter
    def Data(self, value: Set(Byte)) -> None: ...
    @PeerName.setter
    def PeerName(self, value: PeerName) -> None: ...


class PeerNameRecordCollection:
    def __init__(self): ...


class PeerNameRegistration(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, name: PeerName, port: int): ...
    @overload
    def __init__(self, name: PeerName, port: int, cloud: Cloud): ...
    def Dispose(self) -> None: ...
    @property
    def Cloud(self) -> Cloud: ...
    @property
    def Comment(self) -> str: ...
    @property
    def Data(self) -> Set(Byte): ...
    @property
    def EndPointCollection(self) -> IPEndPointCollection: ...
    @property
    def PeerName(self) -> PeerName: ...
    @property
    def Port(self) -> int: ...
    @property
    def UseAutoEndPointSelection(self) -> bool: ...
    def IsRegistered(self) -> bool: ...
    @Cloud.setter
    def Cloud(self, value: Cloud) -> None: ...
    @Comment.setter
    def Comment(self, value: str) -> None: ...
    @Data.setter
    def Data(self, value: Set(Byte)) -> None: ...
    @PeerName.setter
    def PeerName(self, value: PeerName) -> None: ...
    @Port.setter
    def Port(self, value: int) -> None: ...
    @UseAutoEndPointSelection.setter
    def UseAutoEndPointSelection(self, value: bool) -> None: ...
    def Start(self) -> None: ...
    def Stop(self) -> None: ...
    def Update(self) -> None: ...


class PeerNameResolver(Object):
    def __init__(self): ...
    def add_ResolveCompleted(self, value: EventHandler) -> None: ...
    def add_ResolveProgressChanged(self, value: EventHandler) -> None: ...
    def remove_ResolveCompleted(self, value: EventHandler) -> None: ...
    def remove_ResolveProgressChanged(self, value: EventHandler) -> None: ...
    @overload
    def Resolve(self, peerName: PeerName) -> PeerNameRecordCollection: ...
    @overload
    def Resolve(self, peerName: PeerName, cloud: Cloud) -> PeerNameRecordCollection: ...
    @overload
    def Resolve(self, peerName: PeerName, maxRecords: int) -> PeerNameRecordCollection: ...
    @overload
    def Resolve(self, peerName: PeerName, cloud: Cloud, maxRecords: int) -> PeerNameRecordCollection: ...
    @overload
    def ResolveAsync(self, peerName: PeerName, userState: Object) -> None: ...
    @overload
    def ResolveAsync(self, peerName: PeerName, maxRecords: int, userState: Object) -> None: ...
    @overload
    def ResolveAsync(self, peerName: PeerName, cloud: Cloud, userState: Object) -> None: ...
    @overload
    def ResolveAsync(self, peerName: PeerName, cloud: Cloud, maxRecords: int, userState: Object) -> None: ...
    def ResolveAsyncCancel(self, userState: Object) -> None: ...


class PeerNameType:
    Secured = 0
    Unsecured = 1


class PeerToPeerException(Exception):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...


class PnrpPermission(CodeAccessPermission):
    def __init__(self, state: PermissionState): ...
    def Copy(self) -> IPermission: ...
    def FromXml(self, e: SecurityElement) -> None: ...
    def Intersect(self, target: IPermission) -> IPermission: ...
    def IsSubsetOf(self, target: IPermission) -> bool: ...
    def IsUnrestricted(self) -> bool: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, target: IPermission) -> IPermission: ...


class PnrpPermissionAttribute(CodeAccessSecurityAttribute):
    def __init__(self, action: SecurityAction): ...
    def CreatePermission(self) -> IPermission: ...


class PnrpScope:
    All = 0
    Global = 1
    SiteLocal = 2
    LinkLocal = 3


class ResolveCompletedEventArgs(AsyncCompletedEventArgs):
    def __init__(self, peerNameRecordCollection: PeerNameRecordCollection, error: Exception, canceled: bool, userToken: Object): ...
    @property
    def PeerNameRecordCollection(self) -> PeerNameRecordCollection: ...


class ResolveProgressChangedEventArgs(ProgressChangedEventArgs):
    def __init__(self, peerNameRecord: PeerNameRecord, userToken: Object): ...
    @property
    def PeerNameRecord(self) -> PeerNameRecord: ...
