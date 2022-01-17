from typing import Tuple, Set, Iterable, List


class IActivator:
    def CreateInstance(self, expectedBaseType: Type, implementationTypeName: str) -> Object: ...
