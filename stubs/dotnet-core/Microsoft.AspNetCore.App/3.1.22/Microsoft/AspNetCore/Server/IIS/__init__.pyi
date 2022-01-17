__all__ = ['Core']
from typing import Tuple, Set, Iterable, List


class BadHttpRequestException:
    @property
    def StatusCode(self) -> int: ...


class HttpContextExtensions:
    pass


class IISServerDefaults:
    def __init__(self): ...
