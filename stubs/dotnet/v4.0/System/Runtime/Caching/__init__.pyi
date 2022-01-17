__all__ = ['Configuration','Configuration','Configuration','Configuration','Hosting','Hosting','Hosting']
from typing import Tuple, Set, Iterable, List


class SqlChangeMonitor(ChangeMonitor):
    def __init__(self, dependency: SqlDependency): ...
    @property
    def UniqueId(self) -> str: ...
