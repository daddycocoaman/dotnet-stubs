from typing import Tuple, Set, Iterable, List


class ImportDefinition(Object):
    @overload
    def __init__(self, constraint: Expression, contractName: str, cardinality: ImportCardinality, isRecomposable: bool, isPrerequisite: bool): ...
    @overload
    def __init__(self, constraint: Expression, contractName: str, cardinality: ImportCardinality, isRecomposable: bool, isPrerequisite: bool, metadata: IDictionary): ...
    @property
    def Cardinality(self) -> ImportCardinality: ...
    @property
    def Constraint(self) -> Expression: ...
    @property
    def ContractName(self) -> str: ...
    @property
    def IsPrerequisite(self) -> bool: ...
    @property
    def IsRecomposable(self) -> bool: ...
    @property
    def Metadata(self) -> IDictionary: ...
    def IsConstraintSatisfiedBy(self, exportDefinition: ExportDefinition) -> bool: ...
    def ToString(self) -> str: ...
