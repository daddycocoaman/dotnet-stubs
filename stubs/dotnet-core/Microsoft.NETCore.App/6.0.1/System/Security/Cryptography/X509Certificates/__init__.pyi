from typing import Tuple, Set, Iterable, List


class CertificateRequest(Object):
    @overload
    def __init__(self, subjectName: str, key: ECDsa, hashAlgorithm: HashAlgorithmName): ...
    @overload
    def __init__(self, subjectName: X500DistinguishedName, key: ECDsa, hashAlgorithm: HashAlgorithmName): ...
    @overload
    def __init__(self, subjectName: X500DistinguishedName, publicKey: PublicKey, hashAlgorithm: HashAlgorithmName): ...
    @overload
    def __init__(self, subjectName: str, key: RSA, hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding): ...
    @overload
    def __init__(self, subjectName: X500DistinguishedName, key: RSA, hashAlgorithm: HashAlgorithmName, padding: RSASignaturePadding): ...
    @overload
    def Create(self, issuerCertificate: X509Certificate2, notBefore: DateTimeOffset, notAfter: DateTimeOffset, serialNumber: Set(Byte)) -> X509Certificate2: ...
    @overload
    def Create(self, issuerCertificate: X509Certificate2, notBefore: DateTimeOffset, notAfter: DateTimeOffset, serialNumber: ReadOnlySpan) -> X509Certificate2: ...
    @overload
    def Create(self, issuerName: X500DistinguishedName, generator: X509SignatureGenerator, notBefore: DateTimeOffset, notAfter: DateTimeOffset, serialNumber: Set(Byte)) -> X509Certificate2: ...
    @overload
    def Create(self, issuerName: X500DistinguishedName, generator: X509SignatureGenerator, notBefore: DateTimeOffset, notAfter: DateTimeOffset, serialNumber: ReadOnlySpan) -> X509Certificate2: ...
    def CreateSelfSigned(self, notBefore: DateTimeOffset, notAfter: DateTimeOffset) -> X509Certificate2: ...
    @overload
    def CreateSigningRequest(self) -> Set(Byte): ...
    @overload
    def CreateSigningRequest(self, signatureGenerator: X509SignatureGenerator) -> Set(Byte): ...
    @property
    def CertificateExtensions(self) -> Collection: ...
    @property
    def HashAlgorithm(self) -> HashAlgorithmName: ...
    @property
    def PublicKey(self) -> PublicKey: ...
    @property
    def SubjectName(self) -> X500DistinguishedName: ...


class DSACertificateExtensions(Object):
    def CopyWithPrivateKey(certificate: X509Certificate2, privateKey: DSA) -> X509Certificate2: ...
    def GetDSAPrivateKey(certificate: X509Certificate2) -> DSA: ...
    def GetDSAPublicKey(certificate: X509Certificate2) -> DSA: ...


class ECDsaCertificateExtensions(Object):
    def CopyWithPrivateKey(certificate: X509Certificate2, privateKey: ECDsa) -> X509Certificate2: ...
    def GetECDsaPrivateKey(certificate: X509Certificate2) -> ECDsa: ...
    def GetECDsaPublicKey(certificate: X509Certificate2) -> ECDsa: ...


class OpenFlags:
    ReadOnly = 0
    ReadWrite = 1
    MaxAllowed = 2
    OpenExistingOnly = 4
    IncludeArchived = 8


