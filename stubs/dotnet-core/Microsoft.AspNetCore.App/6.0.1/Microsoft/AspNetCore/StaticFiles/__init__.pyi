__all__ = ['Infrastructure','Infrastructure']
from typing import Tuple, Set, Iterable, List


class StaticFileResponseContext:
    def __init__(self, context: HttpContext, file: IFileInfo): ...
    @property
    def Context(self) -> HttpContext: ...
    @property
    def File(self) -> IFileInfo: ...
