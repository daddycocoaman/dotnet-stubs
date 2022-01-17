__all__ = ['CompilerServices']
from typing import Tuple, Set, Iterable, List


class DebugFrame:
    pass


class DebugSourceFile:
    @property
    def Mode(self) -> int: ...


class DebugThread:
    pass


class ForceToGeneratorLoopException:
    def __init__(self): ...


class FunctionInfo:
    pass


class ITraceCallback:
    def OnTraceEvent(self, kind: TraceEventKind, name: str, sourceFileName: str, sourceSpan: SourceSpan, scopeCallback: Func, payload: Object, customPayload: Object) -> None: ...


class ITracePipeline:
    def Close(self) -> None: ...
    @property
    def TraceCallback(self) -> ITraceCallback: ...
    @TraceCallback.setter
    def TraceCallback(self, value: ITraceCallback) -> None: ...
    def TrySetNextStatement(self, sourceFile: str, sourceSpan: SourceSpan) -> bool: ...


class RuntimeOps:
    pass


class TraceEventKind:
    FrameEnter = 0
    FrameExit = 1
    ThreadExit = 2
    TracePoint = 3
    Exception = 4
    ExceptionUnwind = 5


class TracePipeline:
    def Close(self) -> None: ...
    def CreateInstance(debugContext: DebugContext) -> TracePipeline: ...
    @property
    def TraceCallback(self) -> ITraceCallback: ...
    @TraceCallback.setter
    def TraceCallback(self, value: ITraceCallback) -> None: ...
    def TrySetNextStatement(self, sourceFile: str, sourceSpan: SourceSpan) -> bool: ...
