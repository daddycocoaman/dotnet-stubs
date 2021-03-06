from typing import Tuple, Set, Iterable, List


class DiagnosticsElement(ConfigurationElement):
    def __init__(self): ...
    @property
    def SuppressReturningExceptions(self) -> bool: ...
    @SuppressReturningExceptions.setter
    def SuppressReturningExceptions(self, value: bool) -> None: ...


class PriorityGroup:
    High = 0
    Low = 1


class ProtocolElement(ConfigurationElement):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, protocol: WebServiceProtocols): ...
    @property
    def Name(self) -> WebServiceProtocols: ...
    @Name.setter
    def Name(self, value: WebServiceProtocols) -> None: ...


class ProtocolElementCollection(ConfigurationElementCollection):
    def __init__(self): ...
    def Add(self, element: ProtocolElement) -> None: ...
    def Clear(self) -> None: ...
    def ContainsKey(self, key: Object) -> bool: ...
    @overload
    def CopyTo(self, array: Set(ProtocolElement), index: int) -> None: ...
    @property
    def Item(self, key: Object) -> ProtocolElement: ...
    @property
    def Item(self, index: int) -> ProtocolElement: ...
    def IndexOf(self, element: ProtocolElement) -> int: ...
    def Remove(self, element: ProtocolElement) -> None: ...
    @overload
    def RemoveAt(self, key: Object) -> None: ...
    @overload
    def RemoveAt(self, index: int) -> None: ...
    @Item.setter
    def Item(self, index: int, value: ProtocolElement) -> None: ...
    @Item.setter
    def Item(self, key: Object, value: ProtocolElement) -> None: ...


class SoapEnvelopeProcessingElement(ConfigurationElement):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, readTimeout: int): ...
    @overload
    def __init__(self, readTimeout: int, strict: bool): ...
    @property
    def IsStrict(self) -> bool: ...
    @property
    def ReadTimeout(self) -> int: ...
    @IsStrict.setter
    def IsStrict(self, value: bool) -> None: ...
    @ReadTimeout.setter
    def ReadTimeout(self, value: int) -> None: ...


class SoapExtensionTypeElement(ConfigurationElement):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, type: str, priority: int, group: PriorityGroup): ...
    @overload
    def __init__(self, type: Type, priority: int, group: PriorityGroup): ...
    @property
    def Group(self) -> PriorityGroup: ...
    @property
    def Priority(self) -> int: ...
    @property
    def Type(self) -> Type: ...
    @Group.setter
    def Group(self, value: PriorityGroup) -> None: ...
    @Priority.setter
    def Priority(self, value: int) -> None: ...
    @Type.setter
    def Type(self, value: Type) -> None: ...


class SoapExtensionTypeElementCollection(ConfigurationElementCollection):
    def __init__(self): ...
    def Add(self, element: SoapExtensionTypeElement) -> None: ...
    def Clear(self) -> None: ...
    def ContainsKey(self, key: Object) -> bool: ...
    @overload
    def CopyTo(self, array: Set(SoapExtensionTypeElement), index: int) -> None: ...
    @property
    def Item(self, key: Object) -> SoapExtensionTypeElement: ...
    @property
    def Item(self, index: int) -> SoapExtensionTypeElement: ...
    def IndexOf(self, element: SoapExtensionTypeElement) -> int: ...
    def Remove(self, element: SoapExtensionTypeElement) -> None: ...
    @overload
    def RemoveAt(self, key: Object) -> None: ...
    @overload
    def RemoveAt(self, index: int) -> None: ...
    @Item.setter
    def Item(self, index: int, value: SoapExtensionTypeElement) -> None: ...
    @Item.setter
    def Item(self, key: Object, value: SoapExtensionTypeElement) -> None: ...


class TypeElement(ConfigurationElement):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, type: str): ...
    @overload
    def __init__(self, type: Type): ...
    @property
    def Type(self) -> Type: ...
    @Type.setter
    def Type(self, value: Type) -> None: ...


class TypeElementCollection(ConfigurationElementCollection):
    def __init__(self): ...
    def Add(self, element: TypeElement) -> None: ...
    def Clear(self) -> None: ...
    def ContainsKey(self, key: Object) -> bool: ...
    @overload
    def CopyTo(self, array: Set(TypeElement), index: int) -> None: ...
    @property
    def Item(self, key: Object) -> TypeElement: ...
    @property
    def Item(self, index: int) -> TypeElement: ...
    def IndexOf(self, element: TypeElement) -> int: ...
    def Remove(self, element: TypeElement) -> None: ...
    @overload
    def RemoveAt(self, key: Object) -> None: ...
    @overload
    def RemoveAt(self, index: int) -> None: ...
    @Item.setter
    def Item(self, index: int, value: TypeElement) -> None: ...
    @Item.setter
    def Item(self, key: Object, value: TypeElement) -> None: ...


