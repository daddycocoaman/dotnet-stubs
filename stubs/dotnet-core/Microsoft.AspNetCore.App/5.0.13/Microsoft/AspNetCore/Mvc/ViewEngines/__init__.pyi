from typing import Tuple, Set, Iterable, List


class ViewEngineResult:
    def EnsureSuccessful(self, originalLocations: Iterable[str]) -> ViewEngineResult: ...
    def Found(viewName: str, view: IView) -> ViewEngineResult: ...
    @property
    def SearchedLocations(self) -> Iterable[str]: ...
    @property
    def Success(self) -> bool: ...
    @property
    def View(self) -> IView: ...
    @property
    def ViewName(self) -> str: ...
    def NotFound(viewName: str, searchedLocations: Iterable[str]) -> ViewEngineResult: ...
