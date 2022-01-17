__all__ = ['Logging','Logging']
from typing import Tuple, Set, Iterable, List


class IHttpMessageHandlerBuilderFilter:
    def Configure(self, next: Action) -> Action: ...
