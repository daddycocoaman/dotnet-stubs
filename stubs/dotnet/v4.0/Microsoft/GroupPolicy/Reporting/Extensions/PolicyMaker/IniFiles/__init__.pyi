from typing import Tuple, Set, Iterable, List


class IniFileGPOSetting:
    def __init__(self): ...
    def GetHashKey(self) -> str: ...
    def GetKeyComponents(self) -> Set(str): ...


class IniFileRsopSetting(PolicyMakerRsopSetting):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, managementObject: ManagementObject): ...
    def GetHashKey(self) -> str: ...
    def GetItemSubInstanceAttributeName(self) -> str: ...
    def GetKeyComponents(self) -> Set(str): ...


class IniFilesGPOSettings(PolicyMakerElement):
    def __init__(self): ...
    @property
    def IniFilesSettingsList(self) -> Collection: ...
    @IniFilesSettingsList.setter
    def IniFilesSettingsList(self, value: Collection) -> None: ...


class IniFilesSettings(PolicyMakerSettings):
    def __init__(self): ...
    @property
    def IniFilesGPOSettings(self) -> IniFilesGPOSettings: ...
    @property
    def IniFilesRsopSettings(self) -> Collection: ...
    def GetGPOSettings(self) -> ICollection: ...
    def GetRsopSettings(self) -> ICollection: ...
    def Initialize(self, context: ReportingContext) -> None: ...
    @IniFilesGPOSettings.setter
    def IniFilesGPOSettings(self, value: IniFilesGPOSettings) -> None: ...
    @IniFilesRsopSettings.setter
    def IniFilesRsopSettings(self, value: Collection) -> None: ...
