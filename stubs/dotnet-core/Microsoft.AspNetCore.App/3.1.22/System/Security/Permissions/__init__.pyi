from typing import Tuple, Set, Iterable, List


class DataProtectionPermission(CodeAccessPermission):
    @overload
    def __init__(self, state: PermissionState): ...
    @overload
    def __init__(self, flag: DataProtectionPermissionFlags): ...
    def Copy(self) -> IPermission: ...
    def FromXml(self, securityElement: SecurityElement) -> None: ...
    @property
    def Flags(self) -> DataProtectionPermissionFlags: ...
    def Intersect(self, target: IPermission) -> IPermission: ...
    def IsSubsetOf(self, target: IPermission) -> bool: ...
    def IsUnrestricted(self) -> bool: ...
    @Flags.setter
    def Flags(self, value: DataProtectionPermissionFlags) -> None: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, target: IPermission) -> IPermission: ...


class DataProtectionPermissionAttribute(CodeAccessSecurityAttribute):
    def __init__(self, action: SecurityAction): ...
    def CreatePermission(self) -> IPermission: ...
    @property
    def Flags(self) -> DataProtectionPermissionFlags: ...
    @property
    def ProtectData(self) -> bool: ...
    @property
    def ProtectMemory(self) -> bool: ...
    @property
    def UnprotectData(self) -> bool: ...
    @property
    def UnprotectMemory(self) -> bool: ...
    @Flags.setter
    def Flags(self, value: DataProtectionPermissionFlags) -> None: ...
    @ProtectData.setter
    def ProtectData(self, value: bool) -> None: ...
    @ProtectMemory.setter
    def ProtectMemory(self, value: bool) -> None: ...
    @UnprotectData.setter
    def UnprotectData(self, value: bool) -> None: ...
    @UnprotectMemory.setter
    def UnprotectMemory(self, value: bool) -> None: ...


class DataProtectionPermissionFlags:
    NoFlags = 0
    ProtectData = 1
    UnprotectData = 2
    ProtectMemory = 4
    UnprotectMemory = 8
    AllFlags = 15


class EnvironmentPermission(CodeAccessPermission):
    @overload
    def __init__(self, state: PermissionState): ...
    @overload
    def __init__(self, flag: EnvironmentPermissionAccess, pathList: str): ...
    def AddPathList(self, flag: EnvironmentPermissionAccess, pathList: str) -> None: ...
    def Copy(self) -> IPermission: ...
    def FromXml(self, esd: SecurityElement) -> None: ...
    def GetPathList(self, flag: EnvironmentPermissionAccess) -> str: ...
    def Intersect(self, target: IPermission) -> IPermission: ...
    def IsSubsetOf(self, target: IPermission) -> bool: ...
    def IsUnrestricted(self) -> bool: ...
    def SetPathList(self, flag: EnvironmentPermissionAccess, pathList: str) -> None: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, other: IPermission) -> IPermission: ...


class EnvironmentPermissionAccess:
    NoAccess = 0
    Read = 1
    Write = 2
    AllAccess = 3


class EnvironmentPermissionAttribute(CodeAccessSecurityAttribute):
    def __init__(self, action: SecurityAction): ...
    def CreatePermission(self) -> IPermission: ...
    @property
    def All(self) -> str: ...
    @property
    def Read(self) -> str: ...
    @property
    def Write(self) -> str: ...
    @All.setter
    def All(self, value: str) -> None: ...
    @Read.setter
    def Read(self, value: str) -> None: ...
    @Write.setter
    def Write(self, value: str) -> None: ...


class FileDialogPermission(CodeAccessPermission):
    @overload
    def __init__(self, access: FileDialogPermissionAccess): ...
    @overload
    def __init__(self, state: PermissionState): ...
    def Copy(self) -> IPermission: ...
    def FromXml(self, esd: SecurityElement) -> None: ...
    @property
    def Access(self) -> FileDialogPermissionAccess: ...
    def Intersect(self, target: IPermission) -> IPermission: ...
    def IsSubsetOf(self, target: IPermission) -> bool: ...
    def IsUnrestricted(self) -> bool: ...
    @Access.setter
    def Access(self, value: FileDialogPermissionAccess) -> None: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, target: IPermission) -> IPermission: ...


class FileDialogPermissionAccess:
    #None = 0
    Open = 1
    Save = 2
    OpenSave = 3


class FileDialogPermissionAttribute(CodeAccessSecurityAttribute):
    def __init__(self, action: SecurityAction): ...
    def CreatePermission(self) -> IPermission: ...
    @property
    def Open(self) -> bool: ...
    @property
    def Save(self) -> bool: ...
    @Open.setter
    def Open(self, value: bool) -> None: ...
    @Save.setter
    def Save(self, value: bool) -> None: ...


