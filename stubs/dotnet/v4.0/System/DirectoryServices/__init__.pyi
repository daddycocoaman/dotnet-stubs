__all__ = ['ActiveDirectory']
from typing import Tuple, Set, Iterable, List


class ActiveDirectoryAccessRule(ObjectAccessRule):
    @overload
    def __init__(self, identity: IdentityReference, adRights: ActiveDirectoryRights, type: AccessControlType): ...
    @overload
    def __init__(self, identity: IdentityReference, adRights: ActiveDirectoryRights, type: AccessControlType, objectType: Guid): ...
    @overload
    def __init__(self, identity: IdentityReference, adRights: ActiveDirectoryRights, type: AccessControlType, inheritanceType: ActiveDirectorySecurityInheritance): ...
    @overload
    def __init__(self, identity: IdentityReference, adRights: ActiveDirectoryRights, type: AccessControlType, objectType: Guid, inheritanceType: ActiveDirectorySecurityInheritance): ...
    @overload
    def __init__(self, identity: IdentityReference, adRights: ActiveDirectoryRights, type: AccessControlType, inheritanceType: ActiveDirectorySecurityInheritance, inheritedObjectType: Guid): ...
    @overload
    def __init__(self, identity: IdentityReference, adRights: ActiveDirectoryRights, type: AccessControlType, objectType: Guid, inheritanceType: ActiveDirectorySecurityInheritance, inheritedObjectType: Guid): ...
    @property
    def ActiveDirectoryRights(self) -> ActiveDirectoryRights: ...
    @property
    def InheritanceType(self) -> ActiveDirectorySecurityInheritance: ...


class ActiveDirectoryAuditRule(ObjectAuditRule):
    @overload
    def __init__(self, identity: IdentityReference, adRights: ActiveDirectoryRights, auditFlags: AuditFlags): ...
    @overload
    def __init__(self, identity: IdentityReference, adRights: ActiveDirectoryRights, auditFlags: AuditFlags, objectType: Guid): ...
    @overload
    def __init__(self, identity: IdentityReference, adRights: ActiveDirectoryRights, auditFlags: AuditFlags, inheritanceType: ActiveDirectorySecurityInheritance): ...
    @overload
    def __init__(self, identity: IdentityReference, adRights: ActiveDirectoryRights, auditFlags: AuditFlags, objectType: Guid, inheritanceType: ActiveDirectorySecurityInheritance): ...
    @overload
    def __init__(self, identity: IdentityReference, adRights: ActiveDirectoryRights, auditFlags: AuditFlags, inheritanceType: ActiveDirectorySecurityInheritance, inheritedObjectType: Guid): ...
    @overload
    def __init__(self, identity: IdentityReference, adRights: ActiveDirectoryRights, auditFlags: AuditFlags, objectType: Guid, inheritanceType: ActiveDirectorySecurityInheritance, inheritedObjectType: Guid): ...
    @property
    def ActiveDirectoryRights(self) -> ActiveDirectoryRights: ...
    @property
    def InheritanceType(self) -> ActiveDirectorySecurityInheritance: ...


class ActiveDirectoryRights:
    CreateChild = 1
    DeleteChild = 2
    ListChildren = 4
    Self = 8
    ReadProperty = 16
    WriteProperty = 32
    DeleteTree = 64
    ListObject = 128
    ExtendedRight = 256
    Delete = 65536
    ReadControl = 131072
    GenericExecute = 131076
    GenericWrite = 131112
    GenericRead = 131220
    WriteDacl = 262144
    WriteOwner = 524288
    GenericAll = 983551
    Synchronize = 1048576
    AccessSystemSecurity = 16777216


