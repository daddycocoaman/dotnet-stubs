from typing import Tuple, Set, Iterable, List


class IStrongBox:
    @property
    def Value(self) -> Object: ...
    @Value.setter
    def Value(self, value: Object) -> None: ...
