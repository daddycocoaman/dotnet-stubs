__all__ = ['Internal','Internal','Internal','Internal','Internal','Internal','Internal','Internal','Internal','Internal','Internal','Internal','Internal','Internal','Internal','Internal','Provider','Provider','Provider']
from typing import Tuple, Set, Iterable, List


class WhiteSpaceTrimStringConverter(ConfigurationConverterBase):
    def __init__(self): ...
    @overload
    def ConvertFrom(self, ctx: ITypeDescriptorContext, ci: CultureInfo, data: Object) -> Object: ...
    @overload
    def ConvertTo(self, ctx: ITypeDescriptorContext, ci: CultureInfo, value: Object, type: Type) -> Object: ...
