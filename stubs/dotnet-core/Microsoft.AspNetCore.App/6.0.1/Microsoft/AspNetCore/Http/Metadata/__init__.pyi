from typing import Tuple, Set, Iterable, List


class IAcceptsMetadata:
    @property
    def ContentTypes(self) -> IReadOnlyList: ...
    @property
    def IsOptional(self) -> bool: ...
    @property
    def RequestType(self) -> Type: ...


class IFromBodyMetadata:
    @property
    def AllowEmpty(self) -> bool: ...


class IFromHeaderMetadata:
    @property
    def Name(self) -> str: ...


class IFromQueryMetadata:
    @property
    def Name(self) -> str: ...


class IFromRouteMetadata:
    @property
    def Name(self) -> str: ...


class IFromServiceMetadata:
    pass


class IProducesResponseTypeMetadata:
    @property
    def ContentTypes(self) -> Iterable[str]: ...
    @property
    def StatusCode(self) -> int: ...
    @property
    def Type(self) -> Type: ...


class ITagsMetadata:
    @property
    def Tags(self) -> IReadOnlyList: ...
