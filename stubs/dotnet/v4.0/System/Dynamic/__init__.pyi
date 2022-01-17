from typing import Tuple, Set, Iterable, List


class UnaryOperationBinder(DynamicMetaObjectBinder):
    @overload
    def Bind(self, target: DynamicMetaObject, args: Set(DynamicMetaObject)) -> DynamicMetaObject: ...
    @overload
    def FallbackUnaryOperation(self, target: DynamicMetaObject) -> DynamicMetaObject: ...
    @overload
    def FallbackUnaryOperation(self, target: DynamicMetaObject, errorSuggestion: DynamicMetaObject) -> DynamicMetaObject: ...
    @property
    def Operation(self) -> ExpressionType: ...
    @property
    def ReturnType(self) -> Type: ...