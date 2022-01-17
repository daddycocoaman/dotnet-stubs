from typing import Tuple, Set, Iterable, List


class DownloadApplicationCompletedEventArgs(AsyncCompletedEventArgs):
    @property
    def LogFilePath(self) -> str: ...
    @property
    def ShortcutAppId(self) -> str: ...
