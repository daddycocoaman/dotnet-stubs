from typing import Tuple, Set, Iterable, List


class CascadingAuthenticationState(ComponentBase):
    def __init__(self): ...
    @property
    def ChildContent(self) -> RenderFragment: ...
    @ChildContent.setter
    def ChildContent(self, value: RenderFragment) -> None: ...
