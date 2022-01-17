from typing import Tuple, Set, Iterable, List


class ActivityRunMode:
    InProcess = 0
    OutOfProcess = 1


class PSPersistableIdleAction:
    NotDefined = 0
    #None = 1
    Persist = 2
    Unload = 3
    Suspend = 4


class PSWorkflowConfigurationProvider:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, applicationPrivateData: str, configProviderId: str): ...
    def CreateLocalRunspaceProvider(self, isUnbounded: bool) -> RunspaceProvider: ...
    def CreatePSActivityHostController(self) -> PSActivityHostController: ...
    @overload
    def CreatePSWorkflowInstance(self, instanceId: PSWorkflowId) -> PSWorkflowInstance: ...
    @overload
    def CreatePSWorkflowInstance(self, definition: PSWorkflowDefinition, metadata: PSWorkflowContext, pipelineInput: PSDataCollection, job: PSWorkflowJob) -> PSWorkflowInstance: ...
    def CreatePSWorkflowInstanceStore(self, workflowInstance: PSWorkflowInstance) -> PSWorkflowInstanceStore: ...
    def CreateRemoteRunspaceProvider(self) -> RunspaceProvider: ...
    def CreateWorkflowExtensionCreationFunctions(self) -> Iterable[Func]: ...
    def CreateWorkflowExtensions(self) -> Iterable[Object]: ...
    @property
    def ActivitiesCacheCleanupIntervalMSec(self) -> int: ...
    @property
    def ActivityProcessIdleTimeoutSec(self) -> int: ...
    @property
    def AllowedActivity(self) -> Iterable[str]: ...
    @property
    def EnableValidation(self) -> bool: ...
    @property
    def LanguageMode(self) -> Nullable: ...
    @property
    def MaxActivityProcesses(self) -> int: ...
    @property
    def MaxConnectedSessions(self) -> int: ...
    @property
    def MaxDisconnectedSessions(self) -> int: ...
    @property
    def MaxInProcRunspaces(self) -> int: ...
    @property
    def MaxRunningWorkflows(self) -> int: ...
    @property
    def MaxSessionsPerRemoteNode(self) -> int: ...
    @property
    def OutOfProcessActivity(self) -> Iterable[str]: ...
    @property
    def PSWorkflowApplicationPersistUnloadTimeoutSec(self) -> int: ...
    @property
    def RemoteNodeSessionIdleTimeoutSec(self) -> int: ...
    @property
    def Runtime(self) -> PSWorkflowRuntime: ...
    @property
    def SessionThrottleLimit(self) -> int: ...
    @property
    def WSManPluginReportCompletionOnZeroActiveSessionsWaitIntervalMSec(self) -> int: ...
    def GetActivityRunMode(self, activity: Activity) -> ActivityRunMode: ...
    def Populate(self, applicationPrivateData: str, configProviderId: str) -> None: ...


class PSWorkflowContext:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, workflowParameters: Dictionary, workflowCommonParameters: Dictionary, jobMetadata: Dictionary, privateMetadata: Dictionary): ...
    @property
    def JobMetadata(self) -> Dictionary: ...
    @property
    def PrivateMetadata(self) -> Dictionary: ...
    @property
    def PSWorkflowCommonParameters(self) -> Dictionary: ...
    @property
    def WorkflowParameters(self) -> Dictionary: ...
    @JobMetadata.setter
    def JobMetadata(self, value: Dictionary) -> None: ...
    @PrivateMetadata.setter
    def PrivateMetadata(self, value: Dictionary) -> None: ...
    @PSWorkflowCommonParameters.setter
    def PSWorkflowCommonParameters(self, value: Dictionary) -> None: ...
    @WorkflowParameters.setter
    def WorkflowParameters(self, value: Dictionary) -> None: ...


class PSWorkflowDefinition:
    @overload
    def __init__(self, workflow: Activity, workflowXaml: str, runtimeAssemblyPath: str): ...
    @overload
    def __init__(self, workflow: Activity, workflowXaml: str, runtimeAssemblyPath: str, requiredAssemblies: Dictionary): ...
    @property
    def RequiredAssemblies(self) -> Dictionary: ...
    @property
    def RuntimeAssemblyPath(self) -> str: ...
    @property
    def Workflow(self) -> Activity: ...
    @property
    def WorkflowXaml(self) -> str: ...
    @RuntimeAssemblyPath.setter
    def RuntimeAssemblyPath(self, value: str) -> None: ...
    @Workflow.setter
    def Workflow(self, value: Activity) -> None: ...
    @WorkflowXaml.setter
    def WorkflowXaml(self, value: str) -> None: ...


class PSWorkflowExtensions:
    @property
    def CustomHandler() -> Func: ...
    @CustomHandler.setter
    def CustomHandler(value: Func) -> None: ...


