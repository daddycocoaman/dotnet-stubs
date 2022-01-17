from typing import Tuple, Set, Iterable, List


class ReaderWriterLock(CriticalFinalizerObject):
    def __init__(self): ...
    @overload
    def AcquireReaderLock(self, millisecondsTimeout: int) -> None: ...
    @overload
    def AcquireReaderLock(self, timeout: TimeSpan) -> None: ...
    @overload
    def AcquireWriterLock(self, millisecondsTimeout: int) -> None: ...
    @overload
    def AcquireWriterLock(self, timeout: TimeSpan) -> None: ...
    def AnyWritersSince(self, seqNum: int) -> bool: ...
    def DowngradeFromWriterLock(self, lockCookie: LockCookie) -> Tuple[LockCookie]: ...
    @property
    def IsReaderLockHeld(self) -> bool: ...
    @property
    def IsWriterLockHeld(self) -> bool: ...
    @property
    def WriterSeqNum(self) -> int: ...
    def ReleaseLock(self) -> LockCookie: ...
    def ReleaseReaderLock(self) -> None: ...
    def ReleaseWriterLock(self) -> None: ...
    def RestoreLock(self, lockCookie: LockCookie) -> Tuple[LockCookie]: ...
    @overload
    def UpgradeToWriterLock(self, timeout: TimeSpan) -> LockCookie: ...
    @overload
    def UpgradeToWriterLock(self, millisecondsTimeout: int) -> LockCookie: ...
