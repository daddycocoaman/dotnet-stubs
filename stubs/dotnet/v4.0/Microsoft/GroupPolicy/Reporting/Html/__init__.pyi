from typing import Tuple, Set, Iterable, List


class ISectionFormat:
    @property
    def FootFormat(self) -> str: ...
    @property
    def HeadFormat(self) -> str: ...
    @property
    def NeedsTitle(self) -> bool: ...


class PolicySettingState:
    Enabled = 0
    Disabled = 1
    NotConfigured = 2