class ActiveDirectorySecurity(DirectoryObjectSecurity):
    def __init__(self): ...
    @overload
    def AccessRuleFactory(self, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule: ...
    @overload
    def AccessRuleFactory(self, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType, objectGuid: Guid, inheritedObjectGuid: Guid) -> AccessRule: ...
    def AddAccessRule(self, rule: ActiveDirectoryAccessRule) -> None: ...
    def AddAuditRule(self, rule: ActiveDirectoryAuditRule) -> None: ...
    @overload
    def AuditRuleFactory(self, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule: ...
    @overload
    def AuditRuleFactory(self, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags, objectGuid: Guid, inheritedObjectGuid: Guid) -> AuditRule: ...
    @property
    def AccessRightType(self) -> Type: ...
    @property
    def AccessRuleType(self) -> Type: ...
    @property
    def AuditRuleType(self) -> Type: ...
    def ModifyAccessRule(self, modification: AccessControlModification, rule: AccessRule) -> Tuple[bool, bool]: ...
    def ModifyAuditRule(self, modification: AccessControlModification, rule: AuditRule) -> Tuple[bool, bool]: ...
    def PurgeAccessRules(self, identity: IdentityReference) -> None: ...
    def PurgeAuditRules(self, identity: IdentityReference) -> None: ...
    def RemoveAccess(self, identity: IdentityReference, type: AccessControlType) -> None: ...
    def RemoveAccessRule(self, rule: ActiveDirectoryAccessRule) -> bool: ...
    def RemoveAccessRuleSpecific(self, rule: ActiveDirectoryAccessRule) -> None: ...
    def RemoveAudit(self, identity: IdentityReference) -> None: ...
    def RemoveAuditRule(self, rule: ActiveDirectoryAuditRule) -> bool: ...
    def RemoveAuditRuleSpecific(self, rule: ActiveDirectoryAuditRule) -> None: ...
    def ResetAccessRule(self, rule: ActiveDirectoryAccessRule) -> None: ...
    def SetAccessRule(self, rule: ActiveDirectoryAccessRule) -> None: ...
    def SetAuditRule(self, rule: ActiveDirectoryAuditRule) -> None: ...


class ActiveDirectorySecurityInheritance:
    #None = 0
    All = 1
    Descendents = 2
    SelfAndChildren = 3
    Children = 4


class AuthenticationTypes:
    #None = 0
    Secure = 1
    Encryption = 2
    SecureSocketsLayer = 2
    ReadonlyServer = 4
    Anonymous = 16
    FastBind = 32
    Signing = 64
    Sealing = 128
    Delegation = 256
    ServerBind = 512


class CreateChildAccessRule(ActiveDirectoryAccessRule):
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType): ...
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType, childType: Guid): ...
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType, inheritanceType: ActiveDirectorySecurityInheritance): ...
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType, childType: Guid, inheritanceType: ActiveDirectorySecurityInheritance): ...
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType, inheritanceType: ActiveDirectorySecurityInheritance, inheritedObjectType: Guid): ...
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType, childType: Guid, inheritanceType: ActiveDirectorySecurityInheritance, inheritedObjectType: Guid): ...


class DeleteChildAccessRule(ActiveDirectoryAccessRule):
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType): ...
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType, childType: Guid): ...
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType, inheritanceType: ActiveDirectorySecurityInheritance): ...
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType, childType: Guid, inheritanceType: ActiveDirectorySecurityInheritance): ...
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType, inheritanceType: ActiveDirectorySecurityInheritance, inheritedObjectType: Guid): ...
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType, childType: Guid, inheritanceType: ActiveDirectorySecurityInheritance, inheritedObjectType: Guid): ...


class DeleteTreeAccessRule(ActiveDirectoryAccessRule):
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType): ...
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType, inheritanceType: ActiveDirectorySecurityInheritance): ...
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType, inheritanceType: ActiveDirectorySecurityInheritance, inheritedObjectType: Guid): ...


class DereferenceAlias:
    Never = 0
    InSearching = 1
    FindingBaseObject = 2
    Always = 3


class DirectoryEntries(Object):
    def Add(self, name: str, schemaClassName: str) -> DirectoryEntry: ...
    @overload
    def Find(self, name: str) -> DirectoryEntry: ...
    @overload
    def Find(self, name: str, schemaClassName: str) -> DirectoryEntry: ...
    @property
    def SchemaFilter(self) -> SchemaNameCollection: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def Remove(self, entry: DirectoryEntry) -> None: ...


