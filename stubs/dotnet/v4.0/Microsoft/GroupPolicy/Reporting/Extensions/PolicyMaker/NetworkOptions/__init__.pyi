from typing import Tuple, Set, Iterable, List


class DialupOptionGPOSetting(NetworkOptionsGPOSettingBase):
    def __init__(self): ...


class NetworkOptionGPOSetting(NetworkOptionsGPOSettingBase):
    def __init__(self): ...


class NetworkOptionsGPOSettingBase:
    def GetHashKey(self) -> str: ...
    def GetKeyComponents(self) -> Set(str): ...


class NetworkOptionsGPOSettings(PolicyMakerElement):
    def __init__(self): ...
    @property
    def NetworkOptionsSettingsList(self) -> Collection: ...
    @NetworkOptionsSettingsList.setter
    def NetworkOptionsSettingsList(self, value: Collection) -> None: ...


class NetworkOptionsRsopSetting(PolicyMakerRsopSetting):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, managementObject: ManagementObject): ...
    def GetHashKey(self) -> str: ...
    def GetItemSubInstanceAttributeName(self) -> str: ...
    def GetKeyComponents(self) -> Set(str): ...


class NetworkOptionsSettings(PolicyMakerSettings):
    def __init__(self): ...
    @property
    def NetworkOptionsGPOSettings(self) -> NetworkOptionsGPOSettings: ...
    @property
    def NetworkOptionsRsopSettings(self) -> Collection: ...
    def GetGPOSettings(self) -> ICollection: ...
    def GetRsopSettings(self) -> ICollection: ...
    def Initialize(self, context: ReportingContext) -> None: ...
    @NetworkOptionsGPOSettings.setter
    def NetworkOptionsGPOSettings(self, value: NetworkOptionsGPOSettings) -> None: ...
    @NetworkOptionsRsopSettings.setter
    def NetworkOptionsRsopSettings(self, value: Collection) -> None: ...
