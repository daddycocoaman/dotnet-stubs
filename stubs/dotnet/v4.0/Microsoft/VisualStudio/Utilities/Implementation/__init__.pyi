from typing import Tuple, Set, Iterable, List


class IFileExtensionToContentTypeMetadata:
    @property
    def ContentTypes(self) -> Iterable[str]: ...
    @property
    def FileExtension(self) -> str: ...
