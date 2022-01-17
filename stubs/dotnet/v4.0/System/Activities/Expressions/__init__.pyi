from typing import Tuple, Set, Iterable, List






class AndAlso:
    def __init__(self): ...
    @property
    def Left(self) -> Activity: ...
    @property
    def Right(self) -> Activity: ...
    @Left.setter
    def Left(self, value: Activity) -> None: ...
    @Right.setter
    def Right(self, value: Activity) -> None: ...












class AssemblyReference(Object):
    def __init__(self): ...
    @property
    def Assembly(self) -> Assembly: ...
    @property
    def AssemblyName(self) -> AssemblyName: ...
    def LoadAssembly(self) -> None: ...
    @overload
    def op_Implicit(assembly: Assembly) -> AssemblyReference: ...
    @overload
    def op_Implicit(assemblyName: AssemblyName) -> AssemblyReference: ...
    @Assembly.setter
    def Assembly(self, value: Assembly) -> None: ...
    @AssemblyName.setter
    def AssemblyName(self, value: AssemblyName) -> None: ...




class CompiledExpressionInvoker(Object):
    def __init__(self, expression: ITextExpression, isReference: bool, metadata: CodeActivityMetadata): ...
    @property
    def IsStaticallyCompiled(self) -> bool: ...
    def GetCompiledExpressionRoot(target: Object) -> Object: ...
    def GetCompiledExpressionRootForImplementation(target: Object) -> Object: ...
    def InvokeExpression(self, activityContext: ActivityContext) -> Object: ...
    def SetCompiledExpressionRoot(target: Object, compiledExpressionRoot: ICompiledExpressionRoot) -> None: ...
    def SetCompiledExpressionRootForImplementation(target: Object, compiledExpressionRoot: ICompiledExpressionRoot) -> None: ...














class ExpressionServices(Object):
    def Convert(expression: Expression) -> Activity: ...
    def ConvertReference(expression: Expression) -> Activity: ...
    def TryConvert(expression: Expression) -> Tuple[bool, Activity]: ...
    def TryConvertReference(expression: Expression) -> Tuple[bool, Activity]: ...
















































class ITextExpression:
    @property
    def ExpressionText(self) -> str: ...
    @property
    def Language(self) -> str: ...
    @property
    def RequiresCompilation(self) -> bool: ...
    def GetExpressionTree(self) -> Expression: ...




class LambdaSerializationException(Exception):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...
























class OrElse:
    def __init__(self): ...
    @property
    def Left(self) -> Activity: ...
    @property
    def Right(self) -> Activity: ...
    @Left.setter
    def Left(self, value: Activity) -> None: ...
    @Right.setter
    def Right(self, value: Activity) -> None: ...








class TextExpression(Object):
    @property
    def DefaultNamespaces() -> List[str]: ...
    @property
    def DefaultReferences() -> List[AssemblyReference]: ...
    def GetNamespaces(target: Object) -> List[str]: ...
    def GetNamespacesForImplementation(target: Object) -> List[str]: ...
    def GetNamespacesInScope(activity: Activity) -> List[str]: ...
    def GetReferences(target: Object) -> List[AssemblyReference]: ...
    def GetReferencesForImplementation(target: Object) -> List[AssemblyReference]: ...
    def GetReferencesInScope(activity: Activity) -> List[AssemblyReference]: ...
    @overload
    def SetNamespaces(target: Object, namespaces: Set(str)) -> None: ...
    @overload
    def SetNamespaces(target: Object, namespaces: List[str]) -> None: ...
    @overload
    def SetNamespacesForImplementation(target: Object, namespaces: List[str]) -> None: ...
    @overload
    def SetNamespacesForImplementation(target: Object, namespaces: Set(str)) -> None: ...
    @overload
    def SetReferences(target: Object, references: List[AssemblyReference]) -> None: ...
    @overload
    def SetReferences(target: Object, references: Set(AssemblyReference)) -> None: ...
    @overload
    def SetReferencesForImplementation(target: Object, references: List[AssemblyReference]) -> None: ...
    @overload
    def SetReferencesForImplementation(target: Object, references: Set(AssemblyReference)) -> None: ...
    def ShouldSerializeNamespaces(target: Object) -> bool: ...
    def ShouldSerializeNamespacesForImplementation(target: Object) -> bool: ...
    def ShouldSerializeReferences(target: Object) -> bool: ...
    def ShouldSerializeReferencesForImplementation(target: Object) -> bool: ...










