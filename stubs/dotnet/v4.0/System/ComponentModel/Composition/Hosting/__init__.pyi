from typing import Tuple, Set, Iterable, List


class DirectoryCatalog(ComposablePartCatalog):
    @overload
    def __init__(self, path: str): ...
    @overload
    def __init__(self, path: str, reflectionContext: ReflectionContext): ...
    @overload
    def __init__(self, path: str, definitionOrigin: ICompositionElement): ...
    @overload
    def __init__(self, path: str, searchPattern: str): ...
    @overload
    def __init__(self, path: str, reflectionContext: ReflectionContext, definitionOrigin: ICompositionElement): ...
    @overload
    def __init__(self, path: str, searchPattern: str, definitionOrigin: ICompositionElement): ...
    @overload
    def __init__(self, path: str, searchPattern: str, reflectionContext: ReflectionContext): ...
    @overload
    def __init__(self, path: str, searchPattern: str, reflectionContext: ReflectionContext, definitionOrigin: ICompositionElement): ...
    def add_Changed(self, value: EventHandler) -> None: ...
    def add_Changing(self, value: EventHandler) -> None: ...
    @property
    def FullPath(self) -> str: ...
    @property
    def LoadedFiles(self) -> ReadOnlyCollection: ...
    @property
    def Path(self) -> str: ...
    @property
    def SearchPattern(self) -> str: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def GetExports(self, definition: ImportDefinition) -> Iterable[Tuple]: ...
    def Refresh(self) -> None: ...
    def remove_Changed(self, value: EventHandler) -> None: ...
    def remove_Changing(self, value: EventHandler) -> None: ...
    def ToString(self) -> str: ...