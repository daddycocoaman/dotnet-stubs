__all__ = ['Protocol']
from typing import Tuple, Set, Iterable, List


class JsonHubProtocolOptions:
    def __init__(self): ...
    @property
    def PayloadSerializerOptions(self) -> JsonSerializerOptions: ...
    @PayloadSerializerOptions.setter
    def PayloadSerializerOptions(self, value: JsonSerializerOptions) -> None: ...
