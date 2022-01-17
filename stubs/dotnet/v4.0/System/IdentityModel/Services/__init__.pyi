__all__ = ['Configuration','Tokens']
from typing import Tuple, Set, Iterable, List


class ApplicationType:
    AspNetWebApplication = 0
    WcfServiceApplication = 1


class AsynchronousOperationException(Exception):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, innerException: Exception): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class AttributeRequestMessage(WSFederationMessage):
    def __init__(self, baseUrl: Uri): ...
    @property
    def Attribute(self) -> str: ...
    @property
    def AttributePtr(self) -> str: ...
    @property
    def Reply(self) -> str: ...
    @property
    def Result(self) -> str: ...
    @property
    def ResultPtr(self) -> str: ...
    @Attribute.setter
    def Attribute(self, value: str) -> None: ...
    @AttributePtr.setter
    def AttributePtr(self, value: str) -> None: ...
    @Reply.setter
    def Reply(self, value: str) -> None: ...
    @Result.setter
    def Result(self, value: str) -> None: ...
    @ResultPtr.setter
    def ResultPtr(self, value: str) -> None: ...
    def Write(self, writer: TextWriter) -> None: ...


class AuthorizationFailedEventArgs(EventArgs):
    def __init__(self): ...
    @property
    def RedirectToIdentityProvider(self) -> bool: ...
    @RedirectToIdentityProvider.setter
    def RedirectToIdentityProvider(self, value: bool) -> None: ...


class ChunkedCookieHandler(CookieHandler):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, chunkSize: int): ...
    @property
    def ChunkSize(self) -> int: ...


class ChunkedCookieHandlerElement(ConfigurationElement):
    def __init__(self): ...
    @property
    def ChunkSize(self) -> int: ...
    @ChunkSize.setter
    def ChunkSize(self, value: int) -> None: ...


class ClaimsAuthorizationModule(HttpModuleBase):
    def __init__(self): ...
    def Dispose(self) -> None: ...
    @property
    def ClaimsAuthorizationManager(self) -> ClaimsAuthorizationManager: ...
    @ClaimsAuthorizationManager.setter
    def ClaimsAuthorizationManager(self, value: ClaimsAuthorizationManager) -> None: ...


class ClaimsPrincipalPermission(Object):
    def __init__(self, resource: str, action: str): ...
    def CheckAccess(resource: str, action: str) -> None: ...
    def Copy(self) -> IPermission: ...
    def Demand(self) -> None: ...
    def FromXml(self, element: SecurityElement) -> None: ...
    def Intersect(self, target: IPermission) -> IPermission: ...
    def IsSubsetOf(self, target: IPermission) -> bool: ...
    def IsUnrestricted(self) -> bool: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, target: IPermission) -> IPermission: ...


class ClaimsPrincipalPermissionAttribute(CodeAccessSecurityAttribute):
    def __init__(self, action: SecurityAction): ...
    def CreatePermission(self) -> IPermission: ...
    @property
    def Operation(self) -> str: ...
    @property
    def Resource(self) -> str: ...
    @Operation.setter
    def Operation(self, value: str) -> None: ...
    @Resource.setter
    def Resource(self, value: str) -> None: ...


