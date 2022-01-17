from typing import Tuple, Set, Iterable, List


class IApplicationBuilderFactory:
    def CreateBuilder(self, serverFeatures: IFeatureCollection) -> IApplicationBuilder: ...
