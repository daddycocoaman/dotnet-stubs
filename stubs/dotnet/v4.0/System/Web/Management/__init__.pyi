from typing import Tuple, Set, Iterable, List


class WebServiceErrorEvent(WebRequestErrorEvent):
    @property
    def WebServiceErrorEventCode() -> int: ...
