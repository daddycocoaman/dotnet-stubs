__all__ = ['Configuration']
from typing import Tuple, Set, Iterable, List


class ChannelBinding:
    @property
    def Size(self) -> int: ...


class ChannelBindingKind:
    Unknown = 0
    Unique = 25
    Endpoint = 26


class ExtendedProtectionPolicy(Object):
    @overload
    def __init__(self, policyEnforcement: PolicyEnforcement): ...
    @overload
    def __init__(self, policyEnforcement: PolicyEnforcement, customChannelBinding: ChannelBinding): ...
    @overload
    def __init__(self, policyEnforcement: PolicyEnforcement, protectionScenario: ProtectionScenario, customServiceNames: ServiceNameCollection): ...
    @overload
    def __init__(self, policyEnforcement: PolicyEnforcement, protectionScenario: ProtectionScenario, customServiceNames: ICollection): ...
    @property
    def CustomChannelBinding(self) -> ChannelBinding: ...
    @property
    def CustomServiceNames(self) -> ServiceNameCollection: ...
    @property
    def OSSupportsExtendedProtection() -> bool: ...
    @property
    def PolicyEnforcement(self) -> PolicyEnforcement: ...
    @property
    def ProtectionScenario(self) -> ProtectionScenario: ...
    def ToString(self) -> str: ...


class ExtendedProtectionPolicyTypeConverter(TypeConverter):
    def __init__(self): ...
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool: ...
    @overload
    def ConvertTo(self, context: ITypeDescriptorContext, culture: CultureInfo, value: Object, destinationType: Type) -> Object: ...


class PolicyEnforcement:
    Never = 0
    WhenSupported = 1
    Always = 2


class ProtectionScenario:
    TransportSelected = 0
    TrustedProxy = 1


class ServiceNameCollection(ReadOnlyCollectionBase):
    def __init__(self, items: ICollection): ...
    def Contains(self, searchServiceName: str) -> bool: ...
    @overload
    def Merge(self, serviceName: str) -> ServiceNameCollection: ...
    @overload
    def Merge(self, serviceNames: IEnumerable) -> ServiceNameCollection: ...


class TokenBinding(Object):
    @property
    def BindingType(self) -> TokenBindingType: ...
    def GetRawTokenBindingId(self) -> Set(Byte): ...


class TokenBindingType:
    Provided = 0
    Referred = 1
