from typing import Tuple, Set, Iterable, List


class TpmWmiObject:
    def ClearTpmObject() -> None: ...
    @property
    def MachineName() -> str: ...
    @property
    def tpm() -> TrustedPlatformModuleWmi: ...
    @MachineName.setter
    def MachineName(value: str) -> None: ...
