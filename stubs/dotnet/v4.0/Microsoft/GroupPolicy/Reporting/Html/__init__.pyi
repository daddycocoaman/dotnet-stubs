from typing import Tuple, Set, Iterable, List


class ISectionFormat:
    @property
    def FootFormat(self) -> str: ...
    @property
    def HeadFormat(self) -> str: ...
    @property
    def NeedsTitle(self) -> bool: ...
