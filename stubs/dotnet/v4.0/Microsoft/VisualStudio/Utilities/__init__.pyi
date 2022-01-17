__all__ = ['Implementation','Implementation']
from typing import Tuple, Set, Iterable, List


class IObjectTracker:
    def TrackObject(self, value: Object, bucketName: str) -> None: ...
