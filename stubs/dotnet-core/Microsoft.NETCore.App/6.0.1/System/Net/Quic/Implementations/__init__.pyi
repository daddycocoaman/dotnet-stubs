from typing import Tuple, Set, Iterable, List


class QuicImplementationProvider(Object):
    @property
    def IsSupported(self) -> bool: ...