class FileIOPermission(CodeAccessPermission):
    @overload
    def __init__(self, state: PermissionState): ...
    @overload
    def __init__(self, access: FileIOPermissionAccess, path: str): ...
    @overload
    def __init__(self, access: FileIOPermissionAccess, pathList: Set(str)): ...
    @overload
    def __init__(self, access: FileIOPermissionAccess, actions: AccessControlActions, path: str): ...
    @overload
    def __init__(self, access: FileIOPermissionAccess, actions: AccessControlActions, pathList: Set(str)): ...
    @overload
    def AddPathList(self, access: FileIOPermissionAccess, path: str) -> None: ...
    @overload
    def AddPathList(self, access: FileIOPermissionAccess, pathList: Set(str)) -> None: ...
    def Copy(self) -> IPermission: ...
    def Equals(self, o: Object) -> bool: ...
    def FromXml(self, esd: SecurityElement) -> None: ...
    @property
    def AllFiles(self) -> FileIOPermissionAccess: ...
    @property
    def AllLocalFiles(self) -> FileIOPermissionAccess: ...
    def GetHashCode(self) -> int: ...
    def GetPathList(self, access: FileIOPermissionAccess) -> Set(str): ...
    def Intersect(self, target: IPermission) -> IPermission: ...
    def IsSubsetOf(self, target: IPermission) -> bool: ...
    def IsUnrestricted(self) -> bool: ...
    @AllFiles.setter
    def AllFiles(self, value: FileIOPermissionAccess) -> None: ...
    @AllLocalFiles.setter
    def AllLocalFiles(self, value: FileIOPermissionAccess) -> None: ...
    @overload
    def SetPathList(self, access: FileIOPermissionAccess, path: str) -> None: ...
    @overload
    def SetPathList(self, access: FileIOPermissionAccess, pathList: Set(str)) -> None: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, other: IPermission) -> IPermission: ...


class FileIOPermissionAccess:
    NoAccess = 0
    Read = 1
    Write = 2
    Append = 4
    PathDiscovery = 8
    AllAccess = 15


class FileIOPermissionAttribute(CodeAccessSecurityAttribute):
    def __init__(self, action: SecurityAction): ...
    def CreatePermission(self) -> IPermission: ...
    @property
    def All(self) -> str: ...
    @property
    def AllFiles(self) -> FileIOPermissionAccess: ...
    @property
    def AllLocalFiles(self) -> FileIOPermissionAccess: ...
    @property
    def Append(self) -> str: ...
    @property
    def ChangeAccessControl(self) -> str: ...
    @property
    def PathDiscovery(self) -> str: ...
    @property
    def Read(self) -> str: ...
    @property
    def ViewAccessControl(self) -> str: ...
    @property
    def ViewAndModify(self) -> str: ...
    @property
    def Write(self) -> str: ...
    @All.setter
    def All(self, value: str) -> None: ...
    @AllFiles.setter
    def AllFiles(self, value: FileIOPermissionAccess) -> None: ...
    @AllLocalFiles.setter
    def AllLocalFiles(self, value: FileIOPermissionAccess) -> None: ...
    @Append.setter
    def Append(self, value: str) -> None: ...
    @ChangeAccessControl.setter
    def ChangeAccessControl(self, value: str) -> None: ...
    @PathDiscovery.setter
    def PathDiscovery(self, value: str) -> None: ...
    @Read.setter
    def Read(self, value: str) -> None: ...
    @ViewAccessControl.setter
    def ViewAccessControl(self, value: str) -> None: ...
    @ViewAndModify.setter
    def ViewAndModify(self, value: str) -> None: ...
    @Write.setter
    def Write(self, value: str) -> None: ...


class GacIdentityPermission(CodeAccessPermission):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, state: PermissionState): ...
    def Copy(self) -> IPermission: ...
    def FromXml(self, securityElement: SecurityElement) -> None: ...
    def Intersect(self, target: IPermission) -> IPermission: ...
    def IsSubsetOf(self, target: IPermission) -> bool: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, target: IPermission) -> IPermission: ...


class GacIdentityPermissionAttribute(CodeAccessSecurityAttribute):
    def __init__(self, action: SecurityAction): ...
    def CreatePermission(self) -> IPermission: ...


class HostProtectionAttribute(CodeAccessSecurityAttribute):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, action: SecurityAction): ...
    def CreatePermission(self) -> IPermission: ...
    @property
    def ExternalProcessMgmt(self) -> bool: ...
    @property
    def ExternalThreading(self) -> bool: ...
    @property
    def MayLeakOnAbort(self) -> bool: ...
    @property
    def Resources(self) -> HostProtectionResource: ...
    @property
    def SecurityInfrastructure(self) -> bool: ...
    @property
    def SelfAffectingProcessMgmt(self) -> bool: ...
    @property
    def SelfAffectingThreading(self) -> bool: ...
    @property
    def SharedState(self) -> bool: ...
    @property
    def Synchronization(self) -> bool: ...
    @property
    def UI(self) -> bool: ...
    @ExternalProcessMgmt.setter
    def ExternalProcessMgmt(self, value: bool) -> None: ...
    @ExternalThreading.setter
    def ExternalThreading(self, value: bool) -> None: ...
    @MayLeakOnAbort.setter
    def MayLeakOnAbort(self, value: bool) -> None: ...
    @Resources.setter
    def Resources(self, value: HostProtectionResource) -> None: ...
    @SecurityInfrastructure.setter
    def SecurityInfrastructure(self, value: bool) -> None: ...
    @SelfAffectingProcessMgmt.setter
    def SelfAffectingProcessMgmt(self, value: bool) -> None: ...
    @SelfAffectingThreading.setter
    def SelfAffectingThreading(self, value: bool) -> None: ...
    @SharedState.setter
    def SharedState(self, value: bool) -> None: ...
    @Synchronization.setter
    def Synchronization(self, value: bool) -> None: ...
    @UI.setter
    def UI(self, value: bool) -> None: ...


