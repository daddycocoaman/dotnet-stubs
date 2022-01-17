from typing import Tuple, Set, Iterable, List


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