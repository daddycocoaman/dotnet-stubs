from typing import Tuple, Set, Iterable, List


class FederationConfiguration(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, loadConfig: bool): ...
    @overload
    def __init__(self, federationConfigurationName: str): ...
    @property
    def CookieHandler(self) -> CookieHandler: ...
    @property
    def CustomElement(self) -> XmlElement: ...
    @property
    def IdentityConfiguration(self) -> IdentityConfiguration: ...
    @property
    def IsInitialized(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def ServiceCertificate(self) -> X509Certificate2: ...
    @property
    def WsFederationConfiguration(self) -> WsFederationConfiguration: ...
    def Initialize(self) -> None: ...
    @CookieHandler.setter
    def CookieHandler(self, value: CookieHandler) -> None: ...
    @CustomElement.setter
    def CustomElement(self, value: XmlElement) -> None: ...
    @IdentityConfiguration.setter
    def IdentityConfiguration(self, value: IdentityConfiguration) -> None: ...
    @ServiceCertificate.setter
    def ServiceCertificate(self, value: X509Certificate2) -> None: ...
    @WsFederationConfiguration.setter
    def WsFederationConfiguration(self, value: WsFederationConfiguration) -> None: ...


class FederationConfigurationCreatedEventArgs(EventArgs):
    def __init__(self, config: FederationConfiguration): ...
    @property
    def FederationConfiguration(self) -> FederationConfiguration: ...
    @FederationConfiguration.setter
    def FederationConfiguration(self, value: FederationConfiguration) -> None: ...


class FederationConfigurationElement(ConfigurationElement):
    def __init__(self): ...
    @property
    def CookieHandler(self) -> CookieHandlerElement: ...
    @property
    def CustomElement(self) -> XmlElement: ...
    @property
    def IdentityConfigurationName(self) -> str: ...
    @property
    def IsConfigured(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def ServiceCertificate(self) -> ServiceCertificateElement: ...
    @property
    def WsFederation(self) -> WSFederationElement: ...
    @CookieHandler.setter
    def CookieHandler(self, value: CookieHandlerElement) -> None: ...
    @CustomElement.setter
    def CustomElement(self, value: XmlElement) -> None: ...
    @IdentityConfigurationName.setter
    def IdentityConfigurationName(self, value: str) -> None: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    @ServiceCertificate.setter
    def ServiceCertificate(self, value: ServiceCertificateElement) -> None: ...
    @WsFederation.setter
    def WsFederation(self, value: WSFederationElement) -> None: ...


class FederationConfigurationElementCollection(ConfigurationElementCollection):
    def __init__(self): ...
    def GetElement(self, name: str) -> FederationConfigurationElement: ...


class SystemIdentityModelServicesSection(ConfigurationSection):
    def __init__(self): ...
    @property
    def Current() -> SystemIdentityModelServicesSection: ...
    @property
    def DefaultFederationConfigurationElement() -> FederationConfigurationElement: ...
    @property
    def FederationConfigurationElements(self) -> FederationConfigurationElementCollection: ...


class WsFederationConfiguration(Object):
    @overload
    def __init__(self, federationElement: WSFederationElement): ...
    @overload
    def __init__(self, issuer: str, realm: str): ...
    @property
    def AuthenticationType(self) -> str: ...
    @property
    def CustomAttributes(self) -> Dictionary: ...
    @property
    def Freshness(self) -> str: ...
    @property
    def HomeRealm(self) -> str: ...
    @property
    def Issuer(self) -> str: ...
    @property
    def PassiveRedirectEnabled(self) -> bool: ...
    @property
    def PersistentCookiesOnPassiveRedirects(self) -> bool: ...
    @property
    def Policy(self) -> str: ...
    @property
    def Realm(self) -> str: ...
    @property
    def Reply(self) -> str: ...
    @property
    def Request(self) -> str: ...
    @property
    def RequestPtr(self) -> str: ...
    @property
    def RequireHttps(self) -> bool: ...
    @property
    def Resource(self) -> str: ...
    @property
    def SignInQueryString(self) -> str: ...
    @property
    def SignOutQueryString(self) -> str: ...
    @property
    def SignOutReply(self) -> str: ...
    @property
    def XmlDictionaryReaderQuotas(self) -> XmlDictionaryReaderQuotas: ...
    @AuthenticationType.setter
    def AuthenticationType(self, value: str) -> None: ...
    @Freshness.setter
    def Freshness(self, value: str) -> None: ...
    @HomeRealm.setter
    def HomeRealm(self, value: str) -> None: ...
    @Issuer.setter
    def Issuer(self, value: str) -> None: ...
    @PassiveRedirectEnabled.setter
    def PassiveRedirectEnabled(self, value: bool) -> None: ...
    @PersistentCookiesOnPassiveRedirects.setter
    def PersistentCookiesOnPassiveRedirects(self, value: bool) -> None: ...
    @Policy.setter
    def Policy(self, value: str) -> None: ...
    @Realm.setter
    def Realm(self, value: str) -> None: ...
    @Reply.setter
    def Reply(self, value: str) -> None: ...
    @Request.setter
    def Request(self, value: str) -> None: ...
    @RequestPtr.setter
    def RequestPtr(self, value: str) -> None: ...
    @RequireHttps.setter
    def RequireHttps(self, value: bool) -> None: ...
    @Resource.setter
    def Resource(self, value: str) -> None: ...
    @SignInQueryString.setter
    def SignInQueryString(self, value: str) -> None: ...
    @SignOutQueryString.setter
    def SignOutQueryString(self, value: str) -> None: ...
    @SignOutReply.setter
    def SignOutReply(self, value: str) -> None: ...
    @XmlDictionaryReaderQuotas.setter
    def XmlDictionaryReaderQuotas(self, value: XmlDictionaryReaderQuotas) -> None: ...


class WSFederationElement(ConfigurationElement):
    def __init__(self): ...
    @property
    def AuthenticationType(self) -> str: ...
    @property
    def CustomAttributes(self) -> Dictionary: ...
    @property
    def Freshness(self) -> str: ...
    @property
    def HomeRealm(self) -> str: ...
    @property
    def IsConfigured(self) -> bool: ...
    @property
    def Issuer(self) -> str: ...
    @property
    def PassiveRedirectEnabled(self) -> bool: ...
    @property
    def PersistentCookiesOnPassiveRedirects(self) -> bool: ...
    @property
    def Policy(self) -> str: ...
    @property
    def Realm(self) -> str: ...
    @property
    def Reply(self) -> str: ...
    @property
    def Request(self) -> str: ...
    @property
    def RequestPtr(self) -> str: ...
    @property
    def RequireHttps(self) -> bool: ...
    @property
    def Resource(self) -> str: ...
    @property
    def SignInQueryString(self) -> str: ...
    @property
    def SignOutQueryString(self) -> str: ...
    @property
    def SignOutReply(self) -> str: ...
    @AuthenticationType.setter
    def AuthenticationType(self, value: str) -> None: ...
    @Freshness.setter
    def Freshness(self, value: str) -> None: ...
    @HomeRealm.setter
    def HomeRealm(self, value: str) -> None: ...
    @Issuer.setter
    def Issuer(self, value: str) -> None: ...
    @PassiveRedirectEnabled.setter
    def PassiveRedirectEnabled(self, value: bool) -> None: ...
    @PersistentCookiesOnPassiveRedirects.setter
    def PersistentCookiesOnPassiveRedirects(self, value: bool) -> None: ...
    @Policy.setter
    def Policy(self, value: str) -> None: ...
    @Realm.setter
    def Realm(self, value: str) -> None: ...
    @Reply.setter
    def Reply(self, value: str) -> None: ...
    @Request.setter
    def Request(self, value: str) -> None: ...
    @RequestPtr.setter
    def RequestPtr(self, value: str) -> None: ...
    @RequireHttps.setter
    def RequireHttps(self, value: bool) -> None: ...
    @Resource.setter
    def Resource(self, value: str) -> None: ...
    @SignInQueryString.setter
    def SignInQueryString(self, value: str) -> None: ...
    @SignOutQueryString.setter
    def SignOutQueryString(self, value: str) -> None: ...
    @SignOutReply.setter
    def SignOutReply(self, value: str) -> None: ...
