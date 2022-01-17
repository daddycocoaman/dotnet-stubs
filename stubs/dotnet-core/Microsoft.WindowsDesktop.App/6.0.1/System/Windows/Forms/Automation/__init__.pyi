from typing import Tuple, Set, Iterable, List


class IAutomationLiveRegion:
    @property
    def LiveSetting(self) -> AutomationLiveSetting: ...
    @LiveSetting.setter
    def LiveSetting(self, value: AutomationLiveSetting) -> None: ...
