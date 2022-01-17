from typing import Tuple, Set, Iterable, List


class AspNetCacheProfileAttribute(Attribute):
    def __init__(self, cacheProfileName: str): ...
    def AddBindingParameters(self, operationDescription: OperationDescription, bindingParameters: BindingParameterCollection) -> None: ...
    def ApplyClientBehavior(self, operationDescription: OperationDescription, clientOperation: ClientOperation) -> None: ...
    def ApplyDispatchBehavior(self, operationDescription: OperationDescription, dispatchOperation: DispatchOperation) -> None: ...
    @property
    def CacheProfileName(self) -> str: ...
    def Validate(self, operationDescription: OperationDescription) -> None: ...


class IncomingWebRequestContext(Object):
    @overload
    def CheckConditionalRetrieve(self, entityTag: str) -> None: ...
    @overload
    def CheckConditionalRetrieve(self, lastModified: DateTime) -> None: ...
    @overload
    def CheckConditionalRetrieve(self, entityTag: Guid) -> None: ...
    @overload
    def CheckConditionalRetrieve(self, entityTag: Int64) -> None: ...
    @overload
    def CheckConditionalRetrieve(self, entityTag: int) -> None: ...
    @overload
    def CheckConditionalUpdate(self, entityTag: Guid) -> None: ...
    @overload
    def CheckConditionalUpdate(self, entityTag: Int64) -> None: ...
    @overload
    def CheckConditionalUpdate(self, entityTag: int) -> None: ...
    @overload
    def CheckConditionalUpdate(self, entityTag: str) -> None: ...
    @property
    def Accept(self) -> str: ...
    @property
    def ContentLength(self) -> Int64: ...
    @property
    def ContentType(self) -> str: ...
    @property
    def Headers(self) -> WebHeaderCollection: ...
    @property
    def IfMatch(self) -> Iterable[str]: ...
    @property
    def IfModifiedSince(self) -> Nullable: ...
    @property
    def IfNoneMatch(self) -> Iterable[str]: ...
    @property
    def IfUnmodifiedSince(self) -> Nullable: ...
    @property
    def Method(self) -> str: ...
    @property
    def UriTemplateMatch(self) -> UriTemplateMatch: ...
    @property
    def UserAgent(self) -> str: ...
    def GetAcceptHeaderElements(self) -> Collection: ...
    @UriTemplateMatch.setter
    def UriTemplateMatch(self, value: UriTemplateMatch) -> None: ...


class IncomingWebResponseContext(Object):
    @property
    def ContentLength(self) -> Int64: ...
    @property
    def ContentType(self) -> str: ...
    @property
    def ETag(self) -> str: ...
    @property
    def Headers(self) -> WebHeaderCollection: ...
    @property
    def Location(self) -> str: ...
    @property
    def StatusCode(self) -> HttpStatusCode: ...
    @property
    def StatusDescription(self) -> str: ...


class JavascriptCallbackBehaviorAttribute(Attribute):
    def __init__(self): ...
    def AddBindingParameters(self, contractDescription: ContractDescription, endpoint: ServiceEndpoint, bindingParameters: BindingParameterCollection) -> None: ...
    def ApplyClientBehavior(self, contractDescription: ContractDescription, endpoint: ServiceEndpoint, clientRuntime: ClientRuntime) -> None: ...
    def ApplyDispatchBehavior(self, contractDescription: ContractDescription, endpoint: ServiceEndpoint, dispatchRuntime: DispatchRuntime) -> None: ...
    @property
    def UrlParameterName(self) -> str: ...
    @UrlParameterName.setter
    def UrlParameterName(self, value: str) -> None: ...
    def Validate(self, contractDescription: ContractDescription, endpoint: ServiceEndpoint) -> None: ...


