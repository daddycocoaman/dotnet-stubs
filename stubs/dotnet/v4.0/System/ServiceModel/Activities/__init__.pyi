__all__ = ['Configuration','Description','Tracking']
from typing import Tuple, Set, Iterable, List


class CallbackCorrelationInitializer(CorrelationInitializer):
    def __init__(self): ...


class ChannelCacheSettings(Object):
    def __init__(self): ...
    @property
    def IdleTimeout(self) -> TimeSpan: ...
    @property
    def LeaseTimeout(self) -> TimeSpan: ...
    @property
    def MaxItemsInCache(self) -> int: ...
    @IdleTimeout.setter
    def IdleTimeout(self, value: TimeSpan) -> None: ...
    @LeaseTimeout.setter
    def LeaseTimeout(self, value: TimeSpan) -> None: ...
    @MaxItemsInCache.setter
    def MaxItemsInCache(self, value: int) -> None: ...


class ContextCorrelationInitializer(CorrelationInitializer):
    def __init__(self): ...


class CorrelationHandle(Handle):
    def __init__(self): ...


class CorrelationInitializer(Object):
    @property
    def CorrelationHandle(self) -> InArgument: ...
    @CorrelationHandle.setter
    def CorrelationHandle(self, value: InArgument) -> None: ...


class CorrelationScope(NativeActivity):
    def __init__(self): ...
    @property
    def Body(self) -> Activity: ...
    @property
    def CorrelatesWith(self) -> InArgument: ...
    @Body.setter
    def Body(self, value: Activity) -> None: ...
    @CorrelatesWith.setter
    def CorrelatesWith(self, value: InArgument) -> None: ...
    def ShouldSerializeCorrelatesWith(self) -> bool: ...


class DurableInstancingOptions(Object):
    def AddInitialInstanceValues(self, writeOnlyValues: IDictionary) -> None: ...
    def AddInstanceOwnerValues(self, readWriteValues: IDictionary, writeOnlyValues: IDictionary) -> None: ...
    @property
    def InstanceStore(self) -> InstanceStore: ...
    @InstanceStore.setter
    def InstanceStore(self, value: InstanceStore) -> None: ...


class HostSettings(Object):
    def __init__(self): ...
    @property
    def IncludeExceptionDetailInFaults(self) -> bool: ...
    @property
    def ScopeName(self) -> XName: ...
    @property
    def UseNoPersistHandle(self) -> bool: ...
    @IncludeExceptionDetailInFaults.setter
    def IncludeExceptionDetailInFaults(self, value: bool) -> None: ...
    @ScopeName.setter
    def ScopeName(self, value: XName) -> None: ...
    @UseNoPersistHandle.setter
    def UseNoPersistHandle(self, value: bool) -> None: ...


class InitializeCorrelation(NativeActivity):
    def __init__(self): ...
    @property
    def Correlation(self) -> InArgument: ...
    @property
    def CorrelationData(self) -> IDictionary: ...
    @Correlation.setter
    def Correlation(self, value: InArgument) -> None: ...


class IReceiveMessageCallback:
    def OnReceiveMessage(self, operationContext: OperationContext, activityExecutionProperties: ExecutionProperties) -> None: ...


class ISendMessageCallback:
    def OnSendMessage(self, operationContext: OperationContext) -> None: ...


