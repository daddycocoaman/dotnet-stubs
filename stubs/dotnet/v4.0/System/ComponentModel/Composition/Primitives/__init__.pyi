from typing import Tuple, Set, Iterable, List


class ComposablePart(Object):
    def Activate(self) -> None: ...
    @property
    def ExportDefinitions(self) -> Iterable[ExportDefinition]: ...
    @property
    def ImportDefinitions(self) -> Iterable[ImportDefinition]: ...
    @property
    def Metadata(self) -> IDictionary: ...
    def GetExportedValue(self, definition: ExportDefinition) -> Object: ...
    def SetImport(self, definition: ImportDefinition, exports: Iterable[Export]) -> None: ...


class ComposablePartCatalog(Object):
    def Dispose(self) -> None: ...
    @property
    def Parts(self) -> IQueryable: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def GetExports(self, definition: ImportDefinition) -> Iterable[Tuple]: ...


class ComposablePartDefinition(Object):
    def CreatePart(self) -> ComposablePart: ...
    @property
    def ExportDefinitions(self) -> Iterable[ExportDefinition]: ...
    @property
    def ImportDefinitions(self) -> Iterable[ImportDefinition]: ...
    @property
    def Metadata(self) -> IDictionary: ...


class ComposablePartException(Exception):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, element: ICompositionElement): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...
    @overload
    def __init__(self, message: str, element: ICompositionElement, innerException: Exception): ...
    @property
    def Element(self) -> ICompositionElement: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...


class ContractBasedImportDefinition(ImportDefinition):
    @overload
    def __init__(self, contractName: str, requiredTypeIdentity: str, requiredMetadata: Iterable[KeyValuePair], cardinality: ImportCardinality, isRecomposable: bool, isPrerequisite: bool, requiredCreationPolicy: CreationPolicy): ...
    @overload
    def __init__(self, contractName: str, requiredTypeIdentity: str, requiredMetadata: Iterable[KeyValuePair], cardinality: ImportCardinality, isRecomposable: bool, isPrerequisite: bool, requiredCreationPolicy: CreationPolicy, metadata: IDictionary): ...
    @property
    def Constraint(self) -> Expression: ...
    @property
    def RequiredCreationPolicy(self) -> CreationPolicy: ...
    @property
    def RequiredMetadata(self) -> Iterable[KeyValuePair]: ...
    @property
    def RequiredTypeIdentity(self) -> str: ...
    def IsConstraintSatisfiedBy(self, exportDefinition: ExportDefinition) -> bool: ...
    def ToString(self) -> str: ...


class Export(Object):
    @overload
    def __init__(self, contractName: str, exportedValueGetter: Func): ...
    @overload
    def __init__(self, definition: ExportDefinition, exportedValueGetter: Func): ...
    @overload
    def __init__(self, contractName: str, metadata: IDictionary, exportedValueGetter: Func): ...
    @property
    def Definition(self) -> ExportDefinition: ...
    @property
    def Metadata(self) -> IDictionary: ...
    @property
    def Value(self) -> Object: ...


class ExportDefinition(Object):
    def __init__(self, contractName: str, metadata: IDictionary): ...
    @property
    def ContractName(self) -> str: ...
    @property
    def Metadata(self) -> IDictionary: ...
    def ToString(self) -> str: ...


class ExportedDelegate(Object):
    def __init__(self, instance: Object, method: MethodInfo): ...
    def CreateDelegate(self, delegateType: Type) -> Delegate: ...


class ICompositionElement:
    @property
    def DisplayName(self) -> str: ...
    @property
    def Origin(self) -> ICompositionElement: ...


class ImportCardinality:
    ZeroOrOne = 0
    ExactlyOne = 1
    ZeroOrMore = 2


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
