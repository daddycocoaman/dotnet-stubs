__all__ = ['Infrastructure']
from typing import Tuple, Set, Iterable, List


class CompiledPageActionDescriptor(PageActionDescriptor):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, actionDescriptor: PageActionDescriptor): ...
    @property
    def DeclaredModelTypeInfo(self) -> TypeInfo: ...
    @property
    def Endpoint(self) -> Endpoint: ...
    @property
    def HandlerMethods(self) -> List[HandlerMethodDescriptor]: ...
    @property
    def HandlerTypeInfo(self) -> TypeInfo: ...
    @property
    def ModelTypeInfo(self) -> TypeInfo: ...
    @property
    def PageTypeInfo(self) -> TypeInfo: ...
    @DeclaredModelTypeInfo.setter
    def DeclaredModelTypeInfo(self, value: TypeInfo) -> None: ...
    @Endpoint.setter
    def Endpoint(self, value: Endpoint) -> None: ...
    @HandlerMethods.setter
    def HandlerMethods(self, value: List[HandlerMethodDescriptor]) -> None: ...
    @HandlerTypeInfo.setter
    def HandlerTypeInfo(self, value: TypeInfo) -> None: ...
    @ModelTypeInfo.setter
    def ModelTypeInfo(self, value: TypeInfo) -> None: ...
    @PageTypeInfo.setter
    def PageTypeInfo(self, value: TypeInfo) -> None: ...


class IPageActivatorProvider:
    def CreateActivator(self, descriptor: CompiledPageActionDescriptor) -> Func`3: ...
    def CreateAsyncReleaser(self, descriptor: CompiledPageActionDescriptor) -> Func`4: ...
    def CreateReleaser(self, descriptor: CompiledPageActionDescriptor) -> Action`3: ...


class IPageFactoryProvider:
    def CreateAsyncPageDisposer(self, descriptor: CompiledPageActionDescriptor) -> Func`4: ...
    def CreatePageDisposer(self, descriptor: CompiledPageActionDescriptor) -> Action`3: ...
    def CreatePageFactory(self, descriptor: CompiledPageActionDescriptor) -> Func`3: ...


class IPageModelActivatorProvider:
    def CreateActivator(self, descriptor: CompiledPageActionDescriptor) -> Func: ...
    def CreateAsyncReleaser(self, descriptor: CompiledPageActionDescriptor) -> Func`3: ...
    def CreateReleaser(self, descriptor: CompiledPageActionDescriptor) -> Action: ...


class IPageModelFactoryProvider:
    def CreateAsyncModelDisposer(self, descriptor: CompiledPageActionDescriptor) -> Func`3: ...
    def CreateModelDisposer(self, descriptor: CompiledPageActionDescriptor) -> Action: ...
    def CreateModelFactory(self, descriptor: CompiledPageActionDescriptor) -> Func: ...


class NonHandlerAttribute:
    def __init__(self): ...


class Page(PageBase):
    pass


class PageActionDescriptor(ActionDescriptor):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, other: PageActionDescriptor): ...
    @property
    def AreaName(self) -> str: ...
    @property
    def DisplayName(self) -> str: ...
    @property
    def RelativePath(self) -> str: ...
    @property
    def ViewEnginePath(self) -> str: ...
    @AreaName.setter
    def AreaName(self, value: str) -> None: ...
    @DisplayName.setter
    def DisplayName(self, value: str) -> None: ...
    @RelativePath.setter
    def RelativePath(self, value: str) -> None: ...
    @ViewEnginePath.setter
    def ViewEnginePath(self, value: str) -> None: ...


