from typing import Tuple, Set, Iterable, List


class IRelDecryptor:
    def Decrypt(self, encryptionMethod: EncryptionMethod, keyInfo: KeyInfo, toDecrypt: Stream) -> Stream: ...
