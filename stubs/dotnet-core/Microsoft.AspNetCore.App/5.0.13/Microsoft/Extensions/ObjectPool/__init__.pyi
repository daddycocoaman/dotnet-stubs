from typing import Tuple, Set, Iterable, List




class DefaultObjectPoolProvider(ObjectPoolProvider):
    def __init__(self): ...
    @overload
    def Create(self, policy: IPooledObjectPolicy) -> ObjectPool: ...
    @property
    def MaximumRetained(self) -> int: ...
    @MaximumRetained.setter
    def MaximumRetained(self, value: int) -> None: ...








class LeakTrackingObjectPoolProvider(ObjectPoolProvider):
    def __init__(self, inner: ObjectPoolProvider): ...
    @overload
    def Create(self, policy: IPooledObjectPolicy) -> ObjectPool: ...


class ObjectPool:
    def Create(policy: IPooledObjectPolicy) -> ObjectPool: ...




class ObjectPoolProvider:
    @overload
    def Create(self) -> ObjectPool: ...
    @overload
    def Create(self, policy: IPooledObjectPolicy) -> ObjectPool: ...


class ObjectPoolProviderExtensions:
    @overload
    def CreateStringBuilderPool(provider: ObjectPoolProvider) -> ObjectPool: ...
    @overload
    def CreateStringBuilderPool(provider: ObjectPoolProvider, initialCapacity: int, maximumRetainedCapacity: int) -> ObjectPool: ...




class StringBuilderPooledObjectPolicy:
    def __init__(self): ...
    def Create(self) -> StringBuilder: ...
    @property
    def InitialCapacity(self) -> int: ...
    @property
    def MaximumRetainedCapacity(self) -> int: ...
    def Return(self, obj: StringBuilder) -> bool: ...
    @InitialCapacity.setter
    def InitialCapacity(self, value: int) -> None: ...
    @MaximumRetainedCapacity.setter
    def MaximumRetainedCapacity(self, value: int) -> None: ...
