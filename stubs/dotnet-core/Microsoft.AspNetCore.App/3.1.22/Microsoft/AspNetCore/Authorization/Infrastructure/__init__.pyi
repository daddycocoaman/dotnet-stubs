from typing import Tuple, Set, Iterable, List


class AssertionRequirement:
    @overload
    def __init__(self, handler: Func): ...
    @overload
    def __init__(self, handler: Func): ...
    @property
    def Handler(self) -> Func: ...
    def HandleAsync(self, context: AuthorizationHandlerContext) -> Task: ...


class ClaimsAuthorizationRequirement:
    def __init__(self, claimType: str, allowedValues: Iterable[str]): ...
    @property
    def AllowedValues(self) -> Iterable[str]: ...
    @property
    def ClaimType(self) -> str: ...


class DenyAnonymousAuthorizationRequirement:
    def __init__(self): ...


class NameAuthorizationRequirement:
    def __init__(self, requiredName: str): ...
    @property
    def RequiredName(self) -> str: ...


class OperationAuthorizationRequirement:
    def __init__(self): ...
    @property
    def Name(self) -> str: ...
    @Name.setter
    def Name(self, value: str) -> None: ...


class PassThroughAuthorizationHandler:
    def __init__(self): ...
    def HandleAsync(self, context: AuthorizationHandlerContext) -> Task: ...


class RolesAuthorizationRequirement:
    def __init__(self, allowedRoles: Iterable[str]): ...
    @property
    def AllowedRoles(self) -> Iterable[str]: ...
