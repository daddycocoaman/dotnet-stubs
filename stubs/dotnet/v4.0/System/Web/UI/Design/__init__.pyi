__all__ = ['WebControls','WebControls','WebControls','WebControls','WebControls']
from typing import Tuple, Set, Iterable, List


class UpdateProgressDesigner(ControlDesigner):
    def __init__(self): ...
    @overload
    def GetDesignTimeHtml(self, regions: DesignerRegionCollection) -> str: ...
    def GetEditableDesignerRegionContent(self, region: EditableDesignerRegion) -> str: ...
    def SetEditableDesignerRegionContent(self, region: EditableDesignerRegion, content: str) -> None: ...