class PageBase(RazorPageBase):
    @overload
    def BadRequest(self) -> BadRequestResult: ...
    @overload
    def BadRequest(self, modelState: ModelStateDictionary) -> BadRequestObjectResult: ...
    @overload
    def BadRequest(self, error: Object) -> BadRequestObjectResult: ...
    def BeginContext(self, position: int, length: int, isLiteral: bool) -> None: ...
    @overload
    def Challenge(self) -> ChallengeResult: ...
    @overload
    def Challenge(self, properties: AuthenticationProperties) -> ChallengeResult: ...
    @overload
    def Challenge(self, authenticationSchemes: Set(str)) -> ChallengeResult: ...
    @overload
    def Challenge(self, properties: AuthenticationProperties, authenticationSchemes: Set(str)) -> ChallengeResult: ...
    @overload
    def Content(self, content: str) -> ContentResult: ...
    @overload
    def Content(self, content: str, contentType: str) -> ContentResult: ...
    @overload
    def Content(self, content: str, contentType: MediaTypeHeaderValue) -> ContentResult: ...
    @overload
    def Content(self, content: str, contentType: str, contentEncoding: Encoding) -> ContentResult: ...
    def EndContext(self) -> None: ...
    def EnsureRenderedBodyOrSections(self) -> None: ...
    @overload
    def File(self, fileStream: Stream, contentType: str) -> FileStreamResult: ...
    @overload
    def File(self, virtualPath: str, contentType: str) -> VirtualFileResult: ...
    @overload
    def File(self, fileContents: Set(Byte), contentType: str) -> FileContentResult: ...
    @overload
    def File(self, virtualPath: str, contentType: str, fileDownloadName: str) -> VirtualFileResult: ...
    @overload
    def File(self, fileStream: Stream, contentType: str, fileDownloadName: str) -> FileStreamResult: ...
    @overload
    def File(self, fileContents: Set(Byte), contentType: str, fileDownloadName: str) -> FileContentResult: ...
    @overload
    def Forbid(self) -> ForbidResult: ...
    @overload
    def Forbid(self, properties: AuthenticationProperties) -> ForbidResult: ...
    @overload
    def Forbid(self, authenticationSchemes: Set(str)) -> ForbidResult: ...
    @overload
    def Forbid(self, properties: AuthenticationProperties, authenticationSchemes: Set(str)) -> ForbidResult: ...
    @property
    def HttpContext(self) -> HttpContext: ...
    @property
    def MetadataProvider(self) -> IModelMetadataProvider: ...
    @property
    def ModelState(self) -> ModelStateDictionary: ...
    @property
    def PageContext(self) -> PageContext: ...
    @property
    def Request(self) -> HttpRequest: ...
    @property
    def Response(self) -> HttpResponse: ...
    @property
    def RouteData(self) -> RouteData: ...
    @property
    def ViewContext(self) -> ViewContext: ...
    def LocalRedirect(self, localUrl: str) -> LocalRedirectResult: ...
    def LocalRedirectPermanent(self, localUrl: str) -> LocalRedirectResult: ...
    def LocalRedirectPermanentPreserveMethod(self, localUrl: str) -> LocalRedirectResult: ...
    def LocalRedirectPreserveMethod(self, localUrl: str) -> LocalRedirectResult: ...
    @overload
    def NotFound(self) -> NotFoundResult: ...
    @overload
    def NotFound(self, value: Object) -> NotFoundObjectResult: ...
    def Page(self) -> PageResult: ...
    @overload
    def Partial(self, viewName: str) -> PartialViewResult: ...
    @overload
    def Partial(self, viewName: str, model: Object) -> PartialViewResult: ...
    @overload
    def PhysicalFile(self, physicalPath: str, contentType: str) -> PhysicalFileResult: ...
    @overload
    def PhysicalFile(self, physicalPath: str, contentType: str, fileDownloadName: str) -> PhysicalFileResult: ...
    def Redirect(self, url: str) -> RedirectResult: ...
    def RedirectPermanent(self, url: str) -> RedirectResult: ...
    def RedirectPermanentPreserveMethod(self, url: str) -> RedirectResult: ...
    def RedirectPreserveMethod(self, url: str) -> RedirectResult: ...
    @overload
    def RedirectToAction(self, actionName: str) -> RedirectToActionResult: ...
    @overload
    def RedirectToAction(self, actionName: str, routeValues: Object) -> RedirectToActionResult: ...
    @overload
    def RedirectToAction(self, actionName: str, controllerName: str) -> RedirectToActionResult: ...
    @overload
    def RedirectToAction(self, actionName: str, controllerName: str, routeValues: Object) -> RedirectToActionResult: ...
    @overload
    def RedirectToAction(self, actionName: str, controllerName: str, fragment: str) -> RedirectToActionResult: ...
    @overload
    def RedirectToAction(self, actionName: str, controllerName: str, routeValues: Object, fragment: str) -> RedirectToActionResult: ...
    @overload
    def RedirectToActionPermanent(self, actionName: str) -> RedirectToActionResult: ...
    @overload
    def RedirectToActionPermanent(self, actionName: str, routeValues: Object) -> RedirectToActionResult: ...
    @overload
    def RedirectToActionPermanent(self, actionName: str, controllerName: str) -> RedirectToActionResult: ...
    @overload
    def RedirectToActionPermanent(self, actionName: str, controllerName: str, fragment: str) -> RedirectToActionResult: ...
    @overload
    def RedirectToActionPermanent(self, actionName: str, controllerName: str, routeValues: Object) -> RedirectToActionResult: ...
    @overload
    def RedirectToActionPermanent(self, actionName: str, controllerName: str, routeValues: Object, fragment: str) -> RedirectToActionResult: ...
    def RedirectToActionPermanentPreserveMethod(self, actionName: str, controllerName: str, routeValues: Object, fragment: str) -> RedirectToActionResult: ...
    def RedirectToActionPreserveMethod(self, actionName: str, controllerName: str, routeValues: Object, fragment: str) -> RedirectToActionResult: ...
    @overload
    def RedirectToPage(self) -> RedirectToPageResult: ...
    @overload
    def RedirectToPage(self, routeValues: Object) -> RedirectToPageResult: ...
    @overload
    def RedirectToPage(self, pageName: str) -> RedirectToPageResult: ...
    @overload
    def RedirectToPage(self, pageName: str, routeValues: Object) -> RedirectToPageResult: ...
    @overload
    def RedirectToPage(self, pageName: str, pageHandler: str) -> RedirectToPageResult: ...
    @overload
    def RedirectToPage(self, pageName: str, pageHandler: str, fragment: str) -> RedirectToPageResult: ...
    @overload
    def RedirectToPage(self, pageName: str, pageHandler: str, routeValues: Object, fragment: str) -> RedirectToPageResult: ...
    @overload
    def RedirectToPagePermanent(self, pageName: str) -> RedirectToPageResult: ...
    @overload
    def RedirectToPagePermanent(self, pageName: str, pageHandler: str) -> RedirectToPageResult: ...
    @overload
    def RedirectToPagePermanent(self, pageName: str, routeValues: Object) -> RedirectToPageResult: ...
    @overload
    def RedirectToPagePermanent(self, pageName: str, pageHandler: str, routeValues: Object) -> RedirectToPageResult: ...
    @overload
    def RedirectToPagePermanent(self, pageName: str, pageHandler: str, fragment: str) -> RedirectToPageResult: ...
    @overload
    def RedirectToPagePermanent(self, pageName: str, pageHandler: str, routeValues: Object, fragment: str) -> RedirectToPageResult: ...
    def RedirectToPagePermanentPreserveMethod(self, pageName: str, pageHandler: str, routeValues: Object, fragment: str) -> RedirectToPageResult: ...
    def RedirectToPagePreserveMethod(self, pageName: str, pageHandler: str, routeValues: Object, fragment: str) -> RedirectToPageResult: ...
    @overload
    def RedirectToRoute(self, routeValues: Object) -> RedirectToRouteResult: ...
    @overload
    def RedirectToRoute(self, routeName: str) -> RedirectToRouteResult: ...
    @overload
    def RedirectToRoute(self, routeName: str, routeValues: Object) -> RedirectToRouteResult: ...
    @overload
    def RedirectToRoute(self, routeName: str, fragment: str) -> RedirectToRouteResult: ...
    @overload
    def RedirectToRoute(self, routeName: str, routeValues: Object, fragment: str) -> RedirectToRouteResult: ...
    @overload
    def RedirectToRoutePermanent(self, routeName: str) -> RedirectToRouteResult: ...
    @overload
    def RedirectToRoutePermanent(self, routeValues: Object) -> RedirectToRouteResult: ...
    @overload
    def RedirectToRoutePermanent(self, routeName: str, routeValues: Object) -> RedirectToRouteResult: ...
    @overload
    def RedirectToRoutePermanent(self, routeName: str, fragment: str) -> RedirectToRouteResult: ...
    @overload
    def RedirectToRoutePermanent(self, routeName: str, routeValues: Object, fragment: str) -> RedirectToRouteResult: ...
    def RedirectToRoutePermanentPreserveMethod(self, routeName: str, routeValues: Object, fragment: str) -> RedirectToRouteResult: ...
    def RedirectToRoutePreserveMethod(self, routeName: str, routeValues: Object, fragment: str) -> RedirectToRouteResult: ...
    @MetadataProvider.setter
    def MetadataProvider(self, value: IModelMetadataProvider) -> None: ...
    @PageContext.setter
    def PageContext(self, value: PageContext) -> None: ...
    @ViewContext.setter
    def ViewContext(self, value: ViewContext) -> None: ...
    @overload
    def SignIn(self, principal: ClaimsPrincipal, authenticationScheme: str) -> SignInResult: ...
    @overload
    def SignIn(self, principal: ClaimsPrincipal, properties: AuthenticationProperties, authenticationScheme: str) -> SignInResult: ...
    @overload
    def SignOut(self, authenticationSchemes: Set(str)) -> SignOutResult: ...
    @overload
    def SignOut(self, properties: AuthenticationProperties, authenticationSchemes: Set(str)) -> SignOutResult: ...
    @overload
    def StatusCode(self, statusCode: int) -> StatusCodeResult: ...
    @overload
    def StatusCode(self, statusCode: int, value: Object) -> ObjectResult: ...
    @overload
    def TryUpdateModelAsync(self, model: TModel) -> Task: ...
    @overload
    def TryUpdateModelAsync(self, model: TModel, prefix: str) -> Task: ...
    @overload
    def TryUpdateModelAsync(self, model: TModel, prefix: str, propertyFilter: Func) -> Task: ...
    @overload
    def TryUpdateModelAsync(self, model: TModel, prefix: str, includeExpressions: Set(Expression)) -> Task: ...
    @overload
    def TryUpdateModelAsync(self, model: TModel, prefix: str, valueProvider: IValueProvider) -> Task: ...
    @overload
    def TryUpdateModelAsync(self, model: Object, modelType: Type, prefix: str) -> Task: ...
    @overload
    def TryUpdateModelAsync(self, model: TModel, prefix: str, valueProvider: IValueProvider, propertyFilter: Func) -> Task: ...
    @overload
    def TryUpdateModelAsync(self, model: TModel, prefix: str, valueProvider: IValueProvider, includeExpressions: Set(Expression)) -> Task: ...
    @overload
    def TryUpdateModelAsync(self, model: Object, modelType: Type, prefix: str, valueProvider: IValueProvider, propertyFilter: Func) -> Task: ...
    @overload
    def TryValidateModel(self, model: Object) -> bool: ...
    @overload
    def TryValidateModel(self, model: Object, prefix: str) -> bool: ...
    def Unauthorized(self) -> UnauthorizedResult: ...
    @overload
    def ViewComponent(self, componentName: str) -> ViewComponentResult: ...
    @overload
    def ViewComponent(self, componentType: Type) -> ViewComponentResult: ...
    @overload
    def ViewComponent(self, componentName: str, arguments: Object) -> ViewComponentResult: ...
    @overload
    def ViewComponent(self, componentType: Type, arguments: Object) -> ViewComponentResult: ...


