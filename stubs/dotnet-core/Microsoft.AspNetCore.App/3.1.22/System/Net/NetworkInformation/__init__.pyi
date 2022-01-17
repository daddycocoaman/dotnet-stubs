from typing import Tuple, Set, Iterable, List


class NetworkInformationPermissionAttribute(CodeAccessSecurityAttribute):
    def __init__(self, action: SecurityAction): ...
    def CreatePermission(self) -> IPermission: ...
    @property
    def Access(self) -> str: ...
    @Access.setter
    def Access(self, value: str) -> None: ...
