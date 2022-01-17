from typing import Tuple, Set, Iterable, List


class KeyPerFileConfigurationSource:
    def __init__(self): ...
    def Build(self, builder: IConfigurationBuilder) -> IConfigurationProvider: ...
    @property
    def FileProvider(self) -> IFileProvider: ...
    @property
    def IgnoreCondition(self) -> Func: ...
    @property
    def IgnorePrefix(self) -> str: ...
    @property
    def Optional(self) -> bool: ...
    @FileProvider.setter
    def FileProvider(self, value: IFileProvider) -> None: ...
    @IgnoreCondition.setter
    def IgnoreCondition(self, value: Func) -> None: ...
    @IgnorePrefix.setter
    def IgnorePrefix(self, value: str) -> None: ...
    @Optional.setter
    def Optional(self, value: bool) -> None: ...
