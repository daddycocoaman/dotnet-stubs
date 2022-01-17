__all__ = ['Collaboration']
from typing import Tuple, Set, Iterable, List


class PnrpScope:
    All = 0
    Global = 1
    SiteLocal = 2
    LinkLocal = 3
