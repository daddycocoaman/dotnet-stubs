from typing import Tuple, Set, Iterable, List








































class ImmutableArray(Object):
    @overload
    def BinarySearch(array: ImmutableArray, value: T) -> int: ...
    @overload
    def BinarySearch(array: ImmutableArray, value: T, comparer: IComparer) -> int: ...
    @overload
    def BinarySearch(array: ImmutableArray, index: int, length: int, value: T) -> int: ...
    @overload
    def BinarySearch(array: ImmutableArray, index: int, length: int, value: T, comparer: IComparer) -> int: ...
    @overload
    def Create() -> ImmutableArray: ...
    @overload
    def Create(items: Set(T)) -> ImmutableArray: ...
    @overload
    def Create(item: T) -> ImmutableArray: ...
    @overload
    def Create(item1: T, item2: T) -> ImmutableArray: ...
    @overload
    def Create(items: Set(T), start: int, length: int) -> ImmutableArray: ...
    @overload
    def Create(item1: T, item2: T, item3: T) -> ImmutableArray: ...
    @overload
    def Create(items: ImmutableArray, start: int, length: int) -> ImmutableArray: ...
    @overload
    def Create(item1: T, item2: T, item3: T, item4: T) -> ImmutableArray: ...
    @overload
    def CreateBuilder() -> Builder: ...
    @overload
    def CreateBuilder(initialCapacity: int) -> Builder: ...
    @overload
    def CreateRange(items: Iterable[T]) -> ImmutableArray: ...
    @overload
    def CreateRange(items: ImmutableArray, selector: Func) -> ImmutableArray: ...
    @overload
    def CreateRange(items: ImmutableArray, selector: Func`3, arg: TArg) -> ImmutableArray: ...
    @overload
    def CreateRange(items: ImmutableArray, start: int, length: int, selector: Func) -> ImmutableArray: ...
    @overload
    def CreateRange(items: ImmutableArray, start: int, length: int, selector: Func`3, arg: TArg) -> ImmutableArray: ...
    @overload
    def ToImmutableArray(items: Iterable[TSource]) -> ImmutableArray: ...
    @overload
    def ToImmutableArray(builder: Builder) -> ImmutableArray: ...




class ImmutableDictionary(Object):
    def Contains(map: IImmutableDictionary, key: TKey, value: TValue) -> bool: ...
    @overload
    def Create() -> ImmutableDictionary: ...
    @overload
    def Create(keyComparer: IEqualityComparer) -> ImmutableDictionary: ...
    @overload
    def Create(keyComparer: IEqualityComparer, valueComparer: IEqualityComparer) -> ImmutableDictionary: ...
    @overload
    def CreateBuilder() -> Builder: ...
    @overload
    def CreateBuilder(keyComparer: IEqualityComparer) -> Builder: ...
    @overload
    def CreateBuilder(keyComparer: IEqualityComparer, valueComparer: IEqualityComparer) -> Builder: ...
    @overload
    def CreateRange(items: Iterable[KeyValuePair]) -> ImmutableDictionary: ...
    @overload
    def CreateRange(keyComparer: IEqualityComparer, items: Iterable[KeyValuePair]) -> ImmutableDictionary: ...
    @overload
    def CreateRange(keyComparer: IEqualityComparer, valueComparer: IEqualityComparer, items: Iterable[KeyValuePair]) -> ImmutableDictionary: ...
    @overload
    def GetValueOrDefault(dictionary: IImmutableDictionary, key: TKey) -> TValue: ...
    @overload
    def GetValueOrDefault(dictionary: IImmutableDictionary, key: TKey, defaultValue: TValue) -> TValue: ...
    @overload
    def ToImmutableDictionary(builder: Builder) -> ImmutableDictionary: ...
    @overload
    def ToImmutableDictionary(source: Iterable[KeyValuePair]) -> ImmutableDictionary: ...
    @overload
    def ToImmutableDictionary(source: Iterable[KeyValuePair], keyComparer: IEqualityComparer) -> ImmutableDictionary: ...
    @overload
    def ToImmutableDictionary(source: Iterable[TSource], keySelector: Func) -> ImmutableDictionary: ...
    @overload
    def ToImmutableDictionary(source: Iterable[TSource], keySelector: Func, keyComparer: IEqualityComparer) -> ImmutableDictionary: ...
    @overload
    def ToImmutableDictionary(source: Iterable[TSource], keySelector: Func, elementSelector: Func) -> ImmutableDictionary: ...
    @overload
    def ToImmutableDictionary(source: Iterable[KeyValuePair], keyComparer: IEqualityComparer, valueComparer: IEqualityComparer) -> ImmutableDictionary: ...
    @overload
    def ToImmutableDictionary(source: Iterable[TSource], keySelector: Func, elementSelector: Func, keyComparer: IEqualityComparer) -> ImmutableDictionary: ...
    @overload
    def ToImmutableDictionary(source: Iterable[TSource], keySelector: Func, elementSelector: Func, keyComparer: IEqualityComparer, valueComparer: IEqualityComparer) -> ImmutableDictionary: ...




