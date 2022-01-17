__all__ = ['Runtime']
from typing import Tuple, Set, Iterable, List


class IXsltContextFunction:
    @property
    def ArgTypes(self) -> Set(XPathResultType): ...
    @property
    def Maxargs(self) -> int: ...
    @property
    def Minargs(self) -> int: ...
    @property
    def ReturnType(self) -> XPathResultType: ...
    def Invoke(self, xsltContext: XsltContext, args: Set(Object), docContext: XPathNavigator) -> Object: ...


class IXsltContextVariable:
    def Evaluate(self, xsltContext: XsltContext) -> Object: ...
    @property
    def IsLocal(self) -> bool: ...
    @property
    def IsParam(self) -> bool: ...
    @property
    def VariableType(self) -> XPathResultType: ...


class XslCompiledTransform(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, enableDebug: bool): ...
    @property
    def OutputSettings(self) -> XmlWriterSettings: ...
    @overload
    def Load(self, stylesheet: IXPathNavigable) -> None: ...
    @overload
    def Load(self, stylesheetUri: str) -> None: ...
    @overload
    def Load(self, compiledStylesheet: Type) -> None: ...
    @overload
    def Load(self, stylesheet: XmlReader) -> None: ...
    @overload
    def Load(self, stylesheet: IXPathNavigable, settings: XsltSettings, stylesheetResolver: XmlResolver) -> None: ...
    @overload
    def Load(self, stylesheetUri: str, settings: XsltSettings, stylesheetResolver: XmlResolver) -> None: ...
    @overload
    def Load(self, executeMethod: MethodInfo, queryData: Set(Byte), earlyBoundTypes: Set(Type)) -> None: ...
    @overload
    def Load(self, stylesheet: XmlReader, settings: XsltSettings, stylesheetResolver: XmlResolver) -> None: ...
    @overload
    def Transform(self, inputUri: str, resultsFile: str) -> None: ...
    @overload
    def Transform(self, inputUri: str, results: XmlWriter) -> None: ...
    @overload
    def Transform(self, input: XmlReader, results: XmlWriter) -> None: ...
    @overload
    def Transform(self, input: IXPathNavigable, results: XmlWriter) -> None: ...
    @overload
    def Transform(self, input: XmlReader, arguments: XsltArgumentList, results: Stream) -> None: ...
    @overload
    def Transform(self, input: IXPathNavigable, arguments: XsltArgumentList, results: Stream) -> None: ...
    @overload
    def Transform(self, inputUri: str, arguments: XsltArgumentList, results: XmlWriter) -> None: ...
    @overload
    def Transform(self, inputUri: str, arguments: XsltArgumentList, results: TextWriter) -> None: ...
    @overload
    def Transform(self, inputUri: str, arguments: XsltArgumentList, results: Stream) -> None: ...
    @overload
    def Transform(self, input: IXPathNavigable, arguments: XsltArgumentList, results: TextWriter) -> None: ...
    @overload
    def Transform(self, input: IXPathNavigable, arguments: XsltArgumentList, results: XmlWriter) -> None: ...
    @overload
    def Transform(self, input: XmlReader, arguments: XsltArgumentList, results: XmlWriter) -> None: ...
    @overload
    def Transform(self, input: XmlReader, arguments: XsltArgumentList, results: TextWriter) -> None: ...
    @overload
    def Transform(self, input: XmlReader, arguments: XsltArgumentList, results: XmlWriter, documentResolver: XmlResolver) -> None: ...
    @overload
    def Transform(self, input: IXPathNavigable, arguments: XsltArgumentList, results: XmlWriter, documentResolver: XmlResolver) -> None: ...


class XsltArgumentList(Object):
    def __init__(self): ...
    def add_XsltMessageEncountered(self, value: XsltMessageEncounteredEventHandler) -> None: ...
    def AddExtensionObject(self, namespaceUri: str, extension: Object) -> None: ...
    def AddParam(self, name: str, namespaceUri: str, parameter: Object) -> None: ...
    def Clear(self) -> None: ...
    def GetExtensionObject(self, namespaceUri: str) -> Object: ...
    def GetParam(self, name: str, namespaceUri: str) -> Object: ...
    def remove_XsltMessageEncountered(self, value: XsltMessageEncounteredEventHandler) -> None: ...
    def RemoveExtensionObject(self, namespaceUri: str) -> Object: ...
    def RemoveParam(self, name: str, namespaceUri: str) -> Object: ...


