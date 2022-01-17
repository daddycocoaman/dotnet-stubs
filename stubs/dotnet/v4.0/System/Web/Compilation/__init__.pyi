from typing import Tuple, Set, Iterable, List


class IWcfReferenceReceiveContextInformation:
    def ReceiveImportContextInformation(self, serviceReferenceExtensionFileContents: IDictionary, serviceProvider: IServiceProvider) -> None: ...


class WCFBuildProvider(BuildProvider):
    def __init__(self): ...
    def GenerateCode(self, assemblyBuilder: AssemblyBuilder) -> None: ...
