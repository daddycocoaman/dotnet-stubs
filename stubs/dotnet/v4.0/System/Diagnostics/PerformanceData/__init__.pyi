from typing import Tuple, Set, Iterable, List


class CounterData(Object):
    def Decrement(self) -> None: ...
    @property
    def RawValue(self) -> Int64: ...
    @property
    def Value(self) -> Int64: ...
    def Increment(self) -> None: ...
    def IncrementBy(self, value: Int64) -> None: ...
    @RawValue.setter
    def RawValue(self, value: Int64) -> None: ...
    @Value.setter
    def Value(self, value: Int64) -> None: ...


class CounterSet(Object):
    def __init__(self, providerGuid: Guid, counterSetGuid: Guid, instanceType: CounterSetInstanceType): ...
    @overload
    def AddCounter(self, counterId: int, counterType: CounterType) -> None: ...
    @overload
    def AddCounter(self, counterId: int, counterType: CounterType, counterName: str) -> None: ...
    def CreateCounterSetInstance(self, instanceName: str) -> CounterSetInstance: ...
    def Dispose(self) -> None: ...


class CounterSetInstance(Object):
    def Dispose(self) -> None: ...
    @property
    def Counters(self) -> CounterSetInstanceCounterDataSet: ...


class CounterSetInstanceCounterDataSet(Object):
    def Dispose(self) -> None: ...
    @property
    def Item(self, counterId: int) -> CounterData: ...
    @property
    def Item(self, counterName: str) -> CounterData: ...


class CounterSetInstanceType:
    Single = 0
    Multiple = 2
    GlobalAggregate = 4
    MultipleAggregate = 6
    GlobalAggregateWithHistory = 11
    InstanceAggregate = 22


class CounterType:
    RawDataHex32 = 0
    RawDataHex64 = 256
    RawData32 = 65536
    RawData64 = 65792
    Delta32 = 4195328
    Delta64 = 4195584
    SampleCounter = 4260864
    QueueLength = 4523008
    LargeQueueLength = 4523264
    QueueLength100Ns = 5571840
    QueueLengthObjectTime = 6620416
    RateOfCountPerSecond32 = 272696320
    RateOfCountPerSecond64 = 272696576
    RawFraction32 = 537003008
    RawFraction64 = 537003264
    PercentageActive = 541132032
    PrecisionSystemTimer = 541525248
    PercentageActive100Ns = 542180608
    PrecisionTimer100Ns = 542573824
    ObjectSpecificTimer = 543229184
    PrecisionObjectSpecificTimer = 543622400
    SampleFraction = 549585920
    PercentageNotActive = 557909248
    PercentageNotActive100Ns = 558957824
    MultiTimerPercentageActive = 574686464
    MultiTimerPercentageActive100Ns = 575735040
    MultiTimerPercentageNotActive = 591463680
    MultiTimerPercentageNotActive100Ns = 592512256
    AverageTimer32 = 805438464
    ElapsedTime = 807666944
    AverageCount64 = 1073874176
    SampleBase = 1073939457
    AverageBase = 1073939458
    RawBase32 = 1073939459
    RawBase64 = 1073939712
    MultiTimerBase = 1107494144
