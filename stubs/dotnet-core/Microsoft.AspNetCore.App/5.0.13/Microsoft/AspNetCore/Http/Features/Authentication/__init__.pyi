from typing import Tuple, Set, Iterable, List


class IHttpAuthenticationFeature:
    @property
    def User(self) -> ClaimsPrincipal: ...
    @User.setter
    def User(self, value: ClaimsPrincipal) -> None: ...
