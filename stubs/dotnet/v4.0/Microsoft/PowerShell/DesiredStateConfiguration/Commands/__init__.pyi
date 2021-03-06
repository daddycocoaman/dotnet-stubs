__all__ = ['SystemInterface']
from typing import Tuple, Set, Iterable, List


class ConnectDscConfigurationCommand(DscConfigurationCommandBase):
    def __init__(self): ...
    @property
    def Bookmark(self) -> str: ...
    @property
    def InstanceId(self) -> str: ...
    @property
    def JobName(self) -> str: ...
    @property
    def Wait(self) -> SwitchParameter: ...
    @Bookmark.setter
    def Bookmark(self, value: str) -> None: ...
    @InstanceId.setter
    def InstanceId(self, value: str) -> None: ...
    @JobName.setter
    def JobName(self, value: str) -> None: ...
    @Wait.setter
    def Wait(self, value: SwitchParameter) -> None: ...


class DotNetHttpClient:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, requestHandler: WebRequestHandler): ...
    @overload
    def GetAsync(self, uri: str) -> Task: ...
    @overload
    def PostAsync(self, uri: str, content: HttpContent) -> Task: ...


class DownloadManagerCommandBase:
    def __init__(self): ...
    @property
    def AgentId(self) -> str: ...
    @property
    def AllowUnsecureConnection(self) -> str: ...
    @property
    def ConfigurationId(self) -> str: ...
    @property
    def Credential(self) -> PSCredential: ...
    @property
    def ProxyCredential(self) -> PSCredential: ...
    @property
    def ProxyUrl(self) -> str: ...
    def GetHttpConnectionData(self, certificateId: str, cachedOaaSCertificate: str, requestUri: Uri) -> Tuple[str, DotNetHttpClient, ErrorRecord]: ...
    @AgentId.setter
    def AgentId(self, value: str) -> None: ...
    @AllowUnsecureConnection.setter
    def AllowUnsecureConnection(self, value: str) -> None: ...
    @ConfigurationId.setter
    def ConfigurationId(self, value: str) -> None: ...
    @Credential.setter
    def Credential(self, value: PSCredential) -> None: ...
    @ProxyCredential.setter
    def ProxyCredential(self, value: PSCredential) -> None: ...
    @ProxyUrl.setter
    def ProxyUrl(self, value: str) -> None: ...


class DscCmdletCommandBase:
    def __init__(self): ...


class DscConfigurationCommandBase(DscCmdletCommandBase):
    def __init__(self): ...
    @property
    def CimSession(self) -> Set(CimSession): ...
    @property
    def ComputerName(self) -> Set(str): ...
    @property
    def Credential(self) -> PSCredential: ...
    @property
    def ThrottleLimit(self) -> int: ...
    @CimSession.setter
    def CimSession(self, value: Set(CimSession)) -> None: ...
    @ComputerName.setter
    def ComputerName(self, value: Set(str)) -> None: ...
    @Credential.setter
    def Credential(self, value: PSCredential) -> None: ...
    @ThrottleLimit.setter
    def ThrottleLimit(self, value: int) -> None: ...
    @overload
    def ShouldProcess(self, dscEngineMessage: str) -> bool: ...


class ErrorRecordInstance:
    def GetErrorDetails(record: ErrorRecord) -> str: ...


class GetDscActionCommand(GetDscActionCommandBase):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, httpClient: IHttpClient, parameterSetName: str, certificateId: str): ...
    @property
    def CertificateId(self) -> str: ...
    @property
    def ServerUrl(self) -> str: ...
    def GetAction(self) -> None: ...
    def InitializeSerializer(self) -> None: ...
    @CertificateId.setter
    def CertificateId(self, value: str) -> None: ...
    @ServerUrl.setter
    def ServerUrl(self, value: str) -> None: ...


class GetDscActionCommandBase(DownloadManagerCommandBase):
    def __init__(self): ...
    @property
    def ClientStatus(self) -> Set(Hashtable): ...
    @property
    def ConfigurationName(self) -> str: ...
    @property
    def FileHash(self) -> str: ...
    @property
    def NotCompliant(self) -> SwitchParameter: ...
    @property
    def StatusCode(self) -> int: ...
    @ClientStatus.setter
    def ClientStatus(self, value: Set(Hashtable)) -> None: ...
    @ConfigurationName.setter
    def ConfigurationName(self, value: str) -> None: ...
    @FileHash.setter
    def FileHash(self, value: str) -> None: ...
    @NotCompliant.setter
    def NotCompliant(self, value: SwitchParameter) -> None: ...
    @StatusCode.setter
    def StatusCode(self, value: int) -> None: ...


