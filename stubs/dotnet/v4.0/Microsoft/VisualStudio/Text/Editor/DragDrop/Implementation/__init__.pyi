from typing import Tuple, Set, Iterable, List


class IDropHandlerMetadata:
    @property
    def DropFormats(self) -> Iterable[str]: ...
