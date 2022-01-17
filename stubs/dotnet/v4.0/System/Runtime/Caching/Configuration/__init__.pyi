from typing import Tuple, Set, Iterable, List


class CachingSectionGroup(ConfigurationSectionGroup):
    def __init__(self): ...
    @property
    def MemoryCaches(self) -> MemoryCacheSection: ...


class MemoryCacheElement(ConfigurationElement):
    def __init__(self, name: str): ...
    @property
    def CacheMemoryLimitMegabytes(self) -> int: ...
    @property
    def Name(self) -> str: ...
    @property
    def PhysicalMemoryLimitPercentage(self) -> int: ...
    @property
    def PollingInterval(self) -> TimeSpan: ...
    @CacheMemoryLimitMegabytes.setter
    def CacheMemoryLimitMegabytes(self, value: int) -> None: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    @PhysicalMemoryLimitPercentage.setter
    def PhysicalMemoryLimitPercentage(self, value: int) -> None: ...
    @PollingInterval.setter
    def PollingInterval(self, value: TimeSpan) -> None: ...


class MemoryCacheSection(ConfigurationSection):
    def __init__(self): ...
    @property
    def NamedCaches(self) -> MemoryCacheSettingsCollection: ...


class MemoryCacheSettingsCollection(ConfigurationElementCollection):
    def __init__(self): ...
    def Add(self, cache: MemoryCacheElement) -> None: ...
    def Clear(self) -> None: ...
    @property
    def CollectionType(self) -> ConfigurationElementCollectionType: ...
    @property
    def Item(self, index: int) -> MemoryCacheElement: ...
    @property
    def Item(self, key: str) -> MemoryCacheElement: ...
    def IndexOf(self, cache: MemoryCacheElement) -> int: ...
    def Remove(self, cache: MemoryCacheElement) -> None: ...
    def RemoveAt(self, index: int) -> None: ...
    @Item.setter
    def Item(self, index: int, value: MemoryCacheElement) -> None: ...
