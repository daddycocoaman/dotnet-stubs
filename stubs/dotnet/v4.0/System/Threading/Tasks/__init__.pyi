from typing import Tuple, Set, Iterable, List


class TaskExtensions(Object):
    @overload
    def Unwrap(task: Task) -> Task: ...
    @overload
    def Unwrap(task: Task) -> Task: ...
