from typing import Tuple, Set, Iterable, List


class WebHostBuilderSocketExtensions:
    @overload
    def UseSockets(hostBuilder: IWebHostBuilder) -> IWebHostBuilder: ...
    @overload
    def UseSockets(hostBuilder: IWebHostBuilder, configureOptions: Action) -> IWebHostBuilder: ...