class DirectoryEntry(Component):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, path: str): ...
    @overload
    def __init__(self, adsObject: Object): ...
    @overload
    def __init__(self, path: str, username: str, password: str): ...
    @overload
    def __init__(self, path: str, username: str, password: str, authenticationType: AuthenticationTypes): ...
    def Close(self) -> None: ...
    def CommitChanges(self) -> None: ...
    @overload
    def CopyTo(self, newParent: DirectoryEntry) -> DirectoryEntry: ...
    @overload
    def CopyTo(self, newParent: DirectoryEntry, newName: str) -> DirectoryEntry: ...
    def DeleteTree(self) -> None: ...
    def Exists(path: str) -> bool: ...
    @property
    def AuthenticationType(self) -> AuthenticationTypes: ...
    @property
    def Children(self) -> DirectoryEntries: ...
    @property
    def Guid(self) -> Guid: ...
    @property
    def Name(self) -> str: ...
    @property
    def NativeGuid(self) -> str: ...
    @property
    def NativeObject(self) -> Object: ...
    @property
    def ObjectSecurity(self) -> ActiveDirectorySecurity: ...
    @property
    def Options(self) -> DirectoryEntryConfiguration: ...
    @property
    def Parent(self) -> DirectoryEntry: ...
    @property
    def Path(self) -> str: ...
    @property
    def Properties(self) -> PropertyCollection: ...
    @property
    def SchemaClassName(self) -> str: ...
    @property
    def SchemaEntry(self) -> DirectoryEntry: ...
    @property
    def UsePropertyCache(self) -> bool: ...
    @property
    def Username(self) -> str: ...
    def Invoke(self, methodName: str, args: Set(Object)) -> Object: ...
    def InvokeGet(self, propertyName: str) -> Object: ...
    def InvokeSet(self, propertyName: str, args: Set(Object)) -> None: ...
    @overload
    def MoveTo(self, newParent: DirectoryEntry) -> None: ...
    @overload
    def MoveTo(self, newParent: DirectoryEntry, newName: str) -> None: ...
    @overload
    def RefreshCache(self) -> None: ...
    @overload
    def RefreshCache(self, propertyNames: Set(str)) -> None: ...
    def Rename(self, newName: str) -> None: ...
    @AuthenticationType.setter
    def AuthenticationType(self, value: AuthenticationTypes) -> None: ...
    @ObjectSecurity.setter
    def ObjectSecurity(self, value: ActiveDirectorySecurity) -> None: ...
    @Password.setter
    def Password(self, value: str) -> None: ...
    @Path.setter
    def Path(self, value: str) -> None: ...
    @UsePropertyCache.setter
    def UsePropertyCache(self, value: bool) -> None: ...
    @Username.setter
    def Username(self, value: str) -> None: ...


class DirectoryEntryConfiguration(Object):
    @property
    def PageSize(self) -> int: ...
    @property
    def PasswordEncoding(self) -> PasswordEncodingMethod: ...
    @property
    def PasswordPort(self) -> int: ...
    @property
    def Referral(self) -> ReferralChasingOption: ...
    @property
    def SecurityMasks(self) -> SecurityMasks: ...
    def GetCurrentServerName(self) -> str: ...
    def IsMutuallyAuthenticated(self) -> bool: ...
    @PageSize.setter
    def PageSize(self, value: int) -> None: ...
    @PasswordEncoding.setter
    def PasswordEncoding(self, value: PasswordEncodingMethod) -> None: ...
    @PasswordPort.setter
    def PasswordPort(self, value: int) -> None: ...
    @Referral.setter
    def Referral(self, value: ReferralChasingOption) -> None: ...
    @SecurityMasks.setter
    def SecurityMasks(self, value: SecurityMasks) -> None: ...
    def SetUserNameQueryQuota(self, accountName: str) -> None: ...


