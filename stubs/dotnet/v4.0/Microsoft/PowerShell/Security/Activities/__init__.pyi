from typing import Tuple, Set, Iterable, List


class ConvertFromSecureString(PSRemotingActivity):
    def __init__(self): ...
    @property
    def Key(self) -> InArgument: ...
    @property
    def PSCommandName(self) -> str: ...
    @property
    def SecureKey(self) -> InArgument: ...
    @property
    def SecureString(self) -> InArgument: ...
    @Key.setter
    def Key(self, value: InArgument) -> None: ...
    @SecureKey.setter
    def SecureKey(self, value: InArgument) -> None: ...
    @SecureString.setter
    def SecureString(self, value: InArgument) -> None: ...


class ConvertToSecureString(PSRemotingActivity):
    def __init__(self): ...
    @property
    def AsPlainText(self) -> InArgument: ...
    @property
    def Force(self) -> InArgument: ...
    @property
    def Key(self) -> InArgument: ...
    @property
    def PSCommandName(self) -> str: ...
    @property
    def SecureKey(self) -> InArgument: ...
    @property
    def String(self) -> InArgument: ...
    @AsPlainText.setter
    def AsPlainText(self, value: InArgument) -> None: ...
    @Force.setter
    def Force(self, value: InArgument) -> None: ...
    @Key.setter
    def Key(self, value: InArgument) -> None: ...
    @SecureKey.setter
    def SecureKey(self, value: InArgument) -> None: ...
    @String.setter
    def String(self, value: InArgument) -> None: ...


class GetAcl(PSRemotingActivity):
    def __init__(self): ...
    @property
    def AllCentralAccessPolicies(self) -> InArgument: ...
    @property
    def Audit(self) -> InArgument: ...
    @property
    def Exclude(self) -> InArgument: ...
    @property
    def Filter(self) -> InArgument: ...
    @property
    def Include(self) -> InArgument: ...
    @property
    def InputObject(self) -> InArgument: ...
    @property
    def LiteralPath(self) -> InArgument: ...
    @property
    def Path(self) -> InArgument: ...
    @property
    def PSCommandName(self) -> str: ...
    @AllCentralAccessPolicies.setter
    def AllCentralAccessPolicies(self, value: InArgument) -> None: ...
    @Audit.setter
    def Audit(self, value: InArgument) -> None: ...
    @Exclude.setter
    def Exclude(self, value: InArgument) -> None: ...
    @Filter.setter
    def Filter(self, value: InArgument) -> None: ...
    @Include.setter
    def Include(self, value: InArgument) -> None: ...
    @InputObject.setter
    def InputObject(self, value: InArgument) -> None: ...
    @LiteralPath.setter
    def LiteralPath(self, value: InArgument) -> None: ...
    @Path.setter
    def Path(self, value: InArgument) -> None: ...


class GetAuthenticodeSignature(PSRemotingActivity):
    def __init__(self): ...
    @property
    def FilePath(self) -> InArgument: ...
    @property
    def LiteralPath(self) -> InArgument: ...
    @property
    def PSCommandName(self) -> str: ...
    @FilePath.setter
    def FilePath(self, value: InArgument) -> None: ...
    @LiteralPath.setter
    def LiteralPath(self, value: InArgument) -> None: ...


class GetCmsMessage(PSRemotingActivity):
    def __init__(self): ...
    @property
    def Content(self) -> InArgument: ...
    @property
    def LiteralPath(self) -> InArgument: ...
    @property
    def Path(self) -> InArgument: ...
    @property
    def PSCommandName(self) -> str: ...
    @Content.setter
    def Content(self, value: InArgument) -> None: ...
    @LiteralPath.setter
    def LiteralPath(self, value: InArgument) -> None: ...
    @Path.setter
    def Path(self, value: InArgument) -> None: ...


class GetExecutionPolicy(PSRemotingActivity):
    def __init__(self): ...
    @property
    def List(self) -> InArgument: ...
    @property
    def PSCommandName(self) -> str: ...
    @property
    def Scope(self) -> InArgument: ...
    @List.setter
    def List(self, value: InArgument) -> None: ...
    @Scope.setter
    def Scope(self, value: InArgument) -> None: ...


class GetPfxCertificate(PSRemotingActivity):
    def __init__(self): ...
    @property
    def FilePath(self) -> InArgument: ...
    @property
    def LiteralPath(self) -> InArgument: ...
    @property
    def PSCommandName(self) -> str: ...
    @FilePath.setter
    def FilePath(self, value: InArgument) -> None: ...
    @LiteralPath.setter
    def LiteralPath(self, value: InArgument) -> None: ...


