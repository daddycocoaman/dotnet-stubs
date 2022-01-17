__all__ = ['Configuration','Configuration','Configuration']
from typing import Tuple, Set, Iterable, List


class TokenBinding(Object):
    @property
    def BindingType(self) -> TokenBindingType: ...
    def GetRawTokenBindingId(self) -> Set(Byte): ...
