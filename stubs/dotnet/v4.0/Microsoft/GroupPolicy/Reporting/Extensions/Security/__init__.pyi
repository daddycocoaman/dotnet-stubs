from typing import Tuple, Set, Iterable, List


class AccountPolicy(PolicySetting):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, accountPolicyObject: ManagementObject, typeOfSetting: SettingType): ...
    @overload
    def __init__(self, key: str, value: str): ...
    @property
    def Item(self) -> Object: ...
    @property
    def Name(self) -> AccountPolicyName: ...
    @property
    def Type(self) -> AccountPolicyType: ...
    @Item.setter
    def Item(self, value: Object) -> None: ...
    @Name.setter
    def Name(self, value: AccountPolicyName) -> None: ...
    @Type.setter
    def Type(self, value: AccountPolicyType) -> None: ...


class AccountPolicyName:
    MinimumPasswordAge = 0
    MaximumPasswordAge = 1
    MinimumPasswordLength = 2
    PasswordHistorySize = 3
    PasswordComplexity = 4
    ClearTextPassword = 5
    LockoutBadCount = 6
    ResetLockoutCount = 7
    LockoutDuration = 8
    TicketValidateClient = 9
    MaxServiceAge = 10
    MaxTicketAge = 11
    MaxRenewAge = 12
    MaxClockSkew = 13


class AccountPolicyType:
    Password = 0
    AccountLockout = 1
    Kerberos = 2


class DisplayField:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, iName: str, iValue: bool): ...
    @property
    def Name(self) -> str: ...
    @property
    def Value(self) -> bool: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    @Value.setter
    def Value(self, value: bool) -> None: ...


class DisplayFields:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, iField: Set(DisplayField)): ...
    @property
    def Field(self) -> Set(DisplayField): ...
    @Field.setter
    def Field(self, value: Set(DisplayField)) -> None: ...


class EventLogCategory:
    System = 0
    Security = 1
    Application = 2


class EventLogName:
    MaximumLogSize = 0
    RestrictGuestAccess = 1
    RetentionDays = 2
    AuditLogRetentionPeriod = 3


class LocalPoliciesAudit(PolicySetting):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, auditObject: ManagementObject): ...
    @overload
    def __init__(self, key: str, value: str): ...
    @property
    def FailureAttempts(self) -> bool: ...
    @property
    def Name(self) -> LocalPoliciesAuditValue: ...
    @property
    def SuccessAttempts(self) -> bool: ...
    @FailureAttempts.setter
    def FailureAttempts(self, value: bool) -> None: ...
    @Name.setter
    def Name(self, value: LocalPoliciesAuditValue) -> None: ...
    @SuccessAttempts.setter
    def SuccessAttempts(self, value: bool) -> None: ...


class LocalPoliciesAuditValue:
    AuditAccountLogon = 0
    AuditAccountManage = 1
    AuditDSAccess = 2
    AuditLogonEvents = 3
    AuditObjectAccess = 4
    AuditPolicyChange = 5
    AuditPrivilegeUse = 6
    AuditProcessTracking = 7
    AuditSystemEvents = 8


class LocalPoliciesRegType:
    REG_NONE = 0
    REG_SZ = 1
    REG_EXPAND_SZ = 2
    REG_BINARY = 3
    REG_DWORD = 4
    REG_MULTI_SZ = 7
    REG_MULTI_SZ_2 = 8


class LocalPoliciesSecurityOptions(PolicySetting):
    def __init__(self): ...
    @property
    def Data(self) -> Object: ...
    @property
    def Display(self) -> LocalPoliciesSecurityOptionsDisplay: ...
    @property
    def Name(self) -> Object: ...
    def ParseUInt32(value: str) -> UInt32: ...
    @Data.setter
    def Data(self, value: Object) -> None: ...
    @Display.setter
    def Display(self, value: LocalPoliciesSecurityOptionsDisplay) -> None: ...
    @Name.setter
    def Name(self, value: Object) -> None: ...


class LocalPoliciesSecurityOptionsDisplay:
    def __init__(self): ...
    @property
    def Item(self) -> Object: ...
    @property
    def Name(self) -> str: ...
    @property
    def Units(self) -> str: ...
    def GetMap(mapValue: Set(str)) -> ArrayList: ...
    @Item.setter
    def Item(self, value: Object) -> None: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    @Units.setter
    def Units(self, value: str) -> None: ...


