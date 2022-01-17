from typing import Tuple, Set, Iterable, List


class TagHelperMemoryCacheProvider:
    def __init__(self): ...
    @property
    def Cache(self) -> IMemoryCache: ...