class PublicKey(Object):
    @overload
    def __init__(self, key: AsymmetricAlgorithm): ...
    @overload
    def __init__(self, oid: Oid, parameters: AsnEncodedData, keyValue: AsnEncodedData): ...
    def CreateFromSubjectPublicKeyInfo(source: ReadOnlySpan) -> Tuple[PublicKey, int]: ...
    def ExportSubjectPublicKeyInfo(self) -> Set(Byte): ...
    @property
    def EncodedKeyValue(self) -> AsnEncodedData: ...
    @property
    def EncodedParameters(self) -> AsnEncodedData: ...
    @property
    def Key(self) -> AsymmetricAlgorithm: ...
    @property
    def Oid(self) -> Oid: ...
    def GetDSAPublicKey(self) -> DSA: ...
    def GetECDiffieHellmanPublicKey(self) -> ECDiffieHellman: ...
    def GetECDsaPublicKey(self) -> ECDsa: ...
    def GetRSAPublicKey(self) -> RSA: ...
    def TryExportSubjectPublicKeyInfo(self, destination: Span) -> Tuple[bool, int]: ...


class RSACertificateExtensions(Object):
    def CopyWithPrivateKey(certificate: X509Certificate2, privateKey: RSA) -> X509Certificate2: ...
    def GetRSAPrivateKey(certificate: X509Certificate2) -> RSA: ...
    def GetRSAPublicKey(certificate: X509Certificate2) -> RSA: ...


class StoreLocation:
    CurrentUser = 1
    LocalMachine = 2


class StoreName:
    AddressBook = 1
    AuthRoot = 2
    CertificateAuthority = 3
    Disallowed = 4
    My = 5
    Root = 6
    TrustedPeople = 7
    TrustedPublisher = 8


class SubjectAlternativeNameBuilder(Object):
    def __init__(self): ...
    def AddDnsName(self, dnsName: str) -> None: ...
    def AddEmailAddress(self, emailAddress: str) -> None: ...
    def AddIpAddress(self, ipAddress: IPAddress) -> None: ...
    def AddUri(self, uri: Uri) -> None: ...
    def AddUserPrincipalName(self, upn: str) -> None: ...
    def Build(self, critical: bool) -> X509Extension: ...


class X500DistinguishedName(AsnEncodedData):
    @overload
    def __init__(self, encodedDistinguishedName: Set(Byte)): ...
    @overload
    def __init__(self, encodedDistinguishedName: ReadOnlySpan): ...
    @overload
    def __init__(self, encodedDistinguishedName: AsnEncodedData): ...
    @overload
    def __init__(self, distinguishedName: X500DistinguishedName): ...
    @overload
    def __init__(self, distinguishedName: str): ...
    @overload
    def __init__(self, distinguishedName: str, flag: X500DistinguishedNameFlags): ...
    def Decode(self, flag: X500DistinguishedNameFlags) -> str: ...
    def Format(self, multiLine: bool) -> str: ...
    @property
    def Name(self) -> str: ...


class X500DistinguishedNameFlags:
    #None = 0
    Reversed = 1
    UseSemicolons = 16
    DoNotUsePlusSign = 32
    DoNotUseQuotes = 64
    UseCommas = 128
    UseNewLines = 256
    UseUTF8Encoding = 4096
    UseT61Encoding = 8192
    ForceUTF8Encoding = 16384


class X509BasicConstraintsExtension(X509Extension):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, encodedBasicConstraints: AsnEncodedData, critical: bool): ...
    @overload
    def __init__(self, certificateAuthority: bool, hasPathLengthConstraint: bool, pathLengthConstraint: int, critical: bool): ...
    def CopyFrom(self, asnEncodedData: AsnEncodedData) -> None: ...
    @property
    def CertificateAuthority(self) -> bool: ...
    @property
    def HasPathLengthConstraint(self) -> bool: ...
    @property
    def PathLengthConstraint(self) -> int: ...


