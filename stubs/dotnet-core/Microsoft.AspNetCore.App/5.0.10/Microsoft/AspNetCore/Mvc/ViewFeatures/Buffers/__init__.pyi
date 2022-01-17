from typing import Tuple, Set, Iterable, List


class ViewBufferValue:
    @overload
    def __init__(self, value: str): ...
    @overload
    def __init__(self, content: IHtmlContent): ...
    @property
    def Value(self) -> Object: ...
