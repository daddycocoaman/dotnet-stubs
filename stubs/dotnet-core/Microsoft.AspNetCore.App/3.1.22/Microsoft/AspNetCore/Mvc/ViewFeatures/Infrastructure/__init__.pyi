from typing import Tuple, Set, Iterable, List


class TempDataSerializer:
    def CanSerializeType(self, type: Type) -> bool: ...
    def Deserialize(self, unprotectedData: Set(Byte)) -> IDictionary: ...
    def Serialize(self, values: IDictionary) -> Set(Byte): ...