class X509Certificate(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, data: Set(Byte)): ...
    @overload
    def __init__(self, handle: IntPtr): ...
    @overload
    def __init__(self, fileName: str): ...
    @overload
    def __init__(self, cert: X509Certificate): ...
    @overload
    def __init__(self, rawData: Set(Byte), password: str): ...
    @overload
    def __init__(self, rawData: Set(Byte), password: SecureString): ...
    @overload
    def __init__(self, fileName: str, password: str): ...
    @overload
    def __init__(self, fileName: str, password: SecureString): ...
    @overload
    def __init__(self, info: SerializationInfo, context: StreamingContext): ...
    @overload
    def __init__(self, rawData: Set(Byte), password: str, keyStorageFlags: X509KeyStorageFlags): ...
    @overload
    def __init__(self, rawData: Set(Byte), password: SecureString, keyStorageFlags: X509KeyStorageFlags): ...
    @overload
    def __init__(self, fileName: str, password: str, keyStorageFlags: X509KeyStorageFlags): ...
    @overload
    def __init__(self, fileName: str, password: SecureString, keyStorageFlags: X509KeyStorageFlags): ...
    def CreateFromCertFile(filename: str) -> X509Certificate: ...
    def CreateFromSignedFile(filename: str) -> X509Certificate: ...
    def Dispose(self) -> None: ...
    @overload
    def Equals(self, other: X509Certificate) -> bool: ...
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @overload
    def Export(self, contentType: X509ContentType) -> Set(Byte): ...
    @overload
    def Export(self, contentType: X509ContentType, password: str) -> Set(Byte): ...
    @overload
    def Export(self, contentType: X509ContentType, password: SecureString) -> Set(Byte): ...
    @property
    def Handle(self) -> IntPtr: ...
    @property
    def Issuer(self) -> str: ...
    @property
    def Subject(self) -> str: ...
    @overload
    def GetCertHash(self) -> Set(Byte): ...
    @overload
    def GetCertHash(self, hashAlgorithm: HashAlgorithmName) -> Set(Byte): ...
    @overload
    def GetCertHashString(self) -> str: ...
    @overload
    def GetCertHashString(self, hashAlgorithm: HashAlgorithmName) -> str: ...
    def GetEffectiveDateString(self) -> str: ...
    def GetExpirationDateString(self) -> str: ...
    def GetFormat(self) -> str: ...
    def GetHashCode(self) -> int: ...
    def GetKeyAlgorithm(self) -> str: ...
    def GetKeyAlgorithmParameters(self) -> Set(Byte): ...
    def GetKeyAlgorithmParametersString(self) -> str: ...
    def GetPublicKey(self) -> Set(Byte): ...
    def GetPublicKeyString(self) -> str: ...
    def GetRawCertData(self) -> Set(Byte): ...
    def GetRawCertDataString(self) -> str: ...
    def GetSerialNumber(self) -> Set(Byte): ...
    def GetSerialNumberString(self) -> str: ...
    def Reset(self) -> None: ...
    @overload
    def ToString(self) -> str: ...
    @overload
    def ToString(self, fVerbose: bool) -> str: ...
    def TryGetCertHash(self, hashAlgorithm: HashAlgorithmName, destination: Span) -> Tuple[bool, int]: ...