class HostProtectionResource:
    #None = 0
    Synchronization = 1
    SharedState = 2
    ExternalProcessMgmt = 4
    SelfAffectingProcessMgmt = 8
    ExternalThreading = 16
    SelfAffectingThreading = 32
    SecurityInfrastructure = 64
    UI = 128
    MayLeakOnAbort = 256
    All = 511


class IsolatedStorageContainment:
    #None = 0
    DomainIsolationByUser = 16
    ApplicationIsolationByUser = 21
    AssemblyIsolationByUser = 32
    DomainIsolationByMachine = 48
    AssemblyIsolationByMachine = 64
    ApplicationIsolationByMachine = 69
    DomainIsolationByRoamingUser = 80
    AssemblyIsolationByRoamingUser = 96
    ApplicationIsolationByRoamingUser = 101
    AdministerIsolatedStorageByUser = 112
    UnrestrictedIsolatedStorage = 240


class IsolatedStorageFilePermission(IsolatedStoragePermission):
    def __init__(self, state: PermissionState): ...
    def Copy(self) -> IPermission: ...
    def Intersect(self, target: IPermission) -> IPermission: ...
    def IsSubsetOf(self, target: IPermission) -> bool: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, target: IPermission) -> IPermission: ...


class IsolatedStorageFilePermissionAttribute(IsolatedStoragePermissionAttribute):
    def __init__(self, action: SecurityAction): ...
    def CreatePermission(self) -> IPermission: ...


class IsolatedStoragePermission(CodeAccessPermission):
    def FromXml(self, esd: SecurityElement) -> None: ...
    @property
    def UsageAllowed(self) -> IsolatedStorageContainment: ...
    @property
    def UserQuota(self) -> Int64: ...
    def IsUnrestricted(self) -> bool: ...
    @UsageAllowed.setter
    def UsageAllowed(self, value: IsolatedStorageContainment) -> None: ...
    @UserQuota.setter
    def UserQuota(self, value: Int64) -> None: ...
    def ToXml(self) -> SecurityElement: ...


class IsolatedStoragePermissionAttribute(CodeAccessSecurityAttribute):
    @property
    def UsageAllowed(self) -> IsolatedStorageContainment: ...
    @property
    def UserQuota(self) -> Int64: ...
    @UsageAllowed.setter
    def UsageAllowed(self, value: IsolatedStorageContainment) -> None: ...
    @UserQuota.setter
    def UserQuota(self, value: Int64) -> None: ...


class IUnrestrictedPermission:
    def IsUnrestricted(self) -> bool: ...


class KeyContainerPermission(CodeAccessPermission):
    @overload
    def __init__(self, state: PermissionState): ...
    @overload
    def __init__(self, flags: KeyContainerPermissionFlags): ...
    @overload
    def __init__(self, flags: KeyContainerPermissionFlags, accessList: Set(KeyContainerPermissionAccessEntry)): ...
    def Copy(self) -> IPermission: ...
    def FromXml(self, securityElement: SecurityElement) -> None: ...
    @property
    def AccessEntries(self) -> KeyContainerPermissionAccessEntryCollection: ...
    @property
    def Flags(self) -> KeyContainerPermissionFlags: ...
    def Intersect(self, target: IPermission) -> IPermission: ...
    def IsSubsetOf(self, target: IPermission) -> bool: ...
    def IsUnrestricted(self) -> bool: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, target: IPermission) -> IPermission: ...


class KeyContainerPermissionAccessEntry(Object):
    @overload
    def __init__(self, keyContainerName: str, flags: KeyContainerPermissionFlags): ...
    @overload
    def __init__(self, parameters: CspParameters, flags: KeyContainerPermissionFlags): ...
    @overload
    def __init__(self, keyStore: str, providerName: str, providerType: int, keyContainerName: str, keySpec: int, flags: KeyContainerPermissionFlags): ...
    def Equals(self, o: Object) -> bool: ...
    @property
    def Flags(self) -> KeyContainerPermissionFlags: ...
    @property
    def KeyContainerName(self) -> str: ...
    @property
    def KeySpec(self) -> int: ...
    @property
    def KeyStore(self) -> str: ...
    @property
    def ProviderName(self) -> str: ...
    @property
    def ProviderType(self) -> int: ...
    def GetHashCode(self) -> int: ...
    @Flags.setter
    def Flags(self, value: KeyContainerPermissionFlags) -> None: ...
    @KeyContainerName.setter
    def KeyContainerName(self, value: str) -> None: ...
    @KeySpec.setter
    def KeySpec(self, value: int) -> None: ...
    @KeyStore.setter
    def KeyStore(self, value: str) -> None: ...
    @ProviderName.setter
    def ProviderName(self, value: str) -> None: ...
    @ProviderType.setter
    def ProviderType(self, value: int) -> None: ...


