from typing import Tuple, Set, Iterable, List


class IInvokeOnGetBinder:
    @property
    def InvokeOnGet(self) -> bool: ...
