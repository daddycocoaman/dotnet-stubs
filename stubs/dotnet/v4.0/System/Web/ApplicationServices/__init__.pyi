from typing import Tuple, Set, Iterable, List


class ValidatingPropertiesEventArgs(EventArgs):
    @property
    def FailedProperties(self) -> Collection: ...
    @property
    def Properties(self) -> IDictionary: ...