class KeyContainerPermissionAccessEntryCollection(Object):
    def __init__(self): ...
    def Add(self, accessEntry: KeyContainerPermissionAccessEntry) -> int: ...
    def Clear(self) -> None: ...
    @overload
    def CopyTo(self, array: Set(KeyContainerPermissionAccessEntry), index: int) -> None: ...
    @overload
    def CopyTo(self, array: Array, index: int) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsSynchronized(self) -> bool: ...
    @property
    def Item(self, index: int) -> KeyContainerPermissionAccessEntry: ...
    @property
    def SyncRoot(self) -> Object: ...
    def GetEnumerator(self) -> KeyContainerPermissionAccessEntryEnumerator: ...
    def IndexOf(self, accessEntry: KeyContainerPermissionAccessEntry) -> int: ...
    def Remove(self, accessEntry: KeyContainerPermissionAccessEntry) -> None: ...


class KeyContainerPermissionAccessEntryEnumerator(Object):
    def __init__(self): ...
    @property
    def Current(self) -> KeyContainerPermissionAccessEntry: ...
    def MoveNext(self) -> bool: ...
    def Reset(self) -> None: ...


class KeyContainerPermissionAttribute(CodeAccessSecurityAttribute):
    def __init__(self, action: SecurityAction): ...
    def CreatePermission(self) -> IPermission: ...
    @property
    def Flags(self) -> KeyContainerPermissionFlags: ...
    @property
    def KeyContainerName(self) -> str: ...
    @property
    def KeySpec(self) -> int: ...
    @property
    def KeyStore(self) -> str: ...
    @property
    def ProviderName(self) -> str: ...
    @property
    def ProviderType(self) -> int: ...
    @Flags.setter
    def Flags(self, value: KeyContainerPermissionFlags) -> None: ...
    @KeyContainerName.setter
    def KeyContainerName(self, value: str) -> None: ...
    @KeySpec.setter
    def KeySpec(self, value: int) -> None: ...
    @KeyStore.setter
    def KeyStore(self, value: str) -> None: ...
    @ProviderName.setter
    def ProviderName(self, value: str) -> None: ...
    @ProviderType.setter
    def ProviderType(self, value: int) -> None: ...


class KeyContainerPermissionFlags:
    NoFlags = 0
    Create = 1
    Open = 2
    Delete = 4
    Import = 16
    Export = 32
    Sign = 256
    Decrypt = 512
    ViewAcl = 4096
    ChangeAcl = 8192
    AllFlags = 13111


class MediaPermission(CodeAccessPermission):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, state: PermissionState): ...
    @overload
    def __init__(self, permissionAudio: MediaPermissionAudio): ...
    @overload
    def __init__(self, permissionVideo: MediaPermissionVideo): ...
    @overload
    def __init__(self, permissionImage: MediaPermissionImage): ...
    @overload
    def __init__(self, permissionAudio: MediaPermissionAudio, permissionVideo: MediaPermissionVideo, permissionImage: MediaPermissionImage): ...
    def Copy(self) -> IPermission: ...
    def FromXml(self, securityElement: SecurityElement) -> None: ...
    @property
    def Audio(self) -> MediaPermissionAudio: ...
    @property
    def Image(self) -> MediaPermissionImage: ...
    @property
    def Video(self) -> MediaPermissionVideo: ...
    def Intersect(self, target: IPermission) -> IPermission: ...
    def IsSubsetOf(self, target: IPermission) -> bool: ...
    def IsUnrestricted(self) -> bool: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, target: IPermission) -> IPermission: ...


class MediaPermissionAttribute(CodeAccessSecurityAttribute):
    def __init__(self, action: SecurityAction): ...
    def CreatePermission(self) -> IPermission: ...
    @property
    def Audio(self) -> MediaPermissionAudio: ...
    @property
    def Image(self) -> MediaPermissionImage: ...
    @property
    def Video(self) -> MediaPermissionVideo: ...
    @Audio.setter
    def Audio(self, value: MediaPermissionAudio) -> None: ...
    @Image.setter
    def Image(self, value: MediaPermissionImage) -> None: ...
    @Video.setter
    def Video(self, value: MediaPermissionVideo) -> None: ...


class MediaPermissionAudio:
    NoAudio = 0
    SiteOfOriginAudio = 1
    SafeAudio = 2
    AllAudio = 3


