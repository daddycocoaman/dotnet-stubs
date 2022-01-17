from typing import Tuple, Set, Iterable, List


class ISupportsStartup:
    @overload
    def Configure(self, configure: Action) -> IWebHostBuilder: ...
    @overload
    def Configure(self, configure: Action) -> IWebHostBuilder: ...
    @overload
    def UseStartup(self, startupType: Type) -> IWebHostBuilder: ...
    @overload
    def UseStartup(self, startupFactory: Func) -> IWebHostBuilder: ...