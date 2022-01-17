from typing import Tuple, Set, Iterable, List


class Claim(Object):
    @overload
    def __init__(self, reader: BinaryReader): ...
    @overload
    def __init__(self, reader: BinaryReader, subject: ClaimsIdentity): ...
    @overload
    def __init__(self, type: str, value: str): ...
    @overload
    def __init__(self, type: str, value: str, valueType: str): ...
    @overload
    def __init__(self, type: str, value: str, valueType: str, issuer: str): ...
    @overload
    def __init__(self, type: str, value: str, valueType: str, issuer: str, originalIssuer: str): ...
    @overload
    def __init__(self, type: str, value: str, valueType: str, issuer: str, originalIssuer: str, subject: ClaimsIdentity): ...
    @overload
    def Clone(self) -> Claim: ...
    @overload
    def Clone(self, identity: ClaimsIdentity) -> Claim: ...
    @property
    def Issuer(self) -> str: ...
    @property
    def OriginalIssuer(self) -> str: ...
    @property
    def Properties(self) -> IDictionary: ...
    @property
    def Subject(self) -> ClaimsIdentity: ...
    @property
    def Type(self) -> str: ...
    @property
    def Value(self) -> str: ...
    @property
    def ValueType(self) -> str: ...
    def ToString(self) -> str: ...
    def WriteTo(self, writer: BinaryWriter) -> None: ...


class ClaimsIdentity(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, identity: IIdentity): ...
    @overload
    def __init__(self, claims: Iterable[Claim]): ...
    @overload
    def __init__(self, authenticationType: str): ...
    @overload
    def __init__(self, reader: BinaryReader): ...
    @overload
    def __init__(self, claims: Iterable[Claim], authenticationType: str): ...
    @overload
    def __init__(self, identity: IIdentity, claims: Iterable[Claim]): ...
    @overload
    def __init__(self, authenticationType: str, nameType: str, roleType: str): ...
    @overload
    def __init__(self, claims: Iterable[Claim], authenticationType: str, nameType: str, roleType: str): ...
    @overload
    def __init__(self, identity: IIdentity, claims: Iterable[Claim], authenticationType: str, nameType: str, roleType: str): ...
    def AddClaim(self, claim: Claim) -> None: ...
    def AddClaims(self, claims: Iterable[Claim]) -> None: ...
    def Clone(self) -> ClaimsIdentity: ...
    @overload
    def FindAll(self, type: str) -> Iterable[Claim]: ...
    @overload
    def FindAll(self, match: Predicate) -> Iterable[Claim]: ...
    @overload
    def FindFirst(self, type: str) -> Claim: ...
    @overload
    def FindFirst(self, match: Predicate) -> Claim: ...
    @property
    def Actor(self) -> ClaimsIdentity: ...
    @property
    def AuthenticationType(self) -> str: ...
    @property
    def BootstrapContext(self) -> Object: ...
    @property
    def Claims(self) -> Iterable[Claim]: ...
    @property
    def IsAuthenticated(self) -> bool: ...
    @property
    def Label(self) -> str: ...
    @property
    def Name(self) -> str: ...
    @property
    def NameClaimType(self) -> str: ...
    @property
    def RoleClaimType(self) -> str: ...
    @overload
    def HasClaim(self, match: Predicate) -> bool: ...
    @overload
    def HasClaim(self, type: str, value: str) -> bool: ...
    def RemoveClaim(self, claim: Claim) -> None: ...
    @Actor.setter
    def Actor(self, value: ClaimsIdentity) -> None: ...
    @BootstrapContext.setter
    def BootstrapContext(self, value: Object) -> None: ...
    @Label.setter
    def Label(self, value: str) -> None: ...
    def TryRemoveClaim(self, claim: Claim) -> bool: ...
    def WriteTo(self, writer: BinaryWriter) -> None: ...


class ClaimsPrincipal(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, identities: Iterable[ClaimsIdentity]): ...
    @overload
    def __init__(self, identity: IIdentity): ...
    @overload
    def __init__(self, principal: IPrincipal): ...
    @overload
    def __init__(self, reader: BinaryReader): ...
    def AddIdentities(self, identities: Iterable[ClaimsIdentity]) -> None: ...
    def AddIdentity(self, identity: ClaimsIdentity) -> None: ...
    def Clone(self) -> ClaimsPrincipal: ...
    @overload
    def FindAll(self, match: Predicate) -> Iterable[Claim]: ...
    @overload
    def FindAll(self, type: str) -> Iterable[Claim]: ...
    @overload
    def FindFirst(self, match: Predicate) -> Claim: ...
    @overload
    def FindFirst(self, type: str) -> Claim: ...
    @property
    def Claims(self) -> Iterable[Claim]: ...
    @property
    def ClaimsPrincipalSelector() -> Func: ...
    @property
    def Current() -> ClaimsPrincipal: ...
    @property
    def Identities(self) -> Iterable[ClaimsIdentity]: ...
    @property
    def Identity(self) -> IIdentity: ...
    @property
    def PrimaryIdentitySelector() -> Func: ...
    @overload
    def HasClaim(self, match: Predicate) -> bool: ...
    @overload
    def HasClaim(self, type: str, value: str) -> bool: ...
    def IsInRole(self, role: str) -> bool: ...
    @ClaimsPrincipalSelector.setter
    def ClaimsPrincipalSelector(value: Func) -> None: ...
    @PrimaryIdentitySelector.setter
    def PrimaryIdentitySelector(value: Func) -> None: ...
    def WriteTo(self, writer: BinaryWriter) -> None: ...


class ClaimTypes(Object):
    pass


class ClaimValueTypes(Object):
    pass
