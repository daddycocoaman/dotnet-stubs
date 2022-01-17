__all__ = ['TraceSource']
from typing import Tuple, Set, Iterable, List


class TraceSourceFactoryExtensions:
    @overload
    def AddTraceSource(builder: ILoggingBuilder, switchName: str) -> ILoggingBuilder: ...
    @overload
    def AddTraceSource(builder: ILoggingBuilder, sourceSwitch: SourceSwitch) -> ILoggingBuilder: ...
    @overload
    def AddTraceSource(builder: ILoggingBuilder, switchName: str, listener: TraceListener) -> ILoggingBuilder: ...
    @overload
    def AddTraceSource(builder: ILoggingBuilder, sourceSwitch: SourceSwitch, listener: TraceListener) -> ILoggingBuilder: ...