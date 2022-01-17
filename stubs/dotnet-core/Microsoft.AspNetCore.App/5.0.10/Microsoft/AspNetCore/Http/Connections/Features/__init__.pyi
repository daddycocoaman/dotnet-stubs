from typing import Tuple, Set, Iterable, List


class IHttpContextFeature:
    @property
    def HttpContext(self) -> HttpContext: ...
    @HttpContext.setter
    def HttpContext(self, value: HttpContext) -> None: ...


class IHttpTransportFeature:
    @property
    def TransportType(self) -> HttpTransportType: ...