class OutgoingWebRequestContext(Object):
    @property
    def Accept(self) -> str: ...
    @property
    def ContentLength(self) -> Int64: ...
    @property
    def ContentType(self) -> str: ...
    @property
    def Headers(self) -> WebHeaderCollection: ...
    @property
    def IfMatch(self) -> str: ...
    @property
    def IfModifiedSince(self) -> str: ...
    @property
    def IfNoneMatch(self) -> str: ...
    @property
    def IfUnmodifiedSince(self) -> str: ...
    @property
    def Method(self) -> str: ...
    @property
    def SuppressEntityBody(self) -> bool: ...
    @property
    def UserAgent(self) -> str: ...
    @Accept.setter
    def Accept(self, value: str) -> None: ...
    @ContentLength.setter
    def ContentLength(self, value: Int64) -> None: ...
    @ContentType.setter
    def ContentType(self, value: str) -> None: ...
    @IfMatch.setter
    def IfMatch(self, value: str) -> None: ...
    @IfModifiedSince.setter
    def IfModifiedSince(self, value: str) -> None: ...
    @IfNoneMatch.setter
    def IfNoneMatch(self, value: str) -> None: ...
    @IfUnmodifiedSince.setter
    def IfUnmodifiedSince(self, value: str) -> None: ...
    @Method.setter
    def Method(self, value: str) -> None: ...
    @SuppressEntityBody.setter
    def SuppressEntityBody(self, value: bool) -> None: ...
    @UserAgent.setter
    def UserAgent(self, value: str) -> None: ...


class OutgoingWebResponseContext(Object):
    @property
    def BindingWriteEncoding(self) -> Encoding: ...
    @property
    def ContentLength(self) -> Int64: ...
    @property
    def ContentType(self) -> str: ...
    @property
    def ETag(self) -> str: ...
    @property
    def Format(self) -> Nullable: ...
    @property
    def Headers(self) -> WebHeaderCollection: ...
    @property
    def LastModified(self) -> DateTime: ...
    @property
    def Location(self) -> str: ...
    @property
    def StatusCode(self) -> HttpStatusCode: ...
    @property
    def StatusDescription(self) -> str: ...
    @property
    def SuppressEntityBody(self) -> bool: ...
    @ContentLength.setter
    def ContentLength(self, value: Int64) -> None: ...
    @ContentType.setter
    def ContentType(self, value: str) -> None: ...
    @ETag.setter
    def ETag(self, value: str) -> None: ...
    @Format.setter
    def Format(self, value: Nullable) -> None: ...
    @LastModified.setter
    def LastModified(self, value: DateTime) -> None: ...
    @Location.setter
    def Location(self, value: str) -> None: ...
    @StatusCode.setter
    def StatusCode(self, value: HttpStatusCode) -> None: ...
    @StatusDescription.setter
    def StatusDescription(self, value: str) -> None: ...
    @SuppressEntityBody.setter
    def SuppressEntityBody(self, value: bool) -> None: ...
    @overload
    def SetETag(self, entityTag: int) -> None: ...
    @overload
    def SetETag(self, entityTag: Int64) -> None: ...
    @overload
    def SetETag(self, entityTag: str) -> None: ...
    @overload
    def SetETag(self, entityTag: Guid) -> None: ...
    def SetStatusAsCreated(self, locationUri: Uri) -> None: ...
    @overload
    def SetStatusAsNotFound(self) -> None: ...
    @overload
    def SetStatusAsNotFound(self, description: str) -> None: ...




class WebFaultException(FaultException):
    def __init__(self, statusCode: HttpStatusCode): ...
    @property
    def StatusCode(self) -> HttpStatusCode: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...




class WebGetAttribute(Attribute):
    def __init__(self): ...
    @property
    def BodyStyle(self) -> WebMessageBodyStyle: ...
    @property
    def IsBodyStyleSetExplicitly(self) -> bool: ...
    @property
    def IsRequestFormatSetExplicitly(self) -> bool: ...
    @property
    def IsResponseFormatSetExplicitly(self) -> bool: ...
    @property
    def RequestFormat(self) -> WebMessageFormat: ...
    @property
    def ResponseFormat(self) -> WebMessageFormat: ...
    @property
    def UriTemplate(self) -> str: ...
    @BodyStyle.setter
    def BodyStyle(self, value: WebMessageBodyStyle) -> None: ...
    @RequestFormat.setter
    def RequestFormat(self, value: WebMessageFormat) -> None: ...
    @ResponseFormat.setter
    def ResponseFormat(self, value: WebMessageFormat) -> None: ...
    @UriTemplate.setter
    def UriTemplate(self, value: str) -> None: ...