class CookieHandler(Object):
    @overload
    def Delete(self) -> None: ...
    @overload
    def Delete(self, name: str) -> None: ...
    @overload
    def Delete(self, context: HttpContext) -> None: ...
    @overload
    def Delete(self, name: str, context: HttpContext) -> None: ...
    @overload
    def Delete(self, name: str, path: str, domain: str, context: HttpContext) -> None: ...
    @property
    def Domain(self) -> str: ...
    @property
    def HideFromClientScript(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def Path(self) -> str: ...
    @property
    def PersistentSessionLifetime(self) -> Nullable: ...
    @property
    def RequireSsl(self) -> bool: ...
    def MatchCookiePath(self, baseUri: Uri, targetUri: Uri) -> str: ...
    @overload
    def Read(self) -> Set(Byte): ...
    @overload
    def Read(self, name: str) -> Set(Byte): ...
    @overload
    def Read(self, context: HttpContext) -> Set(Byte): ...
    @overload
    def Read(self, name: str, context: HttpContext) -> Set(Byte): ...
    @Domain.setter
    def Domain(self, value: str) -> None: ...
    @HideFromClientScript.setter
    def HideFromClientScript(self, value: bool) -> None: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    @Path.setter
    def Path(self, value: str) -> None: ...
    @PersistentSessionLifetime.setter
    def PersistentSessionLifetime(self, value: Nullable) -> None: ...
    @RequireSsl.setter
    def RequireSsl(self, value: bool) -> None: ...
    @overload
    def Write(self, value: Set(Byte), name: str, expirationTime: DateTime) -> None: ...
    @overload
    def Write(self, value: Set(Byte), isPersistent: bool, tokenExpirationTime: DateTime) -> None: ...
    @overload
    def Write(self, value: Set(Byte), name: str, expirationTime: DateTime, context: HttpContext) -> None: ...
    @overload
    def Write(self, value: Set(Byte), name: str, path: str, domain: str, expirationTime: DateTime, requiresSsl: bool, hideFromClientScript: bool, context: HttpContext) -> None: ...


class CookieHandlerElement(ConfigurationElement):
    def __init__(self): ...
    @property
    def ChunkedCookieHandler(self) -> ChunkedCookieHandlerElement: ...
    @property
    def CustomCookieHandler(self) -> CustomTypeElement: ...
    @property
    def Domain(self) -> str: ...
    @property
    def HideFromScript(self) -> bool: ...
    @property
    def Mode(self) -> CookieHandlerMode: ...
    @property
    def Name(self) -> str: ...
    @property
    def Path(self) -> str: ...
    @property
    def PersistentSessionLifetime(self) -> TimeSpan: ...
    @property
    def RequireSsl(self) -> bool: ...
    def GetConfiguredCookieHandler(self) -> CookieHandler: ...
    @ChunkedCookieHandler.setter
    def ChunkedCookieHandler(self, value: ChunkedCookieHandlerElement) -> None: ...
    @CustomCookieHandler.setter
    def CustomCookieHandler(self, value: CustomTypeElement) -> None: ...
    @Domain.setter
    def Domain(self, value: str) -> None: ...
    @HideFromScript.setter
    def HideFromScript(self, value: bool) -> None: ...
    @Mode.setter
    def Mode(self, value: CookieHandlerMode) -> None: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    @Path.setter
    def Path(self, value: str) -> None: ...
    @PersistentSessionLifetime.setter
    def PersistentSessionLifetime(self, value: TimeSpan) -> None: ...
    @RequireSsl.setter
    def RequireSsl(self, value: bool) -> None: ...


class CookieHandlerMode:
    Default = 0
    Chunked = 1
    Custom = 2


class ErrorEventArgs(CancelEventArgs):
    @overload
    def __init__(self, exception: Exception): ...
    @overload
    def __init__(self, cancel: bool, exception: Exception): ...
    @property
    def Exception(self) -> Exception: ...


class FederatedAuthentication(Object):
    def add_FederationConfigurationCreated(value: EventHandler) -> None: ...
    @property
    def ClaimsAuthorizationModule() -> ClaimsAuthorizationModule: ...
    @property
    def FederationConfiguration() -> FederationConfiguration: ...
    @property
    def SessionAuthenticationModule() -> SessionAuthenticationModule: ...
    @property
    def WSFederationAuthenticationModule() -> WSFederationAuthenticationModule: ...
    def GetHttpModule() -> T: ...
    def remove_FederationConfigurationCreated(value: EventHandler) -> None: ...


class FederatedAuthenticationSessionEndingException(Exception):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, inner: Exception): ...


class FederatedPassiveSecurityTokenServiceOperations(Object):
    @overload
    def ProcessRequest(request: HttpRequest, principal: ClaimsPrincipal, sts: SecurityTokenService, response: HttpResponse) -> None: ...
    @overload
    def ProcessRequest(request: HttpRequest, principal: ClaimsPrincipal, sts: SecurityTokenService, response: HttpResponse, federationSerializer: WSFederationSerializer) -> None: ...
    @overload
    def ProcessSignInRequest(requestMessage: SignInRequestMessage, principal: ClaimsPrincipal, sts: SecurityTokenService) -> SignInResponseMessage: ...
    @overload
    def ProcessSignInRequest(requestMessage: SignInRequestMessage, principal: ClaimsPrincipal, sts: SecurityTokenService, federationSerializer: WSFederationSerializer) -> SignInResponseMessage: ...
    def ProcessSignInResponse(signInResponseMessage: SignInResponseMessage, httpResponse: HttpResponse) -> None: ...
    def ProcessSignOutRequest(requestMessage: FederationMessage, principal: ClaimsPrincipal, reply: str, httpResponse: HttpResponse) -> None: ...


