__all__ = ['Infrastructure','Infrastructure']
from typing import Tuple, Set, Iterable, List


class StaticFileResponseContext:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, context: HttpContext, file: IFileInfo): ...
    @property
    def Context(self) -> HttpContext: ...
    @property
    def File(self) -> IFileInfo: ...
