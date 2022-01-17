from typing import Tuple, Set, Iterable, List


class IPreviewCommand:
    def CancelPreview(self) -> None: ...
    def Preview(self, parameter: Object) -> None: ...


class IPreviewCommandSource:
    @property
    def PreviewCommandParameter(self) -> Object: ...
