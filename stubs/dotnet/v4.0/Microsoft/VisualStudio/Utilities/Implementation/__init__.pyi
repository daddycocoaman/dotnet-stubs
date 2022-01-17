from typing import Tuple, Set, Iterable, List


class IContentTypeDefinitionMetadata:
    @property
    def BaseDefinition(self) -> Iterable[str]: ...
    @property
    def Name(self) -> str: ...


class IFileExtensionToContentTypeMetadata:
    @property
    def ContentTypes(self) -> Iterable[str]: ...
    @property
    def FileExtension(self) -> str: ...
