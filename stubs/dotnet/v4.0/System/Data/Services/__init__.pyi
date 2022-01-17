__all__ = ['Configuration','Internal','Providers']
from typing import Tuple, Set, Iterable, List


class ChangeInterceptorAttribute(Attribute):
    def __init__(self, entitySetName: str): ...
    @property
    def EntitySetName(self) -> str: ...




class DataServiceBehavior(Object):
    @property
    def AcceptCountRequests(self) -> bool: ...
    @property
    def AcceptProjectionRequests(self) -> bool: ...
    @property
    def AcceptReplaceFunctionInQuery(self) -> bool: ...
    @property
    def InvokeInterceptorsOnLinkDelete(self) -> bool: ...
    @property
    def MaxProtocolVersion(self) -> DataServiceProtocolVersion: ...
    @AcceptCountRequests.setter
    def AcceptCountRequests(self, value: bool) -> None: ...
    @AcceptProjectionRequests.setter
    def AcceptProjectionRequests(self, value: bool) -> None: ...
    @AcceptReplaceFunctionInQuery.setter
    def AcceptReplaceFunctionInQuery(self, value: bool) -> None: ...
    @InvokeInterceptorsOnLinkDelete.setter
    def InvokeInterceptorsOnLinkDelete(self, value: bool) -> None: ...
    @MaxProtocolVersion.setter
    def MaxProtocolVersion(self, value: DataServiceProtocolVersion) -> None: ...


class DataServiceConfiguration(Object):
    def EnableTypeAccess(self, typeName: str) -> None: ...
    @property
    def DataServiceBehavior(self) -> DataServiceBehavior: ...
    @property
    def EnableTypeConversion(self) -> bool: ...
    @property
    def MaxBatchCount(self) -> int: ...
    @property
    def MaxChangesetCount(self) -> int: ...
    @property
    def MaxExpandCount(self) -> int: ...
    @property
    def MaxExpandDepth(self) -> int: ...
    @property
    def MaxObjectCountOnInsert(self) -> int: ...
    @property
    def MaxResultsPerCollection(self) -> int: ...
    @property
    def UseVerboseErrors(self) -> bool: ...
    def RegisterKnownType(self, type: Type) -> None: ...
    @EnableTypeConversion.setter
    def EnableTypeConversion(self, value: bool) -> None: ...
    @MaxBatchCount.setter
    def MaxBatchCount(self, value: int) -> None: ...
    @MaxChangesetCount.setter
    def MaxChangesetCount(self, value: int) -> None: ...
    @MaxExpandCount.setter
    def MaxExpandCount(self, value: int) -> None: ...
    @MaxExpandDepth.setter
    def MaxExpandDepth(self, value: int) -> None: ...
    @MaxObjectCountOnInsert.setter
    def MaxObjectCountOnInsert(self, value: int) -> None: ...
    @MaxResultsPerCollection.setter
    def MaxResultsPerCollection(self, value: int) -> None: ...
    @UseVerboseErrors.setter
    def UseVerboseErrors(self, value: bool) -> None: ...
    def SetEntitySetAccessRule(self, name: str, rights: EntitySetRights) -> None: ...
    def SetEntitySetPageSize(self, name: str, size: int) -> None: ...
    def SetServiceOperationAccessRule(self, name: str, rights: ServiceOperationRights) -> None: ...


