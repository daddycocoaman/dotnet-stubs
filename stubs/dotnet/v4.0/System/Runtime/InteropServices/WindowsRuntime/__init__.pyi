from typing import Tuple, Set, Iterable, List


class WindowsRuntimeBufferExtensions(Object):
    @overload
    def AsBuffer(source: Set(Byte)) -> IBuffer: ...
    @overload
    def AsBuffer(source: Set(Byte), offset: int, length: int) -> IBuffer: ...
    @overload
    def AsBuffer(source: Set(Byte), offset: int, length: int, capacity: int) -> IBuffer: ...
    def AsStream(source: IBuffer) -> Stream: ...
    @overload
    def CopyTo(source: IBuffer, destination: IBuffer) -> None: ...
    @overload
    def CopyTo(source: Set(Byte), destination: IBuffer) -> None: ...
    @overload
    def CopyTo(source: IBuffer, destination: Set(Byte)) -> None: ...
    @overload
    def CopyTo(source: Set(Byte), sourceIndex: int, destination: IBuffer, destinationIndex: UInt32, count: int) -> None: ...
    @overload
    def CopyTo(source: IBuffer, sourceIndex: UInt32, destination: IBuffer, destinationIndex: UInt32, count: UInt32) -> None: ...
    @overload
    def CopyTo(source: IBuffer, sourceIndex: UInt32, destination: Set(Byte), destinationIndex: int, count: int) -> None: ...
    def GetByte(source: IBuffer, byteOffset: UInt32) -> Byte: ...
    @overload
    def GetWindowsRuntimeBuffer(underlyingStream: MemoryStream) -> IBuffer: ...
    @overload
    def GetWindowsRuntimeBuffer(underlyingStream: MemoryStream, positionInStream: int, length: int) -> IBuffer: ...
    def IsSameData(buffer: IBuffer, otherBuffer: IBuffer) -> bool: ...
    @overload
    def ToArray(source: IBuffer) -> Set(Byte): ...
    @overload
    def ToArray(source: IBuffer, sourceIndex: UInt32, count: int) -> Set(Byte): ...
