from typing import Tuple, Set, Iterable, List


class IHttpRequestLineHandler:
    def OnStartLine(self, method: HttpMethod, version: HttpVersion, target: Span, path: Span, query: Span, customMethod: Span, pathEncoded: bool) -> None: ...
