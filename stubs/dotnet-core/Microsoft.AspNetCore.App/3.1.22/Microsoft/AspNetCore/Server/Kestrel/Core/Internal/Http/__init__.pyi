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
    Unknown = -1


class IHttpHeadersHandler:
    def OnHeader(self, name: Span, value: Span) -> None: ...
    def OnHeadersComplete(self) -> None: ...




class IHttpRequestLineHandler:
    def OnStartLine(self, method: HttpMethod, version: HttpVersion, target: Span, path: Span, query: Span, customMethod: Span, pathEncoded: bool) -> None: ...
