from typing import Tuple, Set, Iterable, List


class IdentityUser:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, userName: str): ...
