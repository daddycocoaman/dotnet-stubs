from typing import Tuple, Set, Iterable, List


class AutomationLiveSetting:
    Off = 0
    Polite = 1
    Assertive = 2


class AutomationNotificationKind:
    ItemAdded = 0
    ItemRemoved = 1
    ActionCompleted = 2
    ActionAborted = 3
    Other = 4


class AutomationNotificationProcessing:
    ImportantAll = 0
    ImportantMostRecent = 1
    All = 2
    MostRecent = 3
    CurrentThenMostRecent = 4


class IAutomationLiveRegion:
    @property
    def LiveSetting(self) -> AutomationLiveSetting: ...
    @LiveSetting.setter
    def LiveSetting(self, value: AutomationLiveSetting) -> None: ...
