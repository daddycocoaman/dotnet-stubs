__all__ = ['Implementation']
from typing import Tuple, Set, Iterable, List


class DropHandlerBase:
    def HandleDataDropped(self, dragDropInfo: DragDropInfo) -> DragDropPointerEffects: ...
    def HandleDragCanceled(self) -> None: ...
    def HandleDraggingOver(self, dragDropInfo: DragDropInfo) -> DragDropPointerEffects: ...
    def HandleDragStarted(self, dragDropInfo: DragDropInfo) -> DragDropPointerEffects: ...
    def IsDropEnabled(self, dragDropInfo: DragDropInfo) -> bool: ...