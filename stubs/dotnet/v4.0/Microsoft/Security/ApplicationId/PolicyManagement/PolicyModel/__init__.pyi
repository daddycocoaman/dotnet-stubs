from typing import Tuple, Set, Iterable, List


class AppLockerFileType:
    NotSupported = 0
    Exe = 1
    Dll = 2
    WindowsInstaller = 3
    Script = 4
    AppX = 5


class AppLockerPolicy(PolicyElement):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, version: float): ...
    def CreateRuleCollection(self, type: str) -> RuleCollection: ...
    def DeleteRuleCollection(self, type: str) -> None: ...
    def DeleteRuleCollections(self) -> None: ...
    def FromXml(xml: str) -> AppLockerPolicy: ...
    @property
    def RuleCollections(self) -> ICollection: ...
    @property
    def RuleCollectionTypes(self) -> ICollection: ...
    @property
    def Version(self) -> float: ...
    def GetRuleCollection(self, type: str) -> RuleCollection: ...
    def HasRuleCollection(self, type: str) -> bool: ...
    def Load(xmlFilePath: str) -> AppLockerPolicy: ...
    def Merge(self, newPolicy: AppLockerPolicy) -> None: ...
    @Version.setter
    def Version(self, value: float) -> None: ...
    def Store(self, xmlFilePath: str) -> None: ...
    def ToString(self) -> str: ...
    def ToXml(self) -> str: ...


class AppLockerRule(PolicyElement):
    @overload
    def AddCondition(self, condition: FilePathCondition) -> None: ...
    @overload
    def AddCondition(self, condition: RuleCondition) -> None: ...
    @overload
    def AddCondition(self, condition: FilePublisherCondition) -> None: ...
    @overload
    def AddCondition(self, condition: FileHashCondition) -> None: ...
    @overload
    def AddException(self, exception: FileHashCondition) -> None: ...
    @overload
    def AddException(self, exception: FilePathCondition) -> None: ...
    @overload
    def AddException(self, exception: FilePublisherCondition) -> None: ...
    @overload
    def AddException(self, exception: RuleCondition) -> None: ...
    def DeleteConditions(self) -> None: ...
    def DeleteExceptions(self) -> None: ...
    @property
    def Action(self) -> AppLockerRuleActionType: ...
    @property
    def Description(self) -> str: ...
    @property
    def Id(self) -> Id: ...
    @property
    def Name(self) -> str: ...
    @property
    def UserOrGroupSid(self) -> SecurityIdentifier: ...
    def GetConditions(self) -> ICollection: ...
    def GetExceptions(self) -> ICollection: ...
    def GetHashCode(self) -> int: ...
    @Action.setter
    def Action(self, value: AppLockerRuleActionType) -> None: ...
    @Description.setter
    def Description(self, value: str) -> None: ...
    @Id.setter
    def Id(self, value: Id) -> None: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    @UserOrGroupSid.setter
    def UserOrGroupSid(self, value: SecurityIdentifier) -> None: ...
    def ToXml(self) -> str: ...


class AppLockerRuleActionType:
    Allow = 0
    Deny = 1


class EnforcementMode:
    NotConfigured = 0
    Enabled = 1
    AuditOnly = 2


class ExecutionCategory(PolicyElement):
    def __init__(self): ...
    @property
    def Attributes(self) -> HashSet: ...
    @property
    def Id(self) -> Id: ...
    @property
    def PolicyIds(self) -> List: ...
    @Id.setter
    def Id(self, value: Id) -> None: ...


