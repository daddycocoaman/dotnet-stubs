__all__ = ['Xml']
from typing import Tuple, Set, Iterable, List


class XmlDataContractSerializerInputFormatter(TextInputFormatter):
    def __init__(self, options: MvcOptions): ...
    @property
    def ExceptionPolicy(self) -> InputFormatterExceptionPolicy: ...
    @property
    def MaxDepth(self) -> int: ...
    @property
    def SerializerSettings(self) -> DataContractSerializerSettings: ...
    @property
    def WrapperProviderFactories(self) -> List[IWrapperProviderFactory]: ...
    @property
    def XmlDictionaryReaderQuotas(self) -> XmlDictionaryReaderQuotas: ...
    @overload
    def ReadRequestBodyAsync(self, context: InputFormatterContext, encoding: Encoding) -> Task: ...
    @MaxDepth.setter
    def MaxDepth(self, value: int) -> None: ...
    @SerializerSettings.setter
    def SerializerSettings(self, value: DataContractSerializerSettings) -> None: ...


class XmlDataContractSerializerOutputFormatter(TextOutputFormatter):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, loggerFactory: ILoggerFactory): ...
    @overload
    def __init__(self, writerSettings: XmlWriterSettings): ...
    @overload
    def __init__(self, writerSettings: XmlWriterSettings, loggerFactory: ILoggerFactory): ...
    @overload
    def CreateXmlWriter(self, writer: TextWriter, xmlWriterSettings: XmlWriterSettings) -> XmlWriter: ...
    @overload
    def CreateXmlWriter(self, context: OutputFormatterWriteContext, writer: TextWriter, xmlWriterSettings: XmlWriterSettings) -> XmlWriter: ...
    @property
    def SerializerSettings(self) -> DataContractSerializerSettings: ...
    @property
    def WrapperProviderFactories(self) -> List[IWrapperProviderFactory]: ...
    @property
    def WriterSettings(self) -> XmlWriterSettings: ...
    @SerializerSettings.setter
    def SerializerSettings(self, value: DataContractSerializerSettings) -> None: ...
    @overload
    def WriteResponseBodyAsync(self, context: OutputFormatterWriteContext, selectedEncoding: Encoding) -> Task: ...


class XmlSerializerInputFormatter(TextInputFormatter):
    def __init__(self, options: MvcOptions): ...
    @property
    def ExceptionPolicy(self) -> InputFormatterExceptionPolicy: ...
    @property
    def MaxDepth(self) -> int: ...
    @property
    def WrapperProviderFactories(self) -> List[IWrapperProviderFactory]: ...
    @property
    def XmlDictionaryReaderQuotas(self) -> XmlDictionaryReaderQuotas: ...
    @overload
    def ReadRequestBodyAsync(self, context: InputFormatterContext, encoding: Encoding) -> Task: ...
    @MaxDepth.setter
    def MaxDepth(self, value: int) -> None: ...


class XmlSerializerOutputFormatter(TextOutputFormatter):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, loggerFactory: ILoggerFactory): ...
    @overload
    def __init__(self, writerSettings: XmlWriterSettings): ...
    @overload
    def __init__(self, writerSettings: XmlWriterSettings, loggerFactory: ILoggerFactory): ...
    @overload
    def CreateXmlWriter(self, writer: TextWriter, xmlWriterSettings: XmlWriterSettings) -> XmlWriter: ...
    @overload
    def CreateXmlWriter(self, context: OutputFormatterWriteContext, writer: TextWriter, xmlWriterSettings: XmlWriterSettings) -> XmlWriter: ...
    @property
    def WrapperProviderFactories(self) -> List[IWrapperProviderFactory]: ...
    @property
    def WriterSettings(self) -> XmlWriterSettings: ...
    @overload
    def WriteResponseBodyAsync(self, context: OutputFormatterWriteContext, selectedEncoding: Encoding) -> Task: ...