class LocalPoliciesSystemAccessName:
    EnableAdminAccount = 0
    EnableGuestAccount = 1
    NewAdministratorName = 2
    NewGuestName = 3
    LSAAnonymousNameLookup = 4
    ForceLogoffWhenHourExpire = 5


class LocalPoliciesUserRightsAssignment(PolicySetting):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, userRightsObject: ManagementObject, server: str): ...
    @overload
    def __init__(self, key: str, value: str, server: str): ...
    @property
    def Member(self) -> Set(Trustee): ...
    @property
    def Name(self) -> LocalPoliciesUserRightsAssignmentType: ...
    @Member.setter
    def Member(self, value: Set(Trustee)) -> None: ...
    @Name.setter
    def Name(self, value: LocalPoliciesUserRightsAssignmentType) -> None: ...


class LocalPoliciesUserRightsAssignmentType:
    SeNetworkLogonRight = 0
    SeTcbPrivilege = 1
    SeMachineAccountPrivilege = 2
    SeIncreaseQuotaPrivilege = 3
    SeInteractiveLogonRight = 4
    SeRemoteInteractiveLogonRight = 5
    SeBackupPrivilege = 6
    SeChangeNotifyPrivilege = 7
    SeSystemTimePrivilege = 8
    SeCreatePagefilePrivilege = 9
    SeCreateTokenPrivilege = 10
    SeCreatePermanentPrivilege = 11
    SeDebugPrivilege = 12
    SeDenyNetworkLogonRight = 13
    SeDenyBatchLogonRight = 14
    SeDenyServiceLogonRight = 15
    SeDenyInteractiveLogonRight = 16
    SeDenyRemoteInteractiveLogonRight = 17
    SeEnableDelegationPrivilege = 18
    SeRemoteShutdownPrivilege = 19
    SeAuditPrivilege = 20
    SeLoadDriverPrivilege = 21
    SeIncreaseBasePriorityPrivilege = 22
    SeLockMemoryPrivilege = 23
    SeBatchLogonRight = 24
    SeServiceLogonRight = 25
    SeSecurityPrivilege = 26
    SeSystemEnvironmentPrivilege = 27
    SeManageVolumePrivilege = 28
    SeProfileSingleProcessPrivilege = 29
    SeSystemProfilePrivilege = 30
    SeUndockPrivilege = 31
    SeAssignPrimaryTokenPrivilege = 32
    SeRestorePrivilege = 33
    SeShutdownPrivilege = 34
    SeSyncAgentPrivilege = 35
    SeTakeOwnershipPrivilege = 36
    SeUnsolicitedInputPrivilege = 37
    SeImpersonatePrivilege = 38
    SeCreateGlobalPrivilege = 39
    SeTrustedCredManAccessPrivilege = 40
    SeIncreaseWorkingSetPrivilege = 41
    SeRelabelPrivilege = 42
    SeTimeZonePrivilege = 43
    SeCreateSymbolicLinkPrivilege = 44
    SeDelegateSessionUserImpersonatePrivilege = 45


class LogRetentionMethod:
    AsNeeded = 0
    ByDays = 1
    Manually = 2


class PathSecurity(PolicySetting):
    @property
    def Mode(self) -> SecurityType: ...
    @property
    def Path(self) -> str: ...
    @property
    def SecurityDescriptor(self) -> SecurityDescriptor: ...
    @Mode.setter
    def Mode(self, value: SecurityType) -> None: ...
    @Path.setter
    def Path(self, value: str) -> None: ...
    @SecurityDescriptor.setter
    def SecurityDescriptor(self, value: SecurityDescriptor) -> None: ...


class RestrictedGroups(PolicySetting):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, restrictedGrpObject: ManagementObject, server: str, bMemberOf: bool): ...
    @overload
    def __init__(self, membersKey: str, membersValue: str, membersofValue: str, stringsSection: SortedList, server: str): ...
    @property
    def GroupName(self) -> Trustee: ...
    @property
    def Member(self) -> Set(Trustee): ...
    @property
    def Memberof(self) -> Set(Trustee): ...
    @property
    def MemberOfPresent(self) -> bool: ...
    @GroupName.setter
    def GroupName(self, value: Trustee) -> None: ...
    @Member.setter
    def Member(self, value: Set(Trustee)) -> None: ...
    @Memberof.setter
    def Memberof(self, value: Set(Trustee)) -> None: ...


