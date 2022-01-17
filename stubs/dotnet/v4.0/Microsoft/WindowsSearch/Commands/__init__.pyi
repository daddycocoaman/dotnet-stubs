from typing import Tuple, Set, Iterable, List


class ComIServiceProvider:
    def QueryService(self, guidService: Guid, riid: Guid) -> Tuple[Guid, Guid, Object]: ...
