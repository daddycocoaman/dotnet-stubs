from typing import Tuple, Set, Iterable, List


class RazorSourceChecksumAttribute:
    def __init__(self, checksumAlgorithm: str, checksum: str, identifier: str): ...
    @property
    def Checksum(self) -> str: ...
    @property
    def ChecksumAlgorithm(self) -> str: ...
    @property
    def Identifier(self) -> str: ...
