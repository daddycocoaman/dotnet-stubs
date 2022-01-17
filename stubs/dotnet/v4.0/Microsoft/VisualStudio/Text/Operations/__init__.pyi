__all__ = ['Standalone']
from typing import Tuple, Set, Iterable, List


class IEditorOperationsFactoryService:
    def GetEditorOperations(self, textView: ITextView) -> IEditorOperations: ...