class FederatedSessionExpiredException(FederatedAuthenticationSessionEndingException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, tested: DateTime, expired: DateTime): ...
    @overload
    def __init__(self, message: str, inner: Exception): ...
    @overload
    def __init__(self, tested: DateTime, expired: DateTime, inner: Exception): ...
    @property
    def Expired(self) -> DateTime: ...
    @property
    def Tested(self) -> DateTime: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...


class FederationException(Exception):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, inner: Exception): ...


class FederationManagement(Object):
    def CreateApplicationFederationMetadata(applicationUri: Uri, certificate: X509Certificate2, claimsRequired: Collection, applicationType: ApplicationType, audienceUris: Collection) -> XmlReader: ...
    @overload
    def UpdateIdentityProviderTrustInfo(metadataReader: XmlReader, inputConfiguration: XmlReader, claimsOfferedUpdate: bool) -> XmlReader: ...
    @overload
    def UpdateIdentityProviderTrustInfo(metadataReader: XmlReader, inputConfiguration: XmlReader, claimsOfferedUpdate: bool, metadataSerializer: MetadataSerializer) -> XmlReader: ...
    @overload
    def UpdateIdentityProviderTrustInfo(metadataReader: XmlReader, inputConfiguration: XmlReader) -> Tuple[XmlNodeReader, XmlNodeReader]: ...
    @overload
    def UpdateIdentityProviderTrustInfo(metadataReader: XmlReader, inputConfiguration: XmlReader, metadataSerializer: MetadataSerializer) -> Tuple[XmlNodeReader, XmlNodeReader]: ...


class FederationMessage(Object):
    @property
    def BaseUri(self) -> Uri: ...
    @property
    def Parameters(self) -> IDictionary: ...
    def GetBaseUrl(uri: Uri) -> Uri: ...
    def GetParameter(self, parameter: str) -> str: ...
    def ParseQueryString(data: Uri) -> NameValueCollection: ...
    def RemoveParameter(self, parameter: str) -> None: ...
    @BaseUri.setter
    def BaseUri(self, value: Uri) -> None: ...
    def SetParameter(self, parameter: str, value: str) -> None: ...
    def SetUriParameter(self, parameter: str, value: str) -> None: ...
    def Write(self, writer: TextWriter) -> None: ...
    def WriteFormPost(self) -> str: ...
    def WriteQueryString(self) -> str: ...


class HttpModuleBase(Object):
    def Dispose(self) -> None: ...
    @property
    def FederationConfiguration(self) -> FederationConfiguration: ...
    def Init(self, context: HttpApplication) -> None: ...
    @FederationConfiguration.setter
    def FederationConfiguration(self, value: FederationConfiguration) -> None: ...


class MachineKeyTransform(CookieTransform):
    def __init__(self): ...
    def Decode(self, encoded: Set(Byte)) -> Set(Byte): ...
    def Encode(self, value: Set(Byte)) -> Set(Byte): ...


class PseudonymRequestMessage(WSFederationMessage):
    def __init__(self, baseUrl: Uri): ...
    @property
    def Pseudonym(self) -> str: ...
    @property
    def PseudonymPtr(self) -> str: ...
    @property
    def Reply(self) -> str: ...
    @property
    def Result(self) -> str: ...
    @property
    def ResultPtr(self) -> str: ...
    @Pseudonym.setter
    def Pseudonym(self, value: str) -> None: ...
    @PseudonymPtr.setter
    def PseudonymPtr(self, value: str) -> None: ...
    @Reply.setter
    def Reply(self, value: str) -> None: ...
    @Result.setter
    def Result(self, value: str) -> None: ...
    @ResultPtr.setter
    def ResultPtr(self, value: str) -> None: ...
    def Write(self, writer: TextWriter) -> None: ...


class RedirectingToIdentityProviderEventArgs(CancelEventArgs):
    def __init__(self, signInRequestMessage: SignInRequestMessage): ...
    @property
    def SignInRequestMessage(self) -> SignInRequestMessage: ...
    @SignInRequestMessage.setter
    def SignInRequestMessage(self, value: SignInRequestMessage) -> None: ...


class SecurityTokenReceivedEventArgs(CancelEventArgs):
    @overload
    def __init__(self, securityToken: SecurityToken): ...
    @overload
    def __init__(self, securityToken: SecurityToken, signInContext: str): ...
    @property
    def SecurityToken(self) -> SecurityToken: ...
    @property
    def SignInContext(self) -> str: ...
    @SecurityToken.setter
    def SecurityToken(self, value: SecurityToken) -> None: ...


