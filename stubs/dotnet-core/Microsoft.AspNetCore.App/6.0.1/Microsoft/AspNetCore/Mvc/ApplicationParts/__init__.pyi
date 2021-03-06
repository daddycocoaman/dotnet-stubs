from typing import Tuple, Set, Iterable, List


class CompiledRazorAssemblyApplicationPartFactory(ApplicationPartFactory):
    def __init__(self): ...
    def GetApplicationParts(self, assembly: Assembly) -> Iterable[ApplicationPart]: ...
    def GetDefaultApplicationParts(assembly: Assembly) -> Iterable[ApplicationPart]: ...


class CompiledRazorAssemblyPart(ApplicationPart):
    def __init__(self, assembly: Assembly): ...
    @property
    def Assembly(self) -> Assembly: ...
    @property
    def Name(self) -> str: ...


class ConsolidatedAssemblyApplicationPartFactory(ApplicationPartFactory):
    def __init__(self): ...
    def GetApplicationParts(self, assembly: Assembly) -> Iterable[ApplicationPart]: ...


class IRazorCompiledItemProvider:
    @property
    def CompiledItems(self) -> Iterable[RazorCompiledItem]: ...
