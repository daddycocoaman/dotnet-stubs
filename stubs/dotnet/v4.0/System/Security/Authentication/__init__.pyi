__all__ = ['ExtendedProtection']
from typing import Tuple, Set, Iterable, List


class AuthenticationException(SystemException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class CipherAlgorithmType:
    #None = 0
    Null = 24576
    Des = 26113
    Rc2 = 26114
    TripleDes = 26115
    Aes128 = 26126
    Aes192 = 26127
    Aes256 = 26128
    Aes = 26129
    Rc4 = 26625


class ExchangeAlgorithmType:
    #None = 0
    RsaSign = 9216
    RsaKeyX = 41984
    DiffieHellman = 43522


class HashAlgorithmType:
    #None = 0
    Md5 = 32771
    Sha1 = 32772
    Sha256 = 32780
    Sha384 = 32781
    Sha512 = 32782


class InvalidCredentialException(AuthenticationException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class SslProtocols:
    #None = 0
    Ssl2 = 12
    Ssl3 = 48
    Tls = 192
    Default = 240
    Tls11 = 768
    Tls12 = 3072
    Tls13 = 12288
