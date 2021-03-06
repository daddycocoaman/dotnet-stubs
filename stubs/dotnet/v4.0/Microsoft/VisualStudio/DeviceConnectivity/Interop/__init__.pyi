from typing import Tuple, Set, Iterable, List


class _FILETIME:
    pass


class _ICcDatastoreEvents:
    pass


class _ICcDatastoreEvents_Event:
    pass


class _ICcDatastoreEvents_SinkHelper:
    pass


class _SYSTEMTIME:
    pass


class CcBootStrapper:
    pass


class CcBootStrapperClass:
    def __init__(self): ...
    def Abort(self, dwCookieId: UInt32) -> None: ...
    def Connect(self, dwTimeout: UInt32, bAsync: bool) -> UInt32: ...
    def Disconnect(self) -> None: ...
    def Download(self, dwTimeout: UInt32, bAsync: bool, wszSrcFullPath: str, wszDestFullPath: str, bOverwrite: bool) -> UInt32: ...
    def GetCurrentState(self) -> UInt32: ...
    def GetDeviceInfo(self, diRequested: DeviceInfo) -> UInt32: ...
    def GetFile(self, dwTimeout: UInt32, wszSrcFullPath: str, wszDestFullPath: str, bOverwrite: bool) -> None: ...
    def GetFileInfo(self, wszDeviceFile: str) -> tagFileInfox: ...
    def Initialize(self, pszLocalBindingIp: str, portConnectTo: UInt16, portEchoTo: UInt16, pszConnectToIp: str) -> None: ...
    def Launch(self, bstrCommand: str, bstrArguments: str, dwLaunchFlags: UInt32) -> None: ...
    def LockService(self) -> None: ...
    def UnlockService(self) -> None: ...


class CcCollection:
    pass


class CcCollectionClass:
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, index: int) -> CcDatastorePrivate: ...
    def GetEnumerator(self) -> IEnumerator: ...


class CcDatastore:
    pass


class CcDatastoreClass:
    @property
    def DeviceContainer(self) -> ICcDeviceContainer: ...
    @property
    def OSImageContainer(self) -> ICcOSImageContainer: ...
    @property
    def PackageContainer(self) -> ICcPackageContainer: ...
    @property
    def PlatformContainer(self) -> ICcPlatformContainer: ...
    @property
    def PropertyContainer(self) -> ICcPropertyContainer: ...
    @property
    def ServiceCategoryContainer(self) -> ICcServiceCategoryContainer: ...
    @property
    def Version(self) -> str: ...
    def RegisterRefreshEvent(self, EventName: str) -> None: ...
    def Save(self) -> None: ...
    def UnregisterRefreshEvent(self) -> None: ...


class CcDatastoreErrorCodes:
    pass


class CcDatastorePrivate:
    pass


