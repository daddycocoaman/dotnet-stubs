from typing import Tuple, Set, Iterable, List


class RolesAuthorizationRequirement:
    def __init__(self, allowedRoles: Iterable[str]): ...
    @property
    def AllowedRoles(self) -> Iterable[str]: ...
