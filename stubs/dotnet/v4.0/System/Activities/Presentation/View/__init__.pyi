__all__ = ['OutlineView','OutlineView','OutlineView','OutlineView']
from typing import Tuple, Set, Iterable, List


class WorkflowViewService(ViewService):
    def __init__(self, context: EditingContext): ...
    def add_ViewCreated(self, value: EventHandler) -> None: ...
    def GetModel(self, view: DependencyObject) -> ModelItem: ...
    def GetView(self, model: ModelItem) -> DependencyObject: ...
    def GetViewElement(self, modelItem: ModelItem) -> WorkflowViewElement: ...
    def remove_ViewCreated(self, value: EventHandler) -> None: ...