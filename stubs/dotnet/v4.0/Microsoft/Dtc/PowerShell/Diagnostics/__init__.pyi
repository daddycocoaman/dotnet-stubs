__all__ = ['Commands']
from typing import Tuple, Set, Iterable, List


class DtcCmdletBase:
    pass


class DtcDiagnosticException:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class DtcDiagnosticResourceManagerJob:
    @property
    def HasMoreData(self) -> bool: ...
    @property
    def Location(self) -> str: ...
    @property
    def StatusMessage(self) -> str: ...
    def StopJob(self) -> None: ...


class DtcDiagnosticTransaction:
    @property
    def Id(self) -> Guid: ...
