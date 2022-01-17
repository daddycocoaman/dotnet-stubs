__all__ = ['Interpreter']
from typing import Tuple, Set, Iterable, List


class DynamicExpression(Expression):
    @overload
    def Dynamic(binder: CallSiteBinder, returnType: Type, arg0: Expression) -> DynamicExpression: ...
    @overload
    def Dynamic(binder: CallSiteBinder, returnType: Type, arguments: Iterable[Expression]) -> DynamicExpression: ...
    @overload
    def Dynamic(binder: CallSiteBinder, returnType: Type, arguments: Set(Expression)) -> DynamicExpression: ...
    @overload
    def Dynamic(binder: CallSiteBinder, returnType: Type, arg0: Expression, arg1: Expression) -> DynamicExpression: ...
    @overload
    def Dynamic(binder: CallSiteBinder, returnType: Type, arg0: Expression, arg1: Expression, arg2: Expression) -> DynamicExpression: ...
    @overload
    def Dynamic(binder: CallSiteBinder, returnType: Type, arg0: Expression, arg1: Expression, arg2: Expression, arg3: Expression) -> DynamicExpression: ...
    @property
    def Arguments(self) -> ReadOnlyCollection: ...
    @property
    def Binder(self) -> CallSiteBinder: ...
    @property
    def CanReduce(self) -> bool: ...
    @property
    def DelegateType(self) -> Type: ...
    @property
    def NodeType(self) -> ExpressionType: ...
    @property
    def Type(self) -> Type: ...
    @overload
    def MakeDynamic(delegateType: Type, binder: CallSiteBinder, arguments: Iterable[Expression]) -> DynamicExpression: ...
    @overload
    def MakeDynamic(delegateType: Type, binder: CallSiteBinder, arguments: Set(Expression)) -> DynamicExpression: ...
    @overload
    def MakeDynamic(delegateType: Type, binder: CallSiteBinder, arg0: Expression) -> DynamicExpression: ...
    @overload
    def MakeDynamic(delegateType: Type, binder: CallSiteBinder, arg0: Expression, arg1: Expression) -> DynamicExpression: ...
    @overload
    def MakeDynamic(delegateType: Type, binder: CallSiteBinder, arg0: Expression, arg1: Expression, arg2: Expression) -> DynamicExpression: ...
    @overload
    def MakeDynamic(delegateType: Type, binder: CallSiteBinder, arg0: Expression, arg1: Expression, arg2: Expression, arg3: Expression) -> DynamicExpression: ...
    def Reduce(self) -> Expression: ...
    def Update(self, arguments: Iterable[Expression]) -> DynamicExpression: ...
