from typing import Tuple, Set, Iterable, List


class HttpCacheAgeControl:
    #None = 0
    MinFresh = 1
    MaxAge = 2
    MaxAgeAndMinFresh = 3
    MaxStale = 4
    MaxAgeAndMaxStale = 6


class HttpRequestCacheLevel:
    Default = 0
    BypassCache = 1
    CacheOnly = 2
    CacheIfAvailable = 3
    Revalidate = 4
    Reload = 5
    NoCacheNoStore = 6
    CacheOrNextCacheOnly = 7
    Refresh = 8


class HttpRequestCachePolicy(RequestCachePolicy):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, level: HttpRequestCacheLevel): ...
    @overload
    def __init__(self, cacheSyncDate: DateTime): ...
    @overload
    def __init__(self, cacheAgeControl: HttpCacheAgeControl, ageOrFreshOrStale: TimeSpan): ...
    @overload
    def __init__(self, cacheAgeControl: HttpCacheAgeControl, maxAge: TimeSpan, freshOrStale: TimeSpan): ...
    @overload
    def __init__(self, cacheAgeControl: HttpCacheAgeControl, maxAge: TimeSpan, freshOrStale: TimeSpan, cacheSyncDate: DateTime): ...
    @property
    def CacheSyncDate(self) -> DateTime: ...
    @property
    def Level(self) -> HttpRequestCacheLevel: ...
    @property
    def MaxAge(self) -> TimeSpan: ...
    @property
    def MaxStale(self) -> TimeSpan: ...
    @property
    def MinFresh(self) -> TimeSpan: ...
    def ToString(self) -> str: ...
