from typing import Tuple, Set, Iterable, List


class WSTrustSerializationException(Exception):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, inner: Exception): ...
