from typing import Tuple, Set, Iterable, List


class DebugContext:
    def CreateInstance() -> DebugContext: ...
    @property
    def Mode(self) -> int: ...
    def ResetSourceFile(self, sourceFileName: str) -> None: ...
    @overload
    def TransformLambda(self, lambda: LambdaExpression) -> LambdaExpression: ...
    @overload
    def TransformLambda(self, lambda: LambdaExpression, lambdaInfo: DebugLambdaInfo) -> LambdaExpression: ...


class DebugLambdaInfo:
    def __init__(self, compilerSupport: IDebugCompilerSupport, lambdaAlias: str, optimizeForLeafFrames: bool, hiddenVariables: List[ParameterExpression], variableAliases: IDictionary, customPayload: Object): ...
    @property
    def CompilerSupport(self) -> IDebugCompilerSupport: ...
    @property
    def CustomPayload(self) -> Object: ...
    @property
    def HiddenVariables(self) -> List[ParameterExpression]: ...
    @property
    def LambdaAlias(self) -> str: ...
    @property
    def OptimizeForLeafFrames(self) -> bool: ...
    @property
    def VariableAliases(self) -> IDictionary: ...


class IDebugCompilerSupport:
    def DoesExpressionNeedReduction(self, expression: Expression) -> bool: ...
    def IsCallToDebuggableLambda(self, expression: Expression) -> bool: ...
    def QueueExpressionForReduction(self, expression: Expression) -> Expression: ...
