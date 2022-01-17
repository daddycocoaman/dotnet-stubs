from typing import Tuple, Set, Iterable, List


class ViewViewComponentResult:
    def __init__(self): ...
    def Execute(self, context: ViewComponentContext) -> None: ...
    def ExecuteAsync(self, context: ViewComponentContext) -> Task: ...
    @property
    def TempData(self) -> ITempDataDictionary: ...
    @property
    def ViewData(self) -> ViewDataDictionary: ...
    @property
    def ViewEngine(self) -> IViewEngine: ...
    @property
    def ViewName(self) -> str: ...
    @TempData.setter
    def TempData(self, value: ITempDataDictionary) -> None: ...
    @ViewData.setter
    def ViewData(self, value: ViewDataDictionary) -> None: ...
    @ViewEngine.setter
    def ViewEngine(self, value: IViewEngine) -> None: ...
    @ViewName.setter
    def ViewName(self, value: str) -> None: ...