class DirectorySearcher(Component):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, searchRoot: DirectoryEntry): ...
    @overload
    def __init__(self, filter: str): ...
    @overload
    def __init__(self, searchRoot: DirectoryEntry, filter: str): ...
    @overload
    def __init__(self, filter: str, propertiesToLoad: Set(str)): ...
    @overload
    def __init__(self, searchRoot: DirectoryEntry, filter: str, propertiesToLoad: Set(str)): ...
    @overload
    def __init__(self, filter: str, propertiesToLoad: Set(str), scope: SearchScope): ...
    @overload
    def __init__(self, searchRoot: DirectoryEntry, filter: str, propertiesToLoad: Set(str), scope: SearchScope): ...
    def FindAll(self) -> SearchResultCollection: ...
    def FindOne(self) -> SearchResult: ...
    @property
    def Asynchronous(self) -> bool: ...
    @property
    def AttributeScopeQuery(self) -> str: ...
    @property
    def CacheResults(self) -> bool: ...
    @property
    def ClientTimeout(self) -> TimeSpan: ...
    @property
    def DerefAlias(self) -> DereferenceAlias: ...
    @property
    def DirectorySynchronization(self) -> DirectorySynchronization: ...
    @property
    def ExtendedDN(self) -> ExtendedDN: ...
    @property
    def Filter(self) -> str: ...
    @property
    def PageSize(self) -> int: ...
    @property
    def PropertiesToLoad(self) -> StringCollection: ...
    @property
    def PropertyNamesOnly(self) -> bool: ...
    @property
    def ReferralChasing(self) -> ReferralChasingOption: ...
    @property
    def SearchRoot(self) -> DirectoryEntry: ...
    @property
    def SearchScope(self) -> SearchScope: ...
    @property
    def SecurityMasks(self) -> SecurityMasks: ...
    @property
    def ServerPageTimeLimit(self) -> TimeSpan: ...
    @property
    def ServerTimeLimit(self) -> TimeSpan: ...
    @property
    def SizeLimit(self) -> int: ...
    @property
    def Sort(self) -> SortOption: ...
    @property
    def Tombstone(self) -> bool: ...
    @property
    def VirtualListView(self) -> DirectoryVirtualListView: ...
    @Asynchronous.setter
    def Asynchronous(self, value: bool) -> None: ...
    @AttributeScopeQuery.setter
    def AttributeScopeQuery(self, value: str) -> None: ...
    @CacheResults.setter
    def CacheResults(self, value: bool) -> None: ...
    @ClientTimeout.setter
    def ClientTimeout(self, value: TimeSpan) -> None: ...
    @DerefAlias.setter
    def DerefAlias(self, value: DereferenceAlias) -> None: ...
    @DirectorySynchronization.setter
    def DirectorySynchronization(self, value: DirectorySynchronization) -> None: ...
    @ExtendedDN.setter
    def ExtendedDN(self, value: ExtendedDN) -> None: ...
    @Filter.setter
    def Filter(self, value: str) -> None: ...
    @PageSize.setter
    def PageSize(self, value: int) -> None: ...
    @PropertyNamesOnly.setter
    def PropertyNamesOnly(self, value: bool) -> None: ...
    @ReferralChasing.setter
    def ReferralChasing(self, value: ReferralChasingOption) -> None: ...
    @SearchRoot.setter
    def SearchRoot(self, value: DirectoryEntry) -> None: ...
    @SearchScope.setter
    def SearchScope(self, value: SearchScope) -> None: ...
    @SecurityMasks.setter
    def SecurityMasks(self, value: SecurityMasks) -> None: ...
    @ServerPageTimeLimit.setter
    def ServerPageTimeLimit(self, value: TimeSpan) -> None: ...
    @ServerTimeLimit.setter
    def ServerTimeLimit(self, value: TimeSpan) -> None: ...
    @SizeLimit.setter
    def SizeLimit(self, value: int) -> None: ...
    @Sort.setter
    def Sort(self, value: SortOption) -> None: ...
    @Tombstone.setter
    def Tombstone(self, value: bool) -> None: ...
    @VirtualListView.setter
    def VirtualListView(self, value: DirectoryVirtualListView) -> None: ...


