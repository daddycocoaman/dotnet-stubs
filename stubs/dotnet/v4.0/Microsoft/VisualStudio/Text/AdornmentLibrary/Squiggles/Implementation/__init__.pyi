from typing import Tuple, Set, Iterable, List


class IErrorTypeMetadata:
    @property
    def DisplayName(self) -> str: ...
