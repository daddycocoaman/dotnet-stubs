from typing import Tuple, Set, Iterable, List


class IKeyRingProvider:
    def GetCurrentKeyRing(self) -> IKeyRing: ...