class CcDatastorePrivateClass:
    def AddObject(self, in_bstrID: str, in_bstrName: str) -> CcDatastorePrivate: ...
    def AddPropertyContainer(self) -> None: ...
    def DeleteObject(self, in_bstrID: str) -> None: ...
    def EnumerateObjects(self) -> CcCollection: ...
    def FindObject(self, in_bstrID: str) -> CcDatastorePrivate: ...
    @property
    def DeviceContainer(self) -> ICcDeviceContainer: ...
    @property
    def FormFactorContainer(self) -> ICcFormFactorContainer: ...
    @property
    def ID(self) -> str: ...
    @property
    def IsProtected(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def ProjectContainer(self) -> ICcProjectContainer: ...
    @property
    def PropertyContainer(self) -> ICcPropertyContainer: ...
    @property
    def TypeToArchitectureMap(self) -> ICcTypeToArchitectureMap: ...
    @property
    def Value(self) -> str: ...
    @Name.setter
    def Name(self, out_pbstrName: str) -> None: ...
    @Value.setter
    def Value(self, out_pbstrVal: str) -> None: ...


class CcPhoneTargetDevice:
    pass


class CcPhoneTargetDeviceClass:
    def __init__(self): ...
    def BringToFront(self) -> None: ...
    def GetMappedIpPortFromRemotePort(self, remotePort: UInt16) -> Tuple[str, UInt16, str]: ...
    def GetMappedIpPortFromServiceProperty(self, pPropHelper: ICcPropertyHelper) -> Tuple[str, UInt16, UInt16, str]: ...
    def Initialize(self, pPropHelper: ICcPropertyHelper) -> None: ...
    def RegisterForDeviceNotifications(self, pDeviceEventNotifier: IDeviceEventNotifier) -> None: ...
    def UnRegisterForDeviceNotifications(self, pDeviceEventNotifier: IDeviceEventNotifier) -> None: ...


class CcTcpTransportConnect:
    pass


class CcTcpTransportConnectClass:
    def __init__(self): ...
    def Abort(self, dwCookieId: UInt32) -> None: ...
    def Connect(self, dwTimeout: UInt32, bAsync: bool) -> UInt32: ...
    def CreateStream(self, wszStreamId: str, dwTimeout: UInt32, bAsync: bool) -> ICcTransportStream: ...
    def Disconnect(self) -> None: ...
    @property
    def Bandwidth(self) -> UInt32: ...
    @property
    def MTU(self) -> UInt32: ...
    @property
    def SupportsNonUniqueStreamId(self) -> bool: ...
    def GetCurrentState(self) -> UInt32: ...
    def Initialize(self, pszLocalBindingIp: str, portConnectTo: UInt16, portEchoTo: UInt16, pszConnectToIp: str) -> None: ...
    def LockService(self) -> None: ...
    def UnlockService(self) -> None: ...


class CcXDEBootstrap:
    pass


class CcXDEBootstrapClass:
    def __init__(self): ...
    def Abort(self, dwCookieId: UInt32) -> None: ...
    def Connect(self, dwTimeout: UInt32, bAsync: bool) -> UInt32: ...
    def Disconnect(self) -> None: ...
    def Download(self, dwTimeout: UInt32, bAsync: bool, wszSrcFullPath: str, wszDestFullPath: str, bOverwrite: bool) -> UInt32: ...
    def GetCurrentState(self) -> UInt32: ...
    def GetDeviceInfo(self, diRequested: DeviceInfo) -> UInt32: ...
    def GetFile(self, dwTimeout: UInt32, wszSrcFullPath: str, wszDestFullPath: str, bOverwrite: bool) -> None: ...
    def GetFileInfo(self, wszDeviceFile: str) -> tagFileInfox: ...
    def Initialize(self, pszLocalBindingIp: str, portConnectTo: UInt16, portEchoTo: UInt16, pszConnectToIp: str) -> None: ...
    def Launch(self, bstrCommand: str, bstrArguments: str, dwLaunchFlags: UInt32) -> None: ...
    def LockService(self) -> None: ...
    def UnlockService(self) -> None: ...


class CcXDEDMATransportConnect:
    pass


class CcXDEDMATransportConnectClass:
    def __init__(self): ...
    def Abort(self, dwCookieId: UInt32) -> None: ...
    def Connect(self, dwTimeout: UInt32, bAsync: bool) -> UInt32: ...
    def CreateStream(self, wszStreamId: str, dwTimeout: UInt32, bAsync: bool) -> ICcTransportStream: ...
    def Disconnect(self) -> None: ...
    @property
    def Bandwidth(self) -> UInt32: ...
    @property
    def MTU(self) -> UInt32: ...
    @property
    def SupportsNonUniqueStreamId(self) -> bool: ...
    def GetCurrentState(self) -> UInt32: ...
    def Initialize(self, pszLocalBindingIp: str, portConnectTo: UInt16, portEchoTo: UInt16, pszConnectToIp: str) -> None: ...
    def LockService(self) -> None: ...
    def UnlockService(self) -> None: ...


class CcXDETargetDevice:
    pass


class CcXDETargetDeviceClass:
    def __init__(self): ...
    def BringToFront(self) -> None: ...
    def GetMappedIpPortFromRemotePort(self, remotePort: UInt16) -> Tuple[str, UInt16, str]: ...
    def GetMappedIpPortFromServiceProperty(self, pPropHelper: ICcPropertyHelper) -> Tuple[str, UInt16, UInt16, str]: ...
    def Initialize(self, pPropHelper: ICcPropertyHelper) -> None: ...
    def RegisterForDeviceNotifications(self, pDeviceEventNotifier: IDeviceEventNotifier) -> None: ...
    def UnRegisterForDeviceNotifications(self, pDeviceEventNotifier: IDeviceEventNotifier) -> None: ...


class ConMan:
    pass


class ConManClass:
    def __init__(self): ...
    def CreateNewServerGuid(self, in_piDevice: ICcDevice, in_bstrEndPoint: str) -> Tuple[Guid]: ...
    def Datastore(self) -> Tuple[CcDatastore]: ...
    def EnumerateConnections(self, dwSizeActual: UInt32) -> Tuple[bool, UInt32, ConMan]: ...
    def EnumerateConnections2(self) -> Array: ...
    def EnumerateServerGuids(self, in_ArraySize: UInt32) -> Tuple[UInt32, Guid, int]: ...
    @property
    def Locale(self) -> UInt32: ...
    def GetConnection(self, piDevice: ICcDevice, dwTimeout: UInt32, piCallback: ICcServiceCB) -> Tuple[ConManServer, str]: ...
    def GetConnectionFromId(self, bstrConnectionId: str) -> ConManServer: ...
    def GetDatastore(self, dwLocale: UInt32) -> CcDatastore: ...
    def GetDeviceFromServerGuid(self, in_guidServer: Guid) -> Tuple[Guid, ICcDevice]: ...
    def GetServerFromServerGuid(self, in_guidServer: Guid) -> Tuple[Guid, IConManServer]: ...
    def GetServerGuidInfo(self, in_guidServer: Guid) -> Tuple[Guid, str]: ...
    @Locale.setter
    def Locale(self, pdwLocale: UInt32) -> None: ...
    def SetLocale(self, in_dwLangID: UInt32) -> None: ...
    def SetRegistryRoot(self, in_bstrRegistryRoot: str) -> None: ...


class ConManServer:
    pass


class ConManServerClass:
    def __init__(self): ...
    def AbortConnect(self) -> None: ...
    def AbortSend(self) -> None: ...
    def ActivateDevice(self) -> None: ...
    def CloseProcessHandle(self, in_ProcessHandle: UInt32) -> None: ...
    def Connect(self) -> None: ...
    def ConnectDevice(self) -> None: ...
    def CreateRemoteServiceStream(self, bstrServiceId: str, dwTimeout: UInt32) -> ICcTransportStream: ...
    def CreateStream(self, bstrStreamId: str, dwTimeout: UInt32, piCallback: ICcServiceCB) -> Tuple[ICcTransportStream, UInt32]: ...
    def DeleteDirectory(self, in_szDeviceDirectory: str, bRemoveAll: bool) -> None: ...
    def DeployPackage(self, serviceId: str, cmdLineAnnex: str, flags: int) -> None: ...
    def DisconnectDevice(self) -> None: ...
    def DownloadPackage(self, pwszPackageId: str) -> None: ...
    def EnumerateProcesses(self) -> Tuple[Array, Array]: ...
    @property
    def DeviceId(self) -> str: ...
    @property
    def Transport(self) -> ICcTransport: ...
    def GetApplicationType(self, in_pProductId: str) -> UInt32: ...
    def GetDirectoryListing(self, in_szSoureDeviceDirPath: str) -> Array: ...
    def GetEndPoints(self, servicePort: int) -> Tuple[str, str, int]: ...
    def GetFileInfo(self, in_szDeviceFile: str) -> Tuple[tagFileInfo]: ...
    def GetInstalledApplicationCount(self) -> int: ...
    def GetInstalledApplicationIDs(self) -> Tuple[Array, Array]: ...
    def GetInstalledFileInfo(self, in_pProductId: str, in_bstrFileRelativePath: str) -> tagFileInfo: ...
    def GetProcessExitCode(self, in_ProcessID: UInt32) -> Tuple[bool, UInt32]: ...
    def GetServiceStreamId(self, serviceId: str) -> str: ...
    def GetSystemInfo(self) -> Tuple[tagPlatformInfo]: ...
    def GetSystemInfoEx(self) -> Tuple[tagSystemInfoEx]: ...
    def GetTransmitionInfo(self) -> Tuple[tagTransactionInfo]: ...
    def GetUapVersionInfo(self) -> Tuple[tagUapVersionInfo]: ...
    def IConManServerCore_AbortConnect(self) -> None: ...
    def IConManServerCore_Connect(self) -> None: ...
    def IConManServerCore_GetTransmitionInfo(self) -> Tuple[tagTransactionInfo]: ...
    def IConManServerCore_InitEx(self, in_pDevice: ICcDevice, in_pDatastore: CcDatastore) -> None: ...
    def IConManServerCore_IsConnected(self) -> Tuple[int]: ...
    def IConManServerCore_RegisterCallback(self, in_pServerCallback: IConManServerCallback, in_CallbackFilter: UInt32) -> None: ...
    def IConManServerCore_UnregisterCallback(self, in_pServerCallback: IConManServerCallback) -> None: ...
    def InitEx(self, in_pDevice: ICcDevice, in_pDatastore: CcDatastore) -> None: ...
    def InitEx2(self, in_pDevice: ICcDevice, in_pDatastore: CcDatastore, in_lcid: UInt32) -> None: ...
    def InitEx3(self, in_pDevice: ICcDevice, in_pDatastore: CcDatastore, in_lcid: UInt32, in_bstrSirepClientManifest: str) -> None: ...
    def InstallApplication(self, in_pProductId: str, in_pInstanceId: str, in_bstrApplicationGenre: str, in_bstrAppIconPath: str, in_bstrXapPath: str) -> None: ...
    def IsApplicationInstalled(self, in_pProductId: str) -> bool: ...
    def IsApplicationRunning(self, in_pProductId: str) -> bool: ...
    @overload
    def IsConnected(self) -> bool: ...
    @overload
    def IsConnected(self) -> Tuple[int]: ...
    def LaunchApplication(self, in_pProductId: str) -> UInt32: ...
    def LaunchApplicationWithService(self, in_pProductId: str, in_bstrServiceInfo: str) -> None: ...
    def LaunchProcess(self, in_szExecutable: str, in_szArgument: str, in_CreationFlags: UInt32) -> Tuple[UInt32, UInt32]: ...
    def MakeDirectory(self, in_szDeviceDirectory: str) -> None: ...
    def ProvisionDeviceXML(self, pszWXMLin: str, in_Flags: UInt32, in_DllNameName: str) -> Tuple[str]: ...
    def ReceiveFile(self, in_szDeviceFile: str, in_szDesktopFile: str, CreationDisposition: UInt32) -> None: ...
    def RegisterCallback(self, in_pServerCallback: IConManServerCallback, in_CallbackFilter: UInt32) -> None: ...
    def RegisterNotifyCallback(self, pCallBack: ICcServiceCB) -> None: ...
    def RegistryCreateKey(self, hKey: int, lpSubKey: str) -> None: ...
    def RegistryDeleteKey(self, hKey: int, lpSubKey: str) -> None: ...
    def RegistryDeleteValue(self, hKey: int, lpSubKey: str, lpValueName: str) -> None: ...
    def RegistryQueryValue(self, hKey: int, lpSubKey: str, lpValueName: str) -> Tuple[UInt32, ConManServer, UInt32]: ...
    def RegistrySetValue(self, hKey: int, lpSubKey: str, lpValueName: str, dwType: UInt32, lpData: Byte, cbData: UInt32) -> Tuple[Byte]: ...
    def RemoveFile(self, in_szDeviceFile: str) -> None: ...
    def SearchFileSystem(self, in_Criteria: str, in_StartingDirectory: str) -> Tuple[Array]: ...
    def SendFile(self, in_szDesktopFile: str, in_szDeviceFile: str, CreationDisposition: UInt32, in_FileCustomAction: tagFileCustomAction) -> None: ...
    def SetFileInfo(self, in_szDeviceFile: str, in_pFileInfo: tagFileInfo) -> Tuple[tagFileInfo]: ...
    def SetSQMProviderInterface(self, in_pSqmCallback: Object) -> None: ...
    def TerminateProcess(self, in_ProcessID: UInt32) -> None: ...
    def TerminateRunningApplicationInstances(self, in_pProductId: str) -> None: ...
    def UninstallApplication(self, in_pProductId: str) -> None: ...
    def UnregisterCallback(self, in_pServerCallback: IConManServerCallback) -> None: ...
    def UnregisterNotifyCallback(self, in_pServerCallback: ICcServiceCB) -> None: ...
    def UpdateApplication(self, in_pProductId: str, in_pInstanceId: str, in_bstrApplicationGenre: str, in_bstrAppIconPath: str, in_bstrXapPath: str) -> None: ...
    def UpdateInstalledFile(self, in_pProductId: str, in_bstrFileRelativePath: str, in_bstrSourceFilePath: str, in_fUpdateFileInfo: bool) -> None: ...
    def UpdateInstalledFiles(self, in_pProductId: str, in_FileNames: Array, in_XapDeviceRelativePaths: Array) -> Tuple[UInt32, Array, Array]: ...
    def UpdateInstalledFilesInfo(self, in_pProductId: str, in_FileNames: Array, in_XapDeviceRelativePaths: Array) -> Tuple[Array, Array]: ...
    def VerifyFilesInstalled(self, in_ArraySize: UInt32, in_InfoArray: ConManServer) -> Tuple[ConManServer]: ...


class DeviceInfo:
    SYSTEM_INFO_PROCESSOR_ARCHITECTURE = 0


class DevicePackage:
    pass


class DevicePackageClass:
    def __init__(self): ...
    def AbortConnectToDevice(self) -> None: ...
    def AdviseDevicePackageCallback(self, in_pDevicePackageCallBack: IDevicePackageCallback) -> None: ...
    def CancelDeploySession(self) -> None: ...
    def ConnectToDevice(self, in_bstrPlatform: str, in_bstrDevice: str) -> None: ...
    @property
    def ServerGuid(self) -> str: ...
    def GetDebugEngineCount(self, in_bstrDebugLaunchTypeGuid: str, in_bstrRuntimeVersion: str) -> Tuple[UInt32]: ...
    def GetDebugLaunchInfo(self, in_bstrDebugLaunchTypeGuid: str, in_bstrRuntimeVersion: str, in_DebugEngineGuidArraySize: UInt32) -> Tuple[DevicePackage, UInt32, Guid]: ...
    def GetSystemInfo(self) -> Tuple[tagPlatformInfo]: ...
    def Launch(self, in_bstrEXE: str, in_bstrARGS: str) -> Tuple[UInt32]: ...
    def ProvisionDeviceXML(self, pszWXMLin: str, in_Flags: UInt32, in_DllNameName: str) -> Tuple[str]: ...
    @Locale.setter
    def Locale(self, A_1: UInt16) -> None: ...
    def SetVsProviderInterface(self, in_pVsProvider: Object) -> None: ...
    def StartDeploySession(self, in_pEnumReferences: IEnumReferences, in_InstructionSet: UInt32) -> Tuple[UInt32]: ...
    def UnadviseDevicePackageCallback(self, in_pDevicePackageCallBack: IDevicePackageCallback) -> None: ...


class ICcBootstrap:
    def Download(self, dwTimeout: UInt32, bAsync: bool, wszSrcFullPath: str, wszDestFullPath: str, bOverwrite: bool) -> UInt32: ...
    def GetDeviceInfo(self, diRequested: DeviceInfo) -> UInt32: ...
    def GetFile(self, dwTimeout: UInt32, wszSrcFullPath: str, wszDestFullPath: str, bOverwrite: bool) -> None: ...
    def GetFileInfo(self, wszDeviceFile: str) -> tagFileInfox: ...
    def Launch(self, bstrCommand: str, bstrArguments: str, dwLaunchFlags: UInt32) -> None: ...


class ICcCollection:
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, index: int) -> CcDatastorePrivate: ...
    def GetEnumerator(self) -> IEnumerator: ...


