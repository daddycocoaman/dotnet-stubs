from typing import Tuple, Set, Iterable, List


class ApplicationDeployment(Object):
    def add_CheckForUpdateCompleted(self, value: CheckForUpdateCompletedEventHandler) -> None: ...
    def add_CheckForUpdateProgressChanged(self, value: DeploymentProgressChangedEventHandler) -> None: ...
    def add_DownloadFileGroupCompleted(self, value: DownloadFileGroupCompletedEventHandler) -> None: ...
    def add_DownloadFileGroupProgressChanged(self, value: DeploymentProgressChangedEventHandler) -> None: ...
    def add_UpdateCompleted(self, value: AsyncCompletedEventHandler) -> None: ...
    def add_UpdateProgressChanged(self, value: DeploymentProgressChangedEventHandler) -> None: ...
    @overload
    def CheckForDetailedUpdate(self) -> UpdateCheckInfo: ...
    @overload
    def CheckForDetailedUpdate(self, persistUpdateCheckResult: bool) -> UpdateCheckInfo: ...
    @overload
    def CheckForUpdate(self) -> bool: ...
    @overload
    def CheckForUpdate(self, persistUpdateCheckResult: bool) -> bool: ...
    def CheckForUpdateAsync(self) -> None: ...
    def CheckForUpdateAsyncCancel(self) -> None: ...
    def DownloadFileGroup(self, groupName: str) -> None: ...
    @overload
    def DownloadFileGroupAsync(self, groupName: str) -> None: ...
    @overload
    def DownloadFileGroupAsync(self, groupName: str, userState: Object) -> None: ...
    def DownloadFileGroupAsyncCancel(self, groupName: str) -> None: ...
    @property
    def ActivationUri(self) -> Uri: ...
    @property
    def CurrentDeployment() -> ApplicationDeployment: ...
    @property
    def CurrentVersion(self) -> Version: ...
    @property
    def DataDirectory(self) -> str: ...
    @property
    def IsFirstRun(self) -> bool: ...
    @property
    def IsNetworkDeployed() -> bool: ...
    @property
    def TimeOfLastUpdateCheck(self) -> DateTime: ...
    @property
    def UpdatedApplicationFullName(self) -> str: ...
    @property
    def UpdatedVersion(self) -> Version: ...
    @property
    def UpdateLocation(self) -> Uri: ...
    def IsFileGroupDownloaded(self, groupName: str) -> bool: ...
    def remove_CheckForUpdateCompleted(self, value: CheckForUpdateCompletedEventHandler) -> None: ...
    def remove_CheckForUpdateProgressChanged(self, value: DeploymentProgressChangedEventHandler) -> None: ...
    def remove_DownloadFileGroupCompleted(self, value: DownloadFileGroupCompletedEventHandler) -> None: ...
    def remove_DownloadFileGroupProgressChanged(self, value: DeploymentProgressChangedEventHandler) -> None: ...
    def remove_UpdateCompleted(self, value: AsyncCompletedEventHandler) -> None: ...
    def remove_UpdateProgressChanged(self, value: DeploymentProgressChangedEventHandler) -> None: ...
    def Update(self) -> bool: ...
    def UpdateAsync(self) -> None: ...
    def UpdateAsyncCancel(self) -> None: ...


class CheckForUpdateCompletedEventArgs(AsyncCompletedEventArgs):
    @property
    def AvailableVersion(self) -> Version: ...
    @property
    def IsUpdateRequired(self) -> bool: ...
    @property
    def MinimumRequiredVersion(self) -> Version: ...
    @property
    def UpdateAvailable(self) -> bool: ...
    @property
    def UpdateSizeBytes(self) -> Int64: ...


class CheckForUpdateCompletedEventHandler(MulticastDelegate):
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, sender: Object, e: CheckForUpdateCompletedEventArgs, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: Object, e: CheckForUpdateCompletedEventArgs) -> None: ...


class CompatibleFramework(Object):
    @property
    def Profile(self) -> str: ...
    @property
    def SupportedRuntime(self) -> str: ...
    @property
    def TargetVersion(self) -> str: ...


