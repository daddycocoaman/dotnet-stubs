from typing import Tuple, Set, Iterable, List


class ITaggerMetadata:
    @property
    def ContentTypes(self) -> Iterable[str]: ...
    @property
    def TagTypes(self) -> Iterable[Type]: ...
