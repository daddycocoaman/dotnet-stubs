from typing import Tuple, Set, Iterable, List


class UrlEncoder(TextEncoder):
    @overload
    def Create(settings: TextEncoderSettings) -> UrlEncoder: ...
    @overload
    def Create(allowedRanges: Set(UnicodeRange)) -> UrlEncoder: ...
    @property
    def Default() -> UrlEncoder: ...
