__all__ = ['Implementation']
from typing import Tuple, Set, Iterable, List


class Sql2000Provider(SqlProvider):
    def __init__(self): ...


class Sql2005Provider(SqlProvider):
    def __init__(self): ...


class Sql2008Provider(SqlProvider):
    def __init__(self): ...


class SqlHelpers(Object):
    def GetStringContainsPattern(text: str, escape: Char) -> str: ...
    def GetStringEndsWithPattern(text: str, escape: Char) -> str: ...
    def GetStringStartsWithPattern(text: str, escape: Char) -> str: ...
    def TranslateVBLikePattern(pattern: str, escape: Char) -> str: ...


class SqlMethods(Object):
    @overload
    def DateDiffDay(startDate: Nullable, endDate: Nullable) -> Nullable: ...
    @overload
    def DateDiffDay(startDate: DateTime, endDate: DateTime) -> int: ...
    @overload
    def DateDiffDay(startDate: Nullable, endDate: Nullable) -> Nullable: ...
    @overload
    def DateDiffDay(startDate: DateTimeOffset, endDate: DateTimeOffset) -> int: ...
    @overload
    def DateDiffHour(startDate: Nullable, endDate: Nullable) -> Nullable: ...
    @overload
    def DateDiffHour(startDate: DateTimeOffset, endDate: DateTimeOffset) -> int: ...
    @overload
    def DateDiffHour(startDate: Nullable, endDate: Nullable) -> Nullable: ...
    @overload
    def DateDiffHour(startDate: DateTime, endDate: DateTime) -> int: ...
    @overload
    def DateDiffMicrosecond(startDate: Nullable, endDate: Nullable) -> Nullable: ...
    @overload
    def DateDiffMicrosecond(startDate: DateTime, endDate: DateTime) -> int: ...
    @overload
    def DateDiffMicrosecond(startDate: DateTimeOffset, endDate: DateTimeOffset) -> int: ...
    @overload
    def DateDiffMicrosecond(startDate: Nullable, endDate: Nullable) -> Nullable: ...
    @overload
    def DateDiffMillisecond(startDate: DateTime, endDate: DateTime) -> int: ...
    @overload
    def DateDiffMillisecond(startDate: Nullable, endDate: Nullable) -> Nullable: ...
    @overload
    def DateDiffMillisecond(startDate: DateTimeOffset, endDate: DateTimeOffset) -> int: ...
    @overload
    def DateDiffMillisecond(startDate: Nullable, endDate: Nullable) -> Nullable: ...
    @overload
    def DateDiffMinute(startDate: DateTime, endDate: DateTime) -> int: ...
    @overload
    def DateDiffMinute(startDate: Nullable, endDate: Nullable) -> Nullable: ...
    @overload
    def DateDiffMinute(startDate: DateTimeOffset, endDate: DateTimeOffset) -> int: ...
    @overload
    def DateDiffMinute(startDate: Nullable, endDate: Nullable) -> Nullable: ...
    @overload
    def DateDiffMonth(startDate: DateTimeOffset, endDate: DateTimeOffset) -> int: ...
    @overload
    def DateDiffMonth(startDate: Nullable, endDate: Nullable) -> Nullable: ...
    @overload
    def DateDiffMonth(startDate: DateTime, endDate: DateTime) -> int: ...
    @overload
    def DateDiffMonth(startDate: Nullable, endDate: Nullable) -> Nullable: ...
    @overload
    def DateDiffNanosecond(startDate: Nullable, endDate: Nullable) -> Nullable: ...
    @overload
    def DateDiffNanosecond(startDate: DateTime, endDate: DateTime) -> int: ...
    @overload
    def DateDiffNanosecond(startDate: Nullable, endDate: Nullable) -> Nullable: ...
    @overload
    def DateDiffNanosecond(startDate: DateTimeOffset, endDate: DateTimeOffset) -> int: ...
    @overload
    def DateDiffSecond(startDate: Nullable, endDate: Nullable) -> Nullable: ...
    @overload
    def DateDiffSecond(startDate: DateTimeOffset, endDate: DateTimeOffset) -> int: ...
    @overload
    def DateDiffSecond(startDate: Nullable, endDate: Nullable) -> Nullable: ...
    @overload
    def DateDiffSecond(startDate: DateTime, endDate: DateTime) -> int: ...
    @overload
    def DateDiffYear(startDate: DateTime, endDate: DateTime) -> int: ...
    @overload
    def DateDiffYear(startDate: Nullable, endDate: Nullable) -> Nullable: ...
    @overload
    def DateDiffYear(startDate: DateTimeOffset, endDate: DateTimeOffset) -> int: ...
    @overload
    def DateDiffYear(startDate: Nullable, endDate: Nullable) -> Nullable: ...
    @overload
    def Like(matchExpression: str, pattern: str) -> bool: ...
    @overload
    def Like(matchExpression: str, pattern: str, escapeCharacter: Char) -> bool: ...


class SqlProvider(Object):
    def __init__(self): ...
    def Dispose(self) -> None: ...
