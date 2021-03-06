from typing import Tuple, Set, Iterable, List


class AllowAnonymousFilter:
    def __init__(self): ...


class AuthorizeFilter:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, policy: AuthorizationPolicy): ...
    @overload
    def __init__(self, authorizeData: Iterable[IAuthorizeData]): ...
    @overload
    def __init__(self, policy: str): ...
    @overload
    def __init__(self, policyProvider: IAuthorizationPolicyProvider, authorizeData: Iterable[IAuthorizeData]): ...
    @property
    def AuthorizeData(self) -> Iterable[IAuthorizeData]: ...
    @property
    def Policy(self) -> AuthorizationPolicy: ...
    @property
    def PolicyProvider(self) -> IAuthorizationPolicyProvider: ...
    def OnAuthorizationAsync(self, context: AuthorizationFilterContext) -> Task: ...