class WebServiceProtocols:
    Unknown = 0
    HttpSoap = 1
    HttpGet = 2
    HttpPost = 4
    Documentation = 8
    HttpPostLocalhost = 16
    HttpSoap12 = 32
    AnyHttpSoap = 33


class WebServicesSection(ConfigurationSection):
    def __init__(self): ...
    @property
    def ConformanceWarnings(self) -> WsiProfilesElementCollection: ...
    @property
    def Current() -> WebServicesSection: ...
    @property
    def Diagnostics(self) -> DiagnosticsElement: ...
    @property
    def EnabledProtocols(self) -> WebServiceProtocols: ...
    @property
    def Protocols(self) -> ProtocolElementCollection: ...
    @property
    def ServiceDescriptionFormatExtensionTypes(self) -> TypeElementCollection: ...
    @property
    def SoapEnvelopeProcessing(self) -> SoapEnvelopeProcessingElement: ...
    @property
    def SoapExtensionImporterTypes(self) -> TypeElementCollection: ...
    @property
    def SoapExtensionReflectorTypes(self) -> TypeElementCollection: ...
    @property
    def SoapExtensionTypes(self) -> SoapExtensionTypeElementCollection: ...
    @property
    def SoapServerProtocolFactoryType(self) -> TypeElement: ...
    @property
    def SoapTransportImporterTypes(self) -> TypeElementCollection: ...
    @property
    def WsdlHelpGenerator(self) -> WsdlHelpGeneratorElement: ...
    def GetSection(config: Configuration) -> WebServicesSection: ...
    @Diagnostics.setter
    def Diagnostics(self, value: DiagnosticsElement) -> None: ...
    @SoapEnvelopeProcessing.setter
    def SoapEnvelopeProcessing(self, value: SoapEnvelopeProcessingElement) -> None: ...


class WsdlHelpGeneratorElement(ConfigurationElement):
    def __init__(self): ...
    @property
    def Href(self) -> str: ...
    @Href.setter
    def Href(self, value: str) -> None: ...


class WsiProfilesElement(ConfigurationElement):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, name: WsiProfiles): ...
    @property
    def Name(self) -> WsiProfiles: ...
    @Name.setter
    def Name(self, value: WsiProfiles) -> None: ...


class WsiProfilesElementCollection(ConfigurationElementCollection):
    def __init__(self): ...
    def Add(self, element: WsiProfilesElement) -> None: ...
    def Clear(self) -> None: ...
    def ContainsKey(self, key: Object) -> bool: ...
    @overload
    def CopyTo(self, array: Set(WsiProfilesElement), index: int) -> None: ...
    @property
    def Item(self, key: Object) -> WsiProfilesElement: ...
    @property
    def Item(self, index: int) -> WsiProfilesElement: ...
    def IndexOf(self, element: WsiProfilesElement) -> int: ...
    def Remove(self, element: WsiProfilesElement) -> None: ...
    @overload
    def RemoveAt(self, key: Object) -> None: ...
    @overload
    def RemoveAt(self, index: int) -> None: ...
    @Item.setter
    def Item(self, index: int, value: WsiProfilesElement) -> None: ...
    @Item.setter
    def Item(self, key: Object, value: WsiProfilesElement) -> None: ...


class XmlFormatExtensionAttribute(Attribute):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, elementName: str, ns: str, extensionPoint1: Type): ...
    @overload
    def __init__(self, elementName: str, ns: str, extensionPoints: Set(Type)): ...
    @overload
    def __init__(self, elementName: str, ns: str, extensionPoint1: Type, extensionPoint2: Type): ...
    @overload
    def __init__(self, elementName: str, ns: str, extensionPoint1: Type, extensionPoint2: Type, extensionPoint3: Type): ...
    @overload
    def __init__(self, elementName: str, ns: str, extensionPoint1: Type, extensionPoint2: Type, extensionPoint3: Type, extensionPoint4: Type): ...
    @property
    def ElementName(self) -> str: ...
    @property
    def ExtensionPoints(self) -> Set(Type): ...
    @property
    def Namespace(self) -> str: ...
    @ElementName.setter
    def ElementName(self, value: str) -> None: ...
    @ExtensionPoints.setter
    def ExtensionPoints(self, value: Set(Type)) -> None: ...
    @Namespace.setter
    def Namespace(self, value: str) -> None: ...


class XmlFormatExtensionPointAttribute(Attribute):
    def __init__(self, memberName: str): ...
    @property
    def AllowElements(self) -> bool: ...
    @property
    def MemberName(self) -> str: ...
    @AllowElements.setter
    def AllowElements(self, value: bool) -> None: ...
    @MemberName.setter
    def MemberName(self, value: str) -> None: ...


class XmlFormatExtensionPrefixAttribute(Attribute):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, prefix: str, ns: str): ...
    @property
    def Namespace(self) -> str: ...
    @property
    def Prefix(self) -> str: ...
    @Namespace.setter
    def Namespace(self, value: str) -> None: ...
    @Prefix.setter
    def Prefix(self, value: str) -> None: ...
