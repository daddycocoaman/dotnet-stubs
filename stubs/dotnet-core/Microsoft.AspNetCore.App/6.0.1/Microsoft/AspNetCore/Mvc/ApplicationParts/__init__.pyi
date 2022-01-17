from typing import Tuple, Set, Iterable, List


class IRazorCompiledItemProvider:
    @property
    def CompiledItems(self) -> Iterable[RazorCompiledItem]: ...
