from typing import Tuple, Set, Iterable, List


class HostFilteringOptions:
    def __init__(self): ...
    @property
    def AllowedHosts(self) -> List[str]: ...
    @property
    def AllowEmptyHosts(self) -> bool: ...
    @property
    def IncludeFailureMessage(self) -> bool: ...
    @AllowedHosts.setter
    def AllowedHosts(self, value: List[str]) -> None: ...
    @AllowEmptyHosts.setter
    def AllowEmptyHosts(self, value: bool) -> None: ...
    @IncludeFailureMessage.setter
    def IncludeFailureMessage(self, value: bool) -> None: ...
