__all__ = ['Permissions','Policy']
from typing import Tuple, Set, Iterable, List


class HostSecurityManager(Object):
    def __init__(self): ...
    def DetermineApplicationTrust(self, applicationEvidence: Evidence, activatorEvidence: Evidence, context: TrustManagerContext) -> ApplicationTrust: ...
    def GenerateAppDomainEvidence(self, evidenceType: Type) -> EvidenceBase: ...
    def GenerateAssemblyEvidence(self, evidenceType: Type, assembly: Assembly) -> EvidenceBase: ...
    @property
    def DomainPolicy(self) -> PolicyLevel: ...
    @property
    def Flags(self) -> HostSecurityManagerOptions: ...
    def GetHostSuppliedAppDomainEvidenceTypes(self) -> Set(Type): ...
    def GetHostSuppliedAssemblyEvidenceTypes(self, assembly: Assembly) -> Set(Type): ...
    def ProvideAppDomainEvidence(self, inputEvidence: Evidence) -> Evidence: ...
    def ProvideAssemblyEvidence(self, loadedAssembly: Assembly, inputEvidence: Evidence) -> Evidence: ...


class HostSecurityManagerOptions:
    #None = 0
    HostAppDomainEvidence = 1
    HostPolicyLevel = 2
    HostAssemblyEvidence = 4
    HostDetermineApplicationTrust = 8
    HostResolvePolicy = 16
    AllFlags = 31


class IEvidenceFactory:
    @property
    def Evidence(self) -> Evidence: ...


class ISecurityPolicyEncodable:
    def FromXml(self, e: SecurityElement, level: PolicyLevel) -> None: ...
    def ToXml(self, level: PolicyLevel) -> SecurityElement: ...


class PolicyLevelType:
    User = 0
    Machine = 1
    Enterprise = 2
    AppDomain = 3


class SecurityContext(Object):
    def Capture() -> SecurityContext: ...
    def CreateCopy(self) -> SecurityContext: ...
    def Dispose(self) -> None: ...
    def IsFlowSuppressed() -> bool: ...
    def IsWindowsIdentityFlowSuppressed() -> bool: ...
    def RestoreFlow() -> None: ...
    def Run(securityContext: SecurityContext, callback: ContextCallback, state: Object) -> None: ...
    def SuppressFlow() -> AsyncFlowControl: ...
    def SuppressFlowWindowsIdentity() -> AsyncFlowControl: ...


class SecurityContextSource:
    CurrentAppDomain = 0
    CurrentAssembly = 1


class SecurityState(Object):
    def EnsureState(self) -> None: ...
    def IsStateAvailable(self) -> bool: ...


class SecurityZone:
    MyComputer = 0
    Intranet = 1
    Trusted = 2
    Internet = 3
    Untrusted = 4
    NoZone = -1


class XmlSyntaxException(SystemException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, lineNumber: int): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, lineNumber: int, message: str): ...
    @overload
    def __init__(self, message: str, inner: Exception): ...
