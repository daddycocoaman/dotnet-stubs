from typing import Tuple, Set, Iterable, List


class CertificateResolver:
    def __init__(self): ...
    def ResolveCertificate(self, thumbprint: str) -> X509Certificate2: ...


class CertificateXmlEncryptor:
    @overload
    def __init__(self, certificate: X509Certificate2, loggerFactory: ILoggerFactory): ...
    @overload
    def __init__(self, thumbprint: str, certificateResolver: ICertificateResolver, loggerFactory: ILoggerFactory): ...
    def Encrypt(self, plaintextElement: XElement) -> EncryptedXmlInfo: ...


class DpapiNGProtectionDescriptorFlags:
    #None = 0
    NamedDescriptor = 1
    MachineKey = 32


class DpapiNGXmlDecryptor:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, services: IServiceProvider): ...
    def Decrypt(self, encryptedElement: XElement) -> XElement: ...


class DpapiNGXmlEncryptor:
    def __init__(self, protectionDescriptorRule: str, flags: DpapiNGProtectionDescriptorFlags, loggerFactory: ILoggerFactory): ...
    def Encrypt(self, plaintextElement: XElement) -> EncryptedXmlInfo: ...


class DpapiXmlDecryptor:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, services: IServiceProvider): ...
    def Decrypt(self, encryptedElement: XElement) -> XElement: ...


class DpapiXmlEncryptor:
    def __init__(self, protectToLocalMachine: bool, loggerFactory: ILoggerFactory): ...
    def Encrypt(self, plaintextElement: XElement) -> EncryptedXmlInfo: ...


class EncryptedXmlDecryptor:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, services: IServiceProvider): ...
    def Decrypt(self, encryptedElement: XElement) -> XElement: ...


class EncryptedXmlInfo:
    def __init__(self, encryptedElement: XElement, decryptorType: Type): ...
    @property
    def DecryptorType(self) -> Type: ...
    @property
    def EncryptedElement(self) -> XElement: ...


class ICertificateResolver:
    def ResolveCertificate(self, thumbprint: str) -> X509Certificate2: ...


class IXmlDecryptor:
    def Decrypt(self, encryptedElement: XElement) -> XElement: ...


class IXmlEncryptor:
    def Encrypt(self, plaintextElement: XElement) -> EncryptedXmlInfo: ...


class NullXmlDecryptor:
    def __init__(self): ...
    def Decrypt(self, encryptedElement: XElement) -> XElement: ...


class NullXmlEncryptor:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, services: IServiceProvider): ...
    def Encrypt(self, plaintextElement: XElement) -> EncryptedXmlInfo: ...
