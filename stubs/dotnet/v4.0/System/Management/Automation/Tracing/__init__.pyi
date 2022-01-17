from typing import Tuple, Set, Iterable, List


class Tracer(EtwActivity):
    def __init__(self): ...
    def AbortingWorkflowExecution(self, workflowId: Guid, reason: str) -> None: ...
    def ActivityExecutionFinished(self, activityName: str) -> None: ...
    def ActivityExecutionQueued(self, workflowId: Guid, activityName: str) -> None: ...
    def ActivityExecutionStarted(self, activityName: str, activityTypeName: str) -> None: ...
    def BeginContainerParentJobExecution(self, containerParentJobInstanceId: Guid) -> None: ...
    def BeginCreateNewJob(self, trackingId: Guid) -> None: ...
    def BeginJobLogic(self, workflowJobJobInstanceId: Guid) -> None: ...
    def BeginProxyChildJobEventHandler(self, proxyChildJobInstanceId: Guid) -> None: ...
    def BeginProxyJobEventHandler(self, proxyJobInstanceId: Guid) -> None: ...
    def BeginProxyJobExecution(self, proxyJobInstanceId: Guid) -> None: ...
    def BeginRunGarbageCollection(self) -> None: ...
    def BeginStartWorkflowApplication(self, trackingId: Guid) -> None: ...
    def BeginWorkflowExecution(self, workflowJobJobInstanceId: Guid) -> None: ...
    def CancellingWorkflowExecution(self, workflowId: Guid) -> None: ...
    def ChildWorkflowJobAddition(self, workflowJobInstanceId: Guid, containerParentJobInstanceId: Guid) -> None: ...
    @overload
    def DebugMessage(self, message: str) -> None: ...
    @overload
    def DebugMessage(self, exception: Exception) -> None: ...
    def EndContainerParentJobExecution(self, containerParentJobInstanceId: Guid) -> None: ...
    def EndCreateNewJob(self, trackingId: Guid) -> None: ...
    def EndJobLogic(self, workflowJobJobInstanceId: Guid) -> None: ...
    def EndpointDisabled(self, endpointName: str, disabledBy: str) -> None: ...
    def EndpointEnabled(self, endpointName: str, enabledBy: str) -> None: ...
    def EndpointModified(self, endpointName: str, modifiedBy: str) -> None: ...
    def EndpointRegistered(self, endpointName: str, endpointType: str, registeredBy: str) -> None: ...
    def EndpointUnregistered(self, endpointName: str, unregisteredBy: str) -> None: ...
    def EndProxyChildJobEventHandler(self, proxyChildJobInstanceId: Guid) -> None: ...
    def EndProxyJobEventHandler(self, proxyJobInstanceId: Guid) -> None: ...
    def EndProxyJobExecution(self, proxyJobInstanceId: Guid) -> None: ...
    def EndRunGarbageCollection(self) -> None: ...
    def EndStartWorkflowApplication(self, trackingId: Guid) -> None: ...
    def EndWorkflowExecution(self, workflowJobJobInstanceId: Guid) -> None: ...
    def ErrorImportingWorkflowFromXaml(self, workflowId: Guid, errorDescription: str) -> None: ...
    def ForcedWorkflowShutdownError(self, workflowId: Guid, errorDescription: str) -> None: ...
    def ForcedWorkflowShutdownFinished(self, workflowId: Guid) -> None: ...
    def ForcedWorkflowShutdownStarted(self, workflowId: Guid) -> None: ...
    def GetExceptionString(exception: Exception) -> str: ...
    def ImportedWorkflowFromXaml(self, workflowId: Guid, xamlFile: str) -> None: ...
    def ImportingWorkflowFromXaml(self, workflowId: Guid, xamlFile: str) -> None: ...
    def JobCreationComplete(self, jobId: Guid, workflowId: Guid) -> None: ...
    def JobError(self, jobId: int, workflowId: Guid, errorDescription: str) -> None: ...
    def JobRemoved(self, parentJobId: Guid, childJobId: Guid, workflowId: Guid) -> None: ...
    def JobRemoveError(self, parentJobId: Guid, childJobId: Guid, workflowId: Guid, error: str) -> None: ...
    def JobStateChanged(self, jobId: int, workflowId: Guid, newState: str, oldState: str) -> None: ...
    def LoadingWorkflowForExecution(self, workflowId: Guid) -> None: ...
    def OutOfProcessRunspaceStarted(self, command: str) -> None: ...
    def ParameterSplattingWasPerformed(self, parameters: str, computers: str) -> None: ...
    def ParentJobCreated(self, jobId: Guid) -> None: ...
    def PersistenceStoreMaxSizeReached(self) -> None: ...
    def PersistingWorkflow(self, workflowId: Guid, persistPath: str) -> None: ...
    def ProxyJobRemoteJobAssociation(self, proxyJobInstanceId: Guid, containerParentJobInstanceId: Guid) -> None: ...
    def RemoveJobStarted(self, jobId: Guid) -> None: ...
    def RunspaceAvailabilityChanged(self, runspaceId: str, availability: str) -> None: ...
    def RunspaceStateChanged(self, runspaceId: str, newState: str, oldState: str) -> None: ...
    def TrackingGuidContainerParentJobCorrelation(self, trackingId: Guid, containerParentJobInstanceId: Guid) -> None: ...
    def UnloadingWorkflow(self, workflowId: Guid) -> None: ...
    def WorkflowActivityExecutionFailed(self, workflowId: Guid, activityName: str, failureDescription: str) -> None: ...
    def WorkflowActivityValidated(self, workflowId: Guid, activityDisplayName: str, activityType: str) -> None: ...
    def WorkflowActivityValidationFailed(self, workflowId: Guid, activityDisplayName: str, activityType: str) -> None: ...
    def WorkflowCleanupPerformed(self, workflowId: Guid) -> None: ...
    def WorkflowDeletedFromDisk(self, workflowId: Guid, path: str) -> None: ...
    def WorkflowEngineStarted(self, endpointName: str) -> None: ...
    def WorkflowExecutionAborted(self, workflowId: Guid) -> None: ...
    def WorkflowExecutionCancelled(self, workflowId: Guid) -> None: ...
    def WorkflowExecutionError(self, workflowId: Guid, errorDescription: str) -> None: ...
    def WorkflowExecutionFinished(self, workflowId: Guid) -> None: ...
    def WorkflowExecutionStarted(self, workflowId: Guid, managedNodes: str) -> None: ...
    def WorkflowJobCreated(self, parentJobId: Guid, childJobId: Guid, childWorkflowId: Guid) -> None: ...
    def WorkflowLoadedForExecution(self, workflowId: Guid) -> None: ...
    def WorkflowLoadedFromDisk(self, workflowId: Guid, path: str) -> None: ...
    def WorkflowManagerCheckpoint(self, checkpointPath: str, configProviderId: str, userName: str, path: str) -> None: ...
    def WorkflowPersisted(self, workflowId: Guid) -> None: ...
    def WorkflowPluginRequestedToShutdown(self, endpointName: str) -> None: ...
    def WorkflowPluginRestarted(self, endpointName: str) -> None: ...
    def WorkflowPluginStarted(self, endpointName: str, user: str, hostingMode: str, protocol: str, configuration: str) -> None: ...
    def WorkflowQuotaViolated(self, endpointName: str, configName: str, allowedValue: str, valueInQuestion: str) -> None: ...
    def WorkflowResumed(self, workflowId: Guid) -> None: ...
    def WorkflowResuming(self, workflowId: Guid) -> None: ...
    def WorkflowRunspacePoolCreated(self, workflowId: Guid, managedNode: str) -> None: ...
    def WorkflowStateChanged(self, workflowId: Guid, newState: str, oldState: str) -> None: ...
    def WorkflowUnloaded(self, workflowId: Guid) -> None: ...
    def WorkflowValidationError(self, workflowId: Guid) -> None: ...
    def WorkflowValidationFinished(self, workflowId: Guid) -> None: ...
    def WorkflowValidationStarted(self, workflowId: Guid) -> None: ...
    def WriteTransferEvent(self, currentActivityId: Guid, parentActivityId: Guid) -> None: ...