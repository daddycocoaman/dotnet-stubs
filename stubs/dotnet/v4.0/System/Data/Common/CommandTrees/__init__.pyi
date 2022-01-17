__all__ = ['ExpressionBuilder','ExpressionBuilder','ExpressionBuilder']
from typing import Tuple, Set, Iterable, List


class DefaultExpressionVisitor:
    @overload
    def Visit(self, expression: DbSortExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbCaseExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbOfTypeExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbNewInstanceExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbRefExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbRelationshipNavigationExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbDerefExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbRefKeyExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbQuantifierExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbEntityRefExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbCastExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbProjectExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbCrossJoinExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbJoinExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbApplyExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbGroupByExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbSkipExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbScanExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbFilterExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbIsOfExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbExceptExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbConstantExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbNullExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbVariableReferenceExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbParameterReferenceExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbFunctionExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbLambdaExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbPropertyExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbComparisonExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbLikeExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbTreatExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbLimitExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbArithmeticExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbAndExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbOrExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbNotExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbDistinctExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbElementExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbIsEmptyExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbUnionAllExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbIntersectExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbIsNullExpression) -> DbExpression: ...
    @overload
    def Visit(self, expression: DbExpression) -> DbExpression: ...
