__all__ = ['Configuration','Configuration','Configuration','Configuration']
from typing import Tuple, Set, Iterable, List


class XamlBuildProvider(BuildProvider):
    def __init__(self): ...
    def GenerateCode(self, assemblyBuilder: AssemblyBuilder) -> None: ...
    def GetGeneratedType(self, results: CompilerResults) -> Type: ...
    def GetResultFlags(self, results: CompilerResults) -> BuildProviderResultFlags: ...
