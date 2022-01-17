__all__ = ['Features']
from typing import Tuple, Set, Iterable, List


class CookieOptions:
    def __init__(self): ...
    @property
    def Domain(self) -> str: ...
    @property
    def Expires(self) -> Nullable: ...
    @property
    def HttpOnly(self) -> bool: ...
    @property
    def IsEssential(self) -> bool: ...
    @property
    def MaxAge(self) -> Nullable: ...
    @property
    def Path(self) -> str: ...
    @property
    def SameSite(self) -> SameSiteMode: ...
    @property
    def Secure(self) -> bool: ...
    @Domain.setter
    def Domain(self, value: str) -> None: ...
    @Expires.setter
    def Expires(self, value: Nullable) -> None: ...
    @HttpOnly.setter
    def HttpOnly(self, value: bool) -> None: ...
    @IsEssential.setter
    def IsEssential(self, value: bool) -> None: ...
    @MaxAge.setter
    def MaxAge(self, value: Nullable) -> None: ...
    @Path.setter
    def Path(self, value: str) -> None: ...
    @SameSite.setter
    def SameSite(self, value: SameSiteMode) -> None: ...
    @Secure.setter
    def Secure(self, value: bool) -> None: ...


class IFormCollection:
    def ContainsKey(self, key: str) -> bool: ...
    @property
    def Count(self) -> int: ...
    @property
    def Files(self) -> IFormFileCollection: ...
    @property
    def Item(self, key: str) -> StringValues: ...
    @property
    def Keys(self) -> ICollection: ...
    def TryGetValue(self, key: str) -> Tuple[bool, StringValues]: ...


class IFormFile:
    def CopyTo(self, target: Stream) -> None: ...
    def CopyToAsync(self, target: Stream, cancellationToken: CancellationToken) -> Task: ...
    @property
    def ContentDisposition(self) -> str: ...
    @property
    def ContentType(self) -> str: ...
    @property
    def FileName(self) -> str: ...
    @property
    def Headers(self) -> IHeaderDictionary: ...
    @property
    def Length(self) -> Int64: ...
    @property
    def Name(self) -> str: ...
    def OpenReadStream(self) -> Stream: ...


class IFormFileCollection:
    @property
    def Item(self, name: str) -> IFormFile: ...
    def GetFile(self, name: str) -> IFormFile: ...
    def GetFiles(self, name: str) -> IReadOnlyList: ...


class IHeaderDictionary:
    @property
    def ContentLength(self) -> Nullable: ...
    @property
    def Item(self, key: str) -> StringValues: ...
    @ContentLength.setter
    def ContentLength(self, value: Nullable) -> None: ...
    @Item.setter
    def Item(self, key: str, value: StringValues) -> None: ...


class IQueryCollection:
    def ContainsKey(self, key: str) -> bool: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, key: str) -> StringValues: ...
    @property
    def Keys(self) -> ICollection: ...
    def TryGetValue(self, key: str) -> Tuple[bool, StringValues]: ...


class IRequestCookieCollection:
    def ContainsKey(self, key: str) -> bool: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, key: str) -> str: ...
    @property
    def Keys(self) -> ICollection: ...
    def TryGetValue(self, key: str) -> Tuple[bool, str]: ...


class IResponseCookies:
    @overload
    def Append(self, key: str, value: str) -> None: ...
    @overload
    def Append(self, key: str, value: str, options: CookieOptions) -> None: ...
    @overload
    def Delete(self, key: str) -> None: ...
    @overload
    def Delete(self, key: str, options: CookieOptions) -> None: ...


class ISession:
    def Clear(self) -> None: ...
    def CommitAsync(self, cancellationToken: CancellationToken) -> Task: ...
    @property
    def Id(self) -> str: ...
    @property
    def IsAvailable(self) -> bool: ...
    @property
    def Keys(self) -> Iterable[str]: ...
    def LoadAsync(self, cancellationToken: CancellationToken) -> Task: ...
    def Remove(self, key: str) -> None: ...
    def Set(self, key: str, value: Set(Byte)) -> None: ...
    def TryGetValue(self, key: str) -> Tuple[bool, Set(Byte)]: ...


class SameSiteMode:
    #None = 0
    Lax = 1
    Strict = 2
    Unspecified = -1


class WebSocketAcceptContext:
    def __init__(self): ...
    @property
    def SubProtocol(self) -> str: ...
    @SubProtocol.setter
    def SubProtocol(self, value: str) -> None: ...