class GetDscDocumentCommand(GetDscDocumentCommandBase):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, httpClient: DotNetHttpClient, parameterSetName: str): ...
    @property
    def CertificateId(self) -> str: ...
    @property
    def MaximumDownloadSize(self) -> Int64: ...
    @property
    def ServerUrl(self) -> str: ...
    def GetDocument(self) -> None: ...
    @CertificateId.setter
    def CertificateId(self, value: str) -> None: ...
    @MaximumDownloadSize.setter
    def MaximumDownloadSize(self, value: Int64) -> None: ...
    @ServerUrl.setter
    def ServerUrl(self, value: str) -> None: ...


class GetDscDocumentCommandBase(DownloadManagerCommandBase):
    def __init__(self): ...
    @property
    def AssignedConfigurationName(self) -> str: ...
    @property
    def ConfigurationName(self) -> str: ...
    @property
    def DestinationPath(self) -> str: ...
    @AssignedConfigurationName.setter
    def AssignedConfigurationName(self, value: str) -> None: ...
    @ConfigurationName.setter
    def ConfigurationName(self, value: str) -> None: ...
    @DestinationPath.setter
    def DestinationPath(self, value: str) -> None: ...


class GetDscModuleCommand(GetDscModuleCommandBase):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, httpClient: DotNetHttpClient, parameterSetName: str): ...
    @property
    def CertificateId(self) -> str: ...
    @property
    def MaximumDownloadSize(self) -> Int64: ...
    @property
    def ServerUrl(self) -> str: ...
    def GetModule(self) -> None: ...
    @CertificateId.setter
    def CertificateId(self, value: str) -> None: ...
    @MaximumDownloadSize.setter
    def MaximumDownloadSize(self, value: Int64) -> None: ...
    @ServerUrl.setter
    def ServerUrl(self, value: str) -> None: ...


class GetDscModuleCommandBase(DownloadManagerCommandBase):
    def __init__(self): ...
    @property
    def DestinationPath(self) -> str: ...
    @property
    def Module(self) -> Set(ModuleSpecification): ...
    @DestinationPath.setter
    def DestinationPath(self, value: str) -> None: ...
    @Module.setter
    def Module(self, value: Set(ModuleSpecification)) -> None: ...


class InvokeDscResourceMethodCommand(DscCmdletCommandBase):
    def __init__(self): ...
    @property
    def Method(self) -> str: ...
    @property
    def ModuleName(self) -> ModuleSpecification: ...
    @property
    def Name(self) -> str: ...
    @property
    def Property(self) -> Hashtable: ...
    @Method.setter
    def Method(self, value: str) -> None: ...
    @ModuleName.setter
    def ModuleName(self, value: ModuleSpecification) -> None: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    @Property.setter
    def Property(self, value: Hashtable) -> None: ...


class IRotateDscAuthenticationCertificate:
    @property
    def AgentId(self) -> str: ...
    @property
    def AllowUnsecureConnection(self) -> bool: ...
    @property
    def Credential(self) -> NetworkCredential: ...
    @property
    def NewCertificateId(self) -> str: ...
    @property
    def ProxyCredential(self) -> NetworkCredential: ...
    @property
    def ProxyUri(self) -> Uri: ...
    @property
    def ServerUri(self) -> Uri: ...
    def Rotate(self) -> None: ...
    @AgentId.setter
    def AgentId(self, value: str) -> None: ...
    @AllowUnsecureConnection.setter
    def AllowUnsecureConnection(self, value: bool) -> None: ...
    @Credential.setter
    def Credential(self, value: NetworkCredential) -> None: ...
    @NewCertificateId.setter
    def NewCertificateId(self, value: str) -> None: ...
    @ProxyCredential.setter
    def ProxyCredential(self, value: NetworkCredential) -> None: ...
    @ProxyUri.setter
    def ProxyUri(self, value: Uri) -> None: ...
    @ServerUri.setter
    def ServerUri(self, value: Uri) -> None: ...


