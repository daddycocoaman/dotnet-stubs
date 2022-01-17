from typing import Tuple, Set, Iterable, List


class EncoderServiceCollectionExtensions:
    @overload
    def AddWebEncoders(services: IServiceCollection) -> IServiceCollection: ...
    @overload
    def AddWebEncoders(services: IServiceCollection, setupAction: Action) -> IServiceCollection: ...
