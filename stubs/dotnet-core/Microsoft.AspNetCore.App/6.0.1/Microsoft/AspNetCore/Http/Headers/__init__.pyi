from typing import Tuple, Set, Iterable, List


class ResponseHeaders:
    def __init__(self, headers: IHeaderDictionary): ...
    def Append(self, name: str, value: Object) -> None: ...
    def AppendList(self, name: str, values: IList) -> None: ...
    @property
    def CacheControl(self) -> CacheControlHeaderValue: ...
    @property
    def ContentDisposition(self) -> ContentDispositionHeaderValue: ...
    @property
    def ContentLength(self) -> Nullable: ...
    @property
    def ContentRange(self) -> ContentRangeHeaderValue: ...
    @property
    def ContentType(self) -> MediaTypeHeaderValue: ...
    @property
    def Date(self) -> Nullable: ...
    @property
    def ETag(self) -> EntityTagHeaderValue: ...
    @property
    def Expires(self) -> Nullable: ...
    @property
    def Headers(self) -> IHeaderDictionary: ...
    @property
    def LastModified(self) -> Nullable: ...
    @property
    def Location(self) -> Uri: ...
    def Get(self, name: str) -> T: ...
    @property
    def SetCookie(self) -> List[SetCookieHeaderValue]: ...
    def GetList(self, name: str) -> IList: ...
    @CacheControl.setter
    def CacheControl(self, value: CacheControlHeaderValue) -> None: ...
    @ContentDisposition.setter
    def ContentDisposition(self, value: ContentDispositionHeaderValue) -> None: ...
    @ContentLength.setter
    def ContentLength(self, value: Nullable) -> None: ...
    @ContentRange.setter
    def ContentRange(self, value: ContentRangeHeaderValue) -> None: ...
    @ContentType.setter
    def ContentType(self, value: MediaTypeHeaderValue) -> None: ...
    @Date.setter
    def Date(self, value: Nullable) -> None: ...
    @ETag.setter
    def ETag(self, value: EntityTagHeaderValue) -> None: ...
    @Expires.setter
    def Expires(self, value: Nullable) -> None: ...
    @LastModified.setter
    def LastModified(self, value: Nullable) -> None: ...
    @Location.setter
    def Location(self, value: Uri) -> None: ...
    def Set(self, name: str, value: Object) -> None: ...
    @SetCookie.setter
    def SetCookie(self, value: List[SetCookieHeaderValue]) -> None: ...
    def SetList(self, name: str, values: IList) -> None: ...