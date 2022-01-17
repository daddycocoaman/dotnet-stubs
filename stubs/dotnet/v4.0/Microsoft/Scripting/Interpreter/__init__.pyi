from typing import Tuple, Set, Iterable, List


class BranchLabel:
    def __init__(self): ...


class CallInstruction(Instruction):
    def ArrayItemSetter1(array: Array, index0: int, value: Object) -> None: ...
    def ArrayItemSetter2(array: Array, index0: int, index1: int, value: Object) -> None: ...
    def ArrayItemSetter3(array: Array, index0: int, index1: int, index2: int, value: Object) -> None: ...
    @overload
    def CacheAction(method: Action`6) -> MethodInfo: ...
    @overload
    def CacheAction(method: Action`3) -> MethodInfo: ...
    @overload
    def CacheAction(method: Action`4) -> MethodInfo: ...
    @overload
    def CacheAction(method: Action`5) -> MethodInfo: ...
    @overload
    def CacheAction(method: Action) -> MethodInfo: ...
    @overload
    def CacheAction(method: Action`7) -> MethodInfo: ...
    @overload
    def CacheAction(method: Action`8) -> MethodInfo: ...
    @overload
    def CacheAction(method: Action`9) -> MethodInfo: ...
    @overload
    def CacheAction(method: Action) -> MethodInfo: ...
    @overload
    def CacheAction(method: Action) -> MethodInfo: ...
    @overload
    def CacheFunc(method: Func) -> MethodInfo: ...
    @overload
    def CacheFunc(method: Func) -> MethodInfo: ...
    @overload
    def CacheFunc(method: Func`3) -> MethodInfo: ...
    @overload
    def CacheFunc(method: Func`8) -> MethodInfo: ...
    @overload
    def CacheFunc(method: Func`5) -> MethodInfo: ...
    @overload
    def CacheFunc(method: Func`10) -> MethodInfo: ...
    @overload
    def CacheFunc(method: Func`9) -> MethodInfo: ...
    @overload
    def CacheFunc(method: Func`4) -> MethodInfo: ...
    @overload
    def CacheFunc(method: Func`6) -> MethodInfo: ...
    @overload
    def CacheFunc(method: Func`7) -> MethodInfo: ...
    @overload
    def Create(info: MethodInfo) -> CallInstruction: ...
    @overload
    def Create(info: MethodInfo, parameters: Set(ParameterInfo)) -> CallInstruction: ...
    @property
    def ArgumentCount(self) -> int: ...
    @property
    def ConsumedStack(self) -> int: ...
    @property
    def Info(self) -> MethodInfo: ...
    @property
    def InstructionName(self) -> str: ...
    @property
    def ProducedStack(self) -> int: ...
    @overload
    def Invoke(self) -> Object: ...
    @overload
    def Invoke(self, args: Set(Object)) -> Object: ...
    @overload
    def Invoke(self, arg0: Object) -> Object: ...
    @overload
    def Invoke(self, arg0: Object, arg1: Object) -> Object: ...
    @overload
    def Invoke(self, arg0: Object, arg1: Object, arg2: Object) -> Object: ...
    @overload
    def Invoke(self, arg0: Object, arg1: Object, arg2: Object, arg3: Object) -> Object: ...
    @overload
    def Invoke(self, arg0: Object, arg1: Object, arg2: Object, arg3: Object, arg4: Object) -> Object: ...
    @overload
    def Invoke(self, arg0: Object, arg1: Object, arg2: Object, arg3: Object, arg4: Object, arg5: Object) -> Object: ...
    @overload
    def Invoke(self, arg0: Object, arg1: Object, arg2: Object, arg3: Object, arg4: Object, arg5: Object, arg6: Object) -> Object: ...
    @overload
    def Invoke(self, arg0: Object, arg1: Object, arg2: Object, arg3: Object, arg4: Object, arg5: Object, arg6: Object, arg7: Object) -> Object: ...
    @overload
    def Invoke(self, arg0: Object, arg1: Object, arg2: Object, arg3: Object, arg4: Object, arg5: Object, arg6: Object, arg7: Object, arg8: Object) -> Object: ...
    def InvokeInstance(self, instance: Object, args: Set(Object)) -> Object: ...
    def ToString(self) -> str: ...


class DebugInfo:
    def __init__(self): ...
    def GetMatchingDebugInfo(debugInfos: Set(DebugInfo), index: int) -> DebugInfo: ...
    def ToString(self) -> str: ...


class ExceptionHandler:
    @property
    def IsFault(self) -> bool: ...
    def IsBetterThan(self, other: ExceptionHandler) -> bool: ...
    def Matches(self, exceptionType: Type, index: int) -> bool: ...
    def ToString(self) -> str: ...




class IInstructionProvider:
    def AddInstructions(self, compiler: LightCompiler) -> None: ...


class ILightCallSiteBinder:
    @property
    def AcceptsArgumentArray(self) -> bool: ...


class Instruction:
    @property
    def ConsumedContinuations(self) -> int: ...
    @property
    def ConsumedStack(self) -> int: ...
    @property
    def ContinuationsBalance(self) -> int: ...
    @property
    def InstructionName(self) -> str: ...
    @property
    def ProducedContinuations(self) -> int: ...
    @property
    def ProducedStack(self) -> int: ...
    @property
    def StackBalance(self) -> int: ...
    def GetDebugCookie(self, compiler: LightCompiler) -> Object: ...
    def Run(self, frame: InterpretedFrame) -> int: ...
    def ToDebugString(self, instructionIndex: int, cookie: Object, labelIndexer: Func, objects: List[Object]) -> str: ...
    def ToString(self) -> str: ...


class InstructionArray:
    pass


class InstructionFactory:
    pass




class InstructionList:
    def __init__(self): ...
    def Emit(self, instruction: Instruction) -> None: ...
    def EmitAdd(self, type: Type, checked: bool) -> None: ...
    def EmitAssignLocal(self, index: int) -> None: ...
    def EmitAssignLocalBoxed(self, index: int) -> None: ...
    def EmitAssignLocalToClosure(self, index: int) -> None: ...
    @overload
    def EmitBranch(self, label: BranchLabel) -> None: ...
    @overload
    def EmitBranch(self, label: BranchLabel, hasResult: bool, hasValue: bool) -> None: ...
    def EmitBranchFalse(self, elseLabel: BranchLabel) -> None: ...
    def EmitBranchTrue(self, elseLabel: BranchLabel) -> None: ...
    def EmitCoalescingBranch(self, leftNotNull: BranchLabel) -> None: ...
    def EmitDefaultValue(self, type: Type) -> None: ...
    def EmitDiv(self, type: Type) -> None: ...
    def EmitDup(self) -> None: ...
    @overload
    def EmitDynamic(self, binder: CallSiteBinder) -> None: ...
    @overload
    def EmitDynamic(self, binder: CallSiteBinder) -> None: ...
    @overload
    def EmitDynamic(self, binder: CallSiteBinder) -> None: ...
    @overload
    def EmitDynamic(self, binder: CallSiteBinder) -> None: ...
    @overload
    def EmitDynamic(self, binder: CallSiteBinder) -> None: ...
    @overload
    def EmitDynamic(self, binder: CallSiteBinder) -> None: ...
    @overload
    def EmitDynamic(self, binder: CallSiteBinder) -> None: ...
    @overload
    def EmitDynamic(self, binder: CallSiteBinder) -> None: ...
    @overload
    def EmitDynamic(self, binder: CallSiteBinder) -> None: ...
    @overload
    def EmitDynamic(self, binder: CallSiteBinder) -> None: ...
    @overload
    def EmitDynamic(self, binder: CallSiteBinder) -> None: ...
    @overload
    def EmitDynamic(self, binder: CallSiteBinder) -> None: ...
    @overload
    def EmitDynamic(self, binder: CallSiteBinder) -> None: ...
    @overload
    def EmitDynamic(self, binder: CallSiteBinder) -> None: ...
    @overload
    def EmitDynamic(self, binder: CallSiteBinder) -> None: ...
    @overload
    def EmitDynamic(self, type: Type, binder: CallSiteBinder) -> None: ...
    def EmitEnterExceptionHandlerNonVoid(self) -> None: ...
    def EmitEnterExceptionHandlerVoid(self) -> None: ...
    def EmitEnterFinally(self) -> None: ...
    def EmitEnterTryFinally(self, finallyStartLabel: BranchLabel) -> None: ...
    def EmitEqual(self, type: Type) -> None: ...
    def EmitGetArrayItem(self, arrayType: Type) -> None: ...
    def EmitGoto(self, label: BranchLabel, hasResult: bool, hasValue: bool) -> None: ...
    def EmitGreaterThan(self, type: Type) -> None: ...
    def EmitGreaterThanOrEqual(self, type: Type) -> None: ...
    def EmitInitializeLocal(self, index: int, type: Type) -> None: ...
    def EmitLeaveExceptionHandler(self, hasValue: bool, tryExpressionEndLabel: BranchLabel) -> None: ...
    def EmitLeaveFault(self, hasValue: bool) -> None: ...
    def EmitLeaveFinally(self) -> None: ...
    def EmitLessThan(self, type: Type) -> None: ...
    def EmitLessThanOrEqual(self, type: Type) -> None: ...
    @overload
    def EmitLoad(self, value: bool) -> None: ...
    @overload
    def EmitLoad(self, value: Object) -> None: ...
    @overload
    def EmitLoad(self, value: Object, type: Type) -> None: ...
    def EmitLoadField(self, field: FieldInfo) -> None: ...
    def EmitLoadLocal(self, index: int) -> None: ...
    def EmitLoadLocalBoxed(self, index: int) -> None: ...
    def EmitLoadLocalFromClosure(self, index: int) -> None: ...
    def EmitLoadLocalFromClosureBoxed(self, index: int) -> None: ...
    def EmitMul(self, type: Type, checked: bool) -> None: ...
    def EmitNew(self, constructorInfo: ConstructorInfo) -> None: ...
    def EmitNewArray(self, elementType: Type) -> None: ...
    def EmitNewArrayBounds(self, elementType: Type, rank: int) -> None: ...
    def EmitNewArrayInit(self, elementType: Type, elementCount: int) -> None: ...
    def EmitNewRuntimeVariables(self, count: int) -> None: ...
    def EmitNot(self) -> None: ...
    def EmitNotEqual(self, type: Type) -> None: ...
    def EmitNumericConvertChecked(self, from_: TypeCode, to: TypeCode) -> None: ...
    def EmitNumericConvertUnchecked(self, from_: TypeCode, to: TypeCode) -> None: ...
    def EmitPop(self) -> None: ...
    def EmitRethrow(self) -> None: ...
    def EmitRethrowVoid(self) -> None: ...
    def EmitSetArrayItem(self, arrayType: Type) -> None: ...
    def EmitStoreField(self, field: FieldInfo) -> None: ...
    def EmitStoreLocal(self, index: int) -> None: ...
    def EmitStoreLocalBoxed(self, index: int) -> None: ...
    def EmitStoreLocalToClosure(self, index: int) -> None: ...
    def EmitSub(self, type: Type, checked: bool) -> None: ...
    def EmitSwitch(self, cases: Dictionary) -> None: ...
    def EmitThrow(self) -> None: ...
    def EmitThrowVoid(self) -> None: ...
    def EmitTypeAs(self, type: Type) -> None: ...
    def EmitTypeEquals(self) -> None: ...
    def EmitTypeIs(self, type: Type) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def CurrentContinuationsDepth(self) -> int: ...
    @property
    def CurrentStackDepth(self) -> int: ...
    @property
    def MaxStackDepth(self) -> int: ...
    def MakeLabel(self) -> BranchLabel: ...
    def MarkLabel(self, label: BranchLabel) -> None: ...
    def MarkRuntimeLabel(self) -> int: ...
    def SetDebugCookie(self, cookie: Object) -> None: ...
    def ToArray(self) -> InstructionArray: ...


class InterpretedFrame:
    def Dup(self) -> None: ...
    @property
    def Name(self) -> str: ...
    @property
    def Parent(self) -> InterpretedFrame: ...
    def GetDebugInfo(self, instructionIndex: int) -> DebugInfo: ...
    def GetExceptionStackTrace(exception: Exception) -> Set(InterpretedFrameInfo): ...
    def GetStackTraceDebugInfo(self) -> Iterable[InterpretedFrameInfo]: ...
    def Goto(self, labelIndex: int, value: Object) -> int: ...
    def GroupStackFrames(stackTrace: Iterable[StackFrame]) -> Iterable[StackFrame]: ...
    def IsInterpretedFrame(method: MethodBase) -> bool: ...
    def Peek(self) -> Object: ...
    @overload
    def Pop(self) -> Object: ...
    @overload
    def Pop(self, n: int) -> Object: ...
    @overload
    def Push(self, value: int) -> None: ...
    @overload
    def Push(self, value: bool) -> None: ...
    @overload
    def Push(self, value: Object) -> None: ...
    def PushContinuation(self, continuation: int) -> None: ...
    def RemoveContinuation(self) -> None: ...
    def VoidGoto(self, labelIndex: int) -> int: ...
    def YieldToCurrentContinuation(self) -> int: ...
    def YieldToPendingContinuation(self) -> int: ...


class InterpretedFrameInfo:
    def __init__(self, methodName: str, info: DebugInfo): ...
    def ToString(self) -> str: ...


class LabelScopeKind:
    Statement = 0
    Block = 1
    Switch = 2
    Lambda = 3
    Try = 4
    Catch = 5
    Finally = 6
    Filter = 7
    Expression = 8


class LightCompiler:
    def Compile(self, expr: Expression) -> None: ...
    def CompileGetBoxedVariable(self, variable: ParameterExpression) -> None: ...
    def CompileGetVariable(self, variable: ParameterExpression) -> None: ...
    def CompileParameterExpression(self, expr: Expression) -> None: ...
    def CompileSetVariable(self, variable: ParameterExpression, isVoid: bool) -> None: ...
    @overload
    def EmitCall(self, method: MethodInfo) -> None: ...
    @overload
    def EmitCall(self, method: MethodInfo, parameters: Set(ParameterInfo)) -> None: ...
    @property
    def Instructions(self) -> InstructionList: ...
    @property
    def Locals(self) -> LocalVariables: ...
    def GetBranchLabel(self, target: LabelTarget) -> BranchLabel: ...
    def PopLabelBlock(self, kind: LabelScopeKind) -> None: ...
    def PushLabelBlock(self, type: LabelScopeKind) -> None: ...


class LightLambda:
    def add_Compile(self, value: EventHandler) -> None: ...
    def remove_Compile(self, value: EventHandler) -> None: ...
    def Run(self, arguments: Set(Object)) -> Object: ...


class LightLambdaCompileEventArgs:
    @property
    def Compiled(self) -> Delegate: ...


class LocalDefinition:
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    def Equals(self, other: LocalDefinition) -> bool: ...
    @property
    def Index(self) -> int: ...
    @property
    def Parameter(self) -> ParameterExpression: ...
    def GetHashCode(self) -> int: ...
    def op_Equality(self: LocalDefinition, other: LocalDefinition) -> bool: ...
    def op_Inequality(self: LocalDefinition, other: LocalDefinition) -> bool: ...


class LocalVariable:
    @property
    def InClosure(self) -> bool: ...
    @property
    def InClosureOrBoxed(self) -> bool: ...
    @property
    def IsBoxed(self) -> bool: ...
    @IsBoxed.setter
    def IsBoxed(self, value: bool) -> None: ...
    def ToString(self) -> str: ...


class LocalVariables:
    def DefineLocal(self, variable: ParameterExpression, start: int) -> LocalDefinition: ...
    @property
    def LocalCount(self) -> int: ...
    def GetLocalIndex(self, var: ParameterExpression) -> int: ...
    def GetOrDefineLocal(self, var: ParameterExpression) -> int: ...
    def TryGetLocalOrClosure(self, var: ParameterExpression) -> Tuple[bool, LocalVariable]: ...
    def UndefineLocal(self, definition: LocalDefinition, end: int) -> None: ...


class NewArrayBoundsInstruction(Instruction):
    @property
    def ConsumedStack(self) -> int: ...
    @property
    def ProducedStack(self) -> int: ...
    def Run(self, frame: InterpretedFrame) -> int: ...






