from typing import Tuple, Set, Iterable, List


class WorkflowInstanceManagementElement(BehaviorExtensionElement):
    def __init__(self): ...
    @property
    def AuthorizedWindowsGroup(self) -> str: ...
    @property
    def BehaviorType(self) -> Type: ...
    @AuthorizedWindowsGroup.setter
    def AuthorizedWindowsGroup(self, value: str) -> None: ...