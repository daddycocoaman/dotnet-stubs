from typing import Tuple, Set, Iterable, List


class AddInController(Object):
    @property
    def AddInEnvironment(self) -> AddInEnvironment: ...
    @property
    def AppDomain(self) -> AppDomain: ...
    @property
    def Token(self) -> AddInToken: ...
    def GetAddInController(addIn: Object) -> AddInController: ...
    def Shutdown(self) -> None: ...


class AddInEnvironment(Object):
    def __init__(self, appDomain: AppDomain): ...
    @property
    def Process(self) -> AddInProcess: ...


class AddInProcess(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, platform: Platform): ...
    def add_ShuttingDown(self, value: EventHandler) -> None: ...
    @property
    def IsCurrentProcess(self) -> bool: ...
    @property
    def KeepAlive(self) -> bool: ...
    @property
    def Platform(self) -> Platform: ...
    @property
    def ProcessId(self) -> int: ...
    @property
    def StartupTimeout(self) -> TimeSpan: ...
    def remove_ShuttingDown(self, value: EventHandler) -> None: ...
    @KeepAlive.setter
    def KeepAlive(self, value: bool) -> None: ...
    @StartupTimeout.setter
    def StartupTimeout(self, value: TimeSpan) -> None: ...
    def Shutdown(self) -> bool: ...
    def Start(self) -> bool: ...


class AddInSecurityLevel:
    Internet = 0
    Intranet = 1
    FullTrust = 2
    Host = 3


class AddInSegmentDirectoryNotFoundException(Exception):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class AddInSegmentType:
    HostViewOfAddIn = 0
    HostSideAdapter = 1
    Contract = 2
    AddInSideAdapter = 3
    AddInView = 4
    AddIn = 5


class AddInStore(Object):
    def FindAddIn(hostViewOfAddIn: Type, pipelineRootFolderPath: str, addInFilePath: str, addInTypeName: str) -> Collection: ...
    @overload
    def FindAddIns(hostViewOfAddIn: Type, location: PipelineStoreLocation) -> Collection: ...
    @overload
    def FindAddIns(hostViewOfAddIn: Type, location: PipelineStoreLocation, addInFolderPaths: Set(str)) -> Collection: ...
    @overload
    def FindAddIns(hostViewOfAddIn: Type, pipelineRootFolderPath: str, addInFolderPaths: Set(str)) -> Collection: ...
    @overload
    def Rebuild(pipelineRootFolderPath: str) -> Set(str): ...
    @overload
    def Rebuild(location: PipelineStoreLocation) -> Set(str): ...
    def RebuildAddIns(addInsFolderPath: str) -> Set(str): ...
    @overload
    def Update(location: PipelineStoreLocation) -> Set(str): ...
    @overload
    def Update(pipelineRootFolderPath: str) -> Set(str): ...
    def UpdateAddIns(addInsFolderPath: str) -> Set(str): ...


class AddInToken(Object):
    @overload
    def Activate(self, permissions: PermissionSet) -> T: ...
    @overload
    def Activate(self, target: AppDomain) -> T: ...
    @overload
    def Activate(self, trustLevel: AddInSecurityLevel) -> T: ...
    @overload
    def Activate(self, environment: AddInEnvironment) -> T: ...
    @overload
    def Activate(self, process: AddInProcess, level: AddInSecurityLevel) -> T: ...
    @overload
    def Activate(self, process: AddInProcess, permissionSet: PermissionSet) -> T: ...
    @overload
    def Activate(self, trustLevel: AddInSecurityLevel, appDomainName: str) -> T: ...
    def Equals(self, obj: Object) -> bool: ...
    @property
    def AddInFullName(self) -> str: ...
    @property
    def AssemblyName(self) -> AssemblyName: ...
    @property
    def Description(self) -> str: ...
    @property
    def EnableDirectConnect() -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def Publisher(self) -> str: ...
    @property
    def QualificationData(self) -> IDictionary: ...
    @property
    def Version(self) -> str: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def GetHashCode(self) -> int: ...
    @EnableDirectConnect.setter
    def EnableDirectConnect(value: bool) -> None: ...
    def ToString(self) -> str: ...


class InvalidPipelineStoreException(Exception):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class PipelineStoreLocation:
    ApplicationBase = 0


class Platform:
    Host = 0
    AnyCpu = 1
    X86 = 2
    X64 = 3
    ARM = 4


class QualificationDataItem(ValueType):
    def Equals(self, obj: Object) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def Segment(self) -> AddInSegmentType: ...
    @property
    def Value(self) -> str: ...
    def GetHashCode(self) -> int: ...
    def op_Equality(item1: QualificationDataItem, item2: QualificationDataItem) -> bool: ...
    def op_Inequality(item1: QualificationDataItem, item2: QualificationDataItem) -> bool: ...
