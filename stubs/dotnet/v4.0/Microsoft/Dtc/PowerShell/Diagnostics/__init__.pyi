__all__ = ['Commands','Commands','Commands','Commands','Commands','Commands','Commands','Commands']
from typing import Tuple, Set, Iterable, List


class DtcDiagnosticResourceManagerJob:
    @property
    def HasMoreData(self) -> bool: ...
    @property
    def Location(self) -> str: ...
    @property
    def StatusMessage(self) -> str: ...
    def StopJob(self) -> None: ...
