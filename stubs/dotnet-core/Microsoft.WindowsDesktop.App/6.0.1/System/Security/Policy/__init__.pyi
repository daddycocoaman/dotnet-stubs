from typing import Tuple, Set, Iterable, List


class AllMembershipCondition(Object):
    def __init__(self): ...
    def Check(self, evidence: Evidence) -> bool: ...
    def Copy(self) -> IMembershipCondition: ...
    def Equals(self, o: Object) -> bool: ...
    @overload
    def FromXml(self, e: SecurityElement) -> None: ...
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...
    @overload
    def ToXml(self) -> SecurityElement: ...
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...


class ApplicationDirectory(EvidenceBase):
    def __init__(self, name: str): ...
    def Copy(self) -> Object: ...
    def Equals(self, o: Object) -> bool: ...
    @property
    def Directory(self) -> str: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...


class ApplicationDirectoryMembershipCondition(Object):
    def __init__(self): ...
    def Check(self, evidence: Evidence) -> bool: ...
    def Copy(self) -> IMembershipCondition: ...
    def Equals(self, o: Object) -> bool: ...
    @overload
    def FromXml(self, e: SecurityElement) -> None: ...
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...
    @overload
    def ToXml(self) -> SecurityElement: ...
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...


class ApplicationTrust(EvidenceBase):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, identity: ApplicationIdentity): ...
    @overload
    def __init__(self, defaultGrantSet: PermissionSet, fullTrustAssemblies: Iterable[StrongName]): ...
    def FromXml(self, element: SecurityElement) -> None: ...
    @property
    def ApplicationIdentity(self) -> ApplicationIdentity: ...
    @property
    def DefaultGrantSet(self) -> PolicyStatement: ...
    @property
    def ExtraInfo(self) -> Object: ...
    @property
    def FullTrustAssemblies(self) -> List[StrongName]: ...
    @property
    def IsApplicationTrustedToRun(self) -> bool: ...
    @property
    def Persist(self) -> bool: ...
    @ApplicationIdentity.setter
    def ApplicationIdentity(self, value: ApplicationIdentity) -> None: ...
    @DefaultGrantSet.setter
    def DefaultGrantSet(self, value: PolicyStatement) -> None: ...
    @ExtraInfo.setter
    def ExtraInfo(self, value: Object) -> None: ...
    @IsApplicationTrustedToRun.setter
    def IsApplicationTrustedToRun(self, value: bool) -> None: ...
    @Persist.setter
    def Persist(self, value: bool) -> None: ...
    def ToXml(self) -> SecurityElement: ...


class ApplicationTrustCollection(Object):
    def Add(self, trust: ApplicationTrust) -> int: ...
    @overload
    def AddRange(self, trusts: ApplicationTrustCollection) -> None: ...
    @overload
    def AddRange(self, trusts: Set(ApplicationTrust)) -> None: ...
    def Clear(self) -> None: ...
    def CopyTo(self, array: Set(ApplicationTrust), index: int) -> None: ...
    def Find(self, applicationIdentity: ApplicationIdentity, versionMatch: ApplicationVersionMatch) -> ApplicationTrustCollection: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsSynchronized(self) -> bool: ...
    @property
    def Item(self, appFullName: str) -> ApplicationTrust: ...
    @property
    def Item(self, index: int) -> ApplicationTrust: ...
    @property
    def SyncRoot(self) -> Object: ...
    def GetEnumerator(self) -> ApplicationTrustEnumerator: ...
    @overload
    def Remove(self, trust: ApplicationTrust) -> None: ...
    @overload
    def Remove(self, applicationIdentity: ApplicationIdentity, versionMatch: ApplicationVersionMatch) -> None: ...
    @overload
    def RemoveRange(self, trusts: Set(ApplicationTrust)) -> None: ...
    @overload
    def RemoveRange(self, trusts: ApplicationTrustCollection) -> None: ...


class ApplicationTrustEnumerator(Object):
    @property
    def Current(self) -> ApplicationTrust: ...
    def MoveNext(self) -> bool: ...
    def Reset(self) -> None: ...


class ApplicationVersionMatch:
    MatchExactVersion = 0
    MatchAllVersions = 1


class CodeConnectAccess(Object):
    def __init__(self, allowScheme: str, allowPort: int): ...
    def CreateAnySchemeAccess(allowPort: int) -> CodeConnectAccess: ...
    def CreateOriginSchemeAccess(allowPort: int) -> CodeConnectAccess: ...
    def Equals(self, o: Object) -> bool: ...
    @property
    def Port(self) -> int: ...
    @property
    def Scheme(self) -> str: ...
    def GetHashCode(self) -> int: ...