class PageContext(ActionContext):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, actionContext: ActionContext): ...
    @property
    def ActionDescriptor(self) -> CompiledPageActionDescriptor: ...
    @property
    def ValueProviderFactories(self) -> List[IValueProviderFactory]: ...
    @property
    def ViewData(self) -> ViewDataDictionary: ...
    @property
    def ViewStartFactories(self) -> List[IRazorPage]: ...
    @ActionDescriptor.setter
    def ActionDescriptor(self, value: CompiledPageActionDescriptor) -> None: ...
    @ValueProviderFactories.setter
    def ValueProviderFactories(self, value: List[IValueProviderFactory]) -> None: ...
    @ViewData.setter
    def ViewData(self, value: ViewDataDictionary) -> None: ...
    @ViewStartFactories.setter
    def ViewStartFactories(self, value: List[IRazorPage]) -> None: ...


class PageContextAttribute:
    def __init__(self): ...


class PageModel:
    @overload
    def BadRequest(self) -> BadRequestResult: ...
    @overload
    def BadRequest(self, modelState: ModelStateDictionary) -> BadRequestObjectResult: ...
    @overload
    def BadRequest(self, error: Object) -> BadRequestObjectResult: ...
    @overload
    def Challenge(self) -> ChallengeResult: ...
    @overload
    def Challenge(self, properties: AuthenticationProperties) -> ChallengeResult: ...
    @overload
    def Challenge(self, authenticationSchemes: Set(str)) -> ChallengeResult: ...
    @overload
    def Challenge(self, properties: AuthenticationProperties, authenticationSchemes: Set(str)) -> ChallengeResult: ...
    @overload
    def Content(self, content: str) -> ContentResult: ...
    @overload
    def Content(self, content: str, contentType: str) -> ContentResult: ...
    @overload
    def Content(self, content: str, contentType: MediaTypeHeaderValue) -> ContentResult: ...
    @overload
    def Content(self, content: str, contentType: str, contentEncoding: Encoding) -> ContentResult: ...
    @overload
    def File(self, virtualPath: str, contentType: str) -> VirtualFileResult: ...
    @overload
    def File(self, fileStream: Stream, contentType: str) -> FileStreamResult: ...
    @overload
    def File(self, fileContents: Set(Byte), contentType: str) -> FileContentResult: ...
    @overload
    def File(self, fileContents: Set(Byte), contentType: str, fileDownloadName: str) -> FileContentResult: ...
    @overload
    def File(self, fileStream: Stream, contentType: str, fileDownloadName: str) -> FileStreamResult: ...
    @overload
    def File(self, virtualPath: str, contentType: str, fileDownloadName: str) -> VirtualFileResult: ...
    @overload
    def Forbid(self) -> ForbidResult: ...
    @overload
    def Forbid(self, authenticationSchemes: Set(str)) -> ForbidResult: ...
    @overload
    def Forbid(self, properties: AuthenticationProperties) -> ForbidResult: ...
    @overload
    def Forbid(self, properties: AuthenticationProperties, authenticationSchemes: Set(str)) -> ForbidResult: ...
    @property
    def HttpContext(self) -> HttpContext: ...
    @property
    def MetadataProvider(self) -> IModelMetadataProvider: ...
    @property
    def ModelState(self) -> ModelStateDictionary: ...
    @property
    def PageContext(self) -> PageContext: ...
    @property
    def Request(self) -> HttpRequest: ...
    @property
    def Response(self) -> HttpResponse: ...
    @property
    def RouteData(self) -> RouteData: ...
    @property
    def TempData(self) -> ITempDataDictionary: ...
    @property
    def Url(self) -> IUrlHelper: ...
    @property
    def User(self) -> ClaimsPrincipal: ...
    @property
    def ViewData(self) -> ViewDataDictionary: ...
    def LocalRedirect(self, localUrl: str) -> LocalRedirectResult: ...
    def LocalRedirectPermanent(self, localUrl: str) -> LocalRedirectResult: ...
    def LocalRedirectPermanentPreserveMethod(self, localUrl: str) -> LocalRedirectResult: ...
    def LocalRedirectPreserveMethod(self, localUrl: str) -> LocalRedirectResult: ...
    @overload
    def NotFound(self) -> NotFoundResult: ...
    @overload
    def NotFound(self, value: Object) -> NotFoundObjectResult: ...
    def OnPageHandlerExecuted(self, context: PageHandlerExecutedContext) -> None: ...
    def OnPageHandlerExecuting(self, context: PageHandlerExecutingContext) -> None: ...
    def OnPageHandlerExecutionAsync(self, context: PageHandlerExecutingContext, next: PageHandlerExecutionDelegate) -> Task: ...
    def OnPageHandlerSelected(self, context: PageHandlerSelectedContext) -> None: ...
    def OnPageHandlerSelectionAsync(self, context: PageHandlerSelectedContext) -> Task: ...
    def Page(self) -> PageResult: ...
    @overload
    def Partial(self, viewName: str) -> PartialViewResult: ...
    @overload
    def Partial(self, viewName: str, model: Object) -> PartialViewResult: ...
    @overload
    def PhysicalFile(self, physicalPath: str, contentType: str) -> PhysicalFileResult: ...
    @overload
    def PhysicalFile(self, physicalPath: str, contentType: str, fileDownloadName: str) -> PhysicalFileResult: ...
    def RedirectPermanent(self, url: str) -> RedirectResult: ...
    def RedirectPermanentPreserveMethod(self, url: str) -> RedirectResult: ...
    def RedirectPreserveMethod(self, url: str) -> RedirectResult: ...
    @overload
    def RedirectToAction(self, actionName: str) -> RedirectToActionResult: ...
    @overload
    def RedirectToAction(self, actionName: str, routeValues: Object) -> RedirectToActionResult: ...
    @overload
    def RedirectToAction(self, actionName: str, controllerName: str) -> RedirectToActionResult: ...
    @overload
    def RedirectToAction(self, actionName: str, controllerName: str, fragment: str) -> RedirectToActionResult: ...
    @overload
    def RedirectToAction(self, actionName: str, controllerName: str, routeValues: Object) -> RedirectToActionResult: ...
    @overload
    def RedirectToAction(self, actionName: str, controllerName: str, routeValues: Object, fragment: str) -> RedirectToActionResult: ...
    @overload
    def RedirectToActionPermanent(self, actionName: str) -> RedirectToActionResult: ...
    @overload
    def RedirectToActionPermanent(self, actionName: str, routeValues: Object) -> RedirectToActionResult: ...
    @overload
    def RedirectToActionPermanent(self, actionName: str, controllerName: str) -> RedirectToActionResult: ...
    @overload
    def RedirectToActionPermanent(self, actionName: str, controllerName: str, fragment: str) -> RedirectToActionResult: ...
    @overload
    def RedirectToActionPermanent(self, actionName: str, controllerName: str, routeValues: Object) -> RedirectToActionResult: ...
    @overload
    def RedirectToActionPermanent(self, actionName: str, controllerName: str, routeValues: Object, fragment: str) -> RedirectToActionResult: ...
    def RedirectToActionPermanentPreserveMethod(self, actionName: str, controllerName: str, routeValues: Object, fragment: str) -> RedirectToActionResult: ...
    def RedirectToActionPreserveMethod(self, actionName: str, controllerName: str, routeValues: Object, fragment: str) -> RedirectToActionResult: ...
    @overload
    def RedirectToPage(self) -> RedirectToPageResult: ...
    @overload
    def RedirectToPage(self, pageName: str) -> RedirectToPageResult: ...
    @overload
    def RedirectToPage(self, routeValues: Object) -> RedirectToPageResult: ...
    @overload
    def RedirectToPage(self, pageName: str, routeValues: Object) -> RedirectToPageResult: ...
    @overload
    def RedirectToPage(self, pageName: str, pageHandler: str) -> RedirectToPageResult: ...
    @overload
    def RedirectToPage(self, pageName: str, pageHandler: str, fragment: str) -> RedirectToPageResult: ...
    @overload
    def RedirectToPage(self, pageName: str, pageHandler: str, routeValues: Object) -> RedirectToPageResult: ...
    @overload
    def RedirectToPage(self, pageName: str, pageHandler: str, routeValues: Object, fragment: str) -> RedirectToPageResult: ...
    @overload
    def RedirectToPagePermanent(self, pageName: str) -> RedirectToPageResult: ...
    @overload
    def RedirectToPagePermanent(self, pageName: str, routeValues: Object) -> RedirectToPageResult: ...
    @overload
    def RedirectToPagePermanent(self, pageName: str, pageHandler: str) -> RedirectToPageResult: ...
    @overload
    def RedirectToPagePermanent(self, pageName: str, pageHandler: str, routeValues: Object) -> RedirectToPageResult: ...
    @overload
    def RedirectToPagePermanent(self, pageName: str, pageHandler: str, fragment: str) -> RedirectToPageResult: ...
    @overload
    def RedirectToPagePermanent(self, pageName: str, routeValues: Object, fragment: str) -> RedirectToPageResult: ...
    @overload
    def RedirectToPagePermanent(self, pageName: str, pageHandler: str, routeValues: Object, fragment: str) -> RedirectToPageResult: ...
    def RedirectToPagePermanentPreserveMethod(self, pageName: str, pageHandler: str, routeValues: Object, fragment: str) -> RedirectToPageResult: ...
    def RedirectToPagePreserveMethod(self, pageName: str, pageHandler: str, routeValues: Object, fragment: str) -> RedirectToPageResult: ...
    @overload
    def RedirectToRoute(self, routeName: str) -> RedirectToRouteResult: ...
    @overload
    def RedirectToRoute(self, routeValues: Object) -> RedirectToRouteResult: ...
    @overload
    def RedirectToRoute(self, routeName: str, routeValues: Object) -> RedirectToRouteResult: ...
    @overload
    def RedirectToRoute(self, routeName: str, fragment: str) -> RedirectToRouteResult: ...
    @overload
    def RedirectToRoute(self, routeName: str, routeValues: Object, fragment: str) -> RedirectToRouteResult: ...
    @overload
    def RedirectToRoutePermanent(self, routeName: str) -> RedirectToRouteResult: ...
    @overload
    def RedirectToRoutePermanent(self, routeValues: Object) -> RedirectToRouteResult: ...
    @overload
    def RedirectToRoutePermanent(self, routeName: str, routeValues: Object) -> RedirectToRouteResult: ...
    @overload
    def RedirectToRoutePermanent(self, routeName: str, fragment: str) -> RedirectToRouteResult: ...
    @overload
    def RedirectToRoutePermanent(self, routeName: str, routeValues: Object, fragment: str) -> RedirectToRouteResult: ...
    def RedirectToRoutePermanentPreserveMethod(self, routeName: str, routeValues: Object, fragment: str) -> RedirectToRouteResult: ...
    def RedirectToRoutePreserveMethod(self, routeName: str, routeValues: Object, fragment: str) -> RedirectToRouteResult: ...
    @MetadataProvider.setter
    def MetadataProvider(self, value: IModelMetadataProvider) -> None: ...
    @PageContext.setter
    def PageContext(self, value: PageContext) -> None: ...
    @TempData.setter
    def TempData(self, value: ITempDataDictionary) -> None: ...
    @Url.setter
    def Url(self, value: IUrlHelper) -> None: ...
    @overload
    def SignIn(self, principal: ClaimsPrincipal, authenticationScheme: str) -> SignInResult: ...
    @overload
    def SignIn(self, principal: ClaimsPrincipal, properties: AuthenticationProperties, authenticationScheme: str) -> SignInResult: ...
    @overload
    def SignOut(self, authenticationSchemes: Set(str)) -> SignOutResult: ...
    @overload
    def SignOut(self, properties: AuthenticationProperties, authenticationSchemes: Set(str)) -> SignOutResult: ...
    @overload
    def StatusCode(self, statusCode: int) -> StatusCodeResult: ...
    @overload
    def StatusCode(self, statusCode: int, value: Object) -> ObjectResult: ...
    @overload
    def TryValidateModel(self, model: Object) -> bool: ...
    @overload
    def TryValidateModel(self, model: Object, name: str) -> bool: ...
    def Unauthorized(self) -> UnauthorizedResult: ...
    @overload
    def ViewComponent(self, componentName: str) -> ViewComponentResult: ...
    @overload
    def ViewComponent(self, componentType: Type) -> ViewComponentResult: ...
    @overload
    def ViewComponent(self, componentName: str, arguments: Object) -> ViewComponentResult: ...
    @overload
    def ViewComponent(self, componentType: Type, arguments: Object) -> ViewComponentResult: ...


class PageResult(ActionResult):
    def __init__(self): ...
    def ExecuteResultAsync(self, context: ActionContext) -> Task: ...
    @property
    def ContentType(self) -> str: ...
    @property
    def Model(self) -> Object: ...
    @property
    def Page(self) -> PageBase: ...
    @property
    def StatusCode(self) -> Nullable: ...
    @property
    def ViewData(self) -> ViewDataDictionary: ...
    @ContentType.setter
    def ContentType(self, value: str) -> None: ...
    @Page.setter
    def Page(self, value: PageBase) -> None: ...
    @StatusCode.setter
    def StatusCode(self, value: Nullable) -> None: ...
    @ViewData.setter
    def ViewData(self, value: ViewDataDictionary) -> None: ...


class RazorPagesOptions:
    def __init__(self): ...
    @property
    def Conventions(self) -> PageConventionCollection: ...
    @property
    def RootDirectory(self) -> str: ...
    @RootDirectory.setter
    def RootDirectory(self, value: str) -> None: ...
