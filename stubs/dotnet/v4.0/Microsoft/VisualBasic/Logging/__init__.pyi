from typing import Tuple, Set, Iterable, List


class FileLogTraceListener:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, name: str): ...
    def Close(self) -> None: ...
    def Flush(self) -> None: ...
    @property
    def Append(self) -> bool: ...
    @property
    def AutoFlush(self) -> bool: ...
    @property
    def BaseFileName(self) -> str: ...
    @property
    def CustomLocation(self) -> str: ...
    @property
    def Delimiter(self) -> str: ...
    @property
    def DiskSpaceExhaustedBehavior(self) -> DiskSpaceExhaustedOption: ...
    @property
    def Encoding(self) -> Encoding: ...
    @property
    def FullLogFileName(self) -> str: ...
    @property
    def IncludeHostName(self) -> bool: ...
    @property
    def Location(self) -> LogFileLocation: ...
    @property
    def LogFileCreationSchedule(self) -> LogFileCreationScheduleOption: ...
    @property
    def MaxFileSize(self) -> Int64: ...
    @property
    def ReserveDiskSpace(self) -> Int64: ...
    @Append.setter
    def Append(self, value: bool) -> None: ...
    @AutoFlush.setter
    def AutoFlush(self, value: bool) -> None: ...
    @BaseFileName.setter
    def BaseFileName(self, value: str) -> None: ...
    @CustomLocation.setter
    def CustomLocation(self, value: str) -> None: ...
    @Delimiter.setter
    def Delimiter(self, value: str) -> None: ...
    @DiskSpaceExhaustedBehavior.setter
    def DiskSpaceExhaustedBehavior(self, value: DiskSpaceExhaustedOption) -> None: ...
    @Encoding.setter
    def Encoding(self, value: Encoding) -> None: ...
    @IncludeHostName.setter
    def IncludeHostName(self, value: bool) -> None: ...
    @Location.setter
    def Location(self, value: LogFileLocation) -> None: ...
    @LogFileCreationSchedule.setter
    def LogFileCreationSchedule(self, value: LogFileCreationScheduleOption) -> None: ...
    @MaxFileSize.setter
    def MaxFileSize(self, value: Int64) -> None: ...
    @ReserveDiskSpace.setter
    def ReserveDiskSpace(self, value: Int64) -> None: ...
    @overload
    def TraceData(self, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, data: Set(Object)) -> None: ...
    @overload
    def TraceData(self, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, data: Object) -> None: ...
    @overload
    def TraceEvent(self, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, message: str) -> None: ...
    @overload
    def TraceEvent(self, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, format: str, args: Set(Object)) -> None: ...
    @overload
    def Write(self, message: str) -> None: ...
    @overload
    def WriteLine(self, message: str) -> None: ...
