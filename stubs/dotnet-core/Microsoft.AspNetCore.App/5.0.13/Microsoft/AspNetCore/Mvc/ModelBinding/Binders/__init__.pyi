from typing import Tuple, Set, Iterable, List




class ArrayModelBinderProvider:
    def __init__(self): ...
    def GetBinder(self, context: ModelBinderProviderContext) -> IModelBinder: ...


class BinderTypeModelBinder:
    def __init__(self, binderType: Type): ...
    def BindModelAsync(self, bindingContext: ModelBindingContext) -> Task: ...


class BinderTypeModelBinderProvider:
    def __init__(self): ...
    def GetBinder(self, context: ModelBinderProviderContext) -> IModelBinder: ...


class BodyModelBinder:
    @overload
    def __init__(self, formatters: List[IInputFormatter], readerFactory: IHttpRequestStreamReaderFactory): ...
    @overload
    def __init__(self, formatters: List[IInputFormatter], readerFactory: IHttpRequestStreamReaderFactory, loggerFactory: ILoggerFactory): ...
    @overload
    def __init__(self, formatters: List[IInputFormatter], readerFactory: IHttpRequestStreamReaderFactory, loggerFactory: ILoggerFactory, options: MvcOptions): ...
    def BindModelAsync(self, bindingContext: ModelBindingContext) -> Task: ...


class BodyModelBinderProvider:
    @overload
    def __init__(self, formatters: List[IInputFormatter], readerFactory: IHttpRequestStreamReaderFactory): ...
    @overload
    def __init__(self, formatters: List[IInputFormatter], readerFactory: IHttpRequestStreamReaderFactory, loggerFactory: ILoggerFactory): ...
    @overload
    def __init__(self, formatters: List[IInputFormatter], readerFactory: IHttpRequestStreamReaderFactory, loggerFactory: ILoggerFactory, options: MvcOptions): ...
    def GetBinder(self, context: ModelBinderProviderContext) -> IModelBinder: ...


class ByteArrayModelBinder:
    def __init__(self, loggerFactory: ILoggerFactory): ...
    def BindModelAsync(self, bindingContext: ModelBindingContext) -> Task: ...


class ByteArrayModelBinderProvider:
    def __init__(self): ...
    def GetBinder(self, context: ModelBinderProviderContext) -> IModelBinder: ...


class CancellationTokenModelBinder:
    def __init__(self): ...
    def BindModelAsync(self, bindingContext: ModelBindingContext) -> Task: ...


class CancellationTokenModelBinderProvider:
    def __init__(self): ...
    def GetBinder(self, context: ModelBinderProviderContext) -> IModelBinder: ...




class CollectionModelBinderProvider:
    def __init__(self): ...
    def GetBinder(self, context: ModelBinderProviderContext) -> IModelBinder: ...


class ComplexObjectModelBinder:
    def BindModelAsync(self, bindingContext: ModelBindingContext) -> Task: ...


class ComplexObjectModelBinderProvider:
    def __init__(self): ...
    def GetBinder(self, context: ModelBinderProviderContext) -> IModelBinder: ...


class DateTimeModelBinder:
    def __init__(self, supportedStyles: DateTimeStyles, loggerFactory: ILoggerFactory): ...
    def BindModelAsync(self, bindingContext: ModelBindingContext) -> Task: ...


class DateTimeModelBinderProvider:
    def __init__(self): ...
    def GetBinder(self, context: ModelBinderProviderContext) -> IModelBinder: ...


class DecimalModelBinder:
    def __init__(self, supportedStyles: NumberStyles, loggerFactory: ILoggerFactory): ...
    def BindModelAsync(self, bindingContext: ModelBindingContext) -> Task: ...




class DictionaryModelBinderProvider:
    def __init__(self): ...
    def GetBinder(self, context: ModelBinderProviderContext) -> IModelBinder: ...


class DoubleModelBinder:
    def __init__(self, supportedStyles: NumberStyles, loggerFactory: ILoggerFactory): ...
    def BindModelAsync(self, bindingContext: ModelBindingContext) -> Task: ...


class EnumTypeModelBinder(SimpleTypeModelBinder):
    def __init__(self, suppressBindingUndefinedValueToEnumType: bool, modelType: Type, loggerFactory: ILoggerFactory): ...


class EnumTypeModelBinderProvider:
    def __init__(self, options: MvcOptions): ...
    def GetBinder(self, context: ModelBinderProviderContext) -> IModelBinder: ...


class FloatingPointTypeModelBinderProvider:
    def __init__(self): ...
    def GetBinder(self, context: ModelBinderProviderContext) -> IModelBinder: ...


class FloatModelBinder:
    def __init__(self, supportedStyles: NumberStyles, loggerFactory: ILoggerFactory): ...
    def BindModelAsync(self, bindingContext: ModelBindingContext) -> Task: ...


class FormCollectionModelBinder:
    def __init__(self, loggerFactory: ILoggerFactory): ...
    def BindModelAsync(self, bindingContext: ModelBindingContext) -> Task: ...


class FormCollectionModelBinderProvider:
    def __init__(self): ...
    def GetBinder(self, context: ModelBinderProviderContext) -> IModelBinder: ...


class FormFileModelBinder:
    def __init__(self, loggerFactory: ILoggerFactory): ...
    def BindModelAsync(self, bindingContext: ModelBindingContext) -> Task: ...


class FormFileModelBinderProvider:
    def __init__(self): ...
    def GetBinder(self, context: ModelBinderProviderContext) -> IModelBinder: ...


class HeaderModelBinder:
    @overload
    def __init__(self, loggerFactory: ILoggerFactory): ...
    @overload
    def __init__(self, loggerFactory: ILoggerFactory, innerModelBinder: IModelBinder): ...
    def BindModelAsync(self, bindingContext: ModelBindingContext) -> Task: ...


class HeaderModelBinderProvider:
    def __init__(self): ...
    def GetBinder(self, context: ModelBinderProviderContext) -> IModelBinder: ...




class KeyValuePairModelBinderProvider:
    def __init__(self): ...
    def GetBinder(self, context: ModelBinderProviderContext) -> IModelBinder: ...


class ServicesModelBinder:
    def __init__(self): ...
    def BindModelAsync(self, bindingContext: ModelBindingContext) -> Task: ...


class ServicesModelBinderProvider:
    def __init__(self): ...
    def GetBinder(self, context: ModelBinderProviderContext) -> IModelBinder: ...


class SimpleTypeModelBinder:
    def __init__(self, type: Type, loggerFactory: ILoggerFactory): ...
    def BindModelAsync(self, bindingContext: ModelBindingContext) -> Task: ...


class SimpleTypeModelBinderProvider:
    def __init__(self): ...
    def GetBinder(self, context: ModelBinderProviderContext) -> IModelBinder: ...