class X509Certificate2(X509Certificate):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, rawData: Set(Byte)): ...
    @overload
    def __init__(self, rawData: ReadOnlySpan): ...
    @overload
    def __init__(self, handle: IntPtr): ...
    @overload
    def __init__(self, fileName: str): ...
    @overload
    def __init__(self, certificate: X509Certificate): ...
    @overload
    def __init__(self, rawData: Set(Byte), password: str): ...
    @overload
    def __init__(self, rawData: Set(Byte), password: SecureString): ...
    @overload
    def __init__(self, fileName: str, password: str): ...
    @overload
    def __init__(self, fileName: str, password: SecureString): ...
    @overload
    def __init__(self, rawData: Set(Byte), password: str, keyStorageFlags: X509KeyStorageFlags): ...
    @overload
    def __init__(self, rawData: Set(Byte), password: SecureString, keyStorageFlags: X509KeyStorageFlags): ...
    @overload
    def __init__(self, rawData: ReadOnlySpan, password: ReadOnlySpan, keyStorageFlags: X509KeyStorageFlags): ...
    @overload
    def __init__(self, fileName: str, password: str, keyStorageFlags: X509KeyStorageFlags): ...
    @overload
    def __init__(self, fileName: str, password: SecureString, keyStorageFlags: X509KeyStorageFlags): ...
    @overload
    def __init__(self, fileName: str, password: ReadOnlySpan, keyStorageFlags: X509KeyStorageFlags): ...
    def CopyWithPrivateKey(self, privateKey: ECDiffieHellman) -> X509Certificate2: ...
    def CreateFromEncryptedPem(certPem: ReadOnlySpan, keyPem: ReadOnlySpan, password: ReadOnlySpan) -> X509Certificate2: ...
    def CreateFromEncryptedPemFile(certPemFilePath: str, password: ReadOnlySpan, keyPemFilePath: str) -> X509Certificate2: ...
    @overload
    def CreateFromPem(certPem: ReadOnlySpan) -> X509Certificate2: ...
    @overload
    def CreateFromPem(certPem: ReadOnlySpan, keyPem: ReadOnlySpan) -> X509Certificate2: ...
    def CreateFromPemFile(certPemFilePath: str, keyPemFilePath: str) -> X509Certificate2: ...
    @property
    def Archived(self) -> bool: ...
    @property
    def Extensions(self) -> X509ExtensionCollection: ...
    @property
    def FriendlyName(self) -> str: ...
    @property
    def HasPrivateKey(self) -> bool: ...
    @property
    def IssuerName(self) -> X500DistinguishedName: ...
    @property
    def NotAfter(self) -> DateTime: ...
    @property
    def NotBefore(self) -> DateTime: ...
    @property
    def PrivateKey(self) -> AsymmetricAlgorithm: ...
    @property
    def PublicKey(self) -> PublicKey: ...
    @property
    def RawData(self) -> Set(Byte): ...
    @property
    def SerialNumber(self) -> str: ...
    @property
    def SignatureAlgorithm(self) -> Oid: ...
    @property
    def SubjectName(self) -> X500DistinguishedName: ...
    @property
    def Thumbprint(self) -> str: ...
    @property
    def Version(self) -> int: ...
    @overload
    def GetCertContentType(fileName: str) -> X509ContentType: ...
    @overload
    def GetCertContentType(rawData: Set(Byte)) -> X509ContentType: ...
    @overload
    def GetCertContentType(rawData: ReadOnlySpan) -> X509ContentType: ...
    def GetECDiffieHellmanPrivateKey(self) -> ECDiffieHellman: ...
    def GetECDiffieHellmanPublicKey(self) -> ECDiffieHellman: ...
    def GetNameInfo(self, nameType: X509NameType, forIssuer: bool) -> str: ...
    def Reset(self) -> None: ...
    @Archived.setter
    def Archived(self, value: bool) -> None: ...
    @FriendlyName.setter
    def FriendlyName(self, value: str) -> None: ...
    @PrivateKey.setter
    def PrivateKey(self, value: AsymmetricAlgorithm) -> None: ...
    @overload
    def ToString(self) -> str: ...
    @overload
    def ToString(self, verbose: bool) -> str: ...
    def Verify(self) -> bool: ...


