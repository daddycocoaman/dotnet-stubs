from typing import Tuple, Set, Iterable, List


class HttpLoggingFields:
    #None = 0
    RequestPath = 1
    RequestQuery = 2
    RequestProtocol = 4
    RequestMethod = 8
    RequestScheme = 16
    RequestProperties = 29
    ResponseStatusCode = 32
    RequestHeaders = 64
    RequestPropertiesAndHeaders = 93
    ResponseHeaders = 128
    ResponsePropertiesAndHeaders = 160
    RequestTrailers = 256
    ResponseTrailers = 512
    RequestBody = 1024
    Request = 1117
    ResponseBody = 2048
    Response = 2208
    All = 3325


class HttpLoggingOptions:
    def __init__(self): ...
    @property
    def LoggingFields(self) -> HttpLoggingFields: ...
    @property
    def MediaTypeOptions(self) -> MediaTypeOptions: ...
    @property
    def RequestBodyLogLimit(self) -> int: ...
    @property
    def RequestHeaders(self) -> ISet: ...
    @property
    def ResponseBodyLogLimit(self) -> int: ...
    @property
    def ResponseHeaders(self) -> ISet: ...
    @LoggingFields.setter
    def LoggingFields(self, value: HttpLoggingFields) -> None: ...
    @RequestBodyLogLimit.setter
    def RequestBodyLogLimit(self, value: int) -> None: ...
    @ResponseBodyLogLimit.setter
    def ResponseBodyLogLimit(self, value: int) -> None: ...


class MediaTypeOptions:
    @overload
    def AddBinary(self, mediaType: MediaTypeHeaderValue) -> None: ...
    @overload
    def AddBinary(self, contentType: str) -> None: ...
    @overload
    def AddText(self, contentType: str) -> None: ...
    @overload
    def AddText(self, contentType: str, encoding: Encoding) -> None: ...
    def Clear(self) -> None: ...


class W3CLoggerOptions:
    def __init__(self): ...
    @property
    def FileName(self) -> str: ...
    @property
    def FileSizeLimit(self) -> Nullable: ...
    @property
    def FlushInterval(self) -> TimeSpan: ...
    @property
    def LogDirectory(self) -> str: ...
    @property
    def LoggingFields(self) -> W3CLoggingFields: ...
    @property
    def RetainedFileCountLimit(self) -> Nullable: ...
    @FileName.setter
    def FileName(self, value: str) -> None: ...
    @FileSizeLimit.setter
    def FileSizeLimit(self, value: Nullable) -> None: ...
    @FlushInterval.setter
    def FlushInterval(self, value: TimeSpan) -> None: ...
    @LogDirectory.setter
    def LogDirectory(self, value: str) -> None: ...
    @LoggingFields.setter
    def LoggingFields(self, value: W3CLoggingFields) -> None: ...
    @RetainedFileCountLimit.setter
    def RetainedFileCountLimit(self, value: Nullable) -> None: ...


class W3CLoggingFields:
    #None = 0
    Date = 1
    Time = 2
    ClientIpAddress = 4
    UserName = 8
    ServerName = 16
    ServerIpAddress = 32
    ServerPort = 64
    ConnectionInfoFields = 100
    Method = 128
    UriStem = 256
    UriQuery = 512
    ProtocolStatus = 1024
    TimeTaken = 2048
    ProtocolVersion = 4096
    Host = 8192
    UserAgent = 16384
    Cookie = 32768
    Referer = 65536
    RequestHeaders = 90112
    Request = 95104
    All = 131071