class MediaPermissionImage:
    NoImage = 0
    SiteOfOriginImage = 1
    SafeImage = 2
    AllImage = 3


class MediaPermissionVideo:
    NoVideo = 0
    SiteOfOriginVideo = 1
    SafeVideo = 2
    AllVideo = 3


class PermissionSetAttribute(CodeAccessSecurityAttribute):
    def __init__(self, action: SecurityAction): ...
    def CreatePermission(self) -> IPermission: ...
    def CreatePermissionSet(self) -> PermissionSet: ...
    @property
    def File(self) -> str: ...
    @property
    def Hex(self) -> str: ...
    @property
    def Name(self) -> str: ...
    @property
    def UnicodeEncoded(self) -> bool: ...
    @property
    def XML(self) -> str: ...
    @File.setter
    def File(self, value: str) -> None: ...
    @Hex.setter
    def Hex(self, value: str) -> None: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    @UnicodeEncoded.setter
    def UnicodeEncoded(self, value: bool) -> None: ...
    @XML.setter
    def XML(self, value: str) -> None: ...


class PrincipalPermission(Object):
    @overload
    def __init__(self, state: PermissionState): ...
    @overload
    def __init__(self, name: str, role: str): ...
    @overload
    def __init__(self, name: str, role: str, isAuthenticated: bool): ...
    def Copy(self) -> IPermission: ...
    def Demand(self) -> None: ...
    def Equals(self, obj: Object) -> bool: ...
    def FromXml(self, elem: SecurityElement) -> None: ...
    def GetHashCode(self) -> int: ...
    def Intersect(self, target: IPermission) -> IPermission: ...
    def IsSubsetOf(self, target: IPermission) -> bool: ...
    def IsUnrestricted(self) -> bool: ...
    def ToString(self) -> str: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, other: IPermission) -> IPermission: ...


class PrincipalPermissionAttribute(CodeAccessSecurityAttribute):
    def __init__(self, action: SecurityAction): ...
    def CreatePermission(self) -> IPermission: ...
    @property
    def Authenticated(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def Role(self) -> str: ...
    @Authenticated.setter
    def Authenticated(self, value: bool) -> None: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    @Role.setter
    def Role(self, value: str) -> None: ...


class PublisherIdentityPermission(CodeAccessPermission):
    @overload
    def __init__(self, certificate: X509Certificate): ...
    @overload
    def __init__(self, state: PermissionState): ...
    def Copy(self) -> IPermission: ...
    def FromXml(self, esd: SecurityElement) -> None: ...
    @property
    def Certificate(self) -> X509Certificate: ...
    def Intersect(self, target: IPermission) -> IPermission: ...
    def IsSubsetOf(self, target: IPermission) -> bool: ...
    @Certificate.setter
    def Certificate(self, value: X509Certificate) -> None: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, target: IPermission) -> IPermission: ...


class PublisherIdentityPermissionAttribute(CodeAccessSecurityAttribute):
    def __init__(self, action: SecurityAction): ...
    def CreatePermission(self) -> IPermission: ...
    @property
    def CertFile(self) -> str: ...
    @property
    def SignedFile(self) -> str: ...
    @property
    def X509Certificate(self) -> str: ...
    @CertFile.setter
    def CertFile(self, value: str) -> None: ...
    @SignedFile.setter
    def SignedFile(self, value: str) -> None: ...
    @X509Certificate.setter
    def X509Certificate(self, value: str) -> None: ...


class ReflectionPermission(CodeAccessPermission):
    @overload
    def __init__(self, state: PermissionState): ...
    @overload
    def __init__(self, flag: ReflectionPermissionFlag): ...
    def Copy(self) -> IPermission: ...
    def FromXml(self, esd: SecurityElement) -> None: ...
    @property
    def Flags(self) -> ReflectionPermissionFlag: ...
    def Intersect(self, target: IPermission) -> IPermission: ...
    def IsSubsetOf(self, target: IPermission) -> bool: ...
    def IsUnrestricted(self) -> bool: ...
    @Flags.setter
    def Flags(self, value: ReflectionPermissionFlag) -> None: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, other: IPermission) -> IPermission: ...


class ReflectionPermissionAttribute(CodeAccessSecurityAttribute):
    def __init__(self, action: SecurityAction): ...
    def CreatePermission(self) -> IPermission: ...
    @property
    def Flags(self) -> ReflectionPermissionFlag: ...
    @property
    def MemberAccess(self) -> bool: ...
    @property
    def ReflectionEmit(self) -> bool: ...
    @property
    def RestrictedMemberAccess(self) -> bool: ...
    @property
    def TypeInformation(self) -> bool: ...
    @Flags.setter
    def Flags(self, value: ReflectionPermissionFlag) -> None: ...
    @MemberAccess.setter
    def MemberAccess(self, value: bool) -> None: ...
    @ReflectionEmit.setter
    def ReflectionEmit(self, value: bool) -> None: ...
    @RestrictedMemberAccess.setter
    def RestrictedMemberAccess(self, value: bool) -> None: ...
    @TypeInformation.setter
    def TypeInformation(self, value: bool) -> None: ...


