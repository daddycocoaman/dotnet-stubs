__all__ = ['Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Tokens','Tokens']
from typing import Tuple, Set, Iterable, List


class WSFederationAuthenticationModule(HttpModuleBase):
    def __init__(self): ...
    def add_AuthorizationFailed(self, value: EventHandler) -> None: ...
    def add_RedirectingToIdentityProvider(self, value: EventHandler) -> None: ...
    def add_SecurityTokenReceived(self, value: EventHandler) -> None: ...
    def add_SecurityTokenValidated(self, value: EventHandler) -> None: ...
    def add_SessionSecurityTokenCreated(self, value: EventHandler) -> None: ...
    def add_SignedIn(self, value: EventHandler) -> None: ...
    def add_SignedOut(self, value: EventHandler) -> None: ...
    def add_SignInError(self, value: EventHandler) -> None: ...
    def add_SigningOut(self, value: EventHandler) -> None: ...
    def add_SignOutError(self, value: EventHandler) -> None: ...
    @overload
    def CanReadSignInResponse(self, request: HttpRequestBase) -> bool: ...
    @overload
    def CanReadSignInResponse(self, request: HttpRequestBase, onPage: bool) -> bool: ...
    def CreateSignInRequest(self, uniqueId: str, returnUrl: str, rememberMeSet: bool) -> SignInRequestMessage: ...
    def FederatedSignOut(signOutUrl: Uri, replyUrl: Uri) -> None: ...
    @property
    def AuthenticationType(self) -> str: ...
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
    def SignInContext(self) -> str: ...
    @property
    def SignInQueryString(self) -> str: ...
    @property
    def SignOutQueryString(self) -> str: ...
    @property
    def SignOutReply(self) -> str: ...
    @property
    def XmlDictionaryReaderQuotas(self) -> XmlDictionaryReaderQuotas: ...
    def GetFederationPassiveSignOutUrl(issuer: str, signOutReply: str, signOutQueryString: str) -> str: ...
    @overload
    def GetSecurityToken(self, message: SignInResponseMessage) -> SecurityToken: ...
    @overload
    def GetSecurityToken(self, request: HttpRequestBase) -> SecurityToken: ...
    def GetSignInResponseMessage(self, request: HttpRequestBase) -> SignInResponseMessage: ...
    @overload
    def GetXmlTokenFromMessage(self, message: SignInResponseMessage) -> str: ...
    @overload
    def GetXmlTokenFromMessage(self, message: SignInResponseMessage, federationSerializer: WSFederationSerializer) -> str: ...
    def IsSignInResponse(self, request: HttpRequestBase) -> bool: ...
    def RedirectToIdentityProvider(self, uniqueId: str, returnUrl: str, persist: bool) -> None: ...
    def remove_AuthorizationFailed(self, value: EventHandler) -> None: ...
    def remove_RedirectingToIdentityProvider(self, value: EventHandler) -> None: ...
    def remove_SecurityTokenReceived(self, value: EventHandler) -> None: ...
    def remove_SecurityTokenValidated(self, value: EventHandler) -> None: ...
    def remove_SessionSecurityTokenCreated(self, value: EventHandler) -> None: ...
    def remove_SignedIn(self, value: EventHandler) -> None: ...
    def remove_SignedOut(self, value: EventHandler) -> None: ...
    def remove_SignInError(self, value: EventHandler) -> None: ...
    def remove_SigningOut(self, value: EventHandler) -> None: ...
    def remove_SignOutError(self, value: EventHandler) -> None: ...
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
    @SignInContext.setter
    def SignInContext(self, value: str) -> None: ...
    @SignInQueryString.setter
    def SignInQueryString(self, value: str) -> None: ...
    @SignOutQueryString.setter
    def SignOutQueryString(self, value: str) -> None: ...
    @SignOutReply.setter
    def SignOutReply(self, value: str) -> None: ...
    @XmlDictionaryReaderQuotas.setter
    def XmlDictionaryReaderQuotas(self, value: XmlDictionaryReaderQuotas) -> None: ...
    def SetPrincipalAndWriteSessionToken(self, sessionToken: SessionSecurityToken, isSession: bool) -> None: ...
    def SignIn(self, ControlId: str) -> None: ...
    @overload
    def SignOut(self) -> None: ...
    @overload
    def SignOut(self, isIPRequest: bool) -> None: ...
    @overload
    def SignOut(self, redirectUrl: str) -> None: ...
    @overload
    def SignOut(self, redirectUrl: str, initiateSignoutCleanup: bool) -> None: ...
    def VerifyProperties(self) -> None: ...
