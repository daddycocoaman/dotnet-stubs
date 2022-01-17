from typing import Tuple, Set, Iterable, List


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