class SecurityTokenValidatedEventArgs(CancelEventArgs):
    def __init__(self, claimsPrincipal: ClaimsPrincipal): ...
    @property
    def ClaimsPrincipal(self) -> ClaimsPrincipal: ...
    @ClaimsPrincipal.setter
    def ClaimsPrincipal(self, value: ClaimsPrincipal) -> None: ...


class ServiceCertificateElement(ConfigurationElement):
    def __init__(self): ...
    @property
    def CertificateReference(self) -> CertificateReferenceElement: ...
    @CertificateReference.setter
    def CertificateReference(self, value: CertificateReferenceElement) -> None: ...


class SessionAuthenticationModule(HttpModuleBase):
    def __init__(self): ...
    def add_SessionSecurityTokenCreated(self, value: EventHandler) -> None: ...
    def add_SessionSecurityTokenReceived(self, value: EventHandler) -> None: ...
    def add_SignedOut(self, value: EventHandler) -> None: ...
    def add_SigningOut(self, value: EventHandler) -> None: ...
    def add_SignOutError(self, value: EventHandler) -> None: ...
    def AuthenticateSessionSecurityToken(self, sessionToken: SessionSecurityToken, writeCookie: bool) -> None: ...
    def ContainsSessionTokenCookie(self, httpCookieCollection: HttpCookieCollection) -> bool: ...
    def CreateSessionSecurityToken(self, principal: ClaimsPrincipal, context: str, validFrom: DateTime, validTo: DateTime, isPersistent: bool) -> SessionSecurityToken: ...
    def DeleteSessionTokenCookie(self) -> None: ...
    @property
    def ContextSessionSecurityToken(self) -> SessionSecurityToken: ...
    @property
    def CookieHandler(self) -> CookieHandler: ...
    @property
    def IsReferenceMode(self) -> bool: ...
    def ReadSessionTokenFromCookie(self, sessionCookie: Set(Byte)) -> SessionSecurityToken: ...
    def remove_SessionSecurityTokenCreated(self, value: EventHandler) -> None: ...
    def remove_SessionSecurityTokenReceived(self, value: EventHandler) -> None: ...
    def remove_SignedOut(self, value: EventHandler) -> None: ...
    def remove_SigningOut(self, value: EventHandler) -> None: ...
    def remove_SignOutError(self, value: EventHandler) -> None: ...
    @CookieHandler.setter
    def CookieHandler(self, value: CookieHandler) -> None: ...
    @IsReferenceMode.setter
    def IsReferenceMode(self, value: bool) -> None: ...
    def SignOut(self) -> None: ...
    def TryReadSessionTokenFromCookie(self) -> Tuple[bool, SessionSecurityToken]: ...
    def WriteSessionTokenToCookie(self, sessionToken: SessionSecurityToken) -> None: ...


class SessionSecurityTokenCreatedEventArgs(EventArgs):
    def __init__(self, sessionToken: SessionSecurityToken): ...
    @property
    def SessionToken(self) -> SessionSecurityToken: ...
    @property
    def WriteSessionCookie(self) -> bool: ...
    @SessionToken.setter
    def SessionToken(self, value: SessionSecurityToken) -> None: ...
    @WriteSessionCookie.setter
    def WriteSessionCookie(self, value: bool) -> None: ...


class SessionSecurityTokenReceivedEventArgs(CancelEventArgs):
    def __init__(self, sessionToken: SessionSecurityToken): ...
    @property
    def ReissueCookie(self) -> bool: ...
    @property
    def SessionToken(self) -> SessionSecurityToken: ...
    @ReissueCookie.setter
    def ReissueCookie(self, value: bool) -> None: ...
    @SessionToken.setter
    def SessionToken(self, value: SessionSecurityToken) -> None: ...


class SessionSecurityTokenResolver(SecurityTokenResolver):
    def __init__(self, tokenCache: SessionSecurityTokenCache, endpointId: str): ...


class SigningOutEventArgs(EventArgs):
    def __init__(self, isIPInitiated: bool): ...
    @property
    def IPInitiated() -> SigningOutEventArgs: ...
    @property
    def IsIPInitiated(self) -> bool: ...
    @property
    def RPInitiated() -> SigningOutEventArgs: ...