class IWorkflowInstanceManagement:
    def Abandon(self, instanceId: Guid, reason: str) -> None: ...
    def BeginAbandon(self, instanceId: Guid, reason: str, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    def BeginCancel(self, instanceId: Guid, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    def BeginRun(self, instanceId: Guid, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    def BeginSuspend(self, instanceId: Guid, reason: str, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    def BeginTerminate(self, instanceId: Guid, reason: str, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    def BeginTransactedCancel(self, instanceId: Guid, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    def BeginTransactedRun(self, instanceId: Guid, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    def BeginTransactedSuspend(self, instanceId: Guid, reason: str, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    def BeginTransactedTerminate(self, instanceId: Guid, reason: str, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    def BeginTransactedUnsuspend(self, instanceId: Guid, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    def BeginUnsuspend(self, instanceId: Guid, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    def Cancel(self, instanceId: Guid) -> None: ...
    def EndAbandon(self, result: IAsyncResult) -> None: ...
    def EndCancel(self, result: IAsyncResult) -> None: ...
    def EndRun(self, result: IAsyncResult) -> None: ...
    def EndSuspend(self, result: IAsyncResult) -> None: ...
    def EndTerminate(self, result: IAsyncResult) -> None: ...
    def EndTransactedCancel(self, result: IAsyncResult) -> None: ...
    def EndTransactedRun(self, result: IAsyncResult) -> None: ...
    def EndTransactedSuspend(self, result: IAsyncResult) -> None: ...
    def EndTransactedTerminate(self, result: IAsyncResult) -> None: ...
    def EndTransactedUnsuspend(self, result: IAsyncResult) -> None: ...
    def EndUnsuspend(self, result: IAsyncResult) -> None: ...
    def Run(self, instanceId: Guid) -> None: ...
    def Suspend(self, instanceId: Guid, reason: str) -> None: ...
    def Terminate(self, instanceId: Guid, reason: str) -> None: ...
    def TransactedCancel(self, instanceId: Guid) -> None: ...
    def TransactedRun(self, instanceId: Guid) -> None: ...
    def TransactedSuspend(self, instanceId: Guid, reason: str) -> None: ...
    def TransactedTerminate(self, instanceId: Guid, reason: str) -> None: ...
    def TransactedUnsuspend(self, instanceId: Guid) -> None: ...
    def Unsuspend(self, instanceId: Guid) -> None: ...


class IWorkflowUpdateableInstanceManagement:
    def BeginTransactedUpdate(self, instanceId: Guid, updatedDefinitionIdentity: WorkflowIdentity, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    def BeginUpdate(self, instanceId: Guid, updatedDefinitionIdentity: WorkflowIdentity, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    def EndTransactedUpdate(self, result: IAsyncResult) -> None: ...
    def EndUpdate(self, result: IAsyncResult) -> None: ...
    def TransactedUpdate(self, instanceId: Guid, updatedDefinitionIdentity: WorkflowIdentity) -> None: ...
    def Update(self, instanceId: Guid, updatedDefinitionIdentity: WorkflowIdentity) -> None: ...


class MessageContext(Object):
    def __init__(self): ...
    @property
    def EndToEndTracingId(self) -> Guid: ...
    @property
    def Message(self) -> Message: ...
    @EndToEndTracingId.setter
    def EndToEndTracingId(self, value: Guid) -> None: ...
    @Message.setter
    def Message(self, value: Message) -> None: ...


class QueryCorrelationInitializer(CorrelationInitializer):
    def __init__(self): ...
    @property
    def MessageQuerySet(self) -> MessageQuerySet: ...
    @MessageQuerySet.setter
    def MessageQuerySet(self, value: MessageQuerySet) -> None: ...


class Receive(Activity):
    def __init__(self): ...
    def FromOperationDescription(operation: OperationDescription) -> Receive: ...
    @property
    def Action(self) -> str: ...
    @property
    def CanCreateInstance(self) -> bool: ...
    @property
    def Content(self) -> ReceiveContent: ...
    @property
    def CorrelatesOn(self) -> MessageQuerySet: ...
    @property
    def CorrelatesWith(self) -> InArgument: ...
    @property
    def CorrelationInitializers(self) -> Collection: ...
    @property
    def KnownTypes(self) -> Collection: ...
    @property
    def OperationName(self) -> str: ...
    @property
    def ProtectionLevel(self) -> Nullable: ...
    @property
    def SerializerOption(self) -> SerializerOption: ...
    @property
    def ServiceContractName(self) -> XName: ...
    @Action.setter
    def Action(self, value: str) -> None: ...
    @CanCreateInstance.setter
    def CanCreateInstance(self, value: bool) -> None: ...
    @Content.setter
    def Content(self, value: ReceiveContent) -> None: ...
    @CorrelatesOn.setter
    def CorrelatesOn(self, value: MessageQuerySet) -> None: ...
    @CorrelatesWith.setter
    def CorrelatesWith(self, value: InArgument) -> None: ...
    @OperationName.setter
    def OperationName(self, value: str) -> None: ...
    @ProtectionLevel.setter
    def ProtectionLevel(self, value: Nullable) -> None: ...
    @SerializerOption.setter
    def SerializerOption(self, value: SerializerOption) -> None: ...
    @ServiceContractName.setter
    def ServiceContractName(self, value: XName) -> None: ...
    def ShouldSerializeCorrelatesOn(self) -> bool: ...


class ReceiveContent(Object):
    @overload
    def Create(message: OutArgument) -> ReceiveMessageContent: ...
    @overload
    def Create(parameters: IDictionary) -> ReceiveParametersContent: ...
    @overload
    def Create(message: OutArgument, declaredMessageType: Type) -> ReceiveMessageContent: ...


class ReceiveMessageContent(ReceiveContent):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: OutArgument): ...
    @overload
    def __init__(self, message: OutArgument, declaredMessageType: Type): ...
    @property
    def DeclaredMessageType(self) -> Type: ...
    @property
    def Message(self) -> OutArgument: ...
    @DeclaredMessageType.setter
    def DeclaredMessageType(self, value: Type) -> None: ...
    @Message.setter
    def Message(self, value: OutArgument) -> None: ...
    def ShouldSerializeDeclaredMessageType(self) -> bool: ...


class ReceiveParametersContent(ReceiveContent):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, parameters: IDictionary): ...
    @property
    def Parameters(self) -> IDictionary: ...


class ReceiveReply(Activity):
    def __init__(self): ...
    @property
    def Action(self) -> str: ...
    @property
    def Content(self) -> ReceiveContent: ...
    @property
    def CorrelationInitializers(self) -> Collection: ...
    @property
    def Request(self) -> Send: ...
    @Action.setter
    def Action(self, value: str) -> None: ...
    @Content.setter
    def Content(self, value: ReceiveContent) -> None: ...
    @Request.setter
    def Request(self, value: Send) -> None: ...


class ReceiveSettings(Object):
    def __init__(self): ...
    @property
    def Action(self) -> str: ...
    @property
    def CanCreateInstance(self) -> bool: ...
    @property
    def OwnerDisplayName(self) -> str: ...
    @Action.setter
    def Action(self, value: str) -> None: ...
    @CanCreateInstance.setter
    def CanCreateInstance(self, value: bool) -> None: ...
    @OwnerDisplayName.setter
    def OwnerDisplayName(self, value: str) -> None: ...


class RequestReplyCorrelationInitializer(CorrelationInitializer):
    def __init__(self): ...


class Send(Activity):
    def __init__(self): ...
    @property
    def Action(self) -> str: ...
    @property
    def Content(self) -> SendContent: ...
    @property
    def CorrelatesWith(self) -> InArgument: ...
    @property
    def CorrelationInitializers(self) -> Collection: ...
    @property
    def Endpoint(self) -> Endpoint: ...
    @property
    def EndpointAddress(self) -> InArgument: ...
    @property
    def EndpointConfigurationName(self) -> str: ...
    @property
    def KnownTypes(self) -> Collection: ...
    @property
    def OperationName(self) -> str: ...
    @property
    def ProtectionLevel(self) -> Nullable: ...
    @property
    def SerializerOption(self) -> SerializerOption: ...
    @property
    def ServiceContractName(self) -> XName: ...
    @property
    def TokenImpersonationLevel(self) -> TokenImpersonationLevel: ...
    @Action.setter
    def Action(self, value: str) -> None: ...
    @Content.setter
    def Content(self, value: SendContent) -> None: ...
    @CorrelatesWith.setter
    def CorrelatesWith(self, value: InArgument) -> None: ...
    @Endpoint.setter
    def Endpoint(self, value: Endpoint) -> None: ...
    @EndpointAddress.setter
    def EndpointAddress(self, value: InArgument) -> None: ...
    @EndpointConfigurationName.setter
    def EndpointConfigurationName(self, value: str) -> None: ...
    @OperationName.setter
    def OperationName(self, value: str) -> None: ...
    @ProtectionLevel.setter
    def ProtectionLevel(self, value: Nullable) -> None: ...
    @SerializerOption.setter
    def SerializerOption(self, value: SerializerOption) -> None: ...
    @ServiceContractName.setter
    def ServiceContractName(self, value: XName) -> None: ...
    @TokenImpersonationLevel.setter
    def TokenImpersonationLevel(self, value: TokenImpersonationLevel) -> None: ...


class SendContent(Object):
    @overload
    def Create(message: InArgument) -> SendMessageContent: ...
    @overload
    def Create(parameters: IDictionary) -> SendParametersContent: ...
    @overload
    def Create(message: InArgument, declaredMessageType: Type) -> SendMessageContent: ...


class SendMessageChannelCache(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, factorySettings: ChannelCacheSettings, channelSettings: ChannelCacheSettings): ...
    @overload
    def __init__(self, factorySettings: ChannelCacheSettings, channelSettings: ChannelCacheSettings, allowUnsafeCaching: bool): ...
    def Dispose(self) -> None: ...
    @property
    def AllowUnsafeCaching(self) -> bool: ...
    @property
    def ChannelSettings(self) -> ChannelCacheSettings: ...
    @property
    def FactorySettings(self) -> ChannelCacheSettings: ...
    @AllowUnsafeCaching.setter
    def AllowUnsafeCaching(self, value: bool) -> None: ...
    @ChannelSettings.setter
    def ChannelSettings(self, value: ChannelCacheSettings) -> None: ...
    @FactorySettings.setter
    def FactorySettings(self, value: ChannelCacheSettings) -> None: ...


class SendMessageContent(SendContent):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: InArgument): ...
    @overload
    def __init__(self, message: InArgument, declaredMessageType: Type): ...
    @property
    def DeclaredMessageType(self) -> Type: ...
    @property
    def Message(self) -> InArgument: ...
    @DeclaredMessageType.setter
    def DeclaredMessageType(self, value: Type) -> None: ...
    @Message.setter
    def Message(self, value: InArgument) -> None: ...
    def ShouldSerializeDeclaredMessageType(self) -> bool: ...


class SendParametersContent(SendContent):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, parameters: IDictionary): ...
    @property
    def Parameters(self) -> IDictionary: ...


class SendReceiveExtension(Object):
    def Cancel(self, bookmark: Bookmark) -> None: ...
    @property
    def HostSettings(self) -> HostSettings: ...
    def OnUninitializeCorrelation(self, correlationKey: InstanceKey) -> None: ...
    def RegisterReceive(self, settings: ReceiveSettings, correlatesWith: InstanceKey, receiveBookmark: Bookmark) -> None: ...
    def Send(self, message: MessageContext, settings: SendSettings, correlatesWith: InstanceKey, sendCompleteBookmark: Bookmark) -> None: ...


class SendReply(Activity):
    def __init__(self): ...
    def FromOperationDescription(operation: OperationDescription) -> Tuple[SendReply, Iterable[SendReply]]: ...
    @property
    def Action(self) -> str: ...
    @property
    def Content(self) -> SendContent: ...
    @property
    def CorrelationInitializers(self) -> Collection: ...
    @property
    def PersistBeforeSend(self) -> bool: ...
    @property
    def Request(self) -> Receive: ...
    @Action.setter
    def Action(self, value: str) -> None: ...
    @Content.setter
    def Content(self, value: SendContent) -> None: ...
    @PersistBeforeSend.setter
    def PersistBeforeSend(self, value: bool) -> None: ...
    @Request.setter
    def Request(self, value: Receive) -> None: ...


class SendSettings(Object):
    def __init__(self): ...
    @property
    def Endpoint(self) -> Endpoint: ...
    @property
    def EndpointAddress(self) -> Uri: ...
    @property
    def EndpointConfigurationName(self) -> str: ...
    @property
    def IsOneWay(self) -> bool: ...
    @property
    def OwnerDisplayName(self) -> str: ...
    @property
    def ProtectionLevel(self) -> Nullable: ...
    @property
    def RequirePersistBeforeSend(self) -> bool: ...
    @property
    def TokenImpersonationLevel(self) -> TokenImpersonationLevel: ...
    @Endpoint.setter
    def Endpoint(self, value: Endpoint) -> None: ...
    @EndpointAddress.setter
    def EndpointAddress(self, value: Uri) -> None: ...
    @EndpointConfigurationName.setter
    def EndpointConfigurationName(self, value: str) -> None: ...
    @IsOneWay.setter
    def IsOneWay(self, value: bool) -> None: ...
    @OwnerDisplayName.setter
    def OwnerDisplayName(self, value: str) -> None: ...
    @ProtectionLevel.setter
    def ProtectionLevel(self, value: Nullable) -> None: ...
    @RequirePersistBeforeSend.setter
    def RequirePersistBeforeSend(self, value: bool) -> None: ...
    @TokenImpersonationLevel.setter
    def TokenImpersonationLevel(self, value: TokenImpersonationLevel) -> None: ...


class SerializerOption:
    DataContractSerializer = 0
    XmlSerializer = 1


class TransactedReceiveScope(NativeActivity):
    def __init__(self): ...
    @property
    def Body(self) -> Activity: ...
    @property
    def Request(self) -> Receive: ...
    @property
    def Variables(self) -> Collection: ...
    @Body.setter
    def Body(self, value: Activity) -> None: ...
    @Request.setter
    def Request(self, value: Receive) -> None: ...


class WorkflowControlClient:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, endpointConfigurationName: str): ...
    @overload
    def __init__(self, workflowEndpoint: WorkflowControlEndpoint): ...
    @overload
    def __init__(self, endpointConfigurationName: str, remoteAddress: EndpointAddress): ...
    @overload
    def __init__(self, endpointConfigurationName: str, remoteAddress: str): ...
    @overload
    def __init__(self, binding: Binding, remoteAddress: EndpointAddress): ...
    @overload
    def Abandon(self, instanceId: Guid) -> None: ...
    @overload
    def Abandon(self, instanceId: Guid, reason: str) -> None: ...
    @overload
    def AbandonAsync(self, instanceId: Guid) -> None: ...
    @overload
    def AbandonAsync(self, instanceId: Guid, reason: str) -> None: ...
    @overload
    def AbandonAsync(self, instanceId: Guid, userState: Object) -> None: ...
    @overload
    def AbandonAsync(self, instanceId: Guid, reason: str, userState: Object) -> None: ...
    def add_AbandonCompleted(self, value: EventHandler) -> None: ...
    def add_CancelCompleted(self, value: EventHandler) -> None: ...
    def add_RunCompleted(self, value: EventHandler) -> None: ...
    def add_SuspendCompleted(self, value: EventHandler) -> None: ...
    def add_TerminateCompleted(self, value: EventHandler) -> None: ...
    def add_UnsuspendCompleted(self, value: EventHandler) -> None: ...
    @overload
    def BeginAbandon(self, instanceId: Guid, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    @overload
    def BeginAbandon(self, instanceId: Guid, reason: str, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    def BeginCancel(self, instanceId: Guid, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    def BeginRun(self, instanceId: Guid, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    @overload
    def BeginSuspend(self, instanceId: Guid, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    @overload
    def BeginSuspend(self, instanceId: Guid, reason: str, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    @overload
    def BeginTerminate(self, instanceId: Guid, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    @overload
    def BeginTerminate(self, instanceId: Guid, reason: str, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    def BeginUnsuspend(self, instanceId: Guid, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    def Cancel(self, instanceId: Guid) -> None: ...
    @overload
    def CancelAsync(self, instanceId: Guid) -> None: ...
    @overload
    def CancelAsync(self, instanceId: Guid, userState: Object) -> None: ...
    def EndAbandon(self, result: IAsyncResult) -> None: ...
    def EndCancel(self, result: IAsyncResult) -> None: ...
    def EndRun(self, result: IAsyncResult) -> None: ...
    def EndSuspend(self, result: IAsyncResult) -> None: ...
    def EndTerminate(self, result: IAsyncResult) -> None: ...
    def EndUnsuspend(self, result: IAsyncResult) -> None: ...
    def remove_AbandonCompleted(self, value: EventHandler) -> None: ...
    def remove_CancelCompleted(self, value: EventHandler) -> None: ...
    def remove_RunCompleted(self, value: EventHandler) -> None: ...
    def remove_SuspendCompleted(self, value: EventHandler) -> None: ...
    def remove_TerminateCompleted(self, value: EventHandler) -> None: ...
    def remove_UnsuspendCompleted(self, value: EventHandler) -> None: ...
    def Run(self, instanceId: Guid) -> None: ...
    @overload
    def RunAsync(self, instanceId: Guid) -> None: ...
    @overload
    def RunAsync(self, instanceId: Guid, userState: Object) -> None: ...
    @overload
    def Suspend(self, instanceId: Guid) -> None: ...
    @overload
    def Suspend(self, instanceId: Guid, reason: str) -> None: ...
    @overload
    def SuspendAsync(self, instanceId: Guid) -> None: ...
    @overload
    def SuspendAsync(self, instanceId: Guid, reason: str) -> None: ...
    @overload
    def SuspendAsync(self, instanceId: Guid, userState: Object) -> None: ...
    @overload
    def SuspendAsync(self, instanceId: Guid, reason: str, userState: Object) -> None: ...
    @overload
    def Terminate(self, instanceId: Guid) -> None: ...
    @overload
    def Terminate(self, instanceId: Guid, reason: str) -> None: ...
    @overload
    def TerminateAsync(self, instanceId: Guid) -> None: ...
    @overload
    def TerminateAsync(self, instanceId: Guid, userState: Object) -> None: ...
    @overload
    def TerminateAsync(self, instanceId: Guid, reason: str) -> None: ...
    @overload
    def TerminateAsync(self, instanceId: Guid, reason: str, userState: Object) -> None: ...
    def Unsuspend(self, instanceId: Guid) -> None: ...
    @overload
    def UnsuspendAsync(self, instanceId: Guid) -> None: ...
    @overload
    def UnsuspendAsync(self, instanceId: Guid, userState: Object) -> None: ...


class WorkflowControlEndpoint(ServiceEndpoint):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, binding: Binding, address: EndpointAddress): ...


class WorkflowCreationContext(Object):
    def __init__(self): ...
    @property
    def CreateOnly(self) -> bool: ...
    @property
    def IsCompletionTransactionRequired(self) -> bool: ...
    @property
    def WorkflowArguments(self) -> IDictionary: ...
    @CreateOnly.setter
    def CreateOnly(self, value: bool) -> None: ...
    @IsCompletionTransactionRequired.setter
    def IsCompletionTransactionRequired(self, value: bool) -> None: ...


class WorkflowHostingEndpoint(ServiceEndpoint):
    @property
    def CorrelationQueries(self) -> Collection: ...


class WorkflowHostingResponseContext(Object):
    def SendResponse(self, returnValue: Object, outputs: Set(Object)) -> None: ...


class WorkflowService(Object):
    def __init__(self): ...
    @property
    def AllowBufferedReceive(self) -> bool: ...
    @property
    def Body(self) -> Activity: ...
    @property
    def ConfigurationName(self) -> str: ...
    @property
    def DefinitionIdentity(self) -> WorkflowIdentity: ...
    @property
    def Endpoints(self) -> Collection: ...
    @property
    def ImplementedContracts(self) -> Collection: ...
    @property
    def Name(self) -> XName: ...
    @property
    def UpdateMaps(self) -> IDictionary: ...
    def GetContractDescriptions(self) -> IDictionary: ...
    def GetWorkflowRoot(self) -> Activity: ...
    @AllowBufferedReceive.setter
    def AllowBufferedReceive(self, value: bool) -> None: ...
    @Body.setter
    def Body(self, value: Activity) -> None: ...
    @ConfigurationName.setter
    def ConfigurationName(self, value: str) -> None: ...
    @DefinitionIdentity.setter
    def DefinitionIdentity(self, value: WorkflowIdentity) -> None: ...
    @Name.setter
    def Name(self, value: XName) -> None: ...
    def Validate(self, settings: ValidationSettings) -> ValidationResults: ...


class WorkflowServiceHost(ServiceHostBase):
    @overload
    def __init__(self, serviceImplementation: Object, baseAddresses: Set(Uri)): ...
    @overload
    def __init__(self, activity: Activity, baseAddresses: Set(Uri)): ...
    @overload
    def __init__(self, serviceDefinition: WorkflowService, baseAddresses: Set(Uri)): ...
    @overload
    def AddServiceEndpoint(self, endpoint: ServiceEndpoint) -> None: ...
    @overload
    def AddServiceEndpoint(self, implementedContract: str, binding: Binding, address: str) -> ServiceEndpoint: ...
    @overload
    def AddServiceEndpoint(self, implementedContract: str, binding: Binding, address: Uri) -> ServiceEndpoint: ...
    @overload
    def AddServiceEndpoint(self, implementedContract: str, binding: Binding, address: Uri, listenUri: Uri) -> ServiceEndpoint: ...
    @overload
    def AddServiceEndpoint(self, implementedContract: str, binding: Binding, address: str, listenUri: Uri) -> ServiceEndpoint: ...
    @overload
    def AddServiceEndpoint(self, serviceContractName: XName, binding: Binding, address: Uri, listenUri: Uri, behaviorConfigurationName: str) -> ServiceEndpoint: ...
    @overload
    def AddServiceEndpoint(self, serviceContractName: XName, binding: Binding, address: str, listenUri: Uri, behaviorConfigurationName: str) -> ServiceEndpoint: ...
    @property
    def Activity(self) -> Activity: ...
    @property
    def DurableInstancingOptions(self) -> DurableInstancingOptions: ...
    @property
    def SupportedVersions(self) -> ICollection: ...
    @property
    def WorkflowExtensions(self) -> WorkflowInstanceExtensionManager: ...


class WorkflowUpdateableControlClient:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, endpointConfigurationName: str): ...
    @overload
    def __init__(self, workflowEndpoint: WorkflowControlEndpoint): ...
    @overload
    def __init__(self, endpointConfigurationName: str, remoteAddress: EndpointAddress): ...
    @overload
    def __init__(self, endpointConfigurationName: str, remoteAddress: str): ...
    @overload
    def __init__(self, binding: Binding, remoteAddress: EndpointAddress): ...
    @overload
    def Abandon(self, instanceId: Guid) -> None: ...
    @overload
    def Abandon(self, instanceId: Guid, reason: str) -> None: ...
    @overload
    def AbandonAsync(self, instanceId: Guid) -> None: ...
    @overload
    def AbandonAsync(self, instanceId: Guid, reason: str) -> None: ...
    @overload
    def AbandonAsync(self, instanceId: Guid, userState: Object) -> None: ...
    @overload
    def AbandonAsync(self, instanceId: Guid, reason: str, userState: Object) -> None: ...
    def add_AbandonCompleted(self, value: EventHandler) -> None: ...
    def add_CancelCompleted(self, value: EventHandler) -> None: ...
    def add_RunCompleted(self, value: EventHandler) -> None: ...
    def add_SuspendCompleted(self, value: EventHandler) -> None: ...
    def add_TerminateCompleted(self, value: EventHandler) -> None: ...
    def add_UnsuspendCompleted(self, value: EventHandler) -> None: ...
    def add_UpdateCompleted(self, value: EventHandler) -> None: ...
    @overload
    def BeginAbandon(self, instanceId: Guid, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    @overload
    def BeginAbandon(self, instanceId: Guid, reason: str, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    def BeginCancel(self, instanceId: Guid, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    def BeginRun(self, instanceId: Guid, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    @overload
    def BeginSuspend(self, instanceId: Guid, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    @overload
    def BeginSuspend(self, instanceId: Guid, reason: str, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    @overload
    def BeginTerminate(self, instanceId: Guid, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    @overload
    def BeginTerminate(self, instanceId: Guid, reason: str, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    def BeginUnsuspend(self, instanceId: Guid, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    def BeginUpdate(self, instanceId: Guid, updatedDefinitionIdentity: WorkflowIdentity, callback: AsyncCallback, state: Object) -> IAsyncResult: ...
    def Cancel(self, instanceId: Guid) -> None: ...
    @overload
    def CancelAsync(self, instanceId: Guid) -> None: ...
    @overload
    def CancelAsync(self, instanceId: Guid, userState: Object) -> None: ...
    def EndAbandon(self, result: IAsyncResult) -> None: ...
    def EndCancel(self, result: IAsyncResult) -> None: ...
    def EndRun(self, result: IAsyncResult) -> None: ...
    def EndSuspend(self, result: IAsyncResult) -> None: ...
    def EndTerminate(self, result: IAsyncResult) -> None: ...
    def EndUnsuspend(self, result: IAsyncResult) -> None: ...
    def EndUpdate(self, result: IAsyncResult) -> None: ...
    def remove_AbandonCompleted(self, value: EventHandler) -> None: ...
    def remove_CancelCompleted(self, value: EventHandler) -> None: ...
    def remove_RunCompleted(self, value: EventHandler) -> None: ...
    def remove_SuspendCompleted(self, value: EventHandler) -> None: ...
    def remove_TerminateCompleted(self, value: EventHandler) -> None: ...
    def remove_UnsuspendCompleted(self, value: EventHandler) -> None: ...
    def remove_UpdateCompleted(self, value: EventHandler) -> None: ...
    def Run(self, instanceId: Guid) -> None: ...
    @overload
    def RunAsync(self, instanceId: Guid) -> None: ...
    @overload
    def RunAsync(self, instanceId: Guid, userState: Object) -> None: ...
    @overload
    def Suspend(self, instanceId: Guid) -> None: ...
    @overload
    def Suspend(self, instanceId: Guid, reason: str) -> None: ...
    @overload
    def SuspendAsync(self, instanceId: Guid) -> None: ...
    @overload
    def SuspendAsync(self, instanceId: Guid, userState: Object) -> None: ...
    @overload
    def SuspendAsync(self, instanceId: Guid, reason: str) -> None: ...
    @overload
    def SuspendAsync(self, instanceId: Guid, reason: str, userState: Object) -> None: ...
    @overload
    def Terminate(self, instanceId: Guid) -> None: ...
    @overload
    def Terminate(self, instanceId: Guid, reason: str) -> None: ...
    @overload
    def TerminateAsync(self, instanceId: Guid) -> None: ...
    @overload
    def TerminateAsync(self, instanceId: Guid, userState: Object) -> None: ...
    @overload
    def TerminateAsync(self, instanceId: Guid, reason: str) -> None: ...
    @overload
    def TerminateAsync(self, instanceId: Guid, reason: str, userState: Object) -> None: ...
    def Unsuspend(self, instanceId: Guid) -> None: ...
    @overload
    def UnsuspendAsync(self, instanceId: Guid) -> None: ...
    @overload
    def UnsuspendAsync(self, instanceId: Guid, userState: Object) -> None: ...
    def Update(self, instanceId: Guid, updatedDefinitionIdentity: WorkflowIdentity) -> None: ...
    @overload
    def UpdateAsync(self, instanceId: Guid, updatedDefinitionIdentity: WorkflowIdentity) -> None: ...
    @overload
    def UpdateAsync(self, instanceId: Guid, updatedDefinitionIdentity: WorkflowIdentity, userState: Object) -> None: ...
