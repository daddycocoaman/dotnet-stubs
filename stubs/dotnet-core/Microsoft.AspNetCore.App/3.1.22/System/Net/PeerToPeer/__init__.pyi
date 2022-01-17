__all__ = ['Collaboration','Collaboration']
from typing import Tuple, Set, Iterable, List


class PnrpPermissionAttribute(CodeAccessSecurityAttribute):
    def __init__(self, action: SecurityAction): ...
    def CreatePermission(self) -> IPermission: ...