class ReflectionPermissionFlag:
    NoFlags = 0
    TypeInformation = 1
    MemberAccess = 2
    ReflectionEmit = 4
    AllFlags = 7
    RestrictedMemberAccess = 8


class RegistryPermission(CodeAccessPermission):
    @overload
    def __init__(self, state: PermissionState): ...
    @overload
    def __init__(self, access: RegistryPermissionAccess, pathList: str): ...
    @overload
    def __init__(self, access: RegistryPermissionAccess, control: AccessControlActions, pathList: str): ...
    @overload
    def AddPathList(self, access: RegistryPermissionAccess, pathList: str) -> None: ...
    @overload
    def AddPathList(self, access: RegistryPermissionAccess, actions: AccessControlActions, pathList: str) -> None: ...
    def Copy(self) -> IPermission: ...
    def FromXml(self, elem: SecurityElement) -> None: ...
    def GetPathList(self, access: RegistryPermissionAccess) -> str: ...
    def Intersect(self, target: IPermission) -> IPermission: ...
    def IsSubsetOf(self, target: IPermission) -> bool: ...
    def IsUnrestricted(self) -> bool: ...
    def SetPathList(self, access: RegistryPermissionAccess, pathList: str) -> None: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, other: IPermission) -> IPermission: ...


class RegistryPermissionAccess:
    NoAccess = 0
    Read = 1
    Write = 2
    Create = 4
    AllAccess = 7


class RegistryPermissionAttribute(CodeAccessSecurityAttribute):
    def __init__(self, action: SecurityAction): ...
    def CreatePermission(self) -> IPermission: ...
    @property
    def All(self) -> str: ...
    @property
    def ChangeAccessControl(self) -> str: ...
    @property
    def Create(self) -> str: ...
    @property
    def Read(self) -> str: ...
    @property
    def ViewAccessControl(self) -> str: ...
    @property
    def ViewAndModify(self) -> str: ...
    @property
    def Write(self) -> str: ...
    @All.setter
    def All(self, value: str) -> None: ...
    @ChangeAccessControl.setter
    def ChangeAccessControl(self, value: str) -> None: ...
    @Create.setter
    def Create(self, value: str) -> None: ...
    @Read.setter
    def Read(self, value: str) -> None: ...
    @ViewAccessControl.setter
    def ViewAccessControl(self, value: str) -> None: ...
    @ViewAndModify.setter
    def ViewAndModify(self, value: str) -> None: ...
    @Write.setter
    def Write(self, value: str) -> None: ...


class ResourcePermissionBase(CodeAccessPermission):
    def Copy(self) -> IPermission: ...
    def FromXml(self, securityElement: SecurityElement) -> None: ...
    def Intersect(self, target: IPermission) -> IPermission: ...
    def IsSubsetOf(self, target: IPermission) -> bool: ...
    def IsUnrestricted(self) -> bool: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, target: IPermission) -> IPermission: ...


class ResourcePermissionBaseEntry(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, permissionAccess: int, permissionAccessPath: Set(str)): ...
    @property
    def PermissionAccess(self) -> int: ...
    @property
    def PermissionAccessPath(self) -> Set(str): ...


class SecurityPermission(CodeAccessPermission):
    @overload
    def __init__(self, state: PermissionState): ...
    @overload
    def __init__(self, flag: SecurityPermissionFlag): ...
    def Copy(self) -> IPermission: ...
    def FromXml(self, esd: SecurityElement) -> None: ...
    @property
    def Flags(self) -> SecurityPermissionFlag: ...
    def Intersect(self, target: IPermission) -> IPermission: ...
    def IsSubsetOf(self, target: IPermission) -> bool: ...
    def IsUnrestricted(self) -> bool: ...
    @Flags.setter
    def Flags(self, value: SecurityPermissionFlag) -> None: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, target: IPermission) -> IPermission: ...


class SiteIdentityPermission(CodeAccessPermission):
    @overload
    def __init__(self, state: PermissionState): ...
    @overload
    def __init__(self, site: str): ...
    def Copy(self) -> IPermission: ...
    def FromXml(self, esd: SecurityElement) -> None: ...
    @property
    def Site(self) -> str: ...
    def Intersect(self, target: IPermission) -> IPermission: ...
    def IsSubsetOf(self, target: IPermission) -> bool: ...
    @Site.setter
    def Site(self, value: str) -> None: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, target: IPermission) -> IPermission: ...


class SiteIdentityPermissionAttribute(CodeAccessSecurityAttribute):
    def __init__(self, action: SecurityAction): ...
    def CreatePermission(self) -> IPermission: ...
    @property
    def Site(self) -> str: ...
    @Site.setter
    def Site(self, value: str) -> None: ...


