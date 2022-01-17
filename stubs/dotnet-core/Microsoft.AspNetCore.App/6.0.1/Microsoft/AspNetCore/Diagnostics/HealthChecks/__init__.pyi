from typing import Tuple, Set, Iterable, List


class HealthCheckOptions:
    def __init__(self): ...
    @property
    def AllowCachingResponses(self) -> bool: ...
    @property
    def Predicate(self) -> Func: ...
    @property
    def ResponseWriter(self) -> Func`3: ...
    @property
    def ResultStatusCodes(self) -> IDictionary: ...
    @AllowCachingResponses.setter
    def AllowCachingResponses(self, value: bool) -> None: ...
    @Predicate.setter
    def Predicate(self, value: Func) -> None: ...
    @ResponseWriter.setter
    def ResponseWriter(self, value: Func`3) -> None: ...
    @ResultStatusCodes.setter
    def ResultStatusCodes(self, value: IDictionary) -> None: ...