class SecurityEventLog(PolicySetting):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, key: str, value: str, eventLogCategory: EventLogCategory): ...
    @overload
    def __init__(self, key: str, value: str, eventLogCategory: EventLogCategory, typeOfSetting: SettingType, eventLogObject: ManagementObject): ...
    @property
    def Item(self) -> Object: ...
    @property
    def Log(self) -> EventLogCategory: ...
    @property
    def Name(self) -> EventLogName: ...
    @Item.setter
    def Item(self, value: Object) -> None: ...
    @Log.setter
    def Log(self, value: EventLogCategory) -> None: ...
    @Name.setter
    def Name(self, value: EventLogName) -> None: ...


class SecurityFile(PathSecurity):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, key: str, server: str): ...
    @overload
    def __init__(self, fileSecObject: ManagementObject, server: str): ...


class SecurityRegistry(PathSecurity):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, key: str, server: str): ...
    @overload
    def __init__(self, registryObject: ManagementObject, server: str): ...


class SecurityRsopReader:
    pass


class SecuritySettings(GPOExtension):
    def __init__(self): ...
    @property
    def Account(self) -> Set(AccountPolicy): ...
    @property
    def Audit(self) -> Set(LocalPoliciesAudit): ...
    @property
    def Blocked(self) -> bool: ...
    @property
    def EventLog(self) -> Set(SecurityEventLog): ...
    @property
    def File(self) -> Set(SecurityFile): ...
    @property
    def Registry(self) -> Set(SecurityRegistry): ...
    @property
    def RestrictedGroups(self) -> Set(RestrictedGroups): ...
    @property
    def SecurityOptions(self) -> Set(LocalPoliciesSecurityOptions): ...
    @property
    def SystemServices(self) -> Set(SystemServices): ...
    @property
    def UserRightsAssignment(self) -> Set(LocalPoliciesUserRightsAssignment): ...
    def GetTrusteeFromString(group: str, server: str) -> Trustee: ...
    def GetTrusteesFromStrings(groups: Set(str), server: str) -> Set(Trustee): ...
    def Initialize(self, context: ReportingContext) -> None: ...
    def ParseGroups(groups: str, server: str) -> Set(Trustee): ...
    @Account.setter
    def Account(self, value: Set(AccountPolicy)) -> None: ...
    @Audit.setter
    def Audit(self, value: Set(LocalPoliciesAudit)) -> None: ...
    @Blocked.setter
    def Blocked(self, value: bool) -> None: ...
    @EventLog.setter
    def EventLog(self, value: Set(SecurityEventLog)) -> None: ...
    @File.setter
    def File(self, value: Set(SecurityFile)) -> None: ...
    @Registry.setter
    def Registry(self, value: Set(SecurityRegistry)) -> None: ...
    @RestrictedGroups.setter
    def RestrictedGroups(self, value: Set(RestrictedGroups)) -> None: ...
    @SecurityOptions.setter
    def SecurityOptions(self, value: Set(LocalPoliciesSecurityOptions)) -> None: ...
    @SystemServices.setter
    def SystemServices(self, value: Set(SystemServices)) -> None: ...
    @UserRightsAssignment.setter
    def UserRightsAssignment(self, value: Set(LocalPoliciesUserRightsAssignment)) -> None: ...


class SecurityType:
    Propogate = 0
    Prevent = 1
    Replace = 2


class ServiceStartupMode:
    BootStart = 0
    SystemStart = 1
    Automatic = 2
    Manual = 3
    Disabled = 4


class SettingType:
    NumericSetting = 0
    BooleanSetting = 1


class Strings:
    def __init__(self): ...
    @property
    def Value(self) -> Set(str): ...
    @Value.setter
    def Value(self, value: Set(str)) -> None: ...


class SystemServices(PolicySetting):
    def __init__(self): ...
    @property
    def Name(self) -> str: ...
    @property
    def SecurityDescriptor(self) -> SecurityDescriptor: ...
    @property
    def StartupMode(self) -> ServiceStartupMode: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    @SecurityDescriptor.setter
    def SecurityDescriptor(self, value: SecurityDescriptor) -> None: ...
    @StartupMode.setter
    def StartupMode(self, value: ServiceStartupMode) -> None: ...
