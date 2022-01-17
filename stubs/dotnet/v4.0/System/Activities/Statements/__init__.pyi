__all__ = ['Tracking','Tracking']
from typing import Tuple, Set, Iterable, List


class NoPersistScope(NativeActivity):
    def __init__(self): ...
    @property
    def Body(self) -> Activity: ...
    @Body.setter
    def Body(self, value: Activity) -> None: ...