class X509Certificate2Collection(X509CertificateCollection):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, certificate: X509Certificate2): ...
    @overload
    def __init__(self, certificates: Set(X509Certificate2)): ...
    @overload
    def __init__(self, certificates: X509Certificate2Collection): ...
    @overload
    def Add(self, certificate: X509Certificate2) -> int: ...
    @overload
    def AddRange(self, certificates: Set(X509Certificate2)) -> None: ...
    @overload
    def AddRange(self, certificates: X509Certificate2Collection) -> None: ...
    @overload
    def Contains(self, certificate: X509Certificate2) -> bool: ...
    @overload
    def Export(self, contentType: X509ContentType) -> Set(Byte): ...
    @overload
    def Export(self, contentType: X509ContentType, password: str) -> Set(Byte): ...
    def Find(self, findType: X509FindType, findValue: Object, validOnly: bool) -> X509Certificate2Collection: ...
    @property
    def Item(self, index: int) -> X509Certificate2: ...
    @overload
    def GetEnumerator(self) -> X509Certificate2Enumerator: ...
    @overload
    def Import(self, rawData: Set(Byte)) -> None: ...
    @overload
    def Import(self, fileName: str) -> None: ...
    @overload
    def Import(self, rawData: ReadOnlySpan) -> None: ...
    @overload
    def Import(self, fileName: str, password: str, keyStorageFlags: X509KeyStorageFlags) -> None: ...
    @overload
    def Import(self, rawData: ReadOnlySpan, password: ReadOnlySpan, keyStorageFlags: X509KeyStorageFlags) -> None: ...
    @overload
    def Import(self, rawData: ReadOnlySpan, password: str, keyStorageFlags: X509KeyStorageFlags) -> None: ...
    @overload
    def Import(self, rawData: Set(Byte), password: str, keyStorageFlags: X509KeyStorageFlags) -> None: ...
    @overload
    def Import(self, fileName: str, password: ReadOnlySpan, keyStorageFlags: X509KeyStorageFlags) -> None: ...
    def ImportFromPem(self, certPem: ReadOnlySpan) -> None: ...
    def ImportFromPemFile(self, certPemFilePath: str) -> None: ...
    @overload
    def Insert(self, index: int, certificate: X509Certificate2) -> None: ...
    @overload
    def Remove(self, certificate: X509Certificate2) -> None: ...
    @overload
    def RemoveRange(self, certificates: X509Certificate2Collection) -> None: ...
    @overload
    def RemoveRange(self, certificates: Set(X509Certificate2)) -> None: ...
    @Item.setter
    def Item(self, index: int, value: X509Certificate2) -> None: ...


class X509Certificate2Enumerator(Object):
    @property
    def Current(self) -> X509Certificate2: ...
    def MoveNext(self) -> bool: ...
    def Reset(self) -> None: ...


class X509CertificateCollection(CollectionBase):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, value: Set(X509Certificate)): ...
    @overload
    def __init__(self, value: X509CertificateCollection): ...
    def Add(self, value: X509Certificate) -> int: ...
    @overload
    def AddRange(self, value: Set(X509Certificate)) -> None: ...
    @overload
    def AddRange(self, value: X509CertificateCollection) -> None: ...
    def Contains(self, value: X509Certificate) -> bool: ...
    def CopyTo(self, array: Set(X509Certificate), index: int) -> None: ...
    @property
    def Item(self, index: int) -> X509Certificate: ...
    @overload
    def GetEnumerator(self) -> X509CertificateEnumerator: ...
    def GetHashCode(self) -> int: ...
    def IndexOf(self, value: X509Certificate) -> int: ...
    def Insert(self, index: int, value: X509Certificate) -> None: ...
    def Remove(self, value: X509Certificate) -> None: ...
    @Item.setter
    def Item(self, index: int, value: X509Certificate) -> None: ...


class X509CertificateEnumerator(Object):
    def __init__(self, mappings: X509CertificateCollection): ...
    @property
    def Current(self) -> X509Certificate: ...
    def MoveNext(self) -> bool: ...
    def Reset(self) -> None: ...


class X509Chain(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, useMachineContext: bool): ...
    @overload
    def __init__(self, chainContext: IntPtr): ...
    def Build(self, certificate: X509Certificate2) -> bool: ...
    def Create() -> X509Chain: ...
    def Dispose(self) -> None: ...
    @property
    def ChainContext(self) -> IntPtr: ...
    @property
    def ChainElements(self) -> X509ChainElementCollection: ...
    @property
    def ChainPolicy(self) -> X509ChainPolicy: ...
    @property
    def ChainStatus(self) -> Set(X509ChainStatus): ...
    @property
    def SafeHandle(self) -> SafeX509ChainHandle: ...
    def Reset(self) -> None: ...
    @ChainPolicy.setter
    def ChainPolicy(self, value: X509ChainPolicy) -> None: ...


