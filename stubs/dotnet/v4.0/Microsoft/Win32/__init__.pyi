__all__ = ['SafeHandles','SafeHandles']
from typing import Tuple, Set, Iterable, List


class IntranetZoneCredentialPolicy:
    def __init__(self): ...
    def ShouldSendCredential(self, challengeUri: Uri, request: WebRequest, credential: NetworkCredential, authModule: IAuthenticationModule) -> bool: ...