class XsltCompileException(XsltException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...
    @overload
    def __init__(self, inner: Exception, sourceUri: str, lineNumber: int, linePosition: int): ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...


class XsltContext(XmlNamespaceManager):
    def CompareDocument(self, baseUri: str, nextbaseUri: str) -> int: ...
    @property
    def Whitespace(self) -> bool: ...
    def PreserveWhitespace(self, node: XPathNavigator) -> bool: ...
    def ResolveFunction(self, prefix: str, name: str, ArgTypes: Set(XPathResultType)) -> IXsltContextFunction: ...
    def ResolveVariable(self, prefix: str, name: str) -> IXsltContextVariable: ...


class XsltException(SystemException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...
    @property
    def LineNumber(self) -> int: ...
    @property
    def LinePosition(self) -> int: ...
    @property
    def Message(self) -> str: ...
    @property
    def SourceUri(self) -> str: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...


class XsltMessageEncounteredEventArgs(EventArgs):
    @property
    def Message(self) -> str: ...


class XsltMessageEncounteredEventHandler(MulticastDelegate):
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, sender: Object, e: XsltMessageEncounteredEventArgs, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: Object, e: XsltMessageEncounteredEventArgs) -> None: ...


class XslTransform(Object):
    def __init__(self): ...
    @overload
    def Load(self, stylesheet: XmlReader) -> None: ...
    @overload
    def Load(self, stylesheet: IXPathNavigable) -> None: ...
    @overload
    def Load(self, stylesheet: XPathNavigator) -> None: ...
    @overload
    def Load(self, url: str) -> None: ...
    @overload
    def Load(self, stylesheet: XmlReader, resolver: XmlResolver) -> None: ...
    @overload
    def Load(self, stylesheet: IXPathNavigable, resolver: XmlResolver) -> None: ...
    @overload
    def Load(self, stylesheet: XPathNavigator, resolver: XmlResolver) -> None: ...
    @overload
    def Load(self, url: str, resolver: XmlResolver) -> None: ...
    @XmlResolver.setter
    def XmlResolver(self, value: XmlResolver) -> None: ...
    @overload
    def Transform(self, input: XPathNavigator, args: XsltArgumentList) -> XmlReader: ...
    @overload
    def Transform(self, input: IXPathNavigable, args: XsltArgumentList) -> XmlReader: ...
    @overload
    def Transform(self, inputfile: str, outputfile: str) -> None: ...
    @overload
    def Transform(self, input: XPathNavigator, args: XsltArgumentList, output: XmlWriter) -> None: ...
    @overload
    def Transform(self, input: XPathNavigator, args: XsltArgumentList, output: Stream) -> None: ...
    @overload
    def Transform(self, input: XPathNavigator, args: XsltArgumentList, output: TextWriter) -> None: ...
    @overload
    def Transform(self, input: IXPathNavigable, args: XsltArgumentList, resolver: XmlResolver) -> XmlReader: ...
    @overload
    def Transform(self, input: XPathNavigator, args: XsltArgumentList, resolver: XmlResolver) -> XmlReader: ...
    @overload
    def Transform(self, input: IXPathNavigable, args: XsltArgumentList, output: TextWriter) -> None: ...
    @overload
    def Transform(self, input: IXPathNavigable, args: XsltArgumentList, output: Stream) -> None: ...
    @overload
    def Transform(self, inputfile: str, outputfile: str, resolver: XmlResolver) -> None: ...
    @overload
    def Transform(self, input: IXPathNavigable, args: XsltArgumentList, output: XmlWriter) -> None: ...
    @overload
    def Transform(self, input: IXPathNavigable, args: XsltArgumentList, output: Stream, resolver: XmlResolver) -> None: ...
    @overload
    def Transform(self, input: XPathNavigator, args: XsltArgumentList, output: XmlWriter, resolver: XmlResolver) -> None: ...
    @overload
    def Transform(self, input: IXPathNavigable, args: XsltArgumentList, output: TextWriter, resolver: XmlResolver) -> None: ...
    @overload
    def Transform(self, input: XPathNavigator, args: XsltArgumentList, output: Stream, resolver: XmlResolver) -> None: ...
    @overload
    def Transform(self, input: IXPathNavigable, args: XsltArgumentList, output: XmlWriter, resolver: XmlResolver) -> None: ...
    @overload
    def Transform(self, input: XPathNavigator, args: XsltArgumentList, output: TextWriter, resolver: XmlResolver) -> None: ...


class XsltSettings(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, enableDocumentFunction: bool, enableScript: bool): ...
    @property
    def Default() -> XsltSettings: ...
    @property
    def EnableDocumentFunction(self) -> bool: ...
    @property
    def EnableScript(self) -> bool: ...
    @property
    def TrustedXslt() -> XsltSettings: ...
    @EnableDocumentFunction.setter
    def EnableDocumentFunction(self, value: bool) -> None: ...
    @EnableScript.setter
    def EnableScript(self, value: bool) -> None: ...
