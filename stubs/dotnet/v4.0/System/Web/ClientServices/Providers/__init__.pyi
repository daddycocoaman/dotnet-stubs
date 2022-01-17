from typing import Tuple, Set, Iterable, List


class UserValidatedEventArgs(EventArgs):
    def __init__(self, username: str): ...
    @property
    def UserName(self) -> str: ...
