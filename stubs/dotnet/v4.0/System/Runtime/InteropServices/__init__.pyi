from typing import Tuple, Set, Iterable, List


class ComAwareEventInfo(EventInfo):
    def __init__(self, type: Type, eventName: str): ...
    def AddEventHandler(self, target: Object, handler: Delegate) -> None: ...
    @property
    def Attributes(self) -> EventAttributes: ...
    @property
    def DeclaringType(self) -> Type: ...
    @property
    def Name(self) -> str: ...
    @property
    def ReflectedType(self) -> Type: ...
    @overload
    def GetAddMethod(self, nonPublic: bool) -> MethodInfo: ...
    @overload
    def GetCustomAttributes(self, inherit: bool) -> Set(Object): ...
    @overload
    def GetCustomAttributes(self, attributeType: Type, inherit: bool) -> Set(Object): ...
    @overload
    def GetRaiseMethod(self, nonPublic: bool) -> MethodInfo: ...
    @overload
    def GetRemoveMethod(self, nonPublic: bool) -> MethodInfo: ...
    def IsDefined(self, attributeType: Type, inherit: bool) -> bool: ...
    def RemoveEventHandler(self, target: Object, handler: Delegate) -> None: ...