class DataServiceException(InvalidOperationException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...
    @overload
    def __init__(self, statusCode: int, message: str): ...
    @overload
    def __init__(self, statusCode: int, errorCode: str, message: str, messageXmlLang: str, innerException: Exception): ...
    @property
    def ErrorCode(self) -> str: ...
    @property
    def MessageLanguage(self) -> str: ...
    @property
    def StatusCode(self) -> int: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...


class DataServiceHost(WebServiceHost):
    def __init__(self, serviceType: Type, baseAddresses: Set(Uri)): ...


class DataServiceHostFactory(ServiceHostFactory):
    def __init__(self): ...


class DataServiceOperationContext(Object):
    @property
    def AbsoluteRequestUri(self) -> Uri: ...
    @property
    def AbsoluteServiceUri(self) -> Uri: ...
    @property
    def IsBatchRequest(self) -> bool: ...
    @property
    def RequestHeaders(self) -> WebHeaderCollection: ...
    @property
    def RequestMethod(self) -> str: ...
    @property
    def ResponseHeaders(self) -> WebHeaderCollection: ...
    @property
    def ResponseStatusCode(self) -> int: ...
    @ResponseStatusCode.setter
    def ResponseStatusCode(self, value: int) -> None: ...


class DataServiceProcessingPipeline(Object):
    def __init__(self): ...
    def add_ProcessedChangeset(self, value: EventHandler) -> None: ...
    def add_ProcessedRequest(self, value: EventHandler) -> None: ...
    def add_ProcessingChangeset(self, value: EventHandler) -> None: ...
    def add_ProcessingRequest(self, value: EventHandler) -> None: ...
    def remove_ProcessedChangeset(self, value: EventHandler) -> None: ...
    def remove_ProcessedRequest(self, value: EventHandler) -> None: ...
    def remove_ProcessingChangeset(self, value: EventHandler) -> None: ...
    def remove_ProcessingRequest(self, value: EventHandler) -> None: ...


class DataServiceProcessingPipelineEventArgs(EventArgs):
    @property
    def OperationContext(self) -> DataServiceOperationContext: ...


class EntitySetRights:
    #None = 0
    ReadSingle = 1
    ReadMultiple = 2
    AllRead = 3
    WriteAppend = 4
    WriteReplace = 8
    WriteDelete = 16
    WriteMerge = 32
    AllWrite = 60
    All = 63


class ETagAttribute(Attribute):
    @overload
    def __init__(self, propertyName: str): ...
    @overload
    def __init__(self, propertyNames: Set(str)): ...
    @property
    def PropertyNames(self) -> ReadOnlyCollection: ...


class ExpandSegment(Object):
    def __init__(self, name: str, filter: Expression): ...
    @property
    def ExpandedProperty(self) -> ResourceProperty: ...
    @property
    def Filter(self) -> Expression: ...
    @property
    def HasFilter(self) -> bool: ...
    @property
    def MaxResultsExpected(self) -> int: ...
    @property
    def Name(self) -> str: ...
    def PathHasFilter(path: Iterable[ExpandSegment]) -> bool: ...


class ExpandSegmentCollection:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, capacity: int): ...
    @property
    def HasFilter(self) -> bool: ...


class HandleExceptionArgs(Object):
    @property
    def Exception(self) -> Exception: ...
    @property
    def ResponseContentType(self) -> str: ...
    @property
    def ResponseStatusCode(self) -> int: ...
    @property
    def ResponseWritten(self) -> bool: ...
    @property
    def UseVerboseErrors(self) -> bool: ...
    @Exception.setter
    def Exception(self, value: Exception) -> None: ...
    @UseVerboseErrors.setter
    def UseVerboseErrors(self, value: bool) -> None: ...


class IDataServiceConfiguration:
    @property
    def MaxBatchCount(self) -> int: ...
    @property
    def MaxChangesetCount(self) -> int: ...
    @property
    def MaxExpandCount(self) -> int: ...
    @property
    def MaxExpandDepth(self) -> int: ...
    @property
    def MaxObjectCountOnInsert(self) -> int: ...
    @property
    def MaxResultsPerCollection(self) -> int: ...
    @property
    def UseVerboseErrors(self) -> bool: ...
    def RegisterKnownType(self, type: Type) -> None: ...
    @MaxBatchCount.setter
    def MaxBatchCount(self, value: int) -> None: ...
    @MaxChangesetCount.setter
    def MaxChangesetCount(self, value: int) -> None: ...
    @MaxExpandCount.setter
    def MaxExpandCount(self, value: int) -> None: ...
    @MaxExpandDepth.setter
    def MaxExpandDepth(self, value: int) -> None: ...
    @MaxObjectCountOnInsert.setter
    def MaxObjectCountOnInsert(self, value: int) -> None: ...
    @MaxResultsPerCollection.setter
    def MaxResultsPerCollection(self, value: int) -> None: ...
    @UseVerboseErrors.setter
    def UseVerboseErrors(self, value: bool) -> None: ...
    def SetEntitySetAccessRule(self, name: str, rights: EntitySetRights) -> None: ...
    def SetServiceOperationAccessRule(self, name: str, rights: ServiceOperationRights) -> None: ...


