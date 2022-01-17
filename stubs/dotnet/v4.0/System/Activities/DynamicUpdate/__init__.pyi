from typing import Tuple, Set, Iterable, List


class NativeActivityUpdateMapMetadata(UpdateMapMetadata):
    @overload
    def SaveOriginalValue(self, updatedChildActivity: Activity, originalValue: Object) -> None: ...
    @overload
    def SaveOriginalValue(self, propertyName: str, originalValue: Object) -> None: ...
