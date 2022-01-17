from typing import Tuple, Set, Iterable, List


class CustomReflectionContext(ReflectionContext):
    def MapAssembly(self, assembly: Assembly) -> Assembly: ...
    def MapType(self, type: TypeInfo) -> TypeInfo: ...
