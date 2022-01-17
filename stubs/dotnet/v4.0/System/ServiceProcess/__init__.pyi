__all__ = ['Design','Design']
from typing import Tuple, Set, Iterable, List


class TimeoutException(SystemException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...
