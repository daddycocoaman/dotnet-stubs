from typing import Tuple, Set, Iterable, List


class RuleConditionDialog(Form):
    @overload
    def __init__(self, activity: Activity, expression: CodeExpression): ...
    @overload
    def __init__(self, activityType: Type, typeProvider: ITypeProvider, expression: CodeExpression): ...
    @property
    def Expression(self) -> CodeExpression: ...
