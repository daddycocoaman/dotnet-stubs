__all__ = ['Collaboration']
from typing import Tuple, Set, Iterable, List


class PnrpPermission(CodeAccessPermission):
    def __init__(self, state: PermissionState): ...
    def Copy(self) -> IPermission: ...
    def FromXml(self, e: SecurityElement) -> None: ...
    def Intersect(self, target: IPermission) -> IPermission: ...
    def IsSubsetOf(self, target: IPermission) -> bool: ...
    def IsUnrestricted(self) -> bool: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, target: IPermission) -> IPermission: ...


class PnrpPermissionAttribute(CodeAccessSecurityAttribute):
    def __init__(self, action: SecurityAction): ...
    def CreatePermission(self) -> IPermission: ...


class PnrpScope:
    All = 0
    Global = 1
    SiteLocal = 2
    LinkLocal = 3