class ICcConnection:
    def CloseProcessHandle(self, in_ProcessHandle: UInt32) -> None: ...
    def ConnectDevice(self) -> None: ...
    def CreateStream(self, bstrStreamId: str, dwTimeout: UInt32, piCallback: ICcServiceCB) -> Tuple[ICcTransportStream, UInt32]: ...
    def DeleteDirectory(self, in_szDeviceDirectory: str, bRemoveAll: bool) -> None: ...
    def DisconnectDevice(self) -> None: ...
    def DownloadPackage(self, pwszPackageId: str) -> None: ...
    def EnumerateProcesses(self) -> Tuple[Array, Array]: ...
    @property
    def DeviceId(self) -> str: ...
    def GetFileInfo(self, in_szDeviceFile: str) -> Tuple[tagFileInfo]: ...
    def GetProcessExitCode(self, in_ProcessID: UInt32) -> Tuple[bool, UInt32]: ...
    def GetSystemInfo(self) -> Tuple[tagPlatformInfo]: ...
    def IsConnected(self) -> bool: ...
    def LaunchProcess(self, in_szExecutable: str, in_szArgument: str, in_CreationFlags: UInt32) -> Tuple[UInt32, UInt32]: ...
    def MakeDirectory(self, in_szDeviceDirectory: str) -> None: ...
    def ReceiveFile(self, in_szDeviceFile: str, in_szDesktopFile: str, CreationDisposition: UInt32) -> None: ...
    def RegistryCreateKey(self, hKey: int, lpSubKey: str) -> None: ...
    def RegistryDeleteKey(self, hKey: int, lpSubKey: str) -> None: ...
    def RegistryDeleteValue(self, hKey: int, lpSubKey: str, lpValueName: str) -> None: ...
    def RegistryQueryValue(self, hKey: int, lpSubKey: str, lpValueName: str) -> Tuple[UInt32, ConManServer, UInt32]: ...
    def RegistrySetValue(self, hKey: int, lpSubKey: str, lpValueName: str, dwType: UInt32, lpData: Byte, cbData: UInt32) -> Tuple[Byte]: ...
    def RemoveFile(self, in_szDeviceFile: str) -> None: ...
    def SearchFileSystem(self, in_Criteria: str, in_StartingDirectory: str) -> Tuple[Array]: ...
    def SendFile(self, in_szDesktopFile: str, in_szDeviceFile: str, CreationDisposition: UInt32, in_FileCustomAction: tagFileCustomAction) -> None: ...
    def SetFileInfo(self, in_szDeviceFile: str, in_pFileInfo: tagFileInfo) -> Tuple[tagFileInfo]: ...
    def TerminateProcess(self, in_ProcessID: UInt32) -> None: ...
    def VerifyFilesInstalled(self, in_ArraySize: UInt32, in_InfoArray: ConManServer) -> Tuple[ConManServer]: ...


