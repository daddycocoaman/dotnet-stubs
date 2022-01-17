from typing import Tuple, Set, Iterable, List


class ZapPackage(PackageBase):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, appmgmtObject: ManagementObject, server: str): ...
    @overload
    def __init__(self, dsPackage: DirectoryEntry, server: str): ...
