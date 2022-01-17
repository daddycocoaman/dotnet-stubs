__all__ = ['Spatial']
from typing import Tuple, Set, Iterable, List


class Row(Object):
    def __init__(self, columnValue: KeyValuePair, columnValues: Set(KeyValuePair)): ...
    def op_Implicit(row: Row) -> DbExpression: ...
    def ToExpression(self) -> DbNewInstanceExpression: ...