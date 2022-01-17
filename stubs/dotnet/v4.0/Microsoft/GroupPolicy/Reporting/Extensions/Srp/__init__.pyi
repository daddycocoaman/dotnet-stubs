from typing import Tuple, Set, Iterable, List


class EnforcementMode(PolicySetting):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, policySetting: PolicySetting): ...
    @property
    def Mode(self) -> Mode: ...
    @Mode.setter
    def Mode(self, value: Mode) -> None: ...


class FileHash:
    def __init__(self): ...
    @property
    def FileInformation(self) -> FileInformation: ...
    @property
    def Type(self) -> Hash: ...
    @FileInformation.setter
    def FileInformation(self, value: FileInformation) -> None: ...
    @Type.setter
    def Type(self, value: Hash) -> None: ...


class FileHashCondition:
    def __init__(self): ...
    @property
    def FileHash(self) -> Set(FileHash): ...
    @FileHash.setter
    def FileHash(self, value: Set(FileHash)) -> None: ...


class FileHashRule(PolicySetting):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, policySetting: PolicySetting): ...
    @property
    def Action(self) -> RuleAction: ...
    @property
    def Conditions(self) -> FileHashCondition: ...
    @property
    def Description(self) -> str: ...
    @property
    def Id(self) -> str: ...
    @property
    def Name(self) -> str: ...
    @property
    def UserOrGroupSid(self) -> str: ...
    @Action.setter
    def Action(self, value: RuleAction) -> None: ...
    @Conditions.setter
    def Conditions(self, value: FileHashCondition) -> None: ...
    @Description.setter
    def Description(self, value: str) -> None: ...
    @Id.setter
    def Id(self, value: str) -> None: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    @UserOrGroupSid.setter
    def UserOrGroupSid(self, value: str) -> None: ...


class FileInformation:
    def __init__(self): ...
    @property
    def Length(self) -> Int64: ...
    @property
    def Name(self) -> str: ...
    @Length.setter
    def Length(self, value: Int64) -> None: ...
    @Name.setter
    def Name(self, value: str) -> None: ...


class FilePath:
    def __init__(self): ...
    @property
    def Path(self) -> str: ...
    @Path.setter
    def Path(self, value: str) -> None: ...


class FilePathCondition:
    def __init__(self): ...
    @property
    def FilePath(self) -> Set(FilePath): ...
    @FilePath.setter
    def FilePath(self, value: Set(FilePath)) -> None: ...


class FilePathRule(PolicySetting):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, policySetting: PolicySetting): ...
    @property
    def Action(self) -> RuleAction: ...
    @property
    def Conditions(self) -> FilePathCondition: ...
    @property
    def Description(self) -> str: ...
    @property
    def Exceptions(self) -> FilePathRuleExceptions: ...
    @property
    def Id(self) -> str: ...
    @property
    def Name(self) -> str: ...
    @property
    def UserOrGroupSid(self) -> str: ...
    @Action.setter
    def Action(self, value: RuleAction) -> None: ...
    @Conditions.setter
    def Conditions(self, value: FilePathCondition) -> None: ...
    @Description.setter
    def Description(self, value: str) -> None: ...
    @Exceptions.setter
    def Exceptions(self, value: FilePathRuleExceptions) -> None: ...
    @Id.setter
    def Id(self, value: str) -> None: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    @UserOrGroupSid.setter
    def UserOrGroupSid(self, value: str) -> None: ...


class FilePathRuleExceptions:
    def __init__(self): ...
    @property
    def Items(self) -> Set(Object): ...
    @Items.setter
    def Items(self, value: Set(Object)) -> None: ...


class FilePublisher:
    def __init__(self): ...
    @property
    def BinaryName(self) -> str: ...
    @property
    def BinaryVersionRange(self) -> FileVersionRange: ...
    @property
    def ProductName(self) -> str: ...
    @property
    def PublisherName(self) -> str: ...
    @BinaryName.setter
    def BinaryName(self, value: str) -> None: ...
    @BinaryVersionRange.setter
    def BinaryVersionRange(self, value: FileVersionRange) -> None: ...
    @ProductName.setter
    def ProductName(self, value: str) -> None: ...
    @PublisherName.setter
    def PublisherName(self, value: str) -> None: ...


class FilePublisherCondition:
    def __init__(self): ...
    @property
    def FilePublisher(self) -> Set(FilePublisher): ...
    @FilePublisher.setter
    def FilePublisher(self, value: Set(FilePublisher)) -> None: ...


class FilePublisherRule(PolicySetting):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, policySetting: PolicySetting): ...
    @property
    def Action(self) -> RuleAction: ...
    @property
    def Conditions(self) -> FilePublisherCondition: ...
    @property
    def Description(self) -> str: ...
    @property
    def Exceptions(self) -> FilePublisherRuleExceptions: ...
    @property
    def Id(self) -> str: ...
    @property
    def Name(self) -> str: ...
    @property
    def UserOrGroupSid(self) -> str: ...
    @Action.setter
    def Action(self, value: RuleAction) -> None: ...
    @Conditions.setter
    def Conditions(self, value: FilePublisherCondition) -> None: ...
    @Description.setter
    def Description(self, value: str) -> None: ...
    @Exceptions.setter
    def Exceptions(self, value: FilePublisherRuleExceptions) -> None: ...
    @Id.setter
    def Id(self, value: str) -> None: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    @UserOrGroupSid.setter
    def UserOrGroupSid(self, value: str) -> None: ...


class FilePublisherRuleExceptions:
    def __init__(self): ...
    @property
    def Items(self) -> Set(Object): ...
    @Items.setter
    def Items(self, value: Set(Object)) -> None: ...


class FileVersionRange:
    def __init__(self): ...
    @property
    def HighSection(self) -> str: ...
    @property
    def LowSection(self) -> str: ...
    @HighSection.setter
    def HighSection(self, value: str) -> None: ...
    @LowSection.setter
    def LowSection(self, value: str) -> None: ...


class Hash:
    Sha256 = 0
    Sha256Flat = 1
    Sha1 = 2
    Md5Flat = 3


class Mode:
    NotConfigured = 0
    Enabled = 1
    Disabled = 2


class Policy(GPOExtension):
    def __init__(self): ...
    @property
    def RuleCollection(self) -> Set(RuleCollection): ...
    @overload
    def Initialize(self, context: ReportingContext) -> None: ...
    @overload
    def Initialize(self, srpRegistrySettings: ArrayList, context: ReportingContext) -> None: ...
    @RuleCollection.setter
    def RuleCollection(self, value: Set(RuleCollection)) -> None: ...


class PolicyConverter:
    def __init__(self): ...
    def ConvertPolicy(self, srpPolicy: AppLockerPolicy, policy: Policy) -> None: ...
    def ConvertRule(self, omRule: AppLockerRule, policySetting: PolicySetting) -> PolicySetting: ...


class RsopConverter:
    def __init__(self, srpRegistrySettings: ArrayList, rsopContext: RsopContext): ...
    def Convert(self, policy: Policy) -> None: ...


class RuleAction:
    Allow = 0
    Deny = 1


class RuleCollection:
    def __init__(self): ...
    @property
    def EnforcementMode(self) -> EnforcementMode: ...
    @property
    def Items(self) -> Set(PolicySetting): ...
    @property
    def Type(self) -> str: ...
    @EnforcementMode.setter
    def EnforcementMode(self, value: EnforcementMode) -> None: ...
    @Items.setter
    def Items(self, value: Set(PolicySetting)) -> None: ...
    @Type.setter
    def Type(self, value: str) -> None: ...