class FileHash(PolicyElement):
    @overload
    def __init__(self, data: Set(Byte)): ...
    @overload
    def __init__(self, data: str): ...
    @overload
    def __init__(self, type: FileHashType, data: Set(Byte)): ...
    @overload
    def __init__(self, type: FileHashType, data: str): ...
    def CompareTo(self, other: FileHash) -> int: ...
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    def Equals(self, other: FileHash) -> bool: ...
    @property
    def HashData(self) -> ICollection: ...
    @property
    def HashDataString(self) -> str: ...
    @property
    def HashType(self) -> FileHashType: ...
    @property
    def SourceFileLength(self) -> Int64: ...
    @property
    def SourceFileName(self) -> str: ...
    def GetHashCode(self) -> int: ...
    def op_Equality(hash1: FileHash, hash2: FileHash) -> bool: ...
    def op_GreaterThan(hash1: FileHash, hash2: FileHash) -> bool: ...
    def op_GreaterThanOrEqual(hash1: FileHash, hash2: FileHash) -> bool: ...
    def op_Inequality(hash1: FileHash, hash2: FileHash) -> bool: ...
    def op_LessThan(hash1: FileHash, hash2: FileHash) -> bool: ...
    def op_LessThanOrEqual(hash1: FileHash, hash2: FileHash) -> bool: ...
    @SourceFileLength.setter
    def SourceFileLength(self, value: Int64) -> None: ...
    @SourceFileName.setter
    def SourceFileName(self, value: str) -> None: ...
    def SetHash(self, type: FileHashType, data: Set(Byte)) -> None: ...
    def ToString(self) -> str: ...


class FileHashCondition(RuleCondition):
    def __init__(self): ...
    def AddHash(self, hash: FileHash) -> None: ...
    def DeleteHash(self, hash: FileHash) -> None: ...
    @property
    def Hashes(self) -> ICollection: ...
    def ToString(self) -> str: ...


class FileHashRule(AppLockerRule):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, id: Id, name: str, description: str, userOrGroupSid: SecurityIdentifier, action: AppLockerRuleActionType): ...
    @overload
    def AddCondition(self, condition: FileHashCondition) -> None: ...
    def DeleteConditions(self) -> None: ...
    def DeleteExceptions(self) -> None: ...
    def FromXml(xml: str) -> FileHashRule: ...
    @property
    def HashConditions(self) -> ICollection: ...
    def GetConditions(self) -> ICollection: ...
    def GetExceptions(self) -> ICollection: ...


class FileHashType:
    SHA256 = 0
    SHA256Flat = 1
    SHA1 = 2


class FileInformation:
    @overload
    def __init__(self, path: str): ...
    @overload
    def __init__(self, path: FilePath): ...
    @overload
    def __init__(self, path: FilePath, publisher: FilePublisher, hash: FileHash): ...
    @overload
    def __init__(self, path: FilePath, publisher: FilePublisher, hash: FileHash, appX: bool): ...
    def Clone(self) -> Object: ...
    def CompareTo(self, other: FileInformation) -> int: ...
    @overload
    def Equals(self, other: FileInformation) -> bool: ...
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @property
    def AppX(self) -> bool: ...
    @property
    def Hash(self) -> FileHash: ...
    @property
    def Path(self) -> FilePath: ...
    @property
    def Publisher(self) -> FilePublisher: ...
    def GetHashCode(self) -> int: ...
    def op_Equality(information1: FileInformation, information2: FileInformation) -> bool: ...
    def op_GreaterThan(information1: FileInformation, information2: FileInformation) -> bool: ...
    def op_GreaterThanOrEqual(information1: FileInformation, information2: FileInformation) -> bool: ...
    def op_Inequality(information1: FileInformation, information2: FileInformation) -> bool: ...
    def op_LessThan(information1: FileInformation, information2: FileInformation) -> bool: ...
    def op_LessThanOrEqual(information1: FileInformation, information2: FileInformation) -> bool: ...
    @AppX.setter
    def AppX(self, value: bool) -> None: ...
    @Hash.setter
    def Hash(self, value: FileHash) -> None: ...
    @Path.setter
    def Path(self, value: FilePath) -> None: ...
    @Publisher.setter
    def Publisher(self, value: FilePublisher) -> None: ...
    def ToString(self) -> str: ...