class CodeGroup(Object):
    def AddChild(self, group: CodeGroup) -> None: ...
    def Copy(self) -> CodeGroup: ...
    @overload
    def Equals(self, o: Object) -> bool: ...
    @overload
    def Equals(self, cg: CodeGroup, compareChildren: bool) -> bool: ...
    @overload
    def FromXml(self, e: SecurityElement) -> None: ...
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None: ...
    @property
    def AttributeString(self) -> str: ...
    @property
    def Children(self) -> IList: ...
    @property
    def Description(self) -> str: ...
    @property
    def MembershipCondition(self) -> IMembershipCondition: ...
    @property
    def MergeLogic(self) -> str: ...
    @property
    def Name(self) -> str: ...
    @property
    def PermissionSetName(self) -> str: ...
    @property
    def PolicyStatement(self) -> PolicyStatement: ...
    def GetHashCode(self) -> int: ...
    def RemoveChild(self, group: CodeGroup) -> None: ...
    def Resolve(self, evidence: Evidence) -> PolicyStatement: ...
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup: ...
    @Children.setter
    def Children(self, value: IList) -> None: ...
    @Description.setter
    def Description(self, value: str) -> None: ...
    @MembershipCondition.setter
    def MembershipCondition(self, value: IMembershipCondition) -> None: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    @PolicyStatement.setter
    def PolicyStatement(self, value: PolicyStatement) -> None: ...
    @overload
    def ToXml(self) -> SecurityElement: ...
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...


class GacMembershipCondition(Object):
    def __init__(self): ...
    def Check(self, evidence: Evidence) -> bool: ...
    def Copy(self) -> IMembershipCondition: ...
    def Equals(self, o: Object) -> bool: ...
    @overload
    def FromXml(self, e: SecurityElement) -> None: ...
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...
    @overload
    def ToXml(self) -> SecurityElement: ...
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...


class Hash(EvidenceBase):
    def __init__(self, assembly: Assembly): ...
    def CreateMD5(md5: Set(Byte)) -> Hash: ...
    def CreateSHA1(sha1: Set(Byte)) -> Hash: ...
    def CreateSHA256(sha256: Set(Byte)) -> Hash: ...
    def GenerateHash(self, hashAlg: HashAlgorithm) -> Set(Byte): ...
    @property
    def MD5(self) -> Set(Byte): ...
    @property
    def SHA1(self) -> Set(Byte): ...
    @property
    def SHA256(self) -> Set(Byte): ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...
    def ToString(self) -> str: ...


class HashMembershipCondition(Object):
    def __init__(self, hashAlg: HashAlgorithm, value: Set(Byte)): ...
    def Check(self, evidence: Evidence) -> bool: ...
    def Copy(self) -> IMembershipCondition: ...
    def Equals(self, o: Object) -> bool: ...
    @overload
    def FromXml(self, e: SecurityElement) -> None: ...
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None: ...
    @property
    def HashAlgorithm(self) -> HashAlgorithm: ...
    @property
    def HashValue(self) -> Set(Byte): ...
    def GetHashCode(self) -> int: ...
    @HashAlgorithm.setter
    def HashAlgorithm(self, value: HashAlgorithm) -> None: ...
    @HashValue.setter
    def HashValue(self, value: Set(Byte)) -> None: ...
    def ToString(self) -> str: ...
    @overload
    def ToXml(self) -> SecurityElement: ...
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...


class IMembershipCondition:
    def Check(self, evidence: Evidence) -> bool: ...
    def Copy(self) -> IMembershipCondition: ...
    def Equals(self, obj: Object) -> bool: ...
    def ToString(self) -> str: ...


class NetCodeGroup(CodeGroup):
    def __init__(self, membershipCondition: IMembershipCondition): ...
    def AddConnectAccess(self, originScheme: str, connectAccess: CodeConnectAccess) -> None: ...
    def Copy(self) -> CodeGroup: ...
    @overload
    def Equals(self, o: Object) -> bool: ...
    @property
    def AttributeString(self) -> str: ...
    @property
    def MergeLogic(self) -> str: ...
    @property
    def PermissionSetName(self) -> str: ...
    def GetConnectAccessRules(self) -> Set(DictionaryEntry): ...
    def GetHashCode(self) -> int: ...
    def ResetConnectAccess(self) -> None: ...
    def Resolve(self, evidence: Evidence) -> PolicyStatement: ...
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup: ...


class PolicyException(SystemException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, exception: Exception): ...


class PolicyLevel(Object):
    def FromXml(self, e: SecurityElement) -> None: ...
    @property
    def FullTrustAssemblies(self) -> IList: ...
    @property
    def Label(self) -> str: ...
    @property
    def NamedPermissionSets(self) -> IList: ...
    @property
    def RootCodeGroup(self) -> CodeGroup: ...
    @property
    def StoreLocation(self) -> str: ...
    @property
    def Type(self) -> PolicyLevelType: ...
    def Recover(self) -> None: ...
    def Reset(self) -> None: ...
    def Resolve(self, evidence: Evidence) -> PolicyStatement: ...
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup: ...
    @RootCodeGroup.setter
    def RootCodeGroup(self, value: CodeGroup) -> None: ...
    def ToXml(self) -> SecurityElement: ...