class IDataServiceHost:
    @property
    def AbsoluteRequestUri(self) -> Uri: ...
    @property
    def AbsoluteServiceUri(self) -> Uri: ...
    @property
    def RequestAccept(self) -> str: ...
    @property
    def RequestAcceptCharSet(self) -> str: ...
    @property
    def RequestContentType(self) -> str: ...
    @property
    def RequestHttpMethod(self) -> str: ...
    @property
    def RequestIfMatch(self) -> str: ...
    @property
    def RequestIfNoneMatch(self) -> str: ...
    @property
    def RequestMaxVersion(self) -> str: ...
    @property
    def RequestStream(self) -> Stream: ...
    @property
    def RequestVersion(self) -> str: ...
    @property
    def ResponseCacheControl(self) -> str: ...
    @property
    def ResponseContentType(self) -> str: ...
    @property
    def ResponseETag(self) -> str: ...
    @property
    def ResponseLocation(self) -> str: ...
    @property
    def ResponseStatusCode(self) -> int: ...
    @property
    def ResponseStream(self) -> Stream: ...
    @property
    def ResponseVersion(self) -> str: ...
    def GetQueryStringItem(self, item: str) -> str: ...
    def ProcessException(self, args: HandleExceptionArgs) -> None: ...
    @ResponseCacheControl.setter
    def ResponseCacheControl(self, value: str) -> None: ...
    @ResponseContentType.setter
    def ResponseContentType(self, value: str) -> None: ...
    @ResponseETag.setter
    def ResponseETag(self, value: str) -> None: ...
    @ResponseLocation.setter
    def ResponseLocation(self, value: str) -> None: ...
    @ResponseStatusCode.setter
    def ResponseStatusCode(self, value: int) -> None: ...
    @ResponseVersion.setter
    def ResponseVersion(self, value: str) -> None: ...


class IDataServiceHost2:
    @property
    def RequestHeaders(self) -> WebHeaderCollection: ...
    @property
    def ResponseHeaders(self) -> WebHeaderCollection: ...


class IExpandedResult:
    @property
    def ExpandedElement(self) -> Object: ...
    def GetExpandedPropertyValue(self, name: str) -> Object: ...


class IExpandProvider:
    def ApplyExpansions(self, queryable: IQueryable, expandPaths: ICollection) -> IEnumerable: ...


class IgnorePropertiesAttribute(Attribute):
    @overload
    def __init__(self, propertyName: str): ...
    @overload
    def __init__(self, propertyNames: Set(str)): ...
    @property
    def PropertyNames(self) -> ReadOnlyCollection: ...


class IRequestHandler:
    def ProcessRequestForMessage(self, messageBody: Stream) -> Message: ...


class IUpdatable:
    def AddReferenceToCollection(self, targetResource: Object, propertyName: str, resourceToBeAdded: Object) -> None: ...
    def ClearChanges(self) -> None: ...
    def CreateResource(self, containerName: str, fullTypeName: str) -> Object: ...
    def DeleteResource(self, targetResource: Object) -> None: ...
    def GetResource(self, query: IQueryable, fullTypeName: str) -> Object: ...
    def GetValue(self, targetResource: Object, propertyName: str) -> Object: ...
    def RemoveReferenceFromCollection(self, targetResource: Object, propertyName: str, resourceToBeRemoved: Object) -> None: ...
    def ResetResource(self, resource: Object) -> Object: ...
    def ResolveResource(self, resource: Object) -> Object: ...
    def SaveChanges(self) -> None: ...
    def SetReference(self, targetResource: Object, propertyName: str, propertyValue: Object) -> None: ...
    def SetValue(self, targetResource: Object, propertyName: str, propertyValue: Object) -> None: ...


class MimeTypeAttribute(Attribute):
    def __init__(self, memberName: str, mimeType: str): ...
    @property
    def MemberName(self) -> str: ...
    @property
    def MimeType(self) -> str: ...


class ProcessRequestArgs(Object):
    @property
    def IsBatchOperation(self) -> bool: ...
    @property
    def OperationContext(self) -> DataServiceOperationContext: ...
    @property
    def RequestUri(self) -> Uri: ...


class QueryInterceptorAttribute(Attribute):
    def __init__(self, entitySetName: str): ...
    @property
    def EntitySetName(self) -> str: ...


class ServiceOperationRights:
    #None = 0
    ReadSingle = 1
    ReadMultiple = 2
    AllRead = 3
    All = 3
    OverrideEntitySetRights = 4


class SingleResultAttribute(Attribute):
    def __init__(self): ...


class UpdateOperations:
    #None = 0
    Add = 1
    Change = 2
    Delete = 4