class PSWorkflowFileInstanceStore(PSWorkflowInstanceStore):
    def __init__(self, configuration: PSWorkflowConfigurationProvider, instance: PSWorkflowInstance): ...
    def CreateInstanceStore(self) -> InstanceStore: ...
    def CreatePersistenceIOParticipant(self) -> PersistenceIOParticipant: ...
    def GetAllWorkflowInstanceIds() -> Iterable[PSWorkflowId]: ...


class PSWorkflowId:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, value: Guid): ...
    @property
    def Guid(self) -> Guid: ...
    def NewWorkflowGuid() -> PSWorkflowId: ...


class PSWorkflowInstance:
    def Dispose(self) -> None: ...
    def DisposeStreams(self) -> None: ...
    @property
    def CreationContext(self) -> Dictionary: ...
    @property
    def Error(self) -> Exception: ...
    @property
    def InstanceId(self) -> PSWorkflowId: ...
    @property
    def InstanceStore(self) -> PSWorkflowInstanceStore: ...
    @property
    def PSWorkflowContext(self) -> PSWorkflowContext: ...
    @property
    def PSWorkflowDefinition(self) -> PSWorkflowDefinition: ...
    @property
    def PSWorkflowJob(self) -> PSWorkflowJob: ...
    @property
    def RemoteActivityState(self) -> PSWorkflowRemoteActivityState: ...
    @property
    def State(self) -> JobState: ...
    @property
    def Streams(self) -> PowerShellStreams: ...
    @property
    def Timer(self) -> PSWorkflowTimer: ...
    @Error.setter
    def Error(self, value: Exception) -> None: ...
    @PSWorkflowContext.setter
    def PSWorkflowContext(self, value: PSWorkflowContext) -> None: ...
    @PSWorkflowDefinition.setter
    def PSWorkflowDefinition(self, value: PSWorkflowDefinition) -> None: ...
    @RemoteActivityState.setter
    def RemoteActivityState(self, value: PSWorkflowRemoteActivityState) -> None: ...
    @State.setter
    def State(self, value: JobState) -> None: ...
    @Streams.setter
    def Streams(self, value: PowerShellStreams) -> None: ...
    @Timer.setter
    def Timer(self, value: PSWorkflowTimer) -> None: ...


class PSWorkflowInstanceStore:
    def CreateInstanceStore(self) -> InstanceStore: ...
    def CreatePersistenceIOParticipant(self) -> PersistenceIOParticipant: ...
    def Delete(self) -> None: ...
    @property
    def PSWorkflowInstance(self) -> PSWorkflowInstance: ...
    def Load(self, components: WorkflowStoreComponents) -> None: ...
    def Save(self, components: WorkflowStoreComponents) -> None: ...


class PSWorkflowJob:
    @property
    def Debugger(self) -> Debugger: ...
    @property
    def HasMoreData(self) -> bool: ...
    @property
    def IsAsync(self) -> bool: ...
    @property
    def Location(self) -> str: ...
    @property
    def OnIdle(self) -> Action: ...
    @property
    def OnPersistableIdleAction(self) -> Func`4: ...
    @property
    def OnUnloaded(self) -> Action: ...
    @property
    def PSWorkflowDebugger(self) -> Debugger: ...
    @property
    def PSWorkflowInstance(self) -> PSWorkflowInstance: ...
    @property
    def StatusMessage(self) -> str: ...
    def GetPersistableIdleAction(self, bookmarks: ReadOnlyCollection, externalSuspendRequest: bool) -> PSPersistableIdleAction: ...
    @overload
    def ResumeBookmark(self, bookmark: Bookmark, state: Object) -> None: ...
    @overload
    def ResumeBookmark(self, bookmark: Bookmark, supportDisconnectedStreams: bool, streams: PowerShellStreams) -> None: ...
    @overload
    def ResumeBookmark(self, bookmark: Bookmark, supportDisconnectedStreams: bool, streams: PowerShellStreams, exception: Exception) -> None: ...
    @overload
    def ResumeJob(self) -> None: ...
    @overload
    def ResumeJob(self, label: str) -> None: ...
    @overload
    def ResumeJobAsync(self) -> None: ...
    @overload
    def ResumeJobAsync(self, label: str) -> None: ...
    @IsAsync.setter
    def IsAsync(self, value: bool) -> None: ...
    @OnIdle.setter
    def OnIdle(self, value: Action) -> None: ...
    @OnPersistableIdleAction.setter
    def OnPersistableIdleAction(self, value: Func`4) -> None: ...
    @OnUnloaded.setter
    def OnUnloaded(self, value: Action) -> None: ...
    def StartJob(self) -> None: ...
    def StartJobAsync(self) -> None: ...
    @overload
    def StopJob(self) -> None: ...
    @overload
    def StopJob(self, force: bool, reason: str) -> None: ...
    @overload
    def StopJob(self, force: bool, reason: str, suppressError: bool) -> None: ...
    @overload
    def StopJobAsync(self) -> None: ...
    @overload
    def StopJobAsync(self, force: bool, reason: str) -> None: ...
    @overload
    def StopJobAsync(self, force: bool, reason: str, suppressError: bool) -> None: ...
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


