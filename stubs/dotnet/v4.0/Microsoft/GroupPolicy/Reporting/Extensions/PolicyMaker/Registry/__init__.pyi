from typing import Tuple, Set, Iterable, List


class RegistryGPOSettings(PolicyMakerElement):
    def __init__(self): ...
    @property
    def CollectionSettingsList(self) -> Collection: ...
    @property
    def RegistrySettingsList(self) -> Collection: ...
    @CollectionSettingsList.setter
    def CollectionSettingsList(self, value: Collection) -> None: ...
    @RegistrySettingsList.setter
    def RegistrySettingsList(self, value: Collection) -> None: ...
