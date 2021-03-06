from typing import Tuple, Set, Iterable, List


class DynamicRouteValueTransformer:
    def FilterAsync(self, httpContext: HttpContext, values: RouteValueDictionary, endpoints: IReadOnlyList) -> ValueTask: ...
    @property
    def State(self) -> Object: ...
    @State.setter
    def State(self, value: Object) -> None: ...
    def TransformAsync(self, httpContext: HttpContext, values: RouteValueDictionary) -> ValueTask: ...


class HttpMethodAttribute:
    @overload
    def __init__(self, httpMethods: Iterable[str]): ...
    @overload
    def __init__(self, httpMethods: Iterable[str], template: str): ...
    @property
    def HttpMethods(self) -> Iterable[str]: ...
    @property
    def Name(self) -> str: ...
    @property
    def Order(self) -> int: ...
    @property
    def Template(self) -> str: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    @Order.setter
    def Order(self, value: int) -> None: ...


class IActionHttpMethodProvider:
    @property
    def HttpMethods(self) -> Iterable[str]: ...


class IRouteTemplateProvider:
    @property
    def Name(self) -> str: ...
    @property
    def Order(self) -> Nullable: ...
    @property
    def Template(self) -> str: ...


class IRouteValueProvider:
    @property
    def RouteKey(self) -> str: ...
    @property
    def RouteValue(self) -> str: ...


class IUrlHelperFactory:
    def GetUrlHelper(self, context: ActionContext) -> IUrlHelper: ...


class KnownRouteValueConstraint:
    def __init__(self, actionDescriptorCollectionProvider: IActionDescriptorCollectionProvider): ...
    def Match(self, httpContext: HttpContext, route: IRouter, routeKey: str, values: RouteValueDictionary, routeDirection: RouteDirection) -> bool: ...


class RouteValueAttribute:
    @property
    def RouteKey(self) -> str: ...
    @property
    def RouteValue(self) -> str: ...


class UrlHelper(UrlHelperBase):
    def __init__(self, actionContext: ActionContext): ...
    def Action(self, actionContext: UrlActionContext) -> str: ...
    def RouteUrl(self, routeContext: UrlRouteContext) -> str: ...


class UrlHelperBase:
    def Action(self, actionContext: UrlActionContext) -> str: ...
    def Content(self, contentPath: str) -> str: ...
    @property
    def ActionContext(self) -> ActionContext: ...
    def IsLocalUrl(self, url: str) -> bool: ...
    def Link(self, routeName: str, values: Object) -> str: ...
    def RouteUrl(self, routeContext: UrlRouteContext) -> str: ...


class UrlHelperFactory:
    def __init__(self): ...
    def GetUrlHelper(self, context: ActionContext) -> IUrlHelper: ...
