from typing import Tuple, Set, Iterable, List


class ModelPropertyEntryToOwnerActivityConverter(Object):
    def __init__(self): ...
    def Convert(self, value: Object, targetType: Type, parameter: Object, culture: CultureInfo) -> Object: ...
    def ConvertBack(self, value: Object, targetType: Type, parameter: Object, culture: CultureInfo) -> Object: ...