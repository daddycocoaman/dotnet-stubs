from typing import Tuple, Set, Iterable, List


class NetworkShareGPOSetting:
    def __init__(self): ...
    def GetHashKey(self) -> str: ...
    def GetKeyComponents(self) -> Set(str): ...


class NetworkShareRsopSetting(PolicyMakerRsopSetting):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, managementObject: ManagementObject): ...
    def GetHashKey(self) -> str: ...
    def GetItemSubInstanceAttributeName(self) -> str: ...
    def GetKeyComponents(self) -> Set(str): ...


class NetworkSharesGPOSettings(PolicyMakerElement):
    def __init__(self): ...
    @property
    def NetworkSharesSettingsList(self) -> Collection: ...
    @NetworkSharesSettingsList.setter
    def NetworkSharesSettingsList(self, value: Collection) -> None: ...


class NetworkSharesSettings(PolicyMakerSettings):
    def __init__(self): ...
    @property
    def NetworkSharesGPOSettings(self) -> NetworkSharesGPOSettings: ...
    @property
    def NetworkSharesRsopSettings(self) -> Collection: ...
    def GetGPOSettings(self) -> ICollection: ...
    def GetRsopSettings(self) -> ICollection: ...
    def Initialize(self, context: ReportingContext) -> None: ...
    @NetworkSharesGPOSettings.setter
    def NetworkSharesGPOSettings(self, value: NetworkSharesGPOSettings) -> None: ...
    @NetworkSharesRsopSettings.setter
    def NetworkSharesRsopSettings(self, value: Collection) -> None: ...
