from typing import Tuple, Set, Iterable, List


class AutomationLiveSetting:
    Off = 0
    Polite = 1
    Assertive = 2


class SmartTagSurface:
    def __init__(self): ...
    def InitializeComponent(self) -> None: ...
