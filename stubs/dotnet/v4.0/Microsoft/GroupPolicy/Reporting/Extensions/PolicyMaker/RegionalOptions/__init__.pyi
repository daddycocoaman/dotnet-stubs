from typing import Tuple, Set, Iterable, List


class RegionalOptionsGPOSetting:
    def __init__(self): ...
    @property
    def LocaleId(self) -> str: ...
    def GetHashKey(self) -> str: ...


class RegionalOptionsGPOSettings(PolicyMakerElement):
    def __init__(self): ...
    @property
    def RegionalOptions(self) -> Collection: ...
    @RegionalOptions.setter
    def RegionalOptions(self, value: Collection) -> None: ...


class RegionalOptionsRsopSetting(PolicyMakerRsopSetting):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, managementObject: ManagementObject): ...
    @property
    def LocaleId(self) -> str: ...
    def GetHashKey(self) -> str: ...
    def GetItemSubInstanceAttributeName(self) -> str: ...
    def GetKeyComponents(self) -> Set(str): ...


class RegionalOptionsSettings(PolicyMakerSettings):
    def __init__(self): ...
    @property
    def RegionalOptionsGPOSettings(self) -> RegionalOptionsGPOSettings: ...
    @property
    def RegionalOptionsRsopSettings(self) -> Collection: ...
    def GetGPOSettings(self) -> ICollection: ...
    def GetRsopSettings(self) -> ICollection: ...
    def Initialize(self, context: ReportingContext) -> None: ...
    @RegionalOptionsGPOSettings.setter
    def RegionalOptionsGPOSettings(self, value: RegionalOptionsGPOSettings) -> None: ...
    @RegionalOptionsRsopSettings.setter
    def RegionalOptionsRsopSettings(self, value: Collection) -> None: ...
