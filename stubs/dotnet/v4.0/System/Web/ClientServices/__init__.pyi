__all__ = ['Providers','Providers','Providers','Providers','Providers','Providers','Providers','Providers']
from typing import Tuple, Set, Iterable, List


class ClientFormsIdentity(Object):
    def __init__(self, name: str, password: str, provider: MembershipProvider, authenticationType: str, isAuthenticated: bool, authenticationCookies: CookieContainer): ...
    def Dispose(self) -> None: ...
    @property
    def AuthenticationCookies(self) -> CookieContainer: ...
    @property
    def AuthenticationType(self) -> str: ...
    @property
    def IsAuthenticated(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def Provider(self) -> MembershipProvider: ...
    def RevalidateUser(self) -> None: ...