class FilePath(PolicyElement):
    def __init__(self, path: str): ...
    def CompareTo(self, other: FilePath) -> int: ...
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    def Equals(self, other: FilePath) -> bool: ...
    @property
    def Path(self) -> str: ...
    def GetHashCode(self) -> int: ...
    def op_Equality(path1: FilePath, path2: FilePath) -> bool: ...
    def op_GreaterThan(path1: FilePath, path2: FilePath) -> bool: ...
    def op_GreaterThanOrEqual(path1: FilePath, path2: FilePath) -> bool: ...
    def op_Inequality(path1: FilePath, path2: FilePath) -> bool: ...
    def op_LessThan(path1: FilePath, path2: FilePath) -> bool: ...
    def op_LessThanOrEqual(path1: FilePath, path2: FilePath) -> bool: ...
    @Path.setter
    def Path(self, value: str) -> None: ...
    def ToString(self) -> str: ...


class FilePathCondition(RuleCondition):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, path: FilePath): ...
    @property
    def Path(self) -> FilePath: ...
    @Path.setter
    def Path(self, value: FilePath) -> None: ...
    def ToString(self) -> str: ...


class FilePathRule(AppLockerRule):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, id: Id, name: str, description: str, userOrGroupSid: SecurityIdentifier, action: AppLockerRuleActionType): ...
    @overload
    def AddCondition(self, condition: FilePathCondition) -> None: ...
    @overload
    def AddException(self, exception: FilePathCondition) -> None: ...
    @overload
    def AddException(self, exception: FilePublisherCondition) -> None: ...
    @overload
    def AddException(self, exception: FileHashCondition) -> None: ...
    def DeleteConditions(self) -> None: ...
    def DeleteExceptions(self) -> None: ...
    def FromXml(xml: str) -> FilePathRule: ...
    @property
    def HashExceptions(self) -> ICollection: ...
    @property
    def PathConditions(self) -> ICollection: ...
    @property
    def PathExceptions(self) -> ICollection: ...
    @property
    def PublisherExceptions(self) -> ICollection: ...
    def GetConditions(self) -> ICollection: ...
    def GetExceptions(self) -> ICollection: ...


class FilePublisher:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, publisherName: str, productName: str, binaryName: str, binaryVersion: FileVersion): ...
    def Clone(self) -> Object: ...
    def CompareTo(self, other: FilePublisher) -> int: ...
    @overload
    def Equals(self, other: FilePublisher) -> bool: ...
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @property
    def BinaryName(self) -> str: ...
    @property
    def BinaryVersion(self) -> FileVersion: ...
    @property
    def HasBinaryName(self) -> bool: ...
    @property
    def HasProductName(self) -> bool: ...
    @property
    def HasPublisherName(self) -> bool: ...
    @property
    def ProductName(self) -> str: ...
    @property
    def PublisherName(self) -> str: ...
    def GetHashCode(self) -> int: ...
    def op_Equality(publisher1: FilePublisher, publisher2: FilePublisher) -> bool: ...
    def op_GreaterThan(publisher1: FilePublisher, publisher2: FilePublisher) -> bool: ...
    def op_GreaterThanOrEqual(publisher1: FilePublisher, publisher2: FilePublisher) -> bool: ...
    def op_Inequality(publisher1: FilePublisher, publisher2: FilePublisher) -> bool: ...
    def op_LessThan(publisher1: FilePublisher, publisher2: FilePublisher) -> bool: ...
    def op_LessThanOrEqual(publisher1: FilePublisher, publisher2: FilePublisher) -> bool: ...
    @BinaryName.setter
    def BinaryName(self, value: str) -> None: ...
    @BinaryVersion.setter
    def BinaryVersion(self, value: FileVersion) -> None: ...
    @ProductName.setter
    def ProductName(self, value: str) -> None: ...
    @PublisherName.setter
    def PublisherName(self, value: str) -> None: ...
    def ToString(self) -> str: ...


class FilePublisherCondition(RuleCondition):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, publisher: FilePublisher): ...
    @overload
    def __init__(self, publisherName: str, productName: str, binaryName: str, binaryVersionRange: FileVersionRange): ...
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
    def ToString(self) -> str: ...


