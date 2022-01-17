from typing import Tuple, Set, Iterable, List


class XmlAttributeDoesNotExistException(XmlHelperException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...
