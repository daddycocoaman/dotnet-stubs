from typing import Tuple, Set, Iterable, List


class RemoteArgumentDictionaryEntry(ValueType):
    def __init__(self, key: RemoteArgument, value: RemoteArgument): ...
