from typing import Tuple, Set, Iterable, List


class EnvironmentVariablesConfigurationProvider(ConfigurationProvider):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, prefix: str): ...
    def Load(self) -> None: ...


class EnvironmentVariablesConfigurationSource:
    def __init__(self): ...
    def Build(self, builder: IConfigurationBuilder) -> IConfigurationProvider: ...
    @property
    def Prefix(self) -> str: ...
    @Prefix.setter
    def Prefix(self, value: str) -> None: ...
