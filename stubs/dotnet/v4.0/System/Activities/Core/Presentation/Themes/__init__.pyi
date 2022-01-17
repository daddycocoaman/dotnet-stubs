from typing import Tuple, Set, Iterable, List


class DesignerStylesDictionary(ResourceDictionary):
    @property
    def SequenceStyle() -> Style: ...
    def InitializeComponent(self) -> None: ...
