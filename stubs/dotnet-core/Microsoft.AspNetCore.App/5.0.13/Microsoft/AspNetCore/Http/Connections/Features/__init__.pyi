from typing import Tuple, Set, Iterable, List


class IHttpTransportFeature:
    @property
    def TransportType(self) -> HttpTransportType: ...
