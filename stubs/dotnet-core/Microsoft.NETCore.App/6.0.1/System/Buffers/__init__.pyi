__all__ = ['Text']
from typing import Tuple, Set, Iterable, List




class BuffersExtensions(Object):
    def CopyTo(source: ReadOnlySequence, destination: Span) -> Tuple[ReadOnlySequence]: ...
    def PositionOf(source: ReadOnlySequence, value: T) -> Tuple[Nullable, ReadOnlySequence]: ...
    def ToArray(sequence: ReadOnlySequence) -> Tuple[Set(T), ReadOnlySequence]: ...
    def Write(writer: IBufferWriter, value: ReadOnlySpan) -> None: ...












class SequenceReaderExtensions(Object):
    @overload
    def TryReadBigEndian(reader: SequenceReader) -> Tuple[bool, SequenceReader, Int16]: ...
    @overload
    def TryReadBigEndian(reader: SequenceReader) -> Tuple[bool, SequenceReader, int]: ...
    @overload
    def TryReadBigEndian(reader: SequenceReader) -> Tuple[bool, SequenceReader, Int64]: ...
    @overload
    def TryReadLittleEndian(reader: SequenceReader) -> Tuple[bool, SequenceReader, Int16]: ...
    @overload
    def TryReadLittleEndian(reader: SequenceReader) -> Tuple[bool, SequenceReader, int]: ...
    @overload
    def TryReadLittleEndian(reader: SequenceReader) -> Tuple[bool, SequenceReader, Int64]: ...
