__all__ = ['Packaging']
from typing import Tuple, Set, Iterable, List


class FileFormatException(FormatException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, sourceUri: Uri): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...
    @overload
    def __init__(self, sourceUri: Uri, message: str): ...
    @overload
    def __init__(self, sourceUri: Uri, innerException: Exception): ...
    @overload
    def __init__(self, sourceUri: Uri, message: str, innerException: Exception): ...
    @property
    def SourceUri(self) -> Uri: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...