class PolicyStatement(Object):
    @overload
    def __init__(self, permSet: PermissionSet): ...
    @overload
    def __init__(self, permSet: PermissionSet, attributes: PolicyStatementAttribute): ...
    def Copy(self) -> PolicyStatement: ...
    def Equals(self, o: Object) -> bool: ...
    @overload
    def FromXml(self, et: SecurityElement) -> None: ...
    @overload
    def FromXml(self, et: SecurityElement, level: PolicyLevel) -> None: ...
    @property
    def Attributes(self) -> PolicyStatementAttribute: ...
    @property
    def AttributeString(self) -> str: ...
    @property
    def PermissionSet(self) -> PermissionSet: ...
    def GetHashCode(self) -> int: ...
    @Attributes.setter
    def Attributes(self, value: PolicyStatementAttribute) -> None: ...
    @PermissionSet.setter
    def PermissionSet(self, value: PermissionSet) -> None: ...
    @overload
    def ToXml(self) -> SecurityElement: ...
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...


class PolicyStatementAttribute:
    Nothing = 0
    Exclusive = 1
    LevelFinal = 2
    All = 3


class PublisherMembershipCondition(Object):
    def __init__(self, certificate: X509Certificate): ...
    def Check(self, evidence: Evidence) -> bool: ...
    def Copy(self) -> IMembershipCondition: ...
    def Equals(self, o: Object) -> bool: ...
    @overload
    def FromXml(self, e: SecurityElement) -> None: ...
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None: ...
    @property
    def Certificate(self) -> X509Certificate: ...
    def GetHashCode(self) -> int: ...
    @Certificate.setter
    def Certificate(self, value: X509Certificate) -> None: ...
    def ToString(self) -> str: ...
    @overload
    def ToXml(self) -> SecurityElement: ...
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...


class SiteMembershipCondition(Object):
    def __init__(self, site: str): ...
    def Check(self, evidence: Evidence) -> bool: ...
    def Copy(self) -> IMembershipCondition: ...
    def Equals(self, o: Object) -> bool: ...
    @overload
    def FromXml(self, e: SecurityElement) -> None: ...
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None: ...
    @property
    def Site(self) -> str: ...
    def GetHashCode(self) -> int: ...
    @Site.setter
    def Site(self, value: str) -> None: ...
    def ToString(self) -> str: ...
    @overload
    def ToXml(self) -> SecurityElement: ...
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...


class TrustManagerContext(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, uiContext: TrustManagerUIContext): ...
    @property
    def IgnorePersistedDecision(self) -> bool: ...
    @property
    def KeepAlive(self) -> bool: ...
    @property
    def NoPrompt(self) -> bool: ...
    @property
    def Persist(self) -> bool: ...
    @property
    def PreviousApplicationIdentity(self) -> ApplicationIdentity: ...
    @property
    def UIContext(self) -> TrustManagerUIContext: ...
    @IgnorePersistedDecision.setter
    def IgnorePersistedDecision(self, value: bool) -> None: ...
    @KeepAlive.setter
    def KeepAlive(self, value: bool) -> None: ...
    @NoPrompt.setter
    def NoPrompt(self, value: bool) -> None: ...
    @Persist.setter
    def Persist(self, value: bool) -> None: ...
    @PreviousApplicationIdentity.setter
    def PreviousApplicationIdentity(self, value: ApplicationIdentity) -> None: ...
    @UIContext.setter
    def UIContext(self, value: TrustManagerUIContext) -> None: ...


class TrustManagerUIContext:
    Install = 0
    Upgrade = 1
    Run = 2


class UrlMembershipCondition(Object):
    def __init__(self, url: str): ...
    def Check(self, evidence: Evidence) -> bool: ...
    def Copy(self) -> IMembershipCondition: ...
    def Equals(self, obj: Object) -> bool: ...
    @overload
    def FromXml(self, e: SecurityElement) -> None: ...
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None: ...
    @property
    def Url(self) -> str: ...
    def GetHashCode(self) -> int: ...
    @Url.setter
    def Url(self, value: str) -> None: ...
    def ToString(self) -> str: ...
    @overload
    def ToXml(self) -> SecurityElement: ...
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...


class ZoneMembershipCondition(Object):
    def __init__(self, zone: SecurityZone): ...
    def Check(self, evidence: Evidence) -> bool: ...
    def Copy(self) -> IMembershipCondition: ...
    def Equals(self, o: Object) -> bool: ...
    @overload
    def FromXml(self, e: SecurityElement) -> None: ...
    @overload
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None: ...
    @property
    def SecurityZone(self) -> SecurityZone: ...
    def GetHashCode(self) -> int: ...
    @SecurityZone.setter
    def SecurityZone(self, value: SecurityZone) -> None: ...
    def ToString(self) -> str: ...
    @overload
    def ToXml(self) -> SecurityElement: ...
    @overload
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...
