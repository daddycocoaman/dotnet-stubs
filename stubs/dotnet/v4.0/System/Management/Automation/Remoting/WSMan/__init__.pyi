from typing import Tuple, Set, Iterable, List


class ActiveSessionsChangedEventArgs(EventArgs):
    def __init__(self, activeSessionsCount: int): ...
    @property
    def ActiveSessionsCount(self) -> int: ...
