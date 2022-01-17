from typing import Tuple, Set, Iterable, List


class TailPinnedEventArgs(EventArgs):
    def __init__(self, sequenceNumber: SequenceNumber): ...
    @property
    def TargetSequenceNumber(self) -> SequenceNumber: ...