class X509ChainElement(Object):
    @property
    def Certificate(self) -> X509Certificate2: ...
    @property
    def ChainElementStatus(self) -> Set(X509ChainStatus): ...
    @property
    def Information(self) -> str: ...


class X509ChainElementCollection(Object):
    def CopyTo(self, array: Set(X509ChainElement), index: int) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsSynchronized(self) -> bool: ...
    @property
    def Item(self, index: int) -> X509ChainElement: ...
    @property
    def SyncRoot(self) -> Object: ...
    def GetEnumerator(self) -> X509ChainElementEnumerator: ...


class X509ChainElementEnumerator(Object):
    @property
    def Current(self) -> X509ChainElement: ...
    def MoveNext(self) -> bool: ...
    def Reset(self) -> None: ...


class X509ChainPolicy(Object):
    def __init__(self): ...
    @property
    def ApplicationPolicy(self) -> OidCollection: ...
    @property
    def CertificatePolicy(self) -> OidCollection: ...
    @property
    def CustomTrustStore(self) -> X509Certificate2Collection: ...
    @property
    def DisableCertificateDownloads(self) -> bool: ...
    @property
    def ExtraStore(self) -> X509Certificate2Collection: ...
    @property
    def RevocationFlag(self) -> X509RevocationFlag: ...
    @property
    def RevocationMode(self) -> X509RevocationMode: ...
    @property
    def TrustMode(self) -> X509ChainTrustMode: ...
    @property
    def UrlRetrievalTimeout(self) -> TimeSpan: ...
    @property
    def VerificationFlags(self) -> X509VerificationFlags: ...
    @property
    def VerificationTime(self) -> DateTime: ...
    def Reset(self) -> None: ...
    @DisableCertificateDownloads.setter
    def DisableCertificateDownloads(self, value: bool) -> None: ...
    @RevocationFlag.setter
    def RevocationFlag(self, value: X509RevocationFlag) -> None: ...
    @RevocationMode.setter
    def RevocationMode(self, value: X509RevocationMode) -> None: ...
    @TrustMode.setter
    def TrustMode(self, value: X509ChainTrustMode) -> None: ...
    @UrlRetrievalTimeout.setter
    def UrlRetrievalTimeout(self, value: TimeSpan) -> None: ...
    @VerificationFlags.setter
    def VerificationFlags(self, value: X509VerificationFlags) -> None: ...
    @VerificationTime.setter
    def VerificationTime(self, value: DateTime) -> None: ...


class X509ChainStatus(ValueType):
    @property
    def Status(self) -> X509ChainStatusFlags: ...
    @property
    def StatusInformation(self) -> str: ...
    @Status.setter
    def Status(self, value: X509ChainStatusFlags) -> None: ...
    @StatusInformation.setter
    def StatusInformation(self, value: str) -> None: ...


class X509ChainStatusFlags:
    NoError = 0
    NotTimeValid = 1
    NotTimeNested = 2
    Revoked = 4
    NotSignatureValid = 8
    NotValidForUsage = 16
    UntrustedRoot = 32
    RevocationStatusUnknown = 64
    Cyclic = 128
    InvalidExtension = 256
    InvalidPolicyConstraints = 512
    InvalidBasicConstraints = 1024
    InvalidNameConstraints = 2048
    HasNotSupportedNameConstraint = 4096
    HasNotDefinedNameConstraint = 8192
    HasNotPermittedNameConstraint = 16384
    HasExcludedNameConstraint = 32768
    PartialChain = 65536
    CtlNotTimeValid = 131072
    CtlNotSignatureValid = 262144
    CtlNotValidForUsage = 524288
    HasWeakSignature = 1048576
    OfflineRevocation = 16777216
    NoIssuanceChainPolicy = 33554432
    ExplicitDistrust = 67108864
    HasNotSupportedCriticalExtension = 134217728


