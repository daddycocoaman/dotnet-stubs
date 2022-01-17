from typing import Tuple, Set, Iterable, List


class BlockBuilder:
    def __init__(self): ...
    def op_Implicit(block: BlockBuilder) -> Expression: ...
    def ToExpression(self) -> Expression: ...


class ExpressionAccess:
    #None = 0
    Read = 1
    Write = 2
    ReadWrite = 3


class ExpressionCollectionBuilder:
    def __init__(self): ...
    def ToMethodCall(self, instance: Expression, method: MethodInfo) -> Expression: ...




class FinallyFlowControlExpression:
    @property
    def Body(self) -> Expression: ...
    @property
    def CanReduce(self) -> bool: ...
    @property
    def NodeType(self) -> ExpressionType: ...
    @property
    def Type(self) -> Type: ...
    def Reduce(self) -> Expression: ...


class GeneratorExpression:
    @property
    def Body(self) -> Expression: ...
    @property
    def CanReduce(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def NodeType(self) -> ExpressionType: ...
    @property
    def RewriteAssignments(self) -> bool: ...
    @property
    def Target(self) -> LabelTarget: ...
    @property
    def Type(self) -> Type: ...
    def Reduce(self) -> Expression: ...


class IfStatementBuilder:
    @overload
    def Else(self, body: Set(Expression)) -> Expression: ...
    @overload
    def Else(self, body: Expression) -> Expression: ...
    @overload
    def ElseIf(self, test: Expression, body: Set(Expression)) -> IfStatementBuilder: ...
    @overload
    def ElseIf(self, test: Expression, body: Expression) -> IfStatementBuilder: ...
    def op_Implicit(builder: IfStatementBuilder) -> Expression: ...
    def ToStatement(self) -> Expression: ...


class IfStatementTest:
    @property
    def Body(self) -> Expression: ...
    @property
    def Test(self) -> Expression: ...


class ILightExceptionAwareExpression:
    def ReduceForLightExceptions(self) -> Expression: ...


class LambdaBuilder:
    def AddHiddenVariable(self, temp: ParameterExpression) -> None: ...
    def AddParameters(self, parameters: Set(ParameterExpression)) -> None: ...
    def ClosedOverParameter(self, type: Type, name: str) -> ParameterExpression: ...
    def ClosedOverVariable(self, type: Type, name: str) -> Expression: ...
    def CreateHiddenParameter(self, name: str, type: Type) -> ParameterExpression: ...
    def CreateParamsArray(self, type: Type, name: str) -> ParameterExpression: ...
    @property
    def Body(self) -> Expression: ...
    @property
    def Dictionary(self) -> bool: ...
    @property
    def Locals(self) -> List: ...
    @property
    def Name(self) -> str: ...
    @property
    def Parameters(self) -> List: ...
    @property
    def ParamsArray(self) -> ParameterExpression: ...
    @property
    def ReturnType(self) -> Type: ...
    @property
    def Visible(self) -> bool: ...
    def GetVisibleVariables(self) -> List: ...
    def HiddenVariable(self, type: Type, name: str) -> ParameterExpression: ...
    def MakeGenerator(self, label: LabelTarget, lambdaType: Type) -> LambdaExpression: ...
    @overload
    def MakeLambda(self) -> LambdaExpression: ...
    @overload
    def MakeLambda(self, lambdaType: Type) -> LambdaExpression: ...
    def Parameter(self, type: Type, name: str) -> ParameterExpression: ...
    @Body.setter
    def Body(self, value: Expression) -> None: ...
    @Dictionary.setter
    def Dictionary(self, value: bool) -> None: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    @ReturnType.setter
    def ReturnType(self, value: Type) -> None: ...
    @Visible.setter
    def Visible(self, value: bool) -> None: ...
    def Variable(self, type: Type, name: str) -> Expression: ...


class LightDynamicExpression:
    def AddInstructions(self, compiler: LightCompiler) -> None: ...
    @property
    def Binder(self) -> CallSiteBinder: ...
    @property
    def CanReduce(self) -> bool: ...
    @property
    def NodeType(self) -> ExpressionType: ...
    @property
    def Type(self) -> Type: ...
    def Reduce(self) -> Expression: ...


class LightDynamicExpression1(LightDynamicExpression):
    @property
    def Argument0(self) -> Expression: ...
    def Reduce(self) -> Expression: ...


class LightDynamicExpression2(LightDynamicExpression):
    @property
    def Argument0(self) -> Expression: ...
    @property
    def Argument1(self) -> Expression: ...
    def Reduce(self) -> Expression: ...


class LightDynamicExpression3(LightDynamicExpression):
    @property
    def Argument0(self) -> Expression: ...
    @property
    def Argument1(self) -> Expression: ...
    @property
    def Argument2(self) -> Expression: ...
    def Reduce(self) -> Expression: ...


class LightDynamicExpression4(LightDynamicExpression):
    @property
    def Argument0(self) -> Expression: ...
    @property
    def Argument1(self) -> Expression: ...
    @property
    def Argument2(self) -> Expression: ...
    @property
    def Argument3(self) -> Expression: ...
    def Reduce(self) -> Expression: ...




class LightLambdaExpression:
    @overload
    def Compile(self) -> Delegate: ...
    @overload
    def Compile(self, compilationThreshold: int) -> Delegate: ...
    @property
    def Body(self) -> Expression: ...
    @property
    def CanReduce(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def NodeType(self) -> ExpressionType: ...
    @property
    def Parameters(self) -> List[ParameterExpression]: ...
    @property
    def ReturnType(self) -> Type: ...
    def Reduce(self) -> Expression: ...


class LightTypedDynamicExpression1(LightDynamicExpression1):
    @property
    def Type(self) -> Type: ...


class LightTypedDynamicExpression2(LightDynamicExpression2):
    @property
    def Type(self) -> Type: ...


class LightTypedDynamicExpression4(LightDynamicExpression4):
    @property
    def Type(self) -> Type: ...


class LightTypedDynamicExpressionN(LightDynamicExpression):
    @property
    def Arguments(self) -> List[Expression]: ...
    @property
    def Type(self) -> Type: ...
    def Reduce(self) -> Expression: ...


class TryStatementBuilder:
    @overload
    def Catch(self, type: Type, body: Expression) -> TryStatementBuilder: ...
    @overload
    def Catch(self, type: Type, body: Set(Expression)) -> TryStatementBuilder: ...
    @overload
    def Catch(self, holder: ParameterExpression, body: Set(Expression)) -> TryStatementBuilder: ...
    @overload
    def Catch(self, holder: ParameterExpression, body: Expression) -> TryStatementBuilder: ...
    @overload
    def Catch(self, type: Type, expr0: Expression, expr1: Expression) -> TryStatementBuilder: ...
    @overload
    def Catch(self, holder: ParameterExpression, expr0: Expression, expr1: Expression) -> TryStatementBuilder: ...
    @overload
    def Catch(self, type: Type, expr0: Expression, expr1: Expression, expr2: Expression) -> TryStatementBuilder: ...
    @overload
    def Catch(self, holder: ParameterExpression, expr0: Expression, expr1: Expression, expr2: Expression) -> TryStatementBuilder: ...
    @overload
    def Catch(self, type: Type, expr0: Expression, expr1: Expression, expr2: Expression, expr3: Expression) -> TryStatementBuilder: ...
    @overload
    def Catch(self, holder: ParameterExpression, expr0: Expression, expr1: Expression, expr2: Expression, expr3: Expression) -> TryStatementBuilder: ...
    def Fault(self, body: Set(Expression)) -> TryStatementBuilder: ...
    @overload
    def Filter(self, holder: ParameterExpression, condition: Expression, body: Expression) -> TryStatementBuilder: ...
    @overload
    def Filter(self, holder: ParameterExpression, condition: Expression, body: Set(Expression)) -> TryStatementBuilder: ...
    @overload
    def Filter(self, type: Type, condition: Expression, body: Expression) -> TryStatementBuilder: ...
    @overload
    def Filter(self, type: Type, condition: Expression, body: Set(Expression)) -> TryStatementBuilder: ...
    @overload
    def Finally(self, body: Set(Expression)) -> TryStatementBuilder: ...
    @overload
    def Finally(self, body: Expression) -> TryStatementBuilder: ...
    @overload
    def FinallyWithJumps(self, body: Set(Expression)) -> TryStatementBuilder: ...
    @overload
    def FinallyWithJumps(self, body: Expression) -> TryStatementBuilder: ...
    def op_Implicit(builder: TryStatementBuilder) -> Expression: ...
    def ToExpression(self) -> Expression: ...


class Utils:
    @overload
    def AddDebugInfo(expression: Expression, document: SymbolDocumentInfo, start: SourceLocation, end: SourceLocation) -> Expression: ...
    @overload
    def AddDebugInfo(expression: Expression, document: SymbolDocumentInfo, startLine: int, startColumn: int, endLine: int, endColumn: int) -> Expression: ...
    def Box(expression: Expression) -> Expression: ...
    @overload
    def Coalesce(left: Expression, right: Expression) -> Tuple[Expression, ParameterExpression]: ...
    @overload
    def Coalesce(builder: LambdaBuilder, left: Expression, right: Expression) -> Expression: ...
    @overload
    def CoalesceFalse(builder: LambdaBuilder, left: Expression, right: Expression, isTrue: MethodInfo) -> Expression: ...
    @overload
    def CoalesceFalse(left: Expression, right: Expression, isTrue: MethodInfo) -> Tuple[Expression, ParameterExpression]: ...
    @overload
    def CoalesceTrue(builder: LambdaBuilder, left: Expression, right: Expression, isTrue: MethodInfo) -> Expression: ...
    @overload
    def CoalesceTrue(left: Expression, right: Expression, isTrue: MethodInfo) -> Tuple[Expression, ParameterExpression]: ...
    @overload
    def ComplexCallHelper(method: MethodInfo, arguments: Set(Expression)) -> Expression: ...
    @overload
    def ComplexCallHelper(instance: Expression, method: MethodInfo, arguments: Set(Expression)) -> Expression: ...
    @overload
    def Constant(value: Object) -> Expression: ...
    @overload
    def Constant(value: Object, type: Type) -> ConstantExpression: ...
    def Convert(expression: Expression, type: Type) -> Expression: ...
    def DebugMark(expression: Expression, marker: str) -> Expression: ...
    def DebugMarker(marker: str) -> Expression: ...
    def Default(type: Type) -> DefaultExpression: ...
    def Empty() -> DefaultExpression: ...
    def FinallyFlowControl(body: Expression) -> Expression: ...
    @overload
    def Generator(label: LabelTarget, body: Expression) -> GeneratorExpression: ...
    @overload
    def Generator(label: LabelTarget, body: Expression, type: Type) -> GeneratorExpression: ...
    @overload
    def Generator(name: str, label: LabelTarget, body: Expression, type: Type) -> GeneratorExpression: ...
    @overload
    def Generator(name: str, label: LabelTarget, body: Expression, type: Type, rewriteAssignments: bool) -> GeneratorExpression: ...
    @overload
    def GeneratorLambda(label: LabelTarget, body: Expression, parameters: Set(ParameterExpression)) -> Expression: ...
    @overload
    def GeneratorLambda(label: LabelTarget, body: Expression, name: str, parameters: Set(ParameterExpression)) -> Expression: ...
    @overload
    def GeneratorLambda(label: LabelTarget, body: Expression, name: str, parameters: Iterable[ParameterExpression]) -> Expression: ...
    @overload
    def GeneratorLambda(delegateType: Type, label: LabelTarget, body: Expression, parameters: Set(ParameterExpression)) -> LambdaExpression: ...
    @overload
    def GeneratorLambda(delegateType: Type, label: LabelTarget, body: Expression, name: str, parameters: Set(ParameterExpression)) -> LambdaExpression: ...
    @overload
    def GeneratorLambda(delegateType: Type, label: LabelTarget, body: Expression, name: str, parameters: Iterable[ParameterExpression]) -> LambdaExpression: ...
    @overload
    def GeneratorLambda(delegateType: Type, label: LabelTarget, body: Expression, name: str, rewriteAssignments: bool, parameters: Iterable[ParameterExpression]) -> LambdaExpression: ...
    def GetLValueAccess(type: ExpressionType) -> ExpressionAccess: ...
    @overload
    def If() -> IfStatementBuilder: ...
    @overload
    def If(tests: Set(IfStatementTest), else: Expression) -> Expression: ...
    @overload
    def If(test: Expression, body: Set(Expression)) -> IfStatementBuilder: ...
    @overload
    def If(test: Expression, body: Expression) -> IfStatementBuilder: ...
    def IfCondition(test: Expression, body: Expression) -> IfStatementTest: ...
    @overload
    def IfThen(test: Expression, body: Expression) -> Expression: ...
    @overload
    def IfThen(test: Expression, body: Set(Expression)) -> Expression: ...
    def IfThenElse(test: Expression, body: Expression, else: Expression) -> Expression: ...
    @overload
    def Infinite(body: Expression) -> LoopExpression: ...
    @overload
    def Infinite(body: Expression, break: LabelTarget, continue: LabelTarget) -> LoopExpression: ...
    def IsAssignment(type: ExpressionType) -> bool: ...
    def IsLValue(type: ExpressionType) -> bool: ...
    def IsReadWriteAssignment(type: ExpressionType) -> bool: ...
    def IsWriteOnlyAssignment(type: ExpressionType) -> bool: ...
    def Lambda(returnType: Type, name: str) -> LambdaBuilder: ...
    @overload
    def LightDynamic(binder: CallSiteBinder, arguments: List[Expression]) -> LightDynamicExpression: ...
    @overload
    def LightDynamic(binder: CallSiteBinder, arguments: ExpressionCollectionBuilder) -> LightDynamicExpression: ...
    @overload
    def LightDynamic(binder: CallSiteBinder, arg0: Expression) -> LightDynamicExpression: ...
    @overload
    def LightDynamic(binder: CallSiteBinder, returnType: Type, arguments: List[Expression]) -> LightDynamicExpression: ...
    @overload
    def LightDynamic(binder: CallSiteBinder, returnType: Type, arguments: ExpressionCollectionBuilder) -> LightDynamicExpression: ...
    @overload
    def LightDynamic(binder: CallSiteBinder, returnType: Type, arg0: Expression) -> LightDynamicExpression: ...
    @overload
    def LightDynamic(binder: CallSiteBinder, arg0: Expression, arg1: Expression) -> LightDynamicExpression: ...
    @overload
    def LightDynamic(binder: CallSiteBinder, arg0: Expression, arg1: Expression, arg2: Expression) -> LightDynamicExpression: ...
    @overload
    def LightDynamic(binder: CallSiteBinder, returnType: Type, arg0: Expression, arg1: Expression) -> LightDynamicExpression: ...
    @overload
    def LightDynamic(binder: CallSiteBinder, returnType: Type, arg0: Expression, arg1: Expression, arg2: Expression) -> LightDynamicExpression: ...
    @overload
    def LightDynamic(binder: CallSiteBinder, arg0: Expression, arg1: Expression, arg2: Expression, arg3: Expression) -> LightDynamicExpression: ...
    @overload
    def LightDynamic(binder: CallSiteBinder, returnType: Type, arg0: Expression, arg1: Expression, arg2: Expression, arg3: Expression) -> LightDynamicExpression: ...
    @overload
    def LightLambda(retType: Type, body: Expression, name: str, args: List[ParameterExpression]) -> LightExpression: ...
    @overload
    def LightLambda(retType: Type, delegateType: Type, body: Expression, name: str, args: List[ParameterExpression]) -> LightLambdaExpression: ...
    @overload
    def Loop(test: Expression, increment: Expression, body: Expression, else: Expression) -> LoopExpression: ...
    @overload
    def Loop(test: Expression, increment: Expression, body: Expression, else: Expression, break: LabelTarget, continue: LabelTarget) -> LoopExpression: ...
    def MakeYield(target: LabelTarget, value: Expression, yieldMarker: int) -> YieldExpression: ...
    def NewArrayHelper(type: Type, initializers: Iterable[Expression]) -> NewArrayExpression: ...
    @overload
    def SimpleCallHelper(method: MethodInfo, arguments: Set(Expression)) -> MethodCallExpression: ...
    @overload
    def SimpleCallHelper(instance: Expression, method: MethodInfo, arguments: Set(Expression)) -> MethodCallExpression: ...
    def SimpleNewHelper(constructor: ConstructorInfo, arguments: Set(Expression)) -> NewExpression: ...
    @overload
    def Try(body: Set(Expression)) -> TryStatementBuilder: ...
    @overload
    def Try(body: Expression) -> TryStatementBuilder: ...
    @overload
    def Try(expr0: Expression, expr1: Expression) -> TryStatementBuilder: ...
    @overload
    def Try(expr0: Expression, expr1: Expression, expr2: Expression) -> TryStatementBuilder: ...
    @overload
    def Try(expr0: Expression, expr1: Expression, expr2: Expression, expr3: Expression) -> TryStatementBuilder: ...
    def Unless(test: Expression, body: Expression) -> Expression: ...
    def Update(expression: BinaryExpression, left: Expression, right: Expression) -> BinaryExpression: ...
    def Void(expression: Expression) -> Expression: ...
    def WeakConstant(value: Object) -> MemberExpression: ...
    @overload
    def While(test: Expression, body: Expression, else: Expression) -> LoopExpression: ...
    @overload
    def While(test: Expression, body: Expression, else: Expression, break: LabelTarget, continue: LabelTarget) -> LoopExpression: ...
    def YieldBreak(target: LabelTarget) -> YieldExpression: ...
    @overload
    def YieldReturn(target: LabelTarget, value: Expression) -> YieldExpression: ...
    @overload
    def YieldReturn(target: LabelTarget, value: Expression, yieldMarker: int) -> YieldExpression: ...


class YieldExpression:
    @property
    def CanReduce(self) -> bool: ...
    @property
    def NodeType(self) -> ExpressionType: ...
    @property
    def Target(self) -> LabelTarget: ...
    @property
    def Type(self) -> Type: ...
    @property
    def Value(self) -> Expression: ...
    @property
    def YieldMarker(self) -> int: ...
