from typing import Tuple, Set, Iterable, List


class CimInstanceAdapter:
    def __init__(self): ...
    def GetProperties(self, baseObject: Object) -> Collection: ...
    def GetProperty(self, baseObject: Object, propertyName: str) -> PSAdaptedProperty: ...
    def GetPropertyTypeName(self, adaptedProperty: PSAdaptedProperty) -> str: ...
    def GetPropertyValue(self, adaptedProperty: PSAdaptedProperty) -> Object: ...
    def GetTypeNameHierarchy(self, baseObject: Object) -> Collection: ...
    def IsGettable(self, adaptedProperty: PSAdaptedProperty) -> bool: ...
    def IsSettable(self, adaptedProperty: PSAdaptedProperty) -> bool: ...
    def SetPropertyValue(self, adaptedProperty: PSAdaptedProperty, value: Object) -> None: ...
