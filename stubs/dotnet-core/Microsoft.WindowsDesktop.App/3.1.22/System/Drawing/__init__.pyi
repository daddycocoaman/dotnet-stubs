__all__ = ['Printing']
from typing import Tuple, Set, Iterable, List


class FontUnitConverter(EnumConverter):
    def __init__(self): ...
    @overload
    def GetStandardValues(self, context: ITypeDescriptorContext) -> StandardValuesCollection: ...
