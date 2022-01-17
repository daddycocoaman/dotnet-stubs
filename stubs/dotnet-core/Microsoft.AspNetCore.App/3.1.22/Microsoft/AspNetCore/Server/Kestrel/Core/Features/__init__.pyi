from typing import Tuple, Set, Iterable, List


class ITlsApplicationProtocolFeature:
    @property
    def ApplicationProtocol(self) -> ReadOnlyMemory: ...
