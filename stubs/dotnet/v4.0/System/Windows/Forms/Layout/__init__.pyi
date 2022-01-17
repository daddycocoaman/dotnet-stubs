from typing import Tuple, Set, Iterable, List


class LayoutEngine(Object):
    def InitLayout(self, child: Object, specified: BoundsSpecified) -> None: ...
    def Layout(self, container: Object, layoutEventArgs: LayoutEventArgs) -> bool: ...