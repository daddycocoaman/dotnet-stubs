from typing import Tuple, Set, Iterable, List


class IIncrementalSearch:
    def AppendCharAndSearch(self, toAppend: Char) -> IncrementalSearchResult: ...
    def Clear(self) -> None: ...
    def DeleteCharAndSearch(self) -> IncrementalSearchResult: ...
    def Dismiss(self) -> None: ...
    @property
    def IsActive(self) -> bool: ...
    @property
    def SearchDirection(self) -> IncrementalSearchDirection: ...
    @property
    def SearchString(self) -> str: ...
    @property
    def TextView(self) -> ITextView: ...
    def SelectNextResult(self) -> IncrementalSearchResult: ...
    @SearchDirection.setter
    def SearchDirection(self, value: IncrementalSearchDirection) -> None: ...
    @SearchString.setter
    def SearchString(self, value: str) -> None: ...
    def Start(self) -> None: ...


class IIncrementalSearchFactoryService:
    def GetIncrementalSearch(self, textView: ITextView) -> IIncrementalSearch: ...


class IncrementalSearchDirection:
    Forward = 0
    Backward = 1


class IncrementalSearchResult:
    def __init__(self, passedEndOfBuffer: bool, passedStartOfBuffer: bool, passedStartOfSearch: bool, resultFound: bool): ...
    def Equals(self, obj: Object) -> bool: ...
    @property
    def PassedEndOfBuffer(self) -> bool: ...
    @property
    def PassedStartOfBuffer(self) -> bool: ...
    @property
    def PassedStartOfSearch(self) -> bool: ...
    @property
    def ResultFound(self) -> bool: ...
    def GetHashCode(self) -> int: ...
    def op_Equality(first: IncrementalSearchResult, second: IncrementalSearchResult) -> bool: ...
    def op_Inequality(first: IncrementalSearchResult, second: IncrementalSearchResult) -> bool: ...
