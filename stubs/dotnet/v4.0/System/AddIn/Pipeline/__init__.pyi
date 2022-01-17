from typing import Tuple, Set, Iterable, List


class FrameworkElementAdapters(Object):
    def ContractToViewAdapter(nativeHandleContract: INativeHandleContract) -> FrameworkElement: ...
    def ViewToContractAdapter(root: FrameworkElement) -> INativeHandleContract: ...