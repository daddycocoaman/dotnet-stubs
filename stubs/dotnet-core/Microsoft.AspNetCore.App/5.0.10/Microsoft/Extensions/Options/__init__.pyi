from typing import Tuple, Set, Iterable, List


class ValidateOptionsResult:
    def __init__(self): ...
    @overload
    def Fail(failureMessage: str) -> ValidateOptionsResult: ...
    @overload
    def Fail(failures: Iterable[str]) -> ValidateOptionsResult: ...
    @property
    def Failed(self) -> bool: ...
    @property
    def FailureMessage(self) -> str: ...
    @property
    def Failures(self) -> Iterable[str]: ...
    @property
    def Skipped(self) -> bool: ...
    @property
    def Succeeded(self) -> bool: ...
