from typing import Tuple, Set, Iterable, List


class KeyDerivation:
    def Pbkdf2(password: str, salt: Set(Byte), prf: KeyDerivationPrf, iterationCount: int, numBytesRequested: int) -> Set(Byte): ...


class KeyDerivationPrf:
    HMACSHA1 = 0
    HMACSHA256 = 1
    HMACSHA512 = 2