class SignInRequestMessage(WSFederationMessage):
    @overload
    def __init__(self, baseUrl: Uri, realm: str): ...
    @overload
    def __init__(self, baseUrl: Uri, realm: str, reply: str): ...
    @property
    def AuthenticationType(self) -> str: ...
    @property
    def CurrentTime(self) -> str: ...
    @property
    def Federation(self) -> str: ...
    @property
    def Freshness(self) -> str: ...
    @property
    def HomeRealm(self) -> str: ...
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
    def RequestUrl(self) -> str: ...
    @property
    def Resource(self) -> str: ...
    @AuthenticationType.setter
    def AuthenticationType(self, value: str) -> None: ...
    @CurrentTime.setter
    def CurrentTime(self, value: str) -> None: ...
    @Federation.setter
    def Federation(self, value: str) -> None: ...
    @Freshness.setter
    def Freshness(self, value: str) -> None: ...
    @HomeRealm.setter
    def HomeRealm(self, value: str) -> None: ...
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
    @Resource.setter
    def Resource(self, value: str) -> None: ...
    def Write(self, writer: TextWriter) -> None: ...


class SignInResponseMessage(WSFederationMessage):
    @overload
    def __init__(self, baseUrl: Uri, result: str): ...
    @overload
    def __init__(self, baseUrl: Uri, resultPtr: Uri): ...
    @overload
    def __init__(self, baseUrl: Uri, response: RequestSecurityTokenResponse, federationSerializer: WSFederationSerializer, context: WSTrustSerializationContext): ...
    @property
    def Result(self) -> str: ...
    @property
    def ResultPtr(self) -> str: ...
    @Result.setter
    def Result(self, value: str) -> None: ...
    @ResultPtr.setter
    def ResultPtr(self, value: str) -> None: ...
    def Write(self, writer: TextWriter) -> None: ...


class SignOutCleanupRequestMessage(WSFederationMessage):
    @overload
    def __init__(self, baseUrl: Uri): ...
    @overload
    def __init__(self, baseUrl: Uri, reply: str): ...
    @property
    def Reply(self) -> str: ...
    @Reply.setter
    def Reply(self, value: str) -> None: ...
    def Write(self, writer: TextWriter) -> None: ...


class SignOutRequestMessage(WSFederationMessage):
    @overload
    def __init__(self, baseUrl: Uri): ...
    @overload
    def __init__(self, baseUrl: Uri, reply: str): ...
    @property
    def Reply(self) -> str: ...
    @Reply.setter
    def Reply(self, value: str) -> None: ...
    def Write(self, writer: TextWriter) -> None: ...


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


class WSFederationMessage(FederationMessage):
    def __init__(self, baseUrl: Uri, action: str): ...
    def CreateFromFormPost(request: HttpRequestBase) -> WSFederationMessage: ...
    def CreateFromNameValueCollection(baseUrl: Uri, collection: NameValueCollection) -> WSFederationMessage: ...
    def CreateFromUri(requestUri: Uri) -> WSFederationMessage: ...
    @property
    def Action(self) -> str: ...
    @property
    def Context(self) -> str: ...
    @property
    def Encoding(self) -> str: ...
    @Action.setter
    def Action(self, value: str) -> None: ...
    @Context.setter
    def Context(self, value: str) -> None: ...
    @Encoding.setter
    def Encoding(self, value: str) -> None: ...
    def TryCreateFromUri(requestUri: Uri) -> Tuple[bool, WSFederationMessage]: ...


class WSFederationMessageException(Exception):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, inner: Exception): ...


class WSFederationSerializer(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, reader: XmlDictionaryReader): ...
    @overload
    def __init__(self, requestSerializer: WSTrustRequestSerializer, responseSerializer: WSTrustResponseSerializer): ...
    def CanReadRequest(self, trustMessage: str) -> bool: ...
    def CanReadResponse(self, trustMessage: str) -> bool: ...
    def CreateRequest(self, message: FederationMessage, context: WSTrustSerializationContext) -> RequestSecurityToken: ...
    def CreateResponse(self, message: FederationMessage, context: WSTrustSerializationContext) -> RequestSecurityTokenResponse: ...
    def GetReferencedRequest(self, wreqptr: str) -> str: ...
    def GetReferencedResult(self, wresultptr: str) -> str: ...
    def GetRequestAsString(self, request: RequestSecurityToken, context: WSTrustSerializationContext) -> str: ...
    def GetResponseAsString(self, response: RequestSecurityTokenResponse, context: WSTrustSerializationContext) -> str: ...