class StorePermission(CodeAccessPermission):
    @overload
    def __init__(self, state: PermissionState): ...
    @overload
    def __init__(self, flag: StorePermissionFlags): ...
    def Copy(self) -> IPermission: ...
    def FromXml(self, securityElement: SecurityElement) -> None: ...
    @property
    def Flags(self) -> StorePermissionFlags: ...
    def Intersect(self, target: IPermission) -> IPermission: ...
    def IsSubsetOf(self, target: IPermission) -> bool: ...
    def IsUnrestricted(self) -> bool: ...
    @Flags.setter
    def Flags(self, value: StorePermissionFlags) -> None: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, target: IPermission) -> IPermission: ...


class StorePermissionAttribute(CodeAccessSecurityAttribute):
    def __init__(self, action: SecurityAction): ...
    def CreatePermission(self) -> IPermission: ...
    @property
    def AddToStore(self) -> bool: ...
    @property
    def CreateStore(self) -> bool: ...
    @property
    def DeleteStore(self) -> bool: ...
    @property
    def EnumerateCertificates(self) -> bool: ...
    @property
    def EnumerateStores(self) -> bool: ...
    @property
    def Flags(self) -> StorePermissionFlags: ...
    @property
    def OpenStore(self) -> bool: ...
    @property
    def RemoveFromStore(self) -> bool: ...
    @AddToStore.setter
    def AddToStore(self, value: bool) -> None: ...
    @CreateStore.setter
    def CreateStore(self, value: bool) -> None: ...
    @DeleteStore.setter
    def DeleteStore(self, value: bool) -> None: ...
    @EnumerateCertificates.setter
    def EnumerateCertificates(self, value: bool) -> None: ...
    @EnumerateStores.setter
    def EnumerateStores(self, value: bool) -> None: ...
    @Flags.setter
    def Flags(self, value: StorePermissionFlags) -> None: ...
    @OpenStore.setter
    def OpenStore(self, value: bool) -> None: ...
    @RemoveFromStore.setter
    def RemoveFromStore(self, value: bool) -> None: ...


class StorePermissionFlags:
    NoFlags = 0
    CreateStore = 1
    DeleteStore = 2
    EnumerateStores = 4
    OpenStore = 16
    AddToStore = 32
    RemoveFromStore = 64
    EnumerateCertificates = 128
    AllFlags = 247


class StrongNameIdentityPermission(CodeAccessPermission):
    @overload
    def __init__(self, state: PermissionState): ...
    @overload
    def __init__(self, blob: StrongNamePublicKeyBlob, name: str, version: Version): ...
    def Copy(self) -> IPermission: ...
    def FromXml(self, e: SecurityElement) -> None: ...
    @property
    def Name(self) -> str: ...
    @property
    def PublicKey(self) -> StrongNamePublicKeyBlob: ...
    @property
    def Version(self) -> Version: ...
    def Intersect(self, target: IPermission) -> IPermission: ...
    def IsSubsetOf(self, target: IPermission) -> bool: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    @PublicKey.setter
    def PublicKey(self, value: StrongNamePublicKeyBlob) -> None: ...
    @Version.setter
    def Version(self, value: Version) -> None: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, target: IPermission) -> IPermission: ...


class StrongNameIdentityPermissionAttribute(CodeAccessSecurityAttribute):
    def __init__(self, action: SecurityAction): ...
    def CreatePermission(self) -> IPermission: ...
    @property
    def Name(self) -> str: ...
    @property
    def PublicKey(self) -> str: ...
    @property
    def Version(self) -> str: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    @PublicKey.setter
    def PublicKey(self, value: str) -> None: ...
    @Version.setter
    def Version(self, value: str) -> None: ...


class StrongNamePublicKeyBlob(Object):
    def __init__(self, publicKey: Set(Byte)): ...
    def Equals(self, o: Object) -> bool: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...


class TypeDescriptorPermission(CodeAccessPermission):
    @overload
    def __init__(self, state: PermissionState): ...
    @overload
    def __init__(self, flag: TypeDescriptorPermissionFlags): ...
    def Copy(self) -> IPermission: ...
    def FromXml(self, securityElement: SecurityElement) -> None: ...
    @property
    def Flags(self) -> TypeDescriptorPermissionFlags: ...
    def Intersect(self, target: IPermission) -> IPermission: ...
    def IsSubsetOf(self, target: IPermission) -> bool: ...
    def IsUnrestricted(self) -> bool: ...
    @Flags.setter
    def Flags(self, value: TypeDescriptorPermissionFlags) -> None: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, target: IPermission) -> IPermission: ...


class TypeDescriptorPermissionAttribute(CodeAccessSecurityAttribute):
    def __init__(self, action: SecurityAction): ...
    def CreatePermission(self) -> IPermission: ...
    @property
    def Flags(self) -> TypeDescriptorPermissionFlags: ...
    @property
    def RestrictedRegistrationAccess(self) -> bool: ...
    @Flags.setter
    def Flags(self, value: TypeDescriptorPermissionFlags) -> None: ...
    @RestrictedRegistrationAccess.setter
    def RestrictedRegistrationAccess(self, value: bool) -> None: ...


