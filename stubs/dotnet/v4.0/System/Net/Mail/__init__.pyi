from typing import Tuple, Set, Iterable, List


class SmtpPermission(CodeAccessPermission):
    @overload
    def __init__(self, state: PermissionState): ...
    @overload
    def __init__(self, unrestricted: bool): ...
    @overload
    def __init__(self, access: SmtpAccess): ...
    def AddPermission(self, access: SmtpAccess) -> None: ...
    def Copy(self) -> IPermission: ...
    def FromXml(self, securityElement: SecurityElement) -> None: ...
    @property
    def Access(self) -> SmtpAccess: ...
    def Intersect(self, target: IPermission) -> IPermission: ...
    def IsSubsetOf(self, target: IPermission) -> bool: ...
    def IsUnrestricted(self) -> bool: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, target: IPermission) -> IPermission: ...