class PSConfigurationJob:
    @property
    def ApplyUseExisting(self) -> bool: ...
    @property
    def Bookmark(self) -> str: ...
    @property
    def EnableWhatIf(self) -> bool: ...
    @property
    def ErrorRecordInStream(self) -> bool: ...
    @property
    def HasMoreData(self) -> bool: ...
    @property
    def InDisconnectedMode(self) -> bool: ...
    @property
    def JobId(self) -> str: ...
    @property
    def Location(self) -> str: ...
    @property
    def RestartInProgress(self) -> bool: ...
    @property
    def Session(self) -> CimSession: ...
    @property
    def StandardParameters(self) -> CimMethodParametersCollection: ...
    @property
    def StatusMessage(self) -> str: ...
    @property
    def Streamed(self) -> bool: ...
    @property
    def TestDscConfigurationCmdlet(self) -> bool: ...
    @property
    def UpdateConfigCall(self) -> bool: ...
    def ResetCimSession(self) -> None: ...
    def ResumeJob(self) -> None: ...
    def ResumeJobAsync(self) -> None: ...
    @ApplyUseExisting.setter
    def ApplyUseExisting(self, value: bool) -> None: ...
    @Bookmark.setter
    def Bookmark(self, value: str) -> None: ...
    @EnableWhatIf.setter
    def EnableWhatIf(self, value: bool) -> None: ...
    @ErrorRecordInStream.setter
    def ErrorRecordInStream(self, value: bool) -> None: ...
    @InDisconnectedMode.setter
    def InDisconnectedMode(self, value: bool) -> None: ...
    @JobId.setter
    def JobId(self, value: str) -> None: ...
    @RestartInProgress.setter
    def RestartInProgress(self, value: bool) -> None: ...
    @Session.setter
    def Session(self, value: CimSession) -> None: ...
    @StandardParameters.setter
    def StandardParameters(self, value: CimMethodParametersCollection) -> None: ...
    @Streamed.setter
    def Streamed(self, value: bool) -> None: ...
    @TestDscConfigurationCmdlet.setter
    def TestDscConfigurationCmdlet(self, value: bool) -> None: ...
    @UpdateConfigCall.setter
    def UpdateConfigCall(self, value: bool) -> None: ...
    def StartJob(self) -> None: ...
    def StartJobAsync(self) -> None: ...
    @overload
    def StopJob(self) -> None: ...
    @overload
    def StopJob(self, force: bool, reason: str) -> None: ...
    @overload
    def StopJobAsync(self) -> None: ...
    @overload
    def StopJobAsync(self, force: bool, reason: str) -> None: ...
    @overload
    def SuspendJob(self) -> None: ...
    @overload
    def SuspendJob(self, force: bool, reason: str) -> None: ...
    @overload
    def SuspendJobAsync(self) -> None: ...
    @overload
    def SuspendJobAsync(self, force: bool, reason: str) -> None: ...
    def UnblockJob(self) -> None: ...
    def UnblockJobAsync(self) -> None: ...


class PublishDscConfigurationCommand(DscConfigurationCommandBase):
    def __init__(self): ...
    @overload
    def Dispose(self) -> None: ...
    @overload
    def Dispose(self, disposing: bool) -> None: ...
    @property
    def Force(self) -> SwitchParameter: ...
    @property
    def Path(self) -> str: ...
    @Force.setter
    def Force(self, value: SwitchParameter) -> None: ...
    @Path.setter
    def Path(self, value: str) -> None: ...


