from typing import Tuple, Set, Iterable, List


class DispatcherQueueHandler(MulticastDelegate):
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self) -> None: ...


class DispatcherQueuePriority:
    Normal = 0
    High = 10
    Low = -10
