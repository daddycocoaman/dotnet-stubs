from typing import Tuple, Set, Iterable, List


class ParsingEventLogException(PolicyManagementException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, parseEvent: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...
