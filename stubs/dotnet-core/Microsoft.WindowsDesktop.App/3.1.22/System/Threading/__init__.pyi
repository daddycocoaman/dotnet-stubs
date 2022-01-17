from typing import Tuple, Set, Iterable, List


class ThreadingAclExtensions(Object):
    @overload
    def GetAccessControl(handle: EventWaitHandle) -> EventWaitHandleSecurity: ...
    @overload
    def GetAccessControl(mutex: Mutex) -> MutexSecurity: ...
    @overload
    def GetAccessControl(semaphore: Semaphore) -> SemaphoreSecurity: ...
    @overload
    def SetAccessControl(handle: EventWaitHandle, eventSecurity: EventWaitHandleSecurity) -> None: ...
    @overload
    def SetAccessControl(mutex: Mutex, mutexSecurity: MutexSecurity) -> None: ...
    @overload
    def SetAccessControl(semaphore: Semaphore, semaphoreSecurity: SemaphoreSecurity) -> None: ...
