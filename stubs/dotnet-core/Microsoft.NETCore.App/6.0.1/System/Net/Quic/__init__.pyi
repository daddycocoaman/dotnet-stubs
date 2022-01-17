__all__ = ['Implementations']
from typing import Tuple, Set, Iterable, List


class QuicStreamAbortedException(QuicException):
    def __init__(self, message: str, errorCode: Int64): ...
    @property
    def ErrorCode(self) -> Int64: ...
