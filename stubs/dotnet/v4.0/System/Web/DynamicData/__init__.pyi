from typing import Tuple, Set, Iterable, List


class IDynamicValidatorException:
    @property
    def InnerExceptions(self) -> IDictionary: ...