class ICcConnection2:
    def AbortSend(self) -> None: ...
    def CreateRemoteServiceStream(self, bstrServiceId: str, dwTimeout: UInt32) -> ICcTransportStream: ...
    def DeployPackage(self, serviceId: str, cmdLineAnnex: str, flags: int) -> None: ...
    @property
    def Transport(self) -> ICcTransport: ...
    def GetServiceStreamId(self, serviceId: str) -> str: ...
    def GetSystemInfoEx(self) -> Tuple[tagSystemInfoEx]: ...
    def ProvisionDeviceXML(self, pszWXMLin: str, in_Flags: UInt32, in_DllNameName: str) -> Tuple[str]: ...
    def RegisterNotifyCallback(self, pCallBack: ICcServiceCB) -> None: ...
    def SetSQMProviderInterface(self, in_pSqmCallback: Object) -> None: ...
    def UnregisterNotifyCallback(self, in_pServerCallback: ICcServiceCB) -> None: ...


class ICcConnection3:
    def ActivateDevice(self) -> None: ...
    def GetInstalledApplicationCount(self) -> int: ...
    def GetInstalledApplicationIDs(self) -> Tuple[Array, Array]: ...
    def GetInstalledFileInfo(self, in_pProductId: str, in_bstrFileRelativePath: str) -> tagFileInfo: ...
    def InstallApplication(self, in_pProductId: str, in_pInstanceId: str, in_bstrApplicationGenre: str, in_bstrAppIconPath: str, in_bstrXapPath: str) -> None: ...
    def IsApplicationInstalled(self, in_pProductId: str) -> bool: ...
    def IsApplicationRunning(self, in_pProductId: str) -> bool: ...
    def LaunchApplication(self, in_pProductId: str) -> UInt32: ...
    def LaunchApplicationWithService(self, in_pProductId: str, in_bstrServiceInfo: str) -> None: ...
    def TerminateRunningApplicationInstances(self, in_pProductId: str) -> None: ...
    def UninstallApplication(self, in_pProductId: str) -> None: ...
    def UpdateApplication(self, in_pProductId: str, in_pInstanceId: str, in_bstrApplicationGenre: str, in_bstrAppIconPath: str, in_bstrXapPath: str) -> None: ...
    def UpdateInstalledFile(self, in_pProductId: str, in_bstrFileRelativePath: str, in_bstrSourceFilePath: str, in_fUpdateFileInfo: bool) -> None: ...
    def UpdateInstalledFiles(self, in_pProductId: str, in_FileNames: Array, in_XapDeviceRelativePaths: Array) -> Tuple[UInt32, Array, Array]: ...
    def UpdateInstalledFilesInfo(self, in_pProductId: str, in_FileNames: Array, in_XapDeviceRelativePaths: Array) -> Tuple[Array, Array]: ...


