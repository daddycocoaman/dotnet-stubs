from typing import Tuple, Set, Iterable, List


class JsonConfigurationProvider(FileConfigurationProvider):
    def __init__(self, source: JsonConfigurationSource): ...
    @overload
    def Load(self, stream: Stream) -> None: ...


class JsonConfigurationSource(FileConfigurationSource):
    def __init__(self): ...
    def Build(self, builder: IConfigurationBuilder) -> IConfigurationProvider: ...


class JsonStreamConfigurationProvider(StreamConfigurationProvider):
    def __init__(self, source: JsonStreamConfigurationSource): ...
    @overload
    def Load(self, stream: Stream) -> None: ...


class JsonStreamConfigurationSource(StreamConfigurationSource):
    def __init__(self): ...
    def Build(self, builder: IConfigurationBuilder) -> IConfigurationProvider: ...
