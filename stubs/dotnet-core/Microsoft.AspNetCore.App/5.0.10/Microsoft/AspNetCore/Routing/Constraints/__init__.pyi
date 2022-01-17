from typing import Tuple, Set, Iterable, List


class StringRouteConstraint:
    def __init__(self, value: str): ...
    def Match(self, httpContext: HttpContext, route: IRouter, routeKey: str, values: RouteValueDictionary, routeDirection: RouteDirection) -> bool: ...