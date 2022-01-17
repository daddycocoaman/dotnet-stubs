from typing import Tuple, Set, Iterable, List


class PrincipalExtensions(Object):
    def FindFirstValue(principal: ClaimsPrincipal, claimType: str) -> str: ...