class ImmutableHashSet(Object):
    @overload
    def Create() -> ImmutableHashSet: ...
    @overload
    def Create(equalityComparer: IEqualityComparer) -> ImmutableHashSet: ...
    @overload
    def Create(item: T) -> ImmutableHashSet: ...
    @overload
    def Create(items: Set(T)) -> ImmutableHashSet: ...
    @overload
    def Create(equalityComparer: IEqualityComparer, item: T) -> ImmutableHashSet: ...
    @overload
    def Create(equalityComparer: IEqualityComparer, items: Set(T)) -> ImmutableHashSet: ...
    @overload
    def CreateBuilder() -> Builder: ...
    @overload
    def CreateBuilder(equalityComparer: IEqualityComparer) -> Builder: ...
    @overload
    def CreateRange(items: Iterable[T]) -> ImmutableHashSet: ...
    @overload
    def CreateRange(equalityComparer: IEqualityComparer, items: Iterable[T]) -> ImmutableHashSet: ...
    @overload
    def ToImmutableHashSet(builder: Builder) -> ImmutableHashSet: ...
    @overload
    def ToImmutableHashSet(source: Iterable[TSource]) -> ImmutableHashSet: ...
    @overload
    def ToImmutableHashSet(source: Iterable[TSource], equalityComparer: IEqualityComparer) -> ImmutableHashSet: ...