class FilePublisherRule(AppLockerRule):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, id: Id, name: str, description: str, userOrGroupSid: SecurityIdentifier, action: AppLockerRuleActionType): ...
    @overload
    def AddCondition(self, condition: FilePublisherCondition) -> None: ...
    @overload
    def AddException(self, exception: FilePublisherCondition) -> None: ...
    @overload
    def AddException(self, exception: FilePathCondition) -> None: ...
    @overload
    def AddException(self, exception: FileHashCondition) -> None: ...
    def DeleteConditions(self) -> None: ...
    def DeleteExceptions(self) -> None: ...
    def FromXml(xml: str) -> FilePublisherRule: ...
    @property
    def HashExceptions(self) -> ICollection: ...
    @property
    def PathExceptions(self) -> ICollection: ...
    @property
    def PublisherConditions(self) -> ICollection: ...
    @property
    def PublisherExceptions(self) -> ICollection: ...
    def GetConditions(self) -> ICollection: ...
    def GetExceptions(self) -> ICollection: ...


class FileVersion:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, versionNumber: UInt64): ...
    @overload
    def __init__(self, version: str): ...
    @overload
    def __init__(self, majorPartNumber: int, minorPartNumber: int, buildPartNumber: int, privatePartNumber: int): ...
    def Clone(self) -> Object: ...
    def CompareTo(self, other: FileVersion) -> int: ...
    @overload
    def Equals(self, other: FileVersion) -> bool: ...
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @property
    def BuildPartNumber(self) -> int: ...
    @property
    def MajorPartNumber(self) -> int: ...
    @property
    def MinorPartNumber(self) -> int: ...
    @property
    def PrivatePartNumber(self) -> int: ...
    @property
    def VersionNumber(self) -> UInt64: ...
    def GetHashCode(self) -> int: ...
    def op_Equality(version1: FileVersion, version2: FileVersion) -> bool: ...
    def op_GreaterThan(version1: FileVersion, version2: FileVersion) -> bool: ...
    def op_GreaterThanOrEqual(version1: FileVersion, version2: FileVersion) -> bool: ...
    def op_Inequality(version1: FileVersion, version2: FileVersion) -> bool: ...
    def op_LessThan(version1: FileVersion, version2: FileVersion) -> bool: ...
    def op_LessThanOrEqual(version1: FileVersion, version2: FileVersion) -> bool: ...
    @BuildPartNumber.setter
    def BuildPartNumber(self, value: int) -> None: ...
    @MajorPartNumber.setter
    def MajorPartNumber(self, value: int) -> None: ...
    @MinorPartNumber.setter
    def MinorPartNumber(self, value: int) -> None: ...
    @PrivatePartNumber.setter
    def PrivatePartNumber(self, value: int) -> None: ...
    @VersionNumber.setter
    def VersionNumber(self, value: UInt64) -> None: ...
    def ToString(self) -> str: ...


class FileVersionRange(PolicyElement):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, fileVersion: FileVersion): ...
    @overload
    def __init__(self, lowSection: FileVersion, highSection: FileVersion): ...
    def CompareTo(self, other: FileVersionRange) -> int: ...
    @overload
    def Equals(self, other: FileVersionRange) -> bool: ...
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @property
    def HighSection(self) -> FileVersion: ...
    @property
    def LowSection(self) -> FileVersion: ...
    def GetHashCode(self) -> int: ...
    def op_Equality(range1: FileVersionRange, range2: FileVersionRange) -> bool: ...
    def op_GreaterThan(range1: FileVersionRange, range2: FileVersionRange) -> bool: ...
    def op_GreaterThanOrEqual(range1: FileVersionRange, range2: FileVersionRange) -> bool: ...
    def op_Inequality(range1: FileVersionRange, range2: FileVersionRange) -> bool: ...
    def op_LessThan(range1: FileVersionRange, range2: FileVersionRange) -> bool: ...
    def op_LessThanOrEqual(range1: FileVersionRange, range2: FileVersionRange) -> bool: ...
    @HighSection.setter
    def HighSection(self, value: FileVersion) -> None: ...
    @LowSection.setter
    def LowSection(self, value: FileVersion) -> None: ...
    def ToString(self) -> str: ...


