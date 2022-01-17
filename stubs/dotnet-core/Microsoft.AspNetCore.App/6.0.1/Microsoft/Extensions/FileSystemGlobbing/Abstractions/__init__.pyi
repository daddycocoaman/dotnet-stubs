from typing import Tuple, Set, Iterable, List


class FileSystemInfoBase:
    @property
    def FullName(self) -> str: ...
    @property
    def Name(self) -> str: ...
    @property
    def ParentDirectory(self) -> DirectoryInfoBase: ...
