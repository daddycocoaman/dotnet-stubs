from typing import Tuple, Set, Iterable, List


class IClassificationTypeDefinitionMetadata:
    @property
    def BaseDefinition(self) -> Iterable[str]: ...
    @property
    def Name(self) -> str: ...
