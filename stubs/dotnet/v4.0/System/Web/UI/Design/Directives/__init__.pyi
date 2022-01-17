from typing import Tuple, Set, Iterable, List


class SchemaElementNameAttribute(Attribute):
    def __init__(self, value: str): ...
    @property
    def Value(self) -> str: ...
