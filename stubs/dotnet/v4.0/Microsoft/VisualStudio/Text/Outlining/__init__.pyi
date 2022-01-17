from typing import Tuple, Set, Iterable, List


class RegionsChangedEventArgs:
    def __init__(self, affectedSpan: SnapshotSpan): ...
    @property
    def AffectedSpan(self) -> SnapshotSpan: ...
