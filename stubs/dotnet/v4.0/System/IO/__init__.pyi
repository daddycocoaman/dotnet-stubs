from typing import Tuple, Set, Iterable, List


class PipeException(IOException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, errorCode: int): ...
    @overload
    def __init__(self, message: str, inner: Exception): ...
    @property
    def ErrorCode(self) -> int: ...