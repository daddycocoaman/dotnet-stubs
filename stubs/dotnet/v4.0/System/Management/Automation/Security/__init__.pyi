from typing import Tuple, Set, Iterable, List


class SystemEnforcementMode:
    #None = 0
    Audit = 1
    Enforce = 2


class SystemPolicy(Object):
    def GetLockdownPolicy(path: str, handle: SafeHandle) -> SystemEnforcementMode: ...
    def GetSystemLockdownPolicy() -> SystemEnforcementMode: ...
