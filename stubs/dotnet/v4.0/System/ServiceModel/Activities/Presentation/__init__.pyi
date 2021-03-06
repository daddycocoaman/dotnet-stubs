__all__ = ['Factories']
from typing import Tuple, Set, Iterable, List


class ServiceContractImporter(Object):
    def GenerateActivityTemplates(contractType: Type) -> Iterable[ActivityTemplateFactoryBuilder]: ...
    def SaveActivityTemplate(activityTemplate: ActivityTemplateFactoryBuilder) -> str: ...
    def SelectContractType(localAssemblyName: AssemblyName, referencedAssemblies: List[AssemblyName], editingContext: EditingContext) -> Type: ...