class RegisterDscAgentCommand:
    def __init__(self): ...
    @property
    def AgentId(self) -> str: ...
    @property
    def AgentInformation(self) -> IDictionary: ...
    @property
    def AllowUnsecureConnection(self) -> str: ...
    @property
    def CertificateId(self) -> str: ...
    @property
    def ConfigurationNames(self) -> Set(str): ...
    @property
    def Credential(self) -> PSCredential: ...
    @property
    def ProxyCredential(self) -> PSCredential: ...
    @property
    def ProxyUrl(self) -> str: ...
    @property
    def RegistrationKey(self) -> str: ...
    @property
    def RegistrationMessageType(self) -> str: ...
    @property
    def ServerUrl(self) -> str: ...
    @AgentId.setter
    def AgentId(self, value: str) -> None: ...
    @AgentInformation.setter
    def AgentInformation(self, value: IDictionary) -> None: ...
    @AllowUnsecureConnection.setter
    def AllowUnsecureConnection(self, value: str) -> None: ...
    @CertificateId.setter
    def CertificateId(self, value: str) -> None: ...
    @ConfigurationNames.setter
    def ConfigurationNames(self, value: Set(str)) -> None: ...
    @Credential.setter
    def Credential(self, value: PSCredential) -> None: ...
    @ProxyCredential.setter
    def ProxyCredential(self, value: PSCredential) -> None: ...
    @ProxyUrl.setter
    def ProxyUrl(self, value: str) -> None: ...
    @RegistrationKey.setter
    def RegistrationKey(self, value: str) -> None: ...
    @RegistrationMessageType.setter
    def RegistrationMessageType(self, value: str) -> None: ...
    @ServerUrl.setter
    def ServerUrl(self, value: str) -> None: ...


class RotateDscAuthenticationCertificate:
    def __init__(self): ...
    @property
    def AgentId(self) -> str: ...
    @property
    def AllowUnsecureConnection(self) -> bool: ...
    @property
    def Credential(self) -> NetworkCredential: ...
    @property
    def NewCertificateId(self) -> str: ...
    @property
    def ProxyCredential(self) -> NetworkCredential: ...
    @property
    def ProxyUri(self) -> Uri: ...
    @property
    def ServerUri(self) -> Uri: ...
    def Rotate(self) -> None: ...
    @AgentId.setter
    def AgentId(self, value: str) -> None: ...
    @AllowUnsecureConnection.setter
    def AllowUnsecureConnection(self, value: bool) -> None: ...
    @Credential.setter
    def Credential(self, value: NetworkCredential) -> None: ...
    @NewCertificateId.setter
    def NewCertificateId(self, value: str) -> None: ...
    @ProxyCredential.setter
    def ProxyCredential(self, value: NetworkCredential) -> None: ...
    @ProxyUri.setter
    def ProxyUri(self, value: Uri) -> None: ...
    @ServerUri.setter
    def ServerUri(self, value: Uri) -> None: ...


class SendDscStatusCommand(SendDscStatusCommandBase):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, httpClient: DotNetHttpClient, parameterSetName: str): ...
    @property
    def CertificateId(self) -> str: ...
    @property
    def ErrorReport(self) -> Set(str): ...
    @property
    def ServerUrl(self) -> str: ...
    @property
    def StatusReport(self) -> Set(str): ...
    @overload
    def GetHttpConnectionData(self, cachedOaaSCertificate: str) -> Tuple[DotNetHttpClient, ErrorRecord]: ...
    def SendStatus(self) -> None: ...
    @CertificateId.setter
    def CertificateId(self, value: str) -> None: ...
    @ErrorReport.setter
    def ErrorReport(self, value: Set(str)) -> None: ...
    @ServerUrl.setter
    def ServerUrl(self, value: str) -> None: ...
    @StatusReport.setter
    def StatusReport(self, value: Set(str)) -> None: ...


class SendDscStatusCommandBase(DownloadManagerCommandBase):
    def __init__(self): ...
    @property
    def ConfigurationVersion(self) -> str: ...
    @property
    def EndTime(self) -> str: ...
    @property
    def IpAddress(self) -> str: ...
    @property
    def JobId(self) -> str: ...
    @property
    def LcmVersion(self) -> str: ...
    @property
    def NodeName(self) -> str: ...
    @property
    def OperationType(self) -> str: ...
    @property
    def RebootRequested(self) -> str: ...
    @property
    def RefreshMode(self) -> str: ...
    @property
    def ReportFormatVersion(self) -> str: ...
    @property
    def StartTime(self) -> str: ...
    @property
    def Status(self) -> str: ...
    @ConfigurationVersion.setter
    def ConfigurationVersion(self, value: str) -> None: ...
    @EndTime.setter
    def EndTime(self, value: str) -> None: ...
    @IpAddress.setter
    def IpAddress(self, value: str) -> None: ...
    @JobId.setter
    def JobId(self, value: str) -> None: ...
    @LcmVersion.setter
    def LcmVersion(self, value: str) -> None: ...
    @NodeName.setter
    def NodeName(self, value: str) -> None: ...
    @OperationType.setter
    def OperationType(self, value: str) -> None: ...
    @RebootRequested.setter
    def RebootRequested(self, value: str) -> None: ...
    @RefreshMode.setter
    def RefreshMode(self, value: str) -> None: ...
    @ReportFormatVersion.setter
    def ReportFormatVersion(self, value: str) -> None: ...
    @StartTime.setter
    def StartTime(self, value: str) -> None: ...
    @Status.setter
    def Status(self, value: str) -> None: ...


