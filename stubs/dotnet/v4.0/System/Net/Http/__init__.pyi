from typing import Tuple, Set, Iterable, List


class RtcRequestFactory(Object):
    def Create(method: HttpMethod, uri: Uri) -> HttpRequestMessage: ...