class ICcConnection4:
    def GetApplicationType(self, in_pProductId: str) -> UInt32: ...
    def GetDirectoryListing(self, in_szSoureDeviceDirPath: str) -> Array: ...
    def GetEndPoints(self, servicePort: int) -> Tuple[str, str, int]: ...


class ICcConnection5:
    def GetUapVersionInfo(self) -> Tuple[tagUapVersionInfo]: ...


class ICcDatastore:
    @property
    def DeviceContainer(self) -> ICcDeviceContainer: ...
    @property
    def OSImageContainer(self) -> ICcOSImageContainer: ...
    @property
    def PackageContainer(self) -> ICcPackageContainer: ...
    @property
    def PlatformContainer(self) -> ICcPlatformContainer: ...
    @property
    def PropertyContainer(self) -> ICcPropertyContainer: ...
    @property
    def ServiceCategoryContainer(self) -> ICcServiceCategoryContainer: ...
    @property
    def Version(self) -> str: ...
    def RegisterRefreshEvent(self, EventName: str) -> None: ...
    def Save(self) -> None: ...
    def UnregisterRefreshEvent(self) -> None: ...


class ICcDevice:
    def ClearOSImage(self) -> None: ...
    def ClearServiceMap(self, in_bstrServiceCategoryID: str) -> None: ...
    def GetOSImage(self) -> ICcOSImage: ...
    def GetServiceMap(self, in_bstrServiceCategoryID: str) -> ICcServiceInfo: ...
    def SetOSImage(self, in_bstrOSImage: str) -> None: ...
    def SetServiceMap(self, in_bstrServiceCategoryID: str, in_bstrServiceInfoID: str) -> None: ...


