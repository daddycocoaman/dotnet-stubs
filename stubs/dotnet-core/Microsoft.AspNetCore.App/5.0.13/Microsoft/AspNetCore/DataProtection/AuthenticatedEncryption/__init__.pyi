__all__ = ['ConfigurationModel']
from typing import Tuple, Set, Iterable, List


class AuthenticatedEncryptorFactory:
    def __init__(self, loggerFactory: ILoggerFactory): ...
    def CreateEncryptorInstance(self, key: IKey) -> IAuthenticatedEncryptor: ...


class CngCbcAuthenticatedEncryptorFactory:
    def __init__(self, loggerFactory: ILoggerFactory): ...
    def CreateEncryptorInstance(self, key: IKey) -> IAuthenticatedEncryptor: ...


class CngGcmAuthenticatedEncryptorFactory:
    def __init__(self, loggerFactory: ILoggerFactory): ...
    def CreateEncryptorInstance(self, key: IKey) -> IAuthenticatedEncryptor: ...


class EncryptionAlgorithm:
    AES_128_CBC = 0
    AES_192_CBC = 1
    AES_256_CBC = 2
    AES_128_GCM = 3
    AES_192_GCM = 4
    AES_256_GCM = 5


class IAuthenticatedEncryptor:
    def Decrypt(self, ciphertext: ArraySegment, additionalAuthenticatedData: ArraySegment) -> Set(Byte): ...
    def Encrypt(self, plaintext: ArraySegment, additionalAuthenticatedData: ArraySegment) -> Set(Byte): ...


class IAuthenticatedEncryptorFactory:
    def CreateEncryptorInstance(self, key: IKey) -> IAuthenticatedEncryptor: ...


class ManagedAuthenticatedEncryptorFactory:
    def __init__(self, loggerFactory: ILoggerFactory): ...
    def CreateEncryptorInstance(self, key: IKey) -> IAuthenticatedEncryptor: ...


class ValidationAlgorithm:
    HMACSHA256 = 0
    HMACSHA512 = 1
