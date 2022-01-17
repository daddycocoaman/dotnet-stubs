__all__ = ['Automation','Automation','Markup','Media']
from typing import Tuple, Set, Iterable, List


class LayoutCycleException:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...
