from typing import Tuple, Set, Iterable, List


class StringWithQualityHeaderValueComparer:
    def Compare(self, stringWithQuality1: StringWithQualityHeaderValue, stringWithQuality2: StringWithQualityHeaderValue) -> int: ...
    @property
    def QualityComparer() -> StringWithQualityHeaderValueComparer: ...
