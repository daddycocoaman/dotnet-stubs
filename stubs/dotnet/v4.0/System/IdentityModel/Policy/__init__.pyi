from typing import Tuple, Set, Iterable, List


class IAuthorizationPolicy:
    def Evaluate(self, evaluationContext: EvaluationContext, state: Object) -> Tuple[bool, Object]: ...
    @property
    def Issuer(self) -> ClaimSet: ...