class ImmutableInterlocked(Object):
    @overload
    def AddOrUpdate(location: ImmutableDictionary, key: TKey, addValue: TValue, updateValueFactory: Func`3) -> Tuple[TValue, ImmutableDictionary]: ...
    @overload
    def AddOrUpdate(location: ImmutableDictionary, key: TKey, addValueFactory: Func, updateValueFactory: Func`3) -> Tuple[TValue, ImmutableDictionary]: ...
    def Enqueue(location: ImmutableQueue, value: T) -> Tuple[ImmutableQueue]: ...
    @overload
    def GetOrAdd(location: ImmutableDictionary, key: TKey, valueFactory: Func) -> Tuple[TValue, ImmutableDictionary]: ...
    @overload
    def GetOrAdd(location: ImmutableDictionary, key: TKey, value: TValue) -> Tuple[TValue, ImmutableDictionary]: ...
    @overload
    def GetOrAdd(location: ImmutableDictionary, key: TKey, valueFactory: Func`3, factoryArgument: TArg) -> Tuple[TValue, ImmutableDictionary]: ...
    def InterlockedCompareExchange(location: ImmutableArray, value: ImmutableArray, comparand: ImmutableArray) -> Tuple[ImmutableArray, ImmutableArray]: ...
    def InterlockedExchange(location: ImmutableArray, value: ImmutableArray) -> Tuple[ImmutableArray, ImmutableArray]: ...
    def InterlockedInitialize(location: ImmutableArray, value: ImmutableArray) -> Tuple[bool, ImmutableArray]: ...
    def Push(location: ImmutableStack, value: T) -> Tuple[ImmutableStack]: ...
    def TryAdd(location: ImmutableDictionary, key: TKey, value: TValue) -> Tuple[bool, ImmutableDictionary]: ...
    def TryDequeue(location: ImmutableQueue) -> Tuple[bool, ImmutableQueue, T]: ...
    def TryPop(location: ImmutableStack) -> Tuple[bool, ImmutableStack, T]: ...
    def TryRemove(location: ImmutableDictionary, key: TKey) -> Tuple[bool, ImmutableDictionary, TValue]: ...
    def TryUpdate(location: ImmutableDictionary, key: TKey, newValue: TValue, comparisonValue: TValue) -> Tuple[bool, ImmutableDictionary]: ...
    @overload
    def Update(location: ImmutableArray, transformer: Func) -> Tuple[bool, ImmutableArray]: ...
    @overload
    def Update(location: T, transformer: Func) -> Tuple[bool, T]: ...
    @overload
    def Update(location: ImmutableArray, transformer: Func`3, transformerArgument: TArg) -> Tuple[bool, ImmutableArray]: ...
    @overload
    def Update(location: T, transformer: Func`3, transformerArgument: TArg) -> Tuple[bool, T]: ...


class ImmutableList(Object):
    @overload
    def Create() -> ImmutableList: ...
    @overload
    def Create(item: T) -> ImmutableList: ...
    @overload
    def Create(items: Set(T)) -> ImmutableList: ...
    def CreateBuilder() -> Builder: ...
    def CreateRange(items: Iterable[T]) -> ImmutableList: ...
    @overload
    def IndexOf(list: IImmutableList, item: T) -> int: ...
    @overload
    def IndexOf(list: IImmutableList, item: T, equalityComparer: IEqualityComparer) -> int: ...
    @overload
    def IndexOf(list: IImmutableList, item: T, startIndex: int) -> int: ...
    @overload
    def IndexOf(list: IImmutableList, item: T, startIndex: int, count: int) -> int: ...
    @overload
    def LastIndexOf(list: IImmutableList, item: T) -> int: ...
    @overload
    def LastIndexOf(list: IImmutableList, item: T, equalityComparer: IEqualityComparer) -> int: ...
    @overload
    def LastIndexOf(list: IImmutableList, item: T, startIndex: int) -> int: ...
    @overload
    def LastIndexOf(list: IImmutableList, item: T, startIndex: int, count: int) -> int: ...
    def Remove(list: IImmutableList, value: T) -> IImmutableList: ...
    def RemoveRange(list: IImmutableList, items: Iterable[T]) -> IImmutableList: ...
    def Replace(list: IImmutableList, oldValue: T, newValue: T) -> IImmutableList: ...
    @overload
    def ToImmutableList(source: Iterable[TSource]) -> ImmutableList: ...
    @overload
    def ToImmutableList(builder: Builder) -> ImmutableList: ...




class ImmutableQueue(Object):
    @overload
    def Create() -> ImmutableQueue: ...
    @overload
    def Create(item: T) -> ImmutableQueue: ...
    @overload
    def Create(items: Set(T)) -> ImmutableQueue: ...
    def CreateRange(items: Iterable[T]) -> ImmutableQueue: ...
    def Dequeue(queue: IImmutableQueue) -> Tuple[IImmutableQueue, T]: ...




class ImmutableSortedDictionary(Object):
    @overload
    def Create() -> ImmutableSortedDictionary: ...
    @overload
    def Create(keyComparer: IComparer) -> ImmutableSortedDictionary: ...
    @overload
    def Create(keyComparer: IComparer, valueComparer: IEqualityComparer) -> ImmutableSortedDictionary: ...
    @overload
    def CreateBuilder() -> Builder: ...
    @overload
    def CreateBuilder(keyComparer: IComparer) -> Builder: ...
    @overload
    def CreateBuilder(keyComparer: IComparer, valueComparer: IEqualityComparer) -> Builder: ...
    @overload
    def CreateRange(items: Iterable[KeyValuePair]) -> ImmutableSortedDictionary: ...
    @overload
    def CreateRange(keyComparer: IComparer, items: Iterable[KeyValuePair]) -> ImmutableSortedDictionary: ...
    @overload
    def CreateRange(keyComparer: IComparer, valueComparer: IEqualityComparer, items: Iterable[KeyValuePair]) -> ImmutableSortedDictionary: ...
    @overload
    def ToImmutableSortedDictionary(source: Iterable[KeyValuePair]) -> ImmutableSortedDictionary: ...
    @overload
    def ToImmutableSortedDictionary(builder: Builder) -> ImmutableSortedDictionary: ...
    @overload
    def ToImmutableSortedDictionary(source: Iterable[KeyValuePair], keyComparer: IComparer) -> ImmutableSortedDictionary: ...
    @overload
    def ToImmutableSortedDictionary(source: Iterable[TSource], keySelector: Func, elementSelector: Func) -> ImmutableSortedDictionary: ...
    @overload
    def ToImmutableSortedDictionary(source: Iterable[KeyValuePair], keyComparer: IComparer, valueComparer: IEqualityComparer) -> ImmutableSortedDictionary: ...
    @overload
    def ToImmutableSortedDictionary(source: Iterable[TSource], keySelector: Func, elementSelector: Func, keyComparer: IComparer) -> ImmutableSortedDictionary: ...
    @overload
    def ToImmutableSortedDictionary(source: Iterable[TSource], keySelector: Func, elementSelector: Func, keyComparer: IComparer, valueComparer: IEqualityComparer) -> ImmutableSortedDictionary: ...




class ImmutableSortedSet(Object):
    @overload
    def Create() -> ImmutableSortedSet: ...
    @overload
    def Create(comparer: IComparer) -> ImmutableSortedSet: ...
    @overload
    def Create(item: T) -> ImmutableSortedSet: ...
    @overload
    def Create(items: Set(T)) -> ImmutableSortedSet: ...
    @overload
    def Create(comparer: IComparer, item: T) -> ImmutableSortedSet: ...
    @overload
    def Create(comparer: IComparer, items: Set(T)) -> ImmutableSortedSet: ...
    @overload
    def CreateBuilder() -> Builder: ...
    @overload
    def CreateBuilder(comparer: IComparer) -> Builder: ...
    @overload
    def CreateRange(items: Iterable[T]) -> ImmutableSortedSet: ...
    @overload
    def CreateRange(comparer: IComparer, items: Iterable[T]) -> ImmutableSortedSet: ...
    @overload
    def ToImmutableSortedSet(source: Iterable[TSource]) -> ImmutableSortedSet: ...
    @overload
    def ToImmutableSortedSet(builder: Builder) -> ImmutableSortedSet: ...
    @overload
    def ToImmutableSortedSet(source: Iterable[TSource], comparer: IComparer) -> ImmutableSortedSet: ...




class ImmutableStack(Object):
    @overload
    def Create() -> ImmutableStack: ...
    @overload
    def Create(item: T) -> ImmutableStack: ...
    @overload
    def Create(items: Set(T)) -> ImmutableStack: ...
    def CreateRange(items: Iterable[T]) -> ImmutableStack: ...
    def Pop(stack: IImmutableStack) -> Tuple[IImmutableStack, T]: ...