class DirectoryServicesCOMException(COMException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, inner: Exception): ...
    @property
    def ExtendedError(self) -> int: ...
    @property
    def ExtendedErrorMessage(self) -> str: ...
    def GetObjectData(self, serializationInfo: SerializationInfo, streamingContext: StreamingContext) -> None: ...


class DirectoryServicesPermission(ResourcePermissionBase):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, state: PermissionState): ...
    @overload
    def __init__(self, permissionAccessEntries: Set(DirectoryServicesPermissionEntry)): ...
    @overload
    def __init__(self, permissionAccess: DirectoryServicesPermissionAccess, path: str): ...
    @property
    def PermissionEntries(self) -> DirectoryServicesPermissionEntryCollection: ...


class DirectoryServicesPermissionAccess:
    #None = 0
    Browse = 2
    Write = 6


class DirectoryServicesPermissionAttribute(CodeAccessSecurityAttribute):
    def __init__(self, action: SecurityAction): ...
    def CreatePermission(self) -> IPermission: ...
    @property
    def Path(self) -> str: ...
    @property
    def PermissionAccess(self) -> DirectoryServicesPermissionAccess: ...
    @Path.setter
    def Path(self, value: str) -> None: ...
    @PermissionAccess.setter
    def PermissionAccess(self, value: DirectoryServicesPermissionAccess) -> None: ...


class DirectoryServicesPermissionEntry(Object):
    def __init__(self, permissionAccess: DirectoryServicesPermissionAccess, path: str): ...
    @property
    def Path(self) -> str: ...
    @property
    def PermissionAccess(self) -> DirectoryServicesPermissionAccess: ...


class DirectoryServicesPermissionEntryCollection(CollectionBase):
    def Add(self, value: DirectoryServicesPermissionEntry) -> int: ...
    @overload
    def AddRange(self, value: Set(DirectoryServicesPermissionEntry)) -> None: ...
    @overload
    def AddRange(self, value: DirectoryServicesPermissionEntryCollection) -> None: ...
    def Contains(self, value: DirectoryServicesPermissionEntry) -> bool: ...
    def CopyTo(self, array: Set(DirectoryServicesPermissionEntry), index: int) -> None: ...
    @property
    def Item(self, index: int) -> DirectoryServicesPermissionEntry: ...
    def IndexOf(self, value: DirectoryServicesPermissionEntry) -> int: ...
    def Insert(self, index: int, value: DirectoryServicesPermissionEntry) -> None: ...
    def Remove(self, value: DirectoryServicesPermissionEntry) -> None: ...
    @Item.setter
    def Item(self, index: int, value: DirectoryServicesPermissionEntry) -> None: ...


class DirectorySynchronization(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, option: DirectorySynchronizationOptions): ...
    @overload
    def __init__(self, sync: DirectorySynchronization): ...
    @overload
    def __init__(self, cookie: Set(Byte)): ...
    @overload
    def __init__(self, option: DirectorySynchronizationOptions, cookie: Set(Byte)): ...
    def Copy(self) -> DirectorySynchronization: ...
    @property
    def Option(self) -> DirectorySynchronizationOptions: ...
    def GetDirectorySynchronizationCookie(self) -> Set(Byte): ...
    @overload
    def ResetDirectorySynchronizationCookie(self) -> None: ...
    @overload
    def ResetDirectorySynchronizationCookie(self, cookie: Set(Byte)) -> None: ...
    @Option.setter
    def Option(self, value: DirectorySynchronizationOptions) -> None: ...


class DirectorySynchronizationOptions:
    #None = 0
    ObjectSecurity = 1
    ParentsFirst = 2048
    PublicDataOnly = 8192
    IncrementalValues = 2147483648


