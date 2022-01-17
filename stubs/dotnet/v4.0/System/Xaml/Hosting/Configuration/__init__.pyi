from typing import Tuple, Set, Iterable, List


class HandlerElement(ConfigurationElement):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, xamlType: str, handlerType: str): ...
    @property
    def HttpHandlerType(self) -> str: ...
    @property
    def XamlRootElementType(self) -> str: ...
    @HttpHandlerType.setter
    def HttpHandlerType(self, value: str) -> None: ...
    @XamlRootElementType.setter
    def XamlRootElementType(self, value: str) -> None: ...


class HandlerElementCollection(ConfigurationElementCollection):
    def __init__(self): ...
    def Add(self, handlerElement: HandlerElement) -> None: ...
    def Clear(self) -> None: ...
    @property
    def CollectionType(self) -> ConfigurationElementCollectionType: ...
    @property
    def Item(self, index: int) -> HandlerElement: ...
    @overload
    def Remove(self, handlerElement: HandlerElement) -> None: ...
    @overload
    def Remove(self, xamlRootElementType: str) -> None: ...
    def RemoveAt(self, index: int) -> None: ...
    @Item.setter
    def Item(self, index: int, value: HandlerElement) -> None: ...


class XamlHostingSection(ConfigurationSection):
    def __init__(self): ...
    @property
    def Handlers(self) -> HandlerElementCollection: ...


class XamlHostingSectionGroup(ConfigurationSectionGroup):
    def __init__(self): ...
    @property
    def XamlHostingSection(self) -> XamlHostingSection: ...
