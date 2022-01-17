from typing import Tuple, Set, Iterable, List


class KeyDerivation:
    def Pbkdf2(password: str, salt: Set(Byte), prf: KeyDerivationPrf, iterationCount: int, numBytesRequested: int) -> Set(Byte): ...