class DirectoryVirtualListView(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, afterCount: int): ...
    @overload
    def __init__(self, beforeCount: int, afterCount: int, offset: int): ...
    @overload
    def __init__(self, beforeCount: int, afterCount: int, target: str): ...
    @overload
    def __init__(self, beforeCount: int, afterCount: int, offset: int, context: DirectoryVirtualListViewContext): ...
    @overload
    def __init__(self, beforeCount: int, afterCount: int, target: str, context: DirectoryVirtualListViewContext): ...
    @property
    def AfterCount(self) -> int: ...
    @property
    def ApproximateTotal(self) -> int: ...
    @property
    def BeforeCount(self) -> int: ...
    @property
    def DirectoryVirtualListViewContext(self) -> DirectoryVirtualListViewContext: ...
    @property
    def Offset(self) -> int: ...
    @property
    def Target(self) -> str: ...
    @property
    def TargetPercentage(self) -> int: ...
    @AfterCount.setter
    def AfterCount(self, value: int) -> None: ...
    @ApproximateTotal.setter
    def ApproximateTotal(self, value: int) -> None: ...
    @BeforeCount.setter
    def BeforeCount(self, value: int) -> None: ...
    @DirectoryVirtualListViewContext.setter
    def DirectoryVirtualListViewContext(self, value: DirectoryVirtualListViewContext) -> None: ...
    @Offset.setter
    def Offset(self, value: int) -> None: ...
    @Target.setter
    def Target(self, value: str) -> None: ...
    @TargetPercentage.setter
    def TargetPercentage(self, value: int) -> None: ...


class DirectoryVirtualListViewContext(Object):
    def __init__(self): ...
    def Copy(self) -> DirectoryVirtualListViewContext: ...


class DSDescriptionAttribute(DescriptionAttribute):
    def __init__(self, description: str): ...
    @property
    def Description(self) -> str: ...


class ExtendedDN:
    HexString = 0
    Standard = 1
    #None = -1


class ExtendedRightAccessRule(ActiveDirectoryAccessRule):
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType): ...
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType, extendedRightType: Guid): ...
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType, inheritanceType: ActiveDirectorySecurityInheritance): ...
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType, extendedRightType: Guid, inheritanceType: ActiveDirectorySecurityInheritance): ...
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType, inheritanceType: ActiveDirectorySecurityInheritance, inheritedObjectType: Guid): ...
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType, extendedRightType: Guid, inheritanceType: ActiveDirectorySecurityInheritance, inheritedObjectType: Guid): ...


class ListChildrenAccessRule(ActiveDirectoryAccessRule):
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType): ...
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType, inheritanceType: ActiveDirectorySecurityInheritance): ...
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType, inheritanceType: ActiveDirectorySecurityInheritance, inheritedObjectType: Guid): ...


class PasswordEncodingMethod:
    PasswordEncodingSsl = 0
    PasswordEncodingClear = 1


class PropertyAccess:
    Read = 0
    Write = 1


class PropertyAccessRule(ActiveDirectoryAccessRule):
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType, access: PropertyAccess): ...
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType, access: PropertyAccess, propertyType: Guid): ...
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType, access: PropertyAccess, inheritanceType: ActiveDirectorySecurityInheritance): ...
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType, access: PropertyAccess, propertyType: Guid, inheritanceType: ActiveDirectorySecurityInheritance): ...
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType, access: PropertyAccess, inheritanceType: ActiveDirectorySecurityInheritance, inheritedObjectType: Guid): ...
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType, access: PropertyAccess, propertyType: Guid, inheritanceType: ActiveDirectorySecurityInheritance, inheritedObjectType: Guid): ...


class PropertyCollection(Object):
    def Contains(self, propertyName: str) -> bool: ...
    def CopyTo(self, array: Set(PropertyValueCollection), index: int) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, propertyName: str) -> PropertyValueCollection: ...
    @property
    def PropertyNames(self) -> ICollection: ...
    @property
    def Values(self) -> ICollection: ...
    def GetEnumerator(self) -> IDictionaryEnumerator: ...


