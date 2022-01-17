from typing import Tuple, Set, Iterable, List


class ApiConventionNameMatchAttribute:
    def __init__(self, matchBehavior: ApiConventionNameMatchBehavior): ...
    @property
    def MatchBehavior(self) -> ApiConventionNameMatchBehavior: ...


class ApiConventionNameMatchBehavior:
    Any = 0
    Exact = 1
    Prefix = 2
    Suffix = 3


class ApiConventionResult:
    def __init__(self, responseMetadataProviders: IReadOnlyList): ...
    @property
    def ResponseMetadataProviders(self) -> IReadOnlyList: ...


class ApiConventionTypeMatchAttribute:
    def __init__(self, matchBehavior: ApiConventionTypeMatchBehavior): ...
    @property
    def MatchBehavior(self) -> ApiConventionTypeMatchBehavior: ...


class ApiConventionTypeMatchBehavior:
    Any = 0
    AssignableFrom = 1


class IApiDefaultResponseMetadataProvider:
    pass


class IApiDescriptionGroupNameProvider:
    @property
    def GroupName(self) -> str: ...


class IApiDescriptionVisibilityProvider:
    @property
    def IgnoreApi(self) -> bool: ...


class IApiRequestFormatMetadataProvider:
    def GetSupportedContentTypes(self, contentType: str, objectType: Type) -> IReadOnlyList: ...


class IApiRequestMetadataProvider:
    def SetContentTypes(self, contentTypes: MediaTypeCollection) -> None: ...


class IApiResponseMetadataProvider:
    @property
    def StatusCode(self) -> int: ...
    @property
    def Type(self) -> Type: ...
    def SetContentTypes(self, contentTypes: MediaTypeCollection) -> None: ...


class IApiResponseTypeMetadataProvider:
    def GetSupportedContentTypes(self, contentType: str, objectType: Type) -> IReadOnlyList: ...
