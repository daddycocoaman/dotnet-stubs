from typing import Tuple, Set, Iterable, List


class ITimeLimitedDataProtector:
    def CreateProtector(self, purpose: str) -> ITimeLimitedDataProtector: ...
    def Protect(self, plaintext: Set(Byte), expiration: DateTimeOffset) -> Set(Byte): ...
    def Unprotect(self, protectedData: Set(Byte)) -> Tuple[Set(Byte), DateTimeOffset]: ...
