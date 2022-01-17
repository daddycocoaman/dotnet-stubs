from typing import Tuple, Set, Iterable, List


class Binder:
    def BinaryOperation(flags: CSharpBinderFlags, operation: ExpressionType, context: Type, argumentInfo: Iterable[CSharpArgumentInfo]) -> CallSiteBinder: ...
    def Convert(flags: CSharpBinderFlags, type: Type, context: Type) -> CallSiteBinder: ...
    def GetIndex(flags: CSharpBinderFlags, context: Type, argumentInfo: Iterable[CSharpArgumentInfo]) -> CallSiteBinder: ...
    def GetMember(flags: CSharpBinderFlags, name: str, context: Type, argumentInfo: Iterable[CSharpArgumentInfo]) -> CallSiteBinder: ...
    def Invoke(flags: CSharpBinderFlags, context: Type, argumentInfo: Iterable[CSharpArgumentInfo]) -> CallSiteBinder: ...
    def InvokeConstructor(flags: CSharpBinderFlags, context: Type, argumentInfo: Iterable[CSharpArgumentInfo]) -> CallSiteBinder: ...
    def InvokeMember(flags: CSharpBinderFlags, name: str, typeArguments: Iterable[Type], context: Type, argumentInfo: Iterable[CSharpArgumentInfo]) -> CallSiteBinder: ...
    def IsEvent(flags: CSharpBinderFlags, name: str, context: Type) -> CallSiteBinder: ...
    def SetIndex(flags: CSharpBinderFlags, context: Type, argumentInfo: Iterable[CSharpArgumentInfo]) -> CallSiteBinder: ...
    def SetMember(flags: CSharpBinderFlags, name: str, context: Type, argumentInfo: Iterable[CSharpArgumentInfo]) -> CallSiteBinder: ...
    def UnaryOperation(flags: CSharpBinderFlags, operation: ExpressionType, context: Type, argumentInfo: Iterable[CSharpArgumentInfo]) -> CallSiteBinder: ...


class CSharpArgumentInfo:
    def Create(flags: CSharpArgumentInfoFlags, name: str) -> CSharpArgumentInfo: ...


class CSharpArgumentInfoFlags:
    #None = 0
    UseCompileTimeType = 1
    Constant = 2
    NamedArgument = 4
    IsRef = 8
    IsOut = 16
    IsStaticType = 32


class CSharpBinderFlags:
    #None = 0
    CheckedContext = 1
    InvokeSimpleName = 2
    InvokeSpecialName = 4
    BinaryOperationLogical = 8
    ConvertExplicit = 16
    ConvertArrayIndex = 32
    ResultIndexed = 64
    ValueFromCompoundAssignment = 128
    ResultDiscarded = 256


class RuntimeBinderException:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class RuntimeBinderInternalCompilerException:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...
