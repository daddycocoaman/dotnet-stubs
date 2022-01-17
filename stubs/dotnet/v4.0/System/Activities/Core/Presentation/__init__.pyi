__all__ = ['Factories','Themes']
from typing import Tuple, Set, Iterable, List


class ConnectionPointType:
    Default = 0
    Incoming = 1
    Outgoing = 2


class DesignerMetadata(Object):
    def __init__(self): ...
    def Register(self) -> None: ...


class FinalState(Object):
    def __init__(self): ...


class FlowchartDesignerCommands(Object):
    pass


class GenericTypeArgumentConverter(Object):
    def __init__(self): ...
    def Convert(self, value: Object, targetType: Type, parameter: Object, culture: CultureInfo) -> Object: ...
    def ConvertBack(self, value: Object, targetType: Type, parameter: Object, culture: CultureInfo) -> Object: ...


class LocationChangedEventArgs(EventArgs):
    def __init__(self, newLocation: Point): ...
    @property
    def NewLocation(self) -> Point: ...
