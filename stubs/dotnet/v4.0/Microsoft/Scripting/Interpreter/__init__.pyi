from typing import Tuple, Set, Iterable, List


class LocalVariables:
    def DefineLocal(self, variable: ParameterExpression, start: int) -> LocalDefinition: ...
    @property
    def LocalCount(self) -> int: ...
    def GetLocalIndex(self, var: ParameterExpression) -> int: ...
    def GetOrDefineLocal(self, var: ParameterExpression) -> int: ...
    def TryGetLocalOrClosure(self, var: ParameterExpression) -> Tuple[bool, LocalVariable]: ...
    def UndefineLocal(self, definition: LocalDefinition, end: int) -> None: ...