class ICcDeviceContainer:
    pass


class ICcFile:
    @property
    def FileContainer(self) -> ICcFileContainer: ...
    @property
    def IsCollection(self) -> bool: ...
    def MakeCollection(self) -> None: ...


class ICcFileContainer:
    pass


class ICcFormFactorContainer:
    pass


class ICcObject:
    @property
    def ID(self) -> str: ...
    @property
    def IsProtected(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def PropertyContainer(self) -> ICcPropertyContainer: ...
    @Name.setter
    def Name(self, out_pbstrName: str) -> None: ...


class ICcObjectContainer:
    def AddObject(self, in_bstrID: str, in_bstrName: str) -> CcDatastorePrivate: ...
    def DeleteObject(self, in_bstrID: str) -> None: ...
    def EnumerateObjects(self) -> CcCollection: ...
    def FindObject(self, in_bstrID: str) -> CcDatastorePrivate: ...


class ICcOSImage:
    @property
    def SupportedPlatform(self) -> str: ...
    @SupportedPlatform.setter
    def SupportedPlatform(self, out_pbstrSupportedPlatform: str) -> None: ...


class ICcOSImageContainer:
    pass


class ICcPackage:
    @property
    def PackageTypeContainer(self) -> ICcPackageTypeContainer: ...


class ICcPackageContainer:
    pass


class ICcPackageType:
    @property
    def FileContainer(self) -> ICcFileContainer: ...


class ICcPackageTypeContainer:
    pass


class ICcPlatform:
    @property
    def DeviceContainer(self) -> ICcDeviceContainer: ...
    @property
    def FormFactorContainer(self) -> ICcFormFactorContainer: ...
    @property
    def ProjectContainer(self) -> ICcProjectContainer: ...
    @property
    def TypeToArchitectureMap(self) -> ICcTypeToArchitectureMap: ...


class ICcPlatformContainer:
    pass


class ICcProjectContainer:
    pass


class ICcProperty:
    def AddPropertyContainer(self) -> None: ...
    @property
    def Value(self) -> str: ...
    @Value.setter
    def Value(self, out_pbstrVal: str) -> None: ...


class ICcPropertyContainer:
    pass


class ICcPropertyHelper:
    def GetProperty(self, pszName: str) -> Tuple[str]: ...


class ICcServer:
    def EnumerateConnections(self, dwSizeActual: UInt32) -> Tuple[bool, UInt32, ConMan]: ...
    @property
    def Locale(self) -> UInt32: ...
    def GetConnection(self, piDevice: ICcDevice, dwTimeout: UInt32, piCallback: ICcServiceCB) -> Tuple[ConManServer, str]: ...
    def GetConnectionFromId(self, bstrConnectionId: str) -> ConManServer: ...
    def GetDatastore(self, dwLocale: UInt32) -> CcDatastore: ...
    @Locale.setter
    def Locale(self, pdwLocale: UInt32) -> None: ...


class ICcServer2:
    def EnumerateConnections2(self) -> Array: ...


class ICcService:
    def Abort(self, dwCookieId: UInt32) -> None: ...
    def Connect(self, dwTimeout: UInt32, bAsync: bool) -> UInt32: ...
    def Disconnect(self) -> None: ...
    def GetCurrentState(self) -> UInt32: ...
    def Initialize(self, pszLocalBindingIp: str, portConnectTo: UInt16, portEchoTo: UInt16, pszConnectToIp: str) -> None: ...
    def LockService(self) -> None: ...
    def UnlockService(self) -> None: ...


class ICcServiceCategory:
    @property
    def ServiceInfoContainer(self) -> ICcServiceInfoContainer: ...


class ICcServiceCategoryContainer:
    pass


class ICcServiceCB:
    def OnProgressNotify(self, dwCurrentState: UInt32, dwEndState: UInt32, dwCurrentValue: UInt32, dwMaxValue: UInt32) -> None: ...
    def OnStatusChangeNotify(self, dwCurrentState: UInt32, dwEndState: UInt32, pwszStringData: str, pUnk: Object) -> None: ...


class ICcServiceInfo:
    pass


class ICcServiceInfoContainer:
    pass


class ICcTargetDevice:
    def BringToFront(self) -> None: ...
    def GetMappedIpPortFromRemotePort(self, remotePort: UInt16) -> Tuple[str, UInt16, str]: ...
    def GetMappedIpPortFromServiceProperty(self, pPropHelper: ICcPropertyHelper) -> Tuple[str, UInt16, UInt16, str]: ...
    def Initialize(self, pPropHelper: ICcPropertyHelper) -> None: ...
    def RegisterForDeviceNotifications(self, pDeviceEventNotifier: IDeviceEventNotifier) -> None: ...
    def UnRegisterForDeviceNotifications(self, pDeviceEventNotifier: IDeviceEventNotifier) -> None: ...


class ICcTransport:
    def CreateStream(self, wszStreamId: str, dwTimeout: UInt32, bAsync: bool) -> ICcTransportStream: ...
    @property
    def Bandwidth(self) -> UInt32: ...
    @property
    def MTU(self) -> UInt32: ...
    @property
    def SupportsNonUniqueStreamId(self) -> bool: ...


class ICcTransportStream:
    def Disconnect(self) -> None: ...
    @property
    def Buffering(self) -> bool: ...
    @property
    def ID(self) -> str: ...
    def IsConnected(self) -> bool: ...
    def IsDataAvailable(self) -> bool: ...
    def Recv(self, dwTimeout: UInt32) -> Tuple[Byte, UInt32]: ...
    def Send(self, dwTimeout: UInt32, pData: Byte, cbData: UInt32) -> Tuple[Byte]: ...
    @Buffering.setter
    def Buffering(self, pbBuffering: bool) -> None: ...


class ICcTypeToArchitectureMap:
    pass


class IConMan:
    def CreateNewServerGuid(self, in_piDevice: ICcDevice, in_bstrEndPoint: str) -> Tuple[Guid]: ...
    def Datastore(self) -> Tuple[CcDatastore]: ...
    def EnumerateServerGuids(self, in_ArraySize: UInt32) -> Tuple[UInt32, Guid, int]: ...
    def GetDeviceFromServerGuid(self, in_guidServer: Guid) -> Tuple[Guid, ICcDevice]: ...
    def GetServerFromServerGuid(self, in_guidServer: Guid) -> Tuple[Guid, IConManServer]: ...
    def GetServerGuidInfo(self, in_guidServer: Guid) -> Tuple[Guid, str]: ...
    def SetLocale(self, in_dwLangID: UInt32) -> None: ...
    def SetRegistryRoot(self, in_bstrRegistryRoot: str) -> None: ...


class IConManServer:
    def AbortConnect(self) -> None: ...
    def Connect(self) -> None: ...
    def GetTransmitionInfo(self) -> Tuple[tagTransactionInfo]: ...
    def InitEx(self, in_pDevice: ICcDevice, in_pDatastore: CcDatastore) -> None: ...
    def IsConnected(self) -> Tuple[int]: ...
    def RegisterCallback(self, in_pServerCallback: IConManServerCallback, in_CallbackFilter: UInt32) -> None: ...
    def UnregisterCallback(self, in_pServerCallback: IConManServerCallback) -> None: ...


class IConManServer2:
    def InitEx2(self, in_pDevice: ICcDevice, in_pDatastore: CcDatastore, in_lcid: UInt32) -> None: ...


class IConManServer3:
    def InitEx3(self, in_pDevice: ICcDevice, in_pDatastore: CcDatastore, in_lcid: UInt32, in_bstrSirepClientManifest: str) -> None: ...


class IConManServerCallback:
    def NotifyEvent(self, in_OperationID: int, in_szOperation: str, in_EventKind: int, in_EventHResult: int) -> None: ...


class IConManServerCore:
    def AbortConnect(self) -> None: ...
    def Connect(self) -> None: ...
    def GetTransmitionInfo(self) -> Tuple[tagTransactionInfo]: ...
    def InitEx(self, in_pDevice: ICcDevice, in_pDatastore: CcDatastore) -> None: ...
    def IsConnected(self) -> Tuple[int]: ...
    def RegisterCallback(self, in_pServerCallback: IConManServerCallback, in_CallbackFilter: UInt32) -> None: ...
    def UnregisterCallback(self, in_pServerCallback: IConManServerCallback) -> None: ...


class IDeviceEventNotifier:
    def DeviceExit(self) -> None: ...


class IDevicePackage:
    def AbortConnectToDevice(self) -> None: ...
    def AdviseDevicePackageCallback(self, in_pDevicePackageCallBack: IDevicePackageCallback) -> None: ...
    def CancelDeploySession(self) -> None: ...
    def ConnectToDevice(self, in_bstrPlatform: str, in_bstrDevice: str) -> None: ...
    @property
    def ServerGuid(self) -> str: ...
    def GetDebugEngineCount(self, in_bstrDebugLaunchTypeGuid: str, in_bstrRuntimeVersion: str) -> Tuple[UInt32]: ...
    def GetDebugLaunchInfo(self, in_bstrDebugLaunchTypeGuid: str, in_bstrRuntimeVersion: str, in_DebugEngineGuidArraySize: UInt32) -> Tuple[DevicePackage, UInt32, Guid]: ...
    def GetSystemInfo(self) -> Tuple[tagPlatformInfo]: ...
    def Launch(self, in_bstrEXE: str, in_bstrARGS: str) -> Tuple[UInt32]: ...
    def ProvisionDeviceXML(self, pszWXMLin: str, in_Flags: UInt32, in_DllNameName: str) -> Tuple[str]: ...
    @Locale.setter
    def Locale(self, A_1: UInt16) -> None: ...
    def SetVsProviderInterface(self, in_pVsProvider: Object) -> None: ...
    def StartDeploySession(self, in_pEnumReferences: IEnumReferences, in_InstructionSet: UInt32) -> Tuple[UInt32]: ...
    def UnadviseDevicePackageCallback(self, in_pDevicePackageCallBack: IDevicePackageCallback) -> None: ...


class IDevicePackageCallback:
    def NotifyDevicePackageEvent(self, in_pDevicePackage: DevicePackage, in_dpeId: UInt32, in_bstrInfo: str) -> None: ...


class IEnumReferences:
    def GetCount(self) -> Tuple[UInt32]: ...
    def GetNext(self) -> Tuple[str, str, str, str, UInt32]: ...


class tagFileCustomAction:
    FileCustomAction_None = 0
    FileCustomAction_COM = 1
    FileCustomAction_AlwaysOverwrite = 2


class tagFileInfo:
    pass


class tagFileInfox:
    pass


class tagPlatformInfo:
    pass


class tagSystemInfoEx:
    pass


class tagTransactionInfo:
    pass


class tagUapVersionInfo:
    pass
