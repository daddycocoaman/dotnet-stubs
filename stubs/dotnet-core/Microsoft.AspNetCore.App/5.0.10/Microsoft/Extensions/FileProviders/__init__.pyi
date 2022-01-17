__all__ = ['Internal','Physical']
from typing import Tuple, Set, Iterable, List


class PhysicalFileProvider:
    @overload
    def __init__(self, root: str): ...
    @overload
    def __init__(self, root: str, filters: ExclusionFilters): ...
    def Dispose(self) -> None: ...
    @property
    def Root(self) -> str: ...
    @property
    def UseActivePolling(self) -> bool: ...
    @property
    def UsePollingFileWatcher(self) -> bool: ...
    def GetDirectoryContents(self, subpath: str) -> IDirectoryContents: ...
    def GetFileInfo(self, subpath: str) -> IFileInfo: ...
    @UseActivePolling.setter
    def UseActivePolling(self, value: bool) -> None: ...
    @UsePollingFileWatcher.setter
    def UsePollingFileWatcher(self, value: bool) -> None: ...
    def Watch(self, filter: str) -> IChangeToken: ...
