from typing import Tuple, Set, Iterable, List


class DataProtectionScope:
    CurrentUser = 0
    LocalMachine = 1


class ProtectedData(Object):
    def Protect(userData: Set(Byte), optionalEntropy: Set(Byte), scope: DataProtectionScope) -> Set(Byte): ...
    def Unprotect(encryptedData: Set(Byte), optionalEntropy: Set(Byte), scope: DataProtectionScope) -> Set(Byte): ...
