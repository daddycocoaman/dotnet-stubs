from typing import Tuple, Set, Iterable, List


class SharedOptionsBase:
    @property
    def FileProvider(self) -> IFileProvider: ...
    @property
    def RequestPath(self) -> PathString: ...
    @FileProvider.setter
    def FileProvider(self, value: IFileProvider) -> None: ...
    @RequestPath.setter
    def RequestPath(self, value: PathString) -> None: ...