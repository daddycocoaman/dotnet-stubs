__all__ = ['ExtendedProtection','ExtendedProtection','ExtendedProtection','ExtendedProtection','ExtendedProtection','ExtendedProtection','ExtendedProtection','ExtendedProtection','ExtendedProtection']
from typing import Tuple, Set, Iterable, List


class InvalidCredentialException(AuthenticationException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...
