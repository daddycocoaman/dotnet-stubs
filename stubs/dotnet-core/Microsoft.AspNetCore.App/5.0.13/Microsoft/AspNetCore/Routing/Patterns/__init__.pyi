from typing import Tuple, Set, Iterable, List


class RoutePatternTransformer:
    def SubstituteRequiredValues(self, original: RoutePattern, requiredValues: Object) -> RoutePattern: ...
