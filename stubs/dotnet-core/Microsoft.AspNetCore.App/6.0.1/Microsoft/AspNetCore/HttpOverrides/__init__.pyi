from typing import Tuple, Set, Iterable, List


class IPNetwork:
    def __init__(self, prefix: IPAddress, prefixLength: int): ...
    def Contains(self, address: IPAddress) -> bool: ...
    @property
    def Prefix(self) -> IPAddress: ...
    @property
    def PrefixLength(self) -> int: ...
