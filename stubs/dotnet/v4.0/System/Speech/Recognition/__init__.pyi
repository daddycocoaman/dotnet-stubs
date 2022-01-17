__all__ = ['SrgsGrammar','SrgsGrammar','SrgsGrammar','SrgsGrammar','SrgsGrammar','SrgsGrammar','SrgsGrammar','SrgsGrammar','SrgsGrammar','SrgsGrammar','SrgsGrammar','SrgsGrammar','SrgsGrammar','SrgsGrammar','SrgsGrammar','SrgsGrammar']
from typing import Tuple, Set, Iterable, List


class RecognizerUpdateReachedEventArgs(EventArgs):
    @property
    def AudioPosition(self) -> TimeSpan: ...
    @property
    def UserToken(self) -> Object: ...
