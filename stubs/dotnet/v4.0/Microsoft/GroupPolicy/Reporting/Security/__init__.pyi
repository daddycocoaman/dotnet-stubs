from typing import Tuple, Set, Iterable, List


class AccessControlItemType:
    def __init__(self): ...
    @property
    def Item(self) -> Object: ...
    @Item.setter
    def Item(self, value: Object) -> None: ...


class AccessMapper:
    pass


class AccessSpecifierCreator:
    pass


class AllowType:
    Allow = 0
    Deny = 1


class Applicability:
    def __init__(self): ...
    @property
    def ToDescendantContainers(self) -> bool: ...
    @property
    def ToDescendantObjects(self) -> bool: ...
    @property
    def ToDirectDescendantsOnly(self) -> bool: ...
    @property
    def ToSelf(self) -> bool: ...
    @ToDescendantContainers.setter
    def ToDescendantContainers(self, value: bool) -> None: ...
    @ToDescendantObjects.setter
    def ToDescendantObjects(self, value: bool) -> None: ...
    @ToDirectDescendantsOnly.setter
    def ToDirectDescendantsOnly(self, value: bool) -> None: ...
    @ToSelf.setter
    def ToSelf(self, value: bool) -> None: ...


class AuditType(AccessControlItemType):
    def __init__(self): ...


class AuditValue:
    Success = 0
    Failure = 1
    All = 2


class FileAccessSpecifierCreator(AccessSpecifierCreator):
    def __init__(self): ...


class FileGroupedAccess:
    FullControl = 0
    Modify = 1
    ReadandExecute = 2
    ListFolderContents = 3
    Read = 4
    Write = 5


class FileIndividualAccess:
    TraverseFolderExecuteFile = 0
    ListFolderReadData = 1
    ReadAttributes = 2
    ReadExtendedAttributes = 3
    CreateFilesWriteData = 4
    CreateFoldersAppendData = 5
    WriteAttributes = 6
    WriteExtendedAttributes = 7
    DeleteSubfoldersAndFiles = 8
    Delete = 9
    ReadPermissions = 10
    ChangePermissions = 11
    TakeOwnership = 12


class GPOGroupedAccess:
    Read = 0
    EditSettings = 1
    Editdeletemodifysecurity = 2
    Custom = 3
    ApplyGroupPolicy = 4


class GpoSecurityFlags:
    pass


class GpoTrusteeEntryCreator:
    def GetCount(self) -> int: ...


class GroupedAccess:
    def __init__(self): ...
    @property
    def Item(self) -> Object: ...
    @Item.setter
    def Item(self, value: Object) -> None: ...


class IndividualAccess:
    def __init__(self): ...
    @property
    def Item(self) -> Object: ...
    @Item.setter
    def Item(self, value: Object) -> None: ...


class Mapping:
    @property
    def Access(self) -> Object: ...
    @property
    def Mask(self) -> UInt32: ...
    @property
    def ObjectGuid(self) -> str: ...
    @Access.setter
    def Access(self, value: Object) -> None: ...
    @Mask.setter
    def Mask(self, value: UInt32) -> None: ...
    @ObjectGuid.setter
    def ObjectGuid(self, value: str) -> None: ...


class ObjectType:
    File = 0
    Registry = 1
    Service = 2
    GPO = 3
    SoftwareInstallation = 4


class PermissionType(AccessControlItemType):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, permission: AllowType): ...


class RegistryAccessSpecifierCreator(AccessSpecifierCreator):
    def __init__(self): ...


class RegistryGroupedAccess:
    FullControl = 0
    Read = 1


class RegistryIndividualAccess:
    QueryValue = 0
    SetValue = 1
    CreateSubkey = 2
    EnumerateSubkeys = 3
    Notify = 4
    CreateLink = 5
    Delete = 6
    ReadPermissions = 7
    ChangePermissions = 8
    TakeOwnership = 9


class SecurityDescriptor:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, objectType: ObjectType, sddlInput: str, server: str): ...
    @overload
    def __init__(self, objectType: ObjectType, securityDescriptor: Set(Byte), server: str): ...
    @overload
    def __init__(self, objectType: ObjectType, dsEntry: DirectoryEntry, server: str): ...
    @overload
    def __init__(self, objectType: ObjectType, fileObject: FileSecurity, server: str): ...
    @property
    def Auditing(self) -> SecurityDescriptorAuditing: ...
    @property
    def AuditingPresent(self) -> bool: ...
    @property
    def Group(self) -> Trustee: ...
    @property
    def Owner(self) -> Trustee: ...
    @property
    def Permissions(self) -> SecurityDescriptorPermissions: ...
    @property
    def PermissionsPresent(self) -> bool: ...
    @property
    def SDDL(self) -> str: ...
    @Auditing.setter
    def Auditing(self, value: SecurityDescriptorAuditing) -> None: ...
    @AuditingPresent.setter
    def AuditingPresent(self, value: bool) -> None: ...
    @Group.setter
    def Group(self, value: Trustee) -> None: ...
    @Owner.setter
    def Owner(self, value: Trustee) -> None: ...
    @Permissions.setter
    def Permissions(self, value: SecurityDescriptorPermissions) -> None: ...
    @PermissionsPresent.setter
    def PermissionsPresent(self, value: bool) -> None: ...
    @SDDL.setter
    def SDDL(self, value: str) -> None: ...


class SecurityDescriptorAuditing:
    def __init__(self): ...
    @property
    def InheritsFromParent(self) -> bool: ...
    @property
    def TrusteeAuditing(self) -> Set(TrusteeAuditingEntry): ...
    @InheritsFromParent.setter
    def InheritsFromParent(self, value: bool) -> None: ...
    @TrusteeAuditing.setter
    def TrusteeAuditing(self, value: Set(TrusteeAuditingEntry)) -> None: ...


class SecurityDescriptorPermissions:
    def __init__(self): ...
    @property
    def InheritsFromParent(self) -> bool: ...
    @property
    def TrusteePermissions(self) -> Set(TrusteePermissionsEntry): ...
    @InheritsFromParent.setter
    def InheritsFromParent(self, value: bool) -> None: ...
    @TrusteePermissions.setter
    def TrusteePermissions(self, value: Set(TrusteePermissionsEntry)) -> None: ...


class ServiceAccessSpecifierCreator(AccessSpecifierCreator):
    def __init__(self): ...


class ServicesGroupedAccess:
    FullControl = 0
    Read = 1
    StartStopandPause = 2
    Write = 3
    Delete = 4


class ServicesIndividualAccess:
    Querytemplate = 0
    Changetemplate = 1
    Querystatus = 2
    Enumeratedependants = 3
    Start = 4
    Stop = 5
    Pauseandcontinue = 6
    Interrogate = 7
    Userdefinedcontrol = 8
    Delete = 9
    Readpermissions = 10
    Changepermissions = 11
    Takeownership = 12


class SIAccessSpecifierCreator(AccessSpecifierCreator):
    def __init__(self): ...


class SoftwareInstallationGroupedAccess:
    FullControl = 0
    Read = 1
    Write = 2


class TrusteeAccessEntry:
    def __init__(self): ...
    @property
    def AccessMask(self) -> UInt32: ...
    @property
    def Applicability(self) -> Applicability: ...
    @property
    def Condition(self) -> str: ...
    @property
    def Custom(self) -> ArrayList: ...
    @property
    def Inherited(self) -> bool: ...
    @property
    def Standard(self) -> ArrayList: ...
    @property
    def Trustee(self) -> Trustee: ...
    @property
    def Type(self) -> AccessControlItemType: ...
    @AccessMask.setter
    def AccessMask(self, value: UInt32) -> None: ...
    @Applicability.setter
    def Applicability(self, value: Applicability) -> None: ...
    @Condition.setter
    def Condition(self, value: str) -> None: ...
    @Custom.setter
    def Custom(self, value: ArrayList) -> None: ...
    @Inherited.setter
    def Inherited(self, value: bool) -> None: ...
    @Standard.setter
    def Standard(self, value: ArrayList) -> None: ...
    @Trustee.setter
    def Trustee(self, value: Trustee) -> None: ...
    @Type.setter
    def Type(self, value: AccessControlItemType) -> None: ...


class TrusteeAuditingEntry(TrusteeAccessEntry):
    def __init__(self): ...


class TrusteePermissionsEntry(TrusteeAccessEntry):
    def __init__(self): ...