class PropertySetAccessRule(ActiveDirectoryAccessRule):
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType, access: PropertyAccess, propertySetType: Guid): ...
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType, access: PropertyAccess, propertySetType: Guid, inheritanceType: ActiveDirectorySecurityInheritance): ...
    @overload
    def __init__(self, identity: IdentityReference, type: AccessControlType, access: PropertyAccess, propertySetType: Guid, inheritanceType: ActiveDirectorySecurityInheritance, inheritedObjectType: Guid): ...


class PropertyValueCollection(CollectionBase):
    def Add(self, value: Object) -> int: ...
    @overload
    def AddRange(self, value: Set(Object)) -> None: ...
    @overload
    def AddRange(self, value: PropertyValueCollection) -> None: ...
    def Contains(self, value: Object) -> bool: ...
    def CopyTo(self, array: Set(Object), index: int) -> None: ...
    @property
    def Item(self, index: int) -> Object: ...
    @property
    def PropertyName(self) -> str: ...
    @property
    def Value(self) -> Object: ...
    def IndexOf(self, value: Object) -> int: ...
    def Insert(self, index: int, value: Object) -> None: ...
    def Remove(self, value: Object) -> None: ...
    @Item.setter
    def Item(self, index: int, value: Object) -> None: ...
    @Value.setter
    def Value(self, value: Object) -> None: ...


class ReferralChasingOption:
    #None = 0
    Subordinate = 32
    External = 64
    All = 96


class ResultPropertyCollection(DictionaryBase):
    def Contains(self, propertyName: str) -> bool: ...
    @overload
    def CopyTo(self, array: Set(ResultPropertyValueCollection), index: int) -> None: ...
    @property
    def Item(self, name: str) -> ResultPropertyValueCollection: ...
    @property
    def PropertyNames(self) -> ICollection: ...
    @property
    def Values(self) -> ICollection: ...


class ResultPropertyValueCollection(ReadOnlyCollectionBase):
    def Contains(self, value: Object) -> bool: ...
    def CopyTo(self, values: Set(Object), index: int) -> None: ...
    @property
    def Item(self, index: int) -> Object: ...
    def IndexOf(self, value: Object) -> int: ...


class SchemaNameCollection(Object):
    def Add(self, value: str) -> int: ...
    @overload
    def AddRange(self, value: Set(str)) -> None: ...
    @overload
    def AddRange(self, value: SchemaNameCollection) -> None: ...
    def Clear(self) -> None: ...
    def Contains(self, value: str) -> bool: ...
    def CopyTo(self, stringArray: Set(str), index: int) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, index: int) -> str: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def IndexOf(self, value: str) -> int: ...
    def Insert(self, index: int, value: str) -> None: ...
    def Remove(self, value: str) -> None: ...
    def RemoveAt(self, index: int) -> None: ...
    @Item.setter
    def Item(self, index: int, value: str) -> None: ...


class SearchResult(Object):
    @property
    def Path(self) -> str: ...
    @property
    def Properties(self) -> ResultPropertyCollection: ...
    def GetDirectoryEntry(self) -> DirectoryEntry: ...


class SearchResultCollection(MarshalByRefObject):
    def Contains(self, result: SearchResult) -> bool: ...
    def CopyTo(self, results: Set(SearchResult), index: int) -> None: ...
    def Dispose(self) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def Handle(self) -> IntPtr: ...
    @property
    def Item(self, index: int) -> SearchResult: ...
    @property
    def PropertiesLoaded(self) -> Set(str): ...
    def GetEnumerator(self) -> IEnumerator: ...
    def IndexOf(self, result: SearchResult) -> int: ...


class SearchScope:
    Base = 0
    OneLevel = 1
    Subtree = 2


class SecurityMasks:
    #None = 0
    Owner = 1
    Group = 2
    Dacl = 4
    Sacl = 8


class SortDirection:
    Ascending = 0
    Descending = 1


class SortOption(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, propertyName: str, direction: SortDirection): ...
    @property
    def Direction(self) -> SortDirection: ...
    @property
    def PropertyName(self) -> str: ...
    @Direction.setter
    def Direction(self, value: SortDirection) -> None: ...
    @PropertyName.setter
    def PropertyName(self, value: str) -> None: ...