class PSWorkflowJobManager:
    def __init__(self, runtime: PSWorkflowRuntime, throttleLimit: int): ...
    @overload
    def CreateJob(self, jobInstanceId: Guid, workflow: Activity, command: str, name: str, parameters: Dictionary) -> PSWorkflowJob: ...
    @overload
    def CreateJob(self, jobInstanceId: Guid, workflowXaml: str, command: str, name: str, parameters: Dictionary) -> PSWorkflowJob: ...
    @overload
    def CreateJob(self, jobInstanceId: Guid, workflow: Activity, command: str, name: str, parameters: Dictionary, creationContext: Dictionary) -> PSWorkflowJob: ...
    @overload
    def CreateJob(self, jobInstanceId: Guid, workflowXaml: str, command: str, name: str, parameters: Dictionary, creationContext: Dictionary) -> PSWorkflowJob: ...
    def Dispose(self) -> None: ...
    def GetJob(self, instanceId: Guid) -> PSWorkflowJob: ...
    def GetJobs(self) -> Iterable[PSWorkflowJob]: ...
    def LoadJob(self, storedInstanceId: PSWorkflowId) -> PSWorkflowJob: ...
    def RemoveJob(self, instanceId: Guid) -> None: ...
    def ShutdownWorkflowManager(self, timeout: int) -> None: ...
    def UnloadAllJobs(self) -> None: ...
    def UnloadJob(self, instanceId: Guid) -> None: ...


class PSWorkflowRemoteActivityState:
    def __init__(self, store: PSWorkflowInstanceStore, deserializedRemoteActivityState: Dictionary): ...
    def GetSerializedData(self) -> Dictionary: ...


class PSWorkflowRuntime(PSWorkflowHost):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, configuration: PSWorkflowConfigurationProvider): ...
    def Dispose(self) -> None: ...
    @property
    def Configuration(self) -> PSWorkflowConfigurationProvider: ...
    @property
    def JobManager(self) -> PSWorkflowJobManager: ...
    @property
    def LocalRunspaceProvider(self) -> RunspaceProvider: ...
    @property
    def PSActivityHostController(self) -> PSActivityHostController: ...
    @property
    def RemoteRunspaceProvider(self) -> RunspaceProvider: ...
    @property
    def UnboundedLocalRunspaceProvider(self) -> RunspaceProvider: ...


class PSWorkflowSessionConfiguration:
    def __init__(self): ...
    @overload
    def GetInitialSessionState(self, senderInfo: PSSenderInfo) -> InitialSessionState: ...
    @overload
    def GetInitialSessionState(self, sessionConfigurationData: PSSessionConfigurationData, senderInfo: PSSenderInfo, configProviderId: str) -> InitialSessionState: ...


class PSWorkflowTimer:
    def __init__(self, instance: PSWorkflowInstance, deserializedTimers: Object): ...
    def Dispose(self) -> None: ...
    def GetSerializedData(self) -> Object: ...


class PSWorkflowValidator:
    def __init__(self, configuration: PSWorkflowConfigurationProvider): ...
    def ValidateWorkflow(self, workflow: Activity, runtimeAssembly: str) -> ValidationResults: ...


class Validation:
    @property
    def CustomHandler() -> Func: ...
    @CustomHandler.setter
    def CustomHandler(value: Func) -> None: ...


class WorkflowJobSourceAdapter:
    def GetInstance() -> WorkflowJobSourceAdapter: ...
    def GetJobByInstanceId(self, instanceId: Guid, recurse: bool) -> Job2: ...
    def GetJobBySessionId(self, id: int, recurse: bool) -> Job2: ...
    def GetJobManager(self) -> PSWorkflowJobManager: ...
    def GetJobs(self) -> List[Job2]: ...
    def GetJobsByCommand(self, command: str, recurse: bool) -> List[Job2]: ...
    def GetJobsByFilter(self, filter: Dictionary, recurse: bool) -> List[Job2]: ...
    def GetJobsByName(self, name: str, recurse: bool) -> List[Job2]: ...
    def GetJobsByState(self, state: JobState, recurse: bool) -> List[Job2]: ...
    def GetPSWorkflowRuntime(self) -> PSWorkflowRuntime: ...
    @overload
    def NewJob(self, specification: JobInvocationInfo) -> Job2: ...
    def RemoveJob(self, job: Job2) -> None: ...


class WorkflowStoreComponents:
    Streams = 1
    Metadata = 2
    Definition = 4
    Timer = 8
    JobState = 16
    TerminatingError = 32
    ActivityState = 64


class WorkflowUnhandledErrorAction:
    Suspend = 0
    Stop = 1
    Terminate = 2
