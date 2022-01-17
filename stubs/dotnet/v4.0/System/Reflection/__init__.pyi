from typing import Tuple, Set, Iterable, List


class ICustomTypeProvider:
    def GetCustomType(self) -> Type: ...