class X509ChainTrustMode:
    System = 0
    CustomRootTrust = 1


class X509ContentType:
    Unknown = 0
    Cert = 1
    SerializedCert = 2
    Pfx = 3
    Pkcs12 = 3
    SerializedStore = 4
    Pkcs7 = 5
    Authenticode = 6


class X509EnhancedKeyUsageExtension(X509Extension):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, encodedEnhancedKeyUsages: AsnEncodedData, critical: bool): ...
    @overload
    def __init__(self, enhancedKeyUsages: OidCollection, critical: bool): ...
    def CopyFrom(self, asnEncodedData: AsnEncodedData) -> None: ...
    @property
    def EnhancedKeyUsages(self) -> OidCollection: ...


class X509Extension(AsnEncodedData):
    @overload
    def __init__(self, encodedExtension: AsnEncodedData, critical: bool): ...
    @overload
    def __init__(self, oid: Oid, rawData: Set(Byte), critical: bool): ...
    @overload
    def __init__(self, oid: Oid, rawData: ReadOnlySpan, critical: bool): ...
    @overload
    def __init__(self, oid: str, rawData: Set(Byte), critical: bool): ...
    @overload
    def __init__(self, oid: str, rawData: ReadOnlySpan, critical: bool): ...
    def CopyFrom(self, asnEncodedData: AsnEncodedData) -> None: ...
    @property
    def Critical(self) -> bool: ...
    @Critical.setter
    def Critical(self, value: bool) -> None: ...


class X509ExtensionCollection(Object):
    def __init__(self): ...
    def Add(self, extension: X509Extension) -> int: ...
    def CopyTo(self, array: Set(X509Extension), index: int) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsSynchronized(self) -> bool: ...
    @property
    def Item(self, index: int) -> X509Extension: ...
    @property
    def Item(self, oid: str) -> X509Extension: ...
    @property
    def SyncRoot(self) -> Object: ...
    def GetEnumerator(self) -> X509ExtensionEnumerator: ...


class X509ExtensionEnumerator(Object):
    @property
    def Current(self) -> X509Extension: ...
    def MoveNext(self) -> bool: ...
    def Reset(self) -> None: ...


class X509FindType:
    FindByThumbprint = 0
    FindBySubjectName = 1
    FindBySubjectDistinguishedName = 2
    FindByIssuerName = 3
    FindByIssuerDistinguishedName = 4
    FindBySerialNumber = 5
    FindByTimeValid = 6
    FindByTimeNotYetValid = 7
    FindByTimeExpired = 8
    FindByTemplateName = 9
    FindByApplicationPolicy = 10
    FindByCertificatePolicy = 11
    FindByExtension = 12
    FindByKeyUsage = 13
    FindBySubjectKeyIdentifier = 14


class X509IncludeOption:
    #None = 0
    ExcludeRoot = 1
    EndCertOnly = 2
    WholeChain = 3


class X509KeyStorageFlags:
    DefaultKeySet = 0
    UserKeySet = 1
    MachineKeySet = 2
    Exportable = 4
    UserProtected = 8
    PersistKeySet = 16
    EphemeralKeySet = 32


class X509KeyUsageExtension(X509Extension):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, encodedKeyUsage: AsnEncodedData, critical: bool): ...
    @overload
    def __init__(self, keyUsages: X509KeyUsageFlags, critical: bool): ...
    def CopyFrom(self, asnEncodedData: AsnEncodedData) -> None: ...
    @property
    def KeyUsages(self) -> X509KeyUsageFlags: ...


class X509KeyUsageFlags:
    #None = 0
    EncipherOnly = 1
    CrlSign = 2
    KeyCertSign = 4
    KeyAgreement = 8
    DataEncipherment = 16
    KeyEncipherment = 32
    NonRepudiation = 64
    DigitalSignature = 128
    DecipherOnly = 32768


class X509NameType:
    SimpleName = 0
    EmailName = 1
    UpnName = 2
    DnsName = 3
    DnsFromAlternativeName = 4
    UrlName = 5


