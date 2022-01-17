from typing import Tuple, Set, Iterable, List


class UapVersionInfo:
    @property
    def DeviceClass(self) -> str: ...
    @property
    def Platform(self) -> str: ...
    @property
    def UapVersion(self) -> Version: ...
