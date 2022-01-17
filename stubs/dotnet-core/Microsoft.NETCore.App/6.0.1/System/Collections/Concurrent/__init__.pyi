from typing import Tuple, Set, Iterable, List










class EnumerablePartitionerOptions:
    #None = 0
    NoBuffering = 1




class Partitioner(Object):
    @overload
    def Create(source: Iterable[TSource]) -> OrderablePartitioner: ...
    @overload
    def Create(list: IList, loadBalance: bool) -> OrderablePartitioner: ...
    @overload
    def Create(array: Set(TSource), loadBalance: bool) -> OrderablePartitioner: ...
    @overload
    def Create(source: Iterable[TSource], partitionerOptions: EnumerablePartitionerOptions) -> OrderablePartitioner: ...
    @overload
    def Create(fromInclusive: Int64, toExclusive: Int64) -> OrderablePartitioner: ...
    @overload
    def Create(fromInclusive: int, toExclusive: int) -> OrderablePartitioner: ...
    @overload
    def Create(fromInclusive: Int64, toExclusive: Int64, rangeSize: Int64) -> OrderablePartitioner: ...
    @overload
    def Create(fromInclusive: int, toExclusive: int, rangeSize: int) -> OrderablePartitioner: ...


