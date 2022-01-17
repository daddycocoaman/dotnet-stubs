from typing import Tuple, Set, Iterable, List


class ApplicationBuilderFactory:
    def __init__(self, serviceProvider: IServiceProvider): ...
    def CreateBuilder(self, serverFeatures: IFeatureCollection) -> IApplicationBuilder: ...


class IApplicationBuilderFactory:
    def CreateBuilder(self, serverFeatures: IFeatureCollection) -> IApplicationBuilder: ...
