from typing import Tuple, Set, Iterable, List


class CardSpaceException(Exception):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class CardSpacePolicyElement(Object):
    def __init__(self, target: XmlElement, issuer: XmlElement, parameters: Collection, privacyNoticeLink: Uri, privacyNoticeVersion: int, isManagedIssuer: bool): ...
    @property
    def IsManagedIssuer(self) -> bool: ...
    @property
    def Issuer(self) -> XmlElement: ...
    @property
    def Parameters(self) -> Collection: ...
    @property
    def PolicyNoticeLink(self) -> Uri: ...
    @property
    def PolicyNoticeVersion(self) -> int: ...
    @property
    def Target(self) -> XmlElement: ...
    @IsManagedIssuer.setter
    def IsManagedIssuer(self, value: bool) -> None: ...
    @Issuer.setter
    def Issuer(self, value: XmlElement) -> None: ...
    @PolicyNoticeLink.setter
    def PolicyNoticeLink(self, value: Uri) -> None: ...
    @PolicyNoticeVersion.setter
    def PolicyNoticeVersion(self, value: int) -> None: ...
    @Target.setter
    def Target(self, value: XmlElement) -> None: ...


class CardSpaceSelector(Object):
    @overload
    def GetToken(policyChain: Set(CardSpacePolicyElement), tokenSerializer: SecurityTokenSerializer) -> GenericXmlSecurityToken: ...
    @overload
    def GetToken(endpoint: XmlElement, policy: Iterable[XmlElement], requiredRemoteTokenIssuer: XmlElement, tokenSerializer: SecurityTokenSerializer) -> GenericXmlSecurityToken: ...
    def Import(fileName: str) -> None: ...
    def Manage() -> None: ...


class IdentityValidationException(Exception):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class PolicyValidationException(Exception):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class ServiceBusyException(Exception):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class ServiceNotStartedException(Exception):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class StsCommunicationException(Exception):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class UnsupportedPolicyOptionsException(Exception):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class UntrustedRecipientException(Exception):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class UserCancellationException(Exception):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...
