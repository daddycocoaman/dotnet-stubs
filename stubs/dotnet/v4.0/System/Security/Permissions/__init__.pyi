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
