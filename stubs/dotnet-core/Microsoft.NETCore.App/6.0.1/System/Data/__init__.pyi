__all__ = ['Common','Common','Common','Common','Common','Common','Common','Common','Common','Common','Common','Common','Common','Common','Common','Common','Common','Common','Common','Common','Common','Common','Common','Common','Common','Common','Common','Common','Common','Common','Common','Common','Common','Common','Common','Common','Common','SqlTypes','SqlTypes','SqlTypes','SqlTypes','SqlTypes','SqlTypes','SqlTypes','SqlTypes','SqlTypes','SqlTypes','SqlTypes','SqlTypes','SqlTypes','SqlTypes','SqlTypes','SqlTypes','SqlTypes','SqlTypes','SqlTypes','SqlTypes','SqlTypes','SqlTypes','SqlTypes','SqlTypes']
from typing import Tuple, Set, Iterable, List


class SyntaxErrorException(InvalidExpressionException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, s: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...