class CompatibleFrameworkMissingException(DependentPlatformMissingException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...
    @property
    def CompatibleFrameworks(self) -> CompatibleFrameworks: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...


class CompatibleFrameworks(Object):
    @property
    def Frameworks(self) -> List[CompatibleFramework]: ...
    @property
    def SupportUrl(self) -> Uri: ...


class DependentPlatformMissingException(DeploymentException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...
    @overload
    def __init__(self, message: str, supportUrl: Uri): ...
    @property
    def SupportUrl(self) -> Uri: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...


class DeploymentDownloadException(DeploymentException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class DeploymentException(SystemException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...


class DeploymentProgressChangedEventArgs(ProgressChangedEventArgs):
    @property
    def BytesCompleted(self) -> Int64: ...
    @property
    def BytesTotal(self) -> Int64: ...
    @property
    def Group(self) -> str: ...
    @property
    def State(self) -> DeploymentProgressState: ...


class DeploymentProgressChangedEventHandler(MulticastDelegate):
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, sender: Object, e: DeploymentProgressChangedEventArgs, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: Object, e: DeploymentProgressChangedEventArgs) -> None: ...


class DeploymentProgressState:
    DownloadingDeploymentInformation = 0
    DownloadingApplicationInformation = 1
    DownloadingApplicationFiles = 2


class DeploymentServiceCom(Object):
    def __init__(self): ...
    def ActivateApplicationExtension(self, textualSubId: str, deploymentProviderUrl: str, targetAssociatedFile: str) -> None: ...
    def ActivateDeployment(self, deploymentLocation: str, isShortcut: bool) -> None: ...
    def ActivateDeploymentEx(self, deploymentLocation: str, unsignedPolicy: int, signedPolicy: int) -> None: ...
    def CheckForDeploymentUpdate(self, textualSubId: str) -> None: ...
    def CleanOnlineAppCache(self) -> None: ...
    def EndServiceRightNow(self) -> None: ...
    def MaintainSubscription(self, textualSubId: str) -> None: ...


class DownloadApplicationCompletedEventArgs(AsyncCompletedEventArgs):
    @property
    def LogFilePath(self) -> str: ...
    @property
    def ShortcutAppId(self) -> str: ...


class DownloadFileGroupCompletedEventArgs(AsyncCompletedEventArgs):
    @property
    def Group(self) -> str: ...


class DownloadFileGroupCompletedEventHandler(MulticastDelegate):
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, sender: Object, e: DownloadFileGroupCompletedEventArgs, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: Object, e: DownloadFileGroupCompletedEventArgs) -> None: ...


class DownloadProgressChangedEventArgs(ProgressChangedEventArgs):
    @property
    def BytesDownloaded(self) -> Int64: ...
    @property
    def State(self) -> DeploymentProgressState: ...
    @property
    def TotalBytesToDownload(self) -> Int64: ...


class GetManifestCompletedEventArgs(AsyncCompletedEventArgs):
    @property
    def ActivationContext(self) -> ActivationContext: ...
    @property
    def ApplicationIdentity(self) -> ApplicationIdentity: ...
    @property
    def ApplicationManifest(self) -> XmlReader: ...
    @property
    def DeploymentManifest(self) -> XmlReader: ...
    @property
    def IsCached(self) -> bool: ...
    @property
    def LogFilePath(self) -> str: ...
    @property
    def ProductName(self) -> str: ...
    @property
    def SubscriptionIdentity(self) -> str: ...
    @property
    def SupportUri(self) -> Uri: ...
    @property
    def Version(self) -> Version: ...


class InPlaceHostingManager(Object):
    @overload
    def __init__(self, deploymentManifest: Uri): ...
    @overload
    def __init__(self, deploymentManifest: Uri, launchInHostProcess: bool): ...
    def add_DownloadApplicationCompleted(self, value: EventHandler) -> None: ...
    def add_DownloadProgressChanged(self, value: EventHandler) -> None: ...
    def add_GetManifestCompleted(self, value: EventHandler) -> None: ...
    @overload
    def AssertApplicationRequirements(self) -> None: ...
    @overload
    def AssertApplicationRequirements(self, grantApplicationTrust: bool) -> None: ...
    def CancelAsync(self) -> None: ...
    def Dispose(self) -> None: ...
    def DownloadApplicationAsync(self) -> None: ...
    def Execute(self) -> ObjectHandle: ...
    def GetManifestAsync(self) -> None: ...
    def remove_DownloadApplicationCompleted(self, value: EventHandler) -> None: ...
    def remove_DownloadProgressChanged(self, value: EventHandler) -> None: ...
    def remove_GetManifestCompleted(self, value: EventHandler) -> None: ...
    def UninstallCustomAddIn(subscriptionId: str) -> None: ...
    def UninstallCustomUXApplication(subscriptionId: str) -> None: ...


class InvalidDeploymentException(DeploymentException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class SupportedRuntimeMissingException(DependentPlatformMissingException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...
    @property
    def SupportedRuntimeVersion(self) -> str: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...


class TrustNotGrantedException(DeploymentException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class UpdateCheckInfo(Object):
    @property
    def AvailableVersion(self) -> Version: ...
    @property
    def IsUpdateRequired(self) -> bool: ...
    @property
    def MinimumRequiredVersion(self) -> Version: ...
    @property
    def UpdateAvailable(self) -> bool: ...
    @property
    def UpdateSizeBytes(self) -> Int64: ...
