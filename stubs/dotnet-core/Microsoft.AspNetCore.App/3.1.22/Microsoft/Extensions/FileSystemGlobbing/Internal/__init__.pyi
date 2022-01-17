__all__ = ['PathSegments','PathSegments','PathSegments','PathSegments','PathSegments','PatternContexts','PatternContexts','PatternContexts','PatternContexts','PatternContexts','PatternContexts','PatternContexts','PatternContexts','PatternContexts','Patterns']
from typing import Tuple, Set, Iterable, List


class PatternTestResult:
    @property
    def IsSuccessful(self) -> bool: ...
    @property
    def Stem(self) -> str: ...
    def Success(stem: str) -> PatternTestResult: ...
