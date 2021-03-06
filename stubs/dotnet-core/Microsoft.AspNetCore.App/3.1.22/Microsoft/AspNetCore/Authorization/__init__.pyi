from typing import Tuple, Set, Iterable, List


class IAllowAnonymous:
    pass


class IAuthorizeData:
    @property
    def AuthenticationSchemes(self) -> str: ...
    @property
    def Policy(self) -> str: ...
    @property
    def Roles(self) -> str: ...
    @AuthenticationSchemes.setter
    def AuthenticationSchemes(self, value: str) -> None: ...
    @Policy.setter
    def Policy(self, value: str) -> None: ...
    @Roles.setter
    def Roles(self, value: str) -> None: ...
