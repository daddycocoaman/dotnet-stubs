from typing import Tuple, Set, Iterable, List


class DataServicesSectionGroup(ConfigurationSectionGroup):
    def __init__(self): ...
    @property
    def Features(self) -> DataServicesFeaturesSection: ...