class ProtectCmsMessage(PSRemotingActivity):
    def __init__(self): ...
    @property
    def Content(self) -> InArgument: ...
    @property
    def LiteralPath(self) -> InArgument: ...
    @property
    def OutFile(self) -> InArgument: ...
    @property
    def Path(self) -> InArgument: ...
    @property
    def PSCommandName(self) -> str: ...
    @property
    def To(self) -> InArgument: ...
    @Content.setter
    def Content(self, value: InArgument) -> None: ...
    @LiteralPath.setter
    def LiteralPath(self, value: InArgument) -> None: ...
    @OutFile.setter
    def OutFile(self, value: InArgument) -> None: ...
    @Path.setter
    def Path(self, value: InArgument) -> None: ...
    @To.setter
    def To(self, value: InArgument) -> None: ...


class SetAcl(PSRemotingActivity):
    def __init__(self): ...
    @property
    def AclObject(self) -> InArgument: ...
    @property
    def CentralAccessPolicy(self) -> InArgument: ...
    @property
    def ClearCentralAccessPolicy(self) -> InArgument: ...
    @property
    def Exclude(self) -> InArgument: ...
    @property
    def Filter(self) -> InArgument: ...
    @property
    def Include(self) -> InArgument: ...
    @property
    def InputObject(self) -> InArgument: ...
    @property
    def LiteralPath(self) -> InArgument: ...
    @property
    def Passthru(self) -> InArgument: ...
    @property
    def Path(self) -> InArgument: ...
    @property
    def PSCommandName(self) -> str: ...
    @property
    def SecurityDescriptor(self) -> InArgument: ...
    @AclObject.setter
    def AclObject(self, value: InArgument) -> None: ...
    @CentralAccessPolicy.setter
    def CentralAccessPolicy(self, value: InArgument) -> None: ...
    @ClearCentralAccessPolicy.setter
    def ClearCentralAccessPolicy(self, value: InArgument) -> None: ...
    @Exclude.setter
    def Exclude(self, value: InArgument) -> None: ...
    @Filter.setter
    def Filter(self, value: InArgument) -> None: ...
    @Include.setter
    def Include(self, value: InArgument) -> None: ...
    @InputObject.setter
    def InputObject(self, value: InArgument) -> None: ...
    @LiteralPath.setter
    def LiteralPath(self, value: InArgument) -> None: ...
    @Passthru.setter
    def Passthru(self, value: InArgument) -> None: ...
    @Path.setter
    def Path(self, value: InArgument) -> None: ...
    @SecurityDescriptor.setter
    def SecurityDescriptor(self, value: InArgument) -> None: ...


class SetAuthenticodeSignature(PSRemotingActivity):
    def __init__(self): ...
    @property
    def Certificate(self) -> InArgument: ...
    @property
    def FilePath(self) -> InArgument: ...
    @property
    def Force(self) -> InArgument: ...
    @property
    def HashAlgorithm(self) -> InArgument: ...
    @property
    def IncludeChain(self) -> InArgument: ...
    @property
    def LiteralPath(self) -> InArgument: ...
    @property
    def PSCommandName(self) -> str: ...
    @property
    def TimestampServer(self) -> InArgument: ...
    @Certificate.setter
    def Certificate(self, value: InArgument) -> None: ...
    @FilePath.setter
    def FilePath(self, value: InArgument) -> None: ...
    @Force.setter
    def Force(self, value: InArgument) -> None: ...
    @HashAlgorithm.setter
    def HashAlgorithm(self, value: InArgument) -> None: ...
    @IncludeChain.setter
    def IncludeChain(self, value: InArgument) -> None: ...
    @LiteralPath.setter
    def LiteralPath(self, value: InArgument) -> None: ...
    @TimestampServer.setter
    def TimestampServer(self, value: InArgument) -> None: ...


class SetExecutionPolicy(PSRemotingActivity):
    def __init__(self): ...
    @property
    def ExecutionPolicy(self) -> InArgument: ...
    @property
    def Force(self) -> InArgument: ...
    @property
    def PSCommandName(self) -> str: ...
    @property
    def Scope(self) -> InArgument: ...
    @ExecutionPolicy.setter
    def ExecutionPolicy(self, value: InArgument) -> None: ...
    @Force.setter
    def Force(self, value: InArgument) -> None: ...
    @Scope.setter
    def Scope(self, value: InArgument) -> None: ...


class UnprotectCmsMessage(PSRemotingActivity):
    def __init__(self): ...
    @property
    def Content(self) -> InArgument: ...
    @property
    def EventLogRecord(self) -> InArgument: ...
    @property
    def IncludeContext(self) -> InArgument: ...
    @property
    def LiteralPath(self) -> InArgument: ...
    @property
    def Path(self) -> InArgument: ...
    @property
    def PSCommandName(self) -> str: ...
    @property
    def To(self) -> InArgument: ...
    @Content.setter
    def Content(self, value: InArgument) -> None: ...
    @EventLogRecord.setter
    def EventLogRecord(self, value: InArgument) -> None: ...
    @IncludeContext.setter
    def IncludeContext(self, value: InArgument) -> None: ...
    @LiteralPath.setter
    def LiteralPath(self, value: InArgument) -> None: ...
    @Path.setter
    def Path(self, value: InArgument) -> None: ...
    @To.setter
    def To(self, value: InArgument) -> None: ...