class WebInvokeAttribute(Attribute):
    def __init__(self): ...
    @property
    def BodyStyle(self) -> WebMessageBodyStyle: ...
    @property
    def IsBodyStyleSetExplicitly(self) -> bool: ...
    @property
    def IsRequestFormatSetExplicitly(self) -> bool: ...
    @property
    def IsResponseFormatSetExplicitly(self) -> bool: ...
    @property
    def Method(self) -> str: ...
    @property
    def RequestFormat(self) -> WebMessageFormat: ...
    @property
    def ResponseFormat(self) -> WebMessageFormat: ...
    @property
    def UriTemplate(self) -> str: ...
    @BodyStyle.setter
    def BodyStyle(self, value: WebMessageBodyStyle) -> None: ...
    @Method.setter
    def Method(self, value: str) -> None: ...
    @RequestFormat.setter
    def RequestFormat(self, value: WebMessageFormat) -> None: ...
    @ResponseFormat.setter
    def ResponseFormat(self, value: WebMessageFormat) -> None: ...
    @UriTemplate.setter
    def UriTemplate(self, value: str) -> None: ...


class WebMessageBodyStyle:
    Bare = 0
    Wrapped = 1
    WrappedRequest = 2
    WrappedResponse = 3


class WebMessageFormat:
    Xml = 0
    Json = 1


class WebOperationContext(Object):
    def __init__(self, operationContext: OperationContext): ...
    def Attach(self, owner: OperationContext) -> None: ...
    @overload
    def CreateAtom10Response(self, item: SyndicationItem) -> Message: ...
    @overload
    def CreateAtom10Response(self, document: ServiceDocument) -> Message: ...
    @overload
    def CreateAtom10Response(self, feed: SyndicationFeed) -> Message: ...
    @overload
    def CreateJsonResponse(self, instance: T) -> Message: ...
    @overload
    def CreateJsonResponse(self, instance: T, serializer: DataContractJsonSerializer) -> Message: ...
    @overload
    def CreateStreamResponse(self, streamWriter: Action, contentType: str) -> Message: ...
    @overload
    def CreateStreamResponse(self, bodyWriter: StreamBodyWriter, contentType: str) -> Message: ...
    @overload
    def CreateStreamResponse(self, stream: Stream, contentType: str) -> Message: ...
    @overload
    def CreateTextResponse(self, text: str) -> Message: ...
    @overload
    def CreateTextResponse(self, text: str, contentType: str) -> Message: ...
    @overload
    def CreateTextResponse(self, textWriter: Action, contentType: str) -> Message: ...
    @overload
    def CreateTextResponse(self, textWriter: Action, contentType: str, encoding: Encoding) -> Message: ...
    @overload
    def CreateTextResponse(self, text: str, contentType: str, encoding: Encoding) -> Message: ...
    @overload
    def CreateXmlResponse(self, document: XDocument) -> Message: ...
    @overload
    def CreateXmlResponse(self, element: XElement) -> Message: ...
    @overload
    def CreateXmlResponse(self, instance: T) -> Message: ...
    @overload
    def CreateXmlResponse(self, instance: T, serializer: XmlSerializer) -> Message: ...
    @overload
    def CreateXmlResponse(self, instance: T, serializer: XmlObjectSerializer) -> Message: ...
    def Detach(self, owner: OperationContext) -> None: ...
    @property
    def Current() -> WebOperationContext: ...
    @property
    def IncomingRequest(self) -> IncomingWebRequestContext: ...
    @property
    def IncomingResponse(self) -> IncomingWebResponseContext: ...
    @property
    def OutgoingRequest(self) -> OutgoingWebRequestContext: ...
    @property
    def OutgoingResponse(self) -> OutgoingWebResponseContext: ...
    def GetUriTemplate(self, operationName: str) -> UriTemplate: ...


class WebServiceHost(ServiceHost):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, singletonInstance: Object, baseAddresses: Set(Uri)): ...
    @overload
    def __init__(self, serviceType: Type, baseAddresses: Set(Uri)): ...
