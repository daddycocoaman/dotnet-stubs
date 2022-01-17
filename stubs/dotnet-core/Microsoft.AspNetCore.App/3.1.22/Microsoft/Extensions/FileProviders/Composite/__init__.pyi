from typing import Tuple, Set, Iterable, List


class CompositeDirectoryContents:
    def __init__(self, fileProviders: List[IFileProvider], subpath: str): ...
    @property
    def Exists(self) -> bool: ...
    def GetEnumerator(self) -> IEnumerator: ...
