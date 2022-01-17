from typing import Tuple, Set, Iterable, List


class Enumerator:
    @property
    def Current(self) -> EncodedNameValuePair: ...
    def MoveNext(self) -> bool: ...
