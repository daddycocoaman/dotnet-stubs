from typing import Tuple, Set, Iterable, List


class Converter(TypeConverter):
    def __init__(self): ...
    @overload
    def CanConvertFrom(self, context: ITypeDescriptorContext, sourceType: Type) -> bool: ...
    @overload
    def CanConvertTo(self, context: ITypeDescriptorContext, destinationType: Type) -> bool: ...
    @overload
    def ConvertFrom(self, context: ITypeDescriptorContext, culture: CultureInfo, value: Object) -> Object: ...
    @overload
    def ConvertTo(self, context: ITypeDescriptorContext, culture: CultureInfo, value: Object, destinationType: Type) -> Object: ...
