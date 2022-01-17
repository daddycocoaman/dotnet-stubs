from typing import Tuple, Set, Iterable, List


class ProtectedSessionStorage(ProtectedBrowserStorage):
    def __init__(self, jsRuntime: IJSRuntime, dataProtectionProvider: IDataProtectionProvider): ...
