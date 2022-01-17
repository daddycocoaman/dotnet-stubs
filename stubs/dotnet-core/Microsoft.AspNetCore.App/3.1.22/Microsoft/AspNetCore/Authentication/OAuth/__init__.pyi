__all__ = ['Claims','Claims','Claims','Claims','Claims','Claims','Claims']
from typing import Tuple, Set, Iterable, List


class OAuthTokenResponse:
    def Dispose(self) -> None: ...
    def Failed(error: Exception) -> OAuthTokenResponse: ...
    @property
    def AccessToken(self) -> str: ...
    @property
    def Error(self) -> Exception: ...
    @property
    def ExpiresIn(self) -> str: ...
    @property
    def RefreshToken(self) -> str: ...
    @property
    def Response(self) -> JsonDocument: ...
    @property
    def TokenType(self) -> str: ...
    @AccessToken.setter
    def AccessToken(self, value: str) -> None: ...
    @Error.setter
    def Error(self, value: Exception) -> None: ...
    @ExpiresIn.setter
    def ExpiresIn(self, value: str) -> None: ...
    @RefreshToken.setter
    def RefreshToken(self, value: str) -> None: ...
    @Response.setter
    def Response(self, value: JsonDocument) -> None: ...
    @TokenType.setter
    def TokenType(self, value: str) -> None: ...
    def Success(response: JsonDocument) -> OAuthTokenResponse: ...
