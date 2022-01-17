from typing import Tuple, Set, Iterable, List


class ThreadExceptionEventHandler(MulticastDelegate):
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, sender: Object, e: ThreadExceptionEventArgs, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: Object, e: ThreadExceptionEventArgs) -> None: ...