class Id:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, value: Guid): ...
    def Clone(self) -> Object: ...
    def CompareTo(self, other: Id) -> int: ...
    @overload
    def Equals(self, other: Id) -> bool: ...
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @property
    def Empty(self) -> bool: ...
    @property
    def Value(self) -> Guid: ...
    def GetHashCode(self) -> int: ...
    def NewId() -> Id: ...
    def op_Equality(id1: Id, id2: Id) -> bool: ...
    def op_GreaterThan(id1: Id, id2: Id) -> bool: ...
    def op_GreaterThanOrEqual(id1: Id, id2: Id) -> bool: ...
    def op_Inequality(id1: Id, id2: Id) -> bool: ...
    def op_LessThan(id1: Id, id2: Id) -> bool: ...
    def op_LessThanOrEqual(id1: Id, id2: Id) -> bool: ...
    @Value.setter
    def Value(self, value: Guid) -> None: ...
    def ToString(self) -> str: ...


class InvalidPolicyElementException(PolicyModelException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class InvalidXmlPolicyException(PolicyModelException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, reason: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class Plugin(PolicyElement):
    def __init__(self): ...
    @property
    def ExecutionCategories(self) -> List: ...
    @property
    def Id(self) -> Id: ...
    @property
    def Name(self) -> str: ...
    @Id.setter
    def Id(self, value: Id) -> None: ...
    @Name.setter
    def Name(self, value: str) -> None: ...


class PolicyElement(XmlSerializer):
    def Clone(self) -> Object: ...
    def Compare(element1: T, element2: T) -> int: ...


class PolicyMergingException(PolicyModelException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, reason: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class PolicyModelException:
    pass


class RuleAlreadyExistsException(PolicyModelException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class RuleCollection(PolicyElement):
    @overload
    def __init__(self, type: str): ...
    @overload
    def __init__(self, type: str, enforcementMode: EnforcementMode, serviceEnforcementMode: ServiceEnforcementMode, systemAppAllowMode: SystemAppAllowMode, currentOriginDataId: int, trustedOriginDataId: int): ...
    def Add(self, rule: AppLockerRule) -> None: ...
    def Delete(self, ruleId: Id) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def CurrentOriginDataId(self) -> int: ...
    @property
    def Empty(self) -> bool: ...
    @property
    def EnforcementMode(self) -> EnforcementMode: ...
    @property
    def RuleCollectionType(self) -> str: ...
    def Get(self, ruleId: Id) -> AppLockerRule: ...
    @property
    def ServiceEnforcementMode(self) -> ServiceEnforcementMode: ...
    @property
    def SystemAppAllowMode(self) -> SystemAppAllowMode: ...
    @property
    def TrustedOriginDataId(self) -> int: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def Has(self, ruleId: Id) -> bool: ...
    @CurrentOriginDataId.setter
    def CurrentOriginDataId(self, value: int) -> None: ...
    @EnforcementMode.setter
    def EnforcementMode(self, value: EnforcementMode) -> None: ...
    @ServiceEnforcementMode.setter
    def ServiceEnforcementMode(self, value: ServiceEnforcementMode) -> None: ...
    @SystemAppAllowMode.setter
    def SystemAppAllowMode(self, value: SystemAppAllowMode) -> None: ...
    @TrustedOriginDataId.setter
    def TrustedOriginDataId(self, value: int) -> None: ...


class RuleCollectionAlreadyExistsException(PolicyModelException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class RuleCollectionDoesNotExistException(PolicyModelException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class RuleCondition(PolicyElement):
    pass


class RuleConditionIsNotSupportedException(PolicyModelException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class RuleDoesNotExistException(PolicyModelException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class RuleExceptionIsNotSupportedException(PolicyModelException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class ServiceEnforcementMode:
    NotConfigured = 0
    Enabled = 1
    ServicesOnly = 2


class SystemAppAllowMode:
    NotEnabled = 0
    Enabled = 1


class XmlSerializer:
    pass