class TypeDescriptorPermissionFlags:
    NoFlags = 0
    RestrictedRegistrationAccess = 1


class UIPermission(CodeAccessPermission):
    @overload
    def __init__(self, state: PermissionState): ...
    @overload
    def __init__(self, clipboardFlag: UIPermissionClipboard): ...
    @overload
    def __init__(self, windowFlag: UIPermissionWindow): ...
    @overload
    def __init__(self, windowFlag: UIPermissionWindow, clipboardFlag: UIPermissionClipboard): ...
    def Copy(self) -> IPermission: ...
    def FromXml(self, esd: SecurityElement) -> None: ...
    @property
    def Clipboard(self) -> UIPermissionClipboard: ...
    @property
    def Window(self) -> UIPermissionWindow: ...
    def Intersect(self, target: IPermission) -> IPermission: ...
    def IsSubsetOf(self, target: IPermission) -> bool: ...
    def IsUnrestricted(self) -> bool: ...
    @Clipboard.setter
    def Clipboard(self, value: UIPermissionClipboard) -> None: ...
    @Window.setter
    def Window(self, value: UIPermissionWindow) -> None: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, target: IPermission) -> IPermission: ...


class UIPermissionAttribute(CodeAccessSecurityAttribute):
    def __init__(self, action: SecurityAction): ...
    def CreatePermission(self) -> IPermission: ...
    @property
    def Clipboard(self) -> UIPermissionClipboard: ...
    @property
    def Window(self) -> UIPermissionWindow: ...
    @Clipboard.setter
    def Clipboard(self, value: UIPermissionClipboard) -> None: ...
    @Window.setter
    def Window(self, value: UIPermissionWindow) -> None: ...


class UIPermissionClipboard:
    NoClipboard = 0
    OwnClipboard = 1
    AllClipboard = 2


class UIPermissionWindow:
    NoWindows = 0
    SafeSubWindows = 1
    SafeTopLevelWindows = 2
    AllWindows = 3


class UrlIdentityPermission(CodeAccessPermission):
    @overload
    def __init__(self, state: PermissionState): ...
    @overload
    def __init__(self, site: str): ...
    def Copy(self) -> IPermission: ...
    def FromXml(self, esd: SecurityElement) -> None: ...
    @property
    def Url(self) -> str: ...
    def Intersect(self, target: IPermission) -> IPermission: ...
    def IsSubsetOf(self, target: IPermission) -> bool: ...
    @Url.setter
    def Url(self, value: str) -> None: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, target: IPermission) -> IPermission: ...


class UrlIdentityPermissionAttribute(CodeAccessSecurityAttribute):
    def __init__(self, action: SecurityAction): ...
    def CreatePermission(self) -> IPermission: ...
    @property
    def Url(self) -> str: ...
    @Url.setter
    def Url(self, value: str) -> None: ...


class WebBrowserPermission(CodeAccessPermission):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, state: PermissionState): ...
    @overload
    def __init__(self, webBrowserPermissionLevel: WebBrowserPermissionLevel): ...
    def Copy(self) -> IPermission: ...
    def FromXml(self, securityElement: SecurityElement) -> None: ...
    @property
    def Level(self) -> WebBrowserPermissionLevel: ...
    def Intersect(self, target: IPermission) -> IPermission: ...
    def IsSubsetOf(self, target: IPermission) -> bool: ...
    def IsUnrestricted(self) -> bool: ...
    @Level.setter
    def Level(self, value: WebBrowserPermissionLevel) -> None: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, target: IPermission) -> IPermission: ...


class WebBrowserPermissionAttribute(CodeAccessSecurityAttribute):
    def __init__(self, action: SecurityAction): ...
    def CreatePermission(self) -> IPermission: ...
    @property
    def Level(self) -> WebBrowserPermissionLevel: ...
    @Level.setter
    def Level(self, value: WebBrowserPermissionLevel) -> None: ...


class WebBrowserPermissionLevel:
    #None = 0
    Safe = 1
    Unrestricted = 2


class ZoneIdentityPermission(CodeAccessPermission):
    @overload
    def __init__(self, state: PermissionState): ...
    @overload
    def __init__(self, zone: SecurityZone): ...
    def Copy(self) -> IPermission: ...
    def FromXml(self, esd: SecurityElement) -> None: ...
    @property
    def SecurityZone(self) -> SecurityZone: ...
    def Intersect(self, target: IPermission) -> IPermission: ...
    def IsSubsetOf(self, target: IPermission) -> bool: ...
    @SecurityZone.setter
    def SecurityZone(self, value: SecurityZone) -> None: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, target: IPermission) -> IPermission: ...


class ZoneIdentityPermissionAttribute(CodeAccessSecurityAttribute):
    def __init__(self, action: SecurityAction): ...
    def CreatePermission(self) -> IPermission: ...
    @property
    def Zone(self) -> SecurityZone: ...
    @Zone.setter
    def Zone(self, value: SecurityZone) -> None: ...
