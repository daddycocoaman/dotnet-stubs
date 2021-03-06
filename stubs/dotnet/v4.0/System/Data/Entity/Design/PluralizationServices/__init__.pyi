from typing import Tuple, Set, Iterable, List


class ICustomPluralizationMapping:
    def AddWord(self, singular: str, plural: str) -> None: ...


class PluralizationService(Object):
    def CreateService(culture: CultureInfo) -> PluralizationService: ...
    @property
    def Culture(self) -> CultureInfo: ...
    def IsPlural(self, word: str) -> bool: ...
    def IsSingular(self, word: str) -> bool: ...
    def Pluralize(self, word: str) -> str: ...
    def Singularize(self, word: str) -> str: ...
