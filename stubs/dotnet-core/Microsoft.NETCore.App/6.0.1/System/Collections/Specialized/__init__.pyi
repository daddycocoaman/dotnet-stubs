from typing import Tuple, Set, Iterable, List


class INotifyCollectionChanged:
    def add_CollectionChanged(self, value: NotifyCollectionChangedEventHandler) -> None: ...
    def remove_CollectionChanged(self, value: NotifyCollectionChangedEventHandler) -> None: ...


class NotifyCollectionChangedAction:
    Add = 0
    Remove = 1
    Replace = 2
    Move = 3
    Reset = 4


class NotifyCollectionChangedEventArgs(EventArgs):
    @overload
    def __init__(self, action: NotifyCollectionChangedAction): ...
    @overload
    def __init__(self, action: NotifyCollectionChangedAction, changedItem: Object): ...
    @overload
    def __init__(self, action: NotifyCollectionChangedAction, changedItems: IList): ...
    @overload
    def __init__(self, action: NotifyCollectionChangedAction, changedItem: Object, index: int): ...
    @overload
    def __init__(self, action: NotifyCollectionChangedAction, changedItems: IList, startingIndex: int): ...
    @overload
    def __init__(self, action: NotifyCollectionChangedAction, newItem: Object, oldItem: Object): ...
    @overload
    def __init__(self, action: NotifyCollectionChangedAction, newItems: IList, oldItems: IList): ...
    @overload
    def __init__(self, action: NotifyCollectionChangedAction, newItem: Object, oldItem: Object, index: int): ...
    @overload
    def __init__(self, action: NotifyCollectionChangedAction, newItems: IList, oldItems: IList, startingIndex: int): ...
    @overload
    def __init__(self, action: NotifyCollectionChangedAction, changedItem: Object, index: int, oldIndex: int): ...
    @overload
    def __init__(self, action: NotifyCollectionChangedAction, changedItems: IList, index: int, oldIndex: int): ...
    @property
    def Action(self) -> NotifyCollectionChangedAction: ...
    @property
    def NewItems(self) -> IList: ...
    @property
    def NewStartingIndex(self) -> int: ...
    @property
    def OldItems(self) -> IList: ...
    @property
    def OldStartingIndex(self) -> int: ...


class NotifyCollectionChangedEventHandler(MulticastDelegate):
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, sender: Object, e: NotifyCollectionChangedEventArgs, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: Object, e: NotifyCollectionChangedEventArgs) -> None: ...
