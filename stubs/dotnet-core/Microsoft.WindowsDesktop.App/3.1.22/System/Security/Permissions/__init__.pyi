from typing import Tuple, Set, Iterable, List


class ZoneIdentityPermissionAttribute(CodeAccessSecurityAttribute):
    def __init__(self, action: SecurityAction): ...
    def CreatePermission(self) -> IPermission: ...
    @property
    def Zone(self) -> SecurityZone: ...
    @Zone.setter
    def Zone(self, value: SecurityZone) -> None: ...
