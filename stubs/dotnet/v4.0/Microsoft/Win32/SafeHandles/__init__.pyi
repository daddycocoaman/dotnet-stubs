from typing import Tuple, Set, Iterable, List


class SafeMemoryMappedFileHandle(SafeHandleZeroOrMinusOneIsInvalid):
    pass


class SafeMemoryMappedViewHandle:
    pass


class SafeNCryptHandle(SafeHandleZeroOrMinusOneIsInvalid):
    pass


class SafeNCryptKeyHandle(SafeNCryptHandle):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, handle: IntPtr, parentHandle: SafeHandle): ...


class SafeNCryptProviderHandle(SafeNCryptHandle):
    def __init__(self): ...


class SafeNCryptSecretHandle(SafeNCryptHandle):
    def __init__(self): ...


class SafePipeHandle(SafeHandleZeroOrMinusOneIsInvalid):
    def __init__(self, preexistingHandle: IntPtr, ownsHandle: bool): ...
