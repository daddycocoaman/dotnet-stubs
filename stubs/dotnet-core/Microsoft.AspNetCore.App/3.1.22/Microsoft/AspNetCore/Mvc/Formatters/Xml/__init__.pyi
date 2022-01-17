from typing import Tuple, Set, Iterable, List


class WrapperProviderFactoriesExtensions:
    def GetWrapperProvider(wrapperProviderFactories: Iterable[IWrapperProviderFactory], wrapperProviderContext: WrapperProviderContext) -> IWrapperProvider: ...
