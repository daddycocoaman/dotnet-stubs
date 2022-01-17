from typing import Tuple, Set, Iterable, List


class UriHelper:
    def BuildAbsolute(scheme: str, host: HostString, pathBase: PathString, path: PathString, query: QueryString, fragment: FragmentString) -> str: ...
    def BuildRelative(pathBase: PathString, path: PathString, query: QueryString, fragment: FragmentString) -> str: ...
    def Encode(uri: Uri) -> str: ...
    def FromAbsolute(uri: str) -> Tuple[str, HostString, PathString, QueryString, FragmentString]: ...
    def GetDisplayUrl(request: HttpRequest) -> str: ...
    def GetEncodedPathAndQuery(request: HttpRequest) -> str: ...
    def GetEncodedUrl(request: HttpRequest) -> str: ...