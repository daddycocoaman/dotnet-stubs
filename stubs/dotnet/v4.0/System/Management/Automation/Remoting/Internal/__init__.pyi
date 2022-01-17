from typing import Tuple, Set, Iterable, List


class PSStreamObject(Object):
    def __init__(self, objectType: PSStreamObjectType, value: Object): ...
    @property
    def ObjectType(self) -> PSStreamObjectType: ...
    @ObjectType.setter
    def ObjectType(self, value: PSStreamObjectType) -> None: ...
    def WriteStreamObject(self, cmdlet: Cmdlet, overrideInquire: bool) -> None: ...


class PSStreamObjectType:
    Output = 1
    Error = 2
    MethodExecutor = 3
    Warning = 4
    BlockingError = 5
    ShouldMethod = 6
    WarningRecord = 7
    Debug = 8
    Progress = 9
    Verbose = 10
    Information = 11
    Exception = 12
