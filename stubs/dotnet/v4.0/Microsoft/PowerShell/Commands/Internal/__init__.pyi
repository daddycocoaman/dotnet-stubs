__all__ = ['Format']
from typing import Tuple, Set, Iterable, List


class RemotingErrorResources:
    @property
    def CouldNotResolveRoleDefinitionPrincipal() -> str: ...
    @property
    def WinRMRestartWarning() -> str: ...


class TransactedRegistryAccessRule:
    def __init__(self, identity: IdentityReference, registryRights: RegistryRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType): ...
    @property
    def RegistryRights(self) -> RegistryRights: ...


class TransactedRegistryAuditRule:
    @property
    def RegistryRights(self) -> RegistryRights: ...


class TransactedRegistryKey:
    def Close(self) -> None: ...
    @overload
    def CreateSubKey(self, subkey: str) -> TransactedRegistryKey: ...
    @overload
    def CreateSubKey(self, subkey: str, permissionCheck: RegistryKeyPermissionCheck) -> TransactedRegistryKey: ...
    @overload
    def CreateSubKey(self, subkey: str, permissionCheck: RegistryKeyPermissionCheck, registrySecurity: TransactedRegistrySecurity) -> TransactedRegistryKey: ...
    @overload
    def DeleteSubKey(self, subkey: str) -> None: ...
    @overload
    def DeleteSubKey(self, subkey: str, throwOnMissingSubKey: bool) -> None: ...
    def DeleteSubKeyTree(self, subkey: str) -> None: ...
    @overload
    def DeleteValue(self, name: str) -> None: ...
    @overload
    def DeleteValue(self, name: str, throwOnMissingValue: bool) -> None: ...
    def Dispose(self) -> None: ...
    def Flush(self) -> None: ...
    @property
    def Name(self) -> str: ...
    @property
    def SubKeyCount(self) -> int: ...
    @property
    def ValueCount(self) -> int: ...
    @overload
    def GetAccessControl(self) -> TransactedRegistrySecurity: ...
    @overload
    def GetAccessControl(self, includeSections: AccessControlSections) -> TransactedRegistrySecurity: ...
    def GetSubKeyNames(self) -> Set(str): ...
    @overload
    def GetValue(self, name: str) -> Object: ...
    @overload
    def GetValue(self, name: str, defaultValue: Object) -> Object: ...
    @overload
    def GetValue(self, name: str, defaultValue: Object, options: RegistryValueOptions) -> Object: ...
    def GetValueKind(self, name: str) -> RegistryValueKind: ...
    def GetValueNames(self) -> Set(str): ...
    @overload
    def OpenSubKey(self, name: str) -> TransactedRegistryKey: ...
    @overload
    def OpenSubKey(self, name: str, permissionCheck: RegistryKeyPermissionCheck) -> TransactedRegistryKey: ...
    @overload
    def OpenSubKey(self, name: str, writable: bool) -> TransactedRegistryKey: ...
    @overload
    def OpenSubKey(self, name: str, permissionCheck: RegistryKeyPermissionCheck, rights: RegistryRights) -> TransactedRegistryKey: ...
    def SetAccessControl(self, registrySecurity: TransactedRegistrySecurity) -> None: ...
    @overload
    def SetValue(self, name: str, value: Object) -> None: ...
    @overload
    def SetValue(self, name: str, value: Object, valueKind: RegistryValueKind) -> None: ...
    def ToString(self) -> str: ...


class TransactedRegistrySecurity:
    def __init__(self): ...
    def AccessRuleFactory(self, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule: ...
    def AddAccessRule(self, rule: TransactedRegistryAccessRule) -> None: ...
    def AddAuditRule(self, rule: TransactedRegistryAuditRule) -> None: ...
    def AuditRuleFactory(self, identityReference: IdentityReference, accessMask: int, isInherited: bool, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule: ...
    @property
    def AccessRightType(self) -> Type: ...
    @property
    def AccessRuleType(self) -> Type: ...
    @property
    def AuditRuleType(self) -> Type: ...
    def RemoveAccessRule(self, rule: TransactedRegistryAccessRule) -> bool: ...
    def RemoveAccessRuleAll(self, rule: TransactedRegistryAccessRule) -> None: ...
    def RemoveAccessRuleSpecific(self, rule: TransactedRegistryAccessRule) -> None: ...
    def RemoveAuditRule(self, rule: TransactedRegistryAuditRule) -> bool: ...
    def RemoveAuditRuleAll(self, rule: TransactedRegistryAuditRule) -> None: ...
    def RemoveAuditRuleSpecific(self, rule: TransactedRegistryAuditRule) -> None: ...
    def ResetAccessRule(self, rule: TransactedRegistryAccessRule) -> None: ...
    def SetAccessRule(self, rule: TransactedRegistryAccessRule) -> None: ...
    def SetAuditRule(self, rule: TransactedRegistryAuditRule) -> None: ...
