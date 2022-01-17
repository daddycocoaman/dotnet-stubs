from typing import Tuple, Set, Iterable, List


class MemoryConfigurationSource:
    def __init__(self): ...
    def Build(self, builder: IConfigurationBuilder) -> IConfigurationProvider: ...
    @property
    def InitialData(self) -> Iterable[KeyValuePair]: ...
    @InitialData.setter
    def InitialData(self, value: Iterable[KeyValuePair]) -> None: ...
