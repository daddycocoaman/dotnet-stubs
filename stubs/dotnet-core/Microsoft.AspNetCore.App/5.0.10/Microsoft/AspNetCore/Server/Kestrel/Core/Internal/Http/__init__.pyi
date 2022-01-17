from typing import Tuple, Set, Iterable, List


class HttpMethod:
    Get = 0
    Put = 1
    Delete = 2
    Post = 3
    Head = 4
    Trace = 5
    Patch = 6
    Connect = 7
    Options = 8
    Custom = 9
    #None = 255




class HttpScheme:
    Http = 0
    Https = 1
    Unknown = -1


class HttpVersion:
    Http10 = 0
    Http11 = 1
    Http2 = 2
    Http3 = 3
    Unknown = -1


class HttpVersionAndMethod:
    def __init__(self, method: HttpMethod, methodEnd: int): ...
    @property
    def Method(self) -> HttpMethod: ...
    @property
    def MethodEnd(self) -> int: ...
    @property
    def Version(self) -> HttpVersion: ...
    @Version.setter
    def Version(self, value: HttpVersion) -> None: ...


class IHttpHeadersHandler:
    def OnHeader(self, name: ReadOnlySpan, value: ReadOnlySpan) -> None: ...
    def OnHeadersComplete(self, endStream: bool) -> None: ...
    @overload
    def OnStaticIndexedHeader(self, index: int) -> None: ...
    @overload
    def OnStaticIndexedHeader(self, index: int, value: ReadOnlySpan) -> None: ...


class IHttpRequestLineHandler:
    def OnStartLine(self, versionAndMethod: HttpVersionAndMethod, targetPath: TargetOffsetPathLength, startLine: Span) -> None: ...


class TargetOffsetPathLength:
    def __init__(self, offset: int, length: int, isEncoded: bool): ...
    @property
    def IsEncoded(self) -> bool: ...
    @property
    def Length(self) -> int: ...
    @property
    def Offset(self) -> int: ...
