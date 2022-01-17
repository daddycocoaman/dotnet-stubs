from typing import Tuple, Set, Iterable, List


class DotNetInvocationResult:
    @overload
    def __init__(self, result: Object): ...
    @overload
    def __init__(self, exception: Exception, errorKind: str): ...
    @property
    def ErrorKind(self) -> str: ...
    @property
    def Exception(self) -> Exception: ...
    @property
    def Result(self) -> Object: ...
    @property
    def Success(self) -> bool: ...
