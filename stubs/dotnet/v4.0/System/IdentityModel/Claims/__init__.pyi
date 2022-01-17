from typing import Tuple, Set, Iterable, List


class X509CertificateClaimSet(ClaimSet):
    def __init__(self, certificate: X509Certificate2): ...
    def Dispose(self) -> None: ...
    def FindClaims(self, claimType: str, right: str) -> Iterable[Claim]: ...
    @property
    def Count(self) -> int: ...
    @property
    def ExpirationTime(self) -> DateTime: ...
    @property
    def Issuer(self) -> ClaimSet: ...
    @property
    def Item(self, index: int) -> Claim: ...
    @property
    def X509Certificate(self) -> X509Certificate2: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def ToString(self) -> str: ...
