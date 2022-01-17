from typing import Tuple, Set, Iterable, List


class CollectionExtensions(Object):
    @overload
    def GetValueOrDefault(dictionary: IReadOnlyDictionary, key: TKey) -> TValue: ...
    @overload
    def GetValueOrDefault(dictionary: IReadOnlyDictionary, key: TKey, defaultValue: TValue) -> TValue: ...
    def Remove(dictionary: IDictionary, key: TKey) -> Tuple[bool, TValue]: ...
    def TryAdd(dictionary: IDictionary, key: TKey, value: TValue) -> bool: ...










