class SetDscLocalConfigurationManagerCommand(DscConfigurationCommandBase):
    def __init__(self): ...
    @overload
    def Dispose(self) -> None: ...
    @overload
    def Dispose(self, disposing: bool) -> None: ...
    @property
    def Force(self) -> SwitchParameter: ...
    @property
    def Path(self) -> str: ...
    @Force.setter
    def Force(self, value: SwitchParameter) -> None: ...
    @Path.setter
    def Path(self, value: str) -> None: ...


class StartDscConfigurationCommand(DscConfigurationCommandBase):
    def __init__(self): ...
    @property
    def CimSession(self) -> Set(CimSession): ...
    @property
    def ComputerName(self) -> Set(str): ...
    @property
    def Credential(self) -> PSCredential: ...
    @property
    def Force(self) -> SwitchParameter: ...
    @property
    def JobName(self) -> str: ...
    @property
    def Path(self) -> str: ...
    @property
    def ThrottleLimit(self) -> int: ...
    @property
    def UseExisting(self) -> SwitchParameter: ...
    @property
    def Wait(self) -> SwitchParameter: ...
    @CimSession.setter
    def CimSession(self, value: Set(CimSession)) -> None: ...
    @ComputerName.setter
    def ComputerName(self, value: Set(str)) -> None: ...
    @Credential.setter
    def Credential(self, value: PSCredential) -> None: ...
    @Force.setter
    def Force(self, value: SwitchParameter) -> None: ...
    @JobName.setter
    def JobName(self, value: str) -> None: ...
    @Path.setter
    def Path(self, value: str) -> None: ...
    @ThrottleLimit.setter
    def ThrottleLimit(self, value: int) -> None: ...
    @UseExisting.setter
    def UseExisting(self, value: SwitchParameter) -> None: ...
    @Wait.setter
    def Wait(self, value: SwitchParameter) -> None: ...


class TestDscConfigurationCommand(DscConfigurationCommandBase):
    def __init__(self): ...
    @property
    def AsJob(self) -> SwitchParameter: ...
    @property
    def CimSession(self) -> Set(CimSession): ...
    @property
    def ComputerName(self) -> Set(str): ...
    @property
    def Credential(self) -> PSCredential: ...
    @property
    def Detailed(self) -> SwitchParameter: ...
    @property
    def Path(self) -> str: ...
    @property
    def ReferenceConfiguration(self) -> str: ...
    @property
    def ThrottleLimit(self) -> int: ...
    @AsJob.setter
    def AsJob(self, value: SwitchParameter) -> None: ...
    @CimSession.setter
    def CimSession(self, value: Set(CimSession)) -> None: ...
    @ComputerName.setter
    def ComputerName(self, value: Set(str)) -> None: ...
    @Credential.setter
    def Credential(self, value: PSCredential) -> None: ...
    @Detailed.setter
    def Detailed(self, value: SwitchParameter) -> None: ...
    @Path.setter
    def Path(self, value: str) -> None: ...
    @ReferenceConfiguration.setter
    def ReferenceConfiguration(self, value: str) -> None: ...
    @ThrottleLimit.setter
    def ThrottleLimit(self, value: int) -> None: ...


class UpdateDscConfigurationCommand(DscConfigurationCommandBase):
    def __init__(self): ...
    @property
    def JobName(self) -> str: ...
    @property
    def Wait(self) -> SwitchParameter: ...
    @JobName.setter
    def JobName(self, value: str) -> None: ...
    @Wait.setter
    def Wait(self, value: SwitchParameter) -> None: ...
