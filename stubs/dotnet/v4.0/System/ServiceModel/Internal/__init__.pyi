from typing import Tuple, Set, Iterable, List


class TransactionBridge(Object):
    def __init__(self): ...
    def Init(self, bridgeConfig: Object) -> None: ...
    def Shutdown(self) -> None: ...
    def Start(self) -> None: ...