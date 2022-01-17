__all__ = ['Binary']
from typing import Tuple, Set, Iterable, List


class FormatterAssemblyStyle:
    Simple = 0
    Full = 1


class FormatterTypeStyle:
    TypesWhenNeeded = 0
    TypesAlways = 1
    XsdString = 2


class IFieldInfo:
    @property
    def FieldNames(self) -> Set(str): ...
    @property
    def FieldTypes(self) -> Set(Type): ...
    @FieldNames.setter
    def FieldNames(self, value: Set(str)) -> None: ...
    @FieldTypes.setter
    def FieldTypes(self, value: Set(Type)) -> None: ...


class TypeFilterLevel:
    Low = 2
    Full = 3
