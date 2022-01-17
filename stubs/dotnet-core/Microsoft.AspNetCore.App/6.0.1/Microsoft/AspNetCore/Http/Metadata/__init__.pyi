from typing import Tuple, Set, Iterable, List


class ITagsMetadata:
    @property
    def Tags(self) -> IReadOnlyList: ...
