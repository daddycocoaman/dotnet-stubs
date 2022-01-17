from typing import Tuple, Set, Iterable, List


class IApiResponseTypeMetadataProvider:
    def GetSupportedContentTypes(self, contentType: str, objectType: Type) -> IReadOnlyList: ...
