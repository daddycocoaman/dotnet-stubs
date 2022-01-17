from typing import Tuple, Set, Iterable, List


class ConsoleInputStream:
    def Flush(self) -> None: ...
    @property
    def CanRead(self) -> bool: ...
    @property
    def CanSeek(self) -> bool: ...
    @property
    def CanWrite(self) -> bool: ...
    @property
    def Length(self) -> Int64: ...
    @property
    def Position(self) -> Int64: ...
    def Read(self, buffer: Set(Byte), offset: int, count: int) -> int: ...
    def Seek(self, offset: Int64, origin: SeekOrigin) -> Int64: ...
    @Position.setter
    def Position(self, value: Int64) -> None: ...
    def SetLength(self, value: Int64) -> None: ...
    def Write(self, buffer: Set(Byte), offset: int, count: int) -> None: ...


class ConsoleStreamType:
    Input = 0
    Output = 1
    ErrorOutput = 2


class EnumBounds:
    def IsValid(value: SourceCodeKind) -> bool: ...
