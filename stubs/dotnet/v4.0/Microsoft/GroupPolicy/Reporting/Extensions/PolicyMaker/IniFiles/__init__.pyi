from typing import Tuple, Set, Iterable, List


class IniFileGPOSetting:
    def __init__(self): ...
    def GetHashKey(self) -> str: ...
    def GetKeyComponents(self) -> Set(str): ...
