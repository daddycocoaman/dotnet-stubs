__all__ = ['CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','CommandTrees','EntitySql','EntitySql','EntitySql']
from typing import Tuple, Set, Iterable, List


class FieldMetadata(ValueType):
    def __init__(self, ordinal: int, fieldType: EdmMember): ...
    @property
    def FieldType(self) -> EdmMember: ...
    @property
    def Ordinal(self) -> int: ...