class X509RevocationFlag:
    EndCertificateOnly = 0
    EntireChain = 1
    ExcludeRoot = 2


class X509RevocationMode:
    NoCheck = 0
    Online = 1
    Offline = 2


class X509SignatureGenerator(Object):
    def CreateForECDsa(key: ECDsa) -> X509SignatureGenerator: ...
    def CreateForRSA(key: RSA, signaturePadding: RSASignaturePadding) -> X509SignatureGenerator: ...
    @property
    def PublicKey(self) -> PublicKey: ...
    def GetSignatureAlgorithmIdentifier(self, hashAlgorithm: HashAlgorithmName) -> Set(Byte): ...
    def SignData(self, data: Set(Byte), hashAlgorithm: HashAlgorithmName) -> Set(Byte): ...


class X509Store(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, storeName: str): ...
    @overload
    def __init__(self, storeName: StoreName): ...
    @overload
    def __init__(self, storeLocation: StoreLocation): ...
    @overload
    def __init__(self, storeHandle: IntPtr): ...
    @overload
    def __init__(self, storeName: StoreName, storeLocation: StoreLocation): ...
    @overload
    def __init__(self, storeName: str, storeLocation: StoreLocation): ...
    @overload
    def __init__(self, storeName: StoreName, storeLocation: StoreLocation, flags: OpenFlags): ...
    @overload
    def __init__(self, storeName: str, storeLocation: StoreLocation, flags: OpenFlags): ...
    def Add(self, certificate: X509Certificate2) -> None: ...
    def AddRange(self, certificates: X509Certificate2Collection) -> None: ...
    def Close(self) -> None: ...
    def Dispose(self) -> None: ...
    @property
    def Certificates(self) -> X509Certificate2Collection: ...
    @property
    def IsOpen(self) -> bool: ...
    @property
    def Location(self) -> StoreLocation: ...
    @property
    def Name(self) -> str: ...
    @property
    def StoreHandle(self) -> IntPtr: ...
    def Open(self, flags: OpenFlags) -> None: ...
    def Remove(self, certificate: X509Certificate2) -> None: ...
    def RemoveRange(self, certificates: X509Certificate2Collection) -> None: ...


class X509SubjectKeyIdentifierExtension(X509Extension):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, encodedSubjectKeyIdentifier: AsnEncodedData, critical: bool): ...
    @overload
    def __init__(self, subjectKeyIdentifier: Set(Byte), critical: bool): ...
    @overload
    def __init__(self, subjectKeyIdentifier: ReadOnlySpan, critical: bool): ...
    @overload
    def __init__(self, key: PublicKey, critical: bool): ...
    @overload
    def __init__(self, subjectKeyIdentifier: str, critical: bool): ...
    @overload
    def __init__(self, key: PublicKey, algorithm: X509SubjectKeyIdentifierHashAlgorithm, critical: bool): ...
    def CopyFrom(self, asnEncodedData: AsnEncodedData) -> None: ...
    @property
    def SubjectKeyIdentifier(self) -> str: ...


class X509SubjectKeyIdentifierHashAlgorithm:
    Sha1 = 0
    ShortSha1 = 1
    CapiSha1 = 2


class X509VerificationFlags:
    NoFlag = 0
    IgnoreNotTimeValid = 1
    IgnoreCtlNotTimeValid = 2
    IgnoreNotTimeNested = 4
    IgnoreInvalidBasicConstraints = 8
    AllowUnknownCertificateAuthority = 16
    IgnoreWrongUsage = 32
    IgnoreInvalidName = 64
    IgnoreInvalidPolicy = 128
    IgnoreEndRevocationUnknown = 256
    IgnoreCtlSignerRevocationUnknown = 512
    IgnoreCertificateAuthorityRevocationUnknown = 1024
    IgnoreRootRevocationUnknown = 2048
    AllFlags = 4095
