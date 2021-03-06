from typing import Tuple, Set, Iterable, List


class AncestorDocOrderIterator(ValueType):
    def Create(self, context: XPathNavigator, filter: XmlNavigatorFilter, orSelf: bool) -> None: ...
    @property
    def Current(self) -> XPathNavigator: ...
    def MoveNext(self) -> bool: ...


class AncestorIterator(ValueType):
    def Create(self, context: XPathNavigator, filter: XmlNavigatorFilter, orSelf: bool) -> None: ...
    @property
    def Current(self) -> XPathNavigator: ...
    def MoveNext(self) -> bool: ...


class AttributeContentIterator(ValueType):
    def Create(self, context: XPathNavigator) -> None: ...
    @property
    def Current(self) -> XPathNavigator: ...
    def MoveNext(self) -> bool: ...


class AttributeIterator(ValueType):
    def Create(self, context: XPathNavigator) -> None: ...
    @property
    def Current(self) -> XPathNavigator: ...
    def MoveNext(self) -> bool: ...


class ContentIterator(ValueType):
    def Create(self, context: XPathNavigator) -> None: ...
    @property
    def Current(self) -> XPathNavigator: ...
    def MoveNext(self) -> bool: ...


class ContentMergeIterator(ValueType):
    def Create(self, filter: XmlNavigatorFilter) -> None: ...
    @property
    def Current(self) -> XPathNavigator: ...
    def MoveNext(self, input: XPathNavigator) -> IteratorResult: ...


class DecimalAggregator(ValueType):
    def Average(self, value: Decimal) -> None: ...
    def Create(self) -> None: ...
    @property
    def AverageResult(self) -> Decimal: ...
    @property
    def IsEmpty(self) -> bool: ...
    @property
    def MaximumResult(self) -> Decimal: ...
    @property
    def MinimumResult(self) -> Decimal: ...
    @property
    def SumResult(self) -> Decimal: ...
    def Maximum(self, value: Decimal) -> None: ...
    def Minimum(self, value: Decimal) -> None: ...
    def Sum(self, value: Decimal) -> None: ...


class DescendantIterator(ValueType):
    def Create(self, input: XPathNavigator, filter: XmlNavigatorFilter, orSelf: bool) -> None: ...
    @property
    def Current(self) -> XPathNavigator: ...
    def MoveNext(self) -> bool: ...


class DescendantMergeIterator(ValueType):
    def Create(self, filter: XmlNavigatorFilter, orSelf: bool) -> None: ...
    @property
    def Current(self) -> XPathNavigator: ...
    def MoveNext(self, input: XPathNavigator) -> IteratorResult: ...


class DifferenceIterator(ValueType):
    def Create(self, runtime: XmlQueryRuntime) -> None: ...
    @property
    def Current(self) -> XPathNavigator: ...
    def MoveNext(self, nestedNavigator: XPathNavigator) -> SetIteratorResult: ...


class DodSequenceMerge(ValueType):
    def AddSequence(self, sequence: List[XPathNavigator]) -> None: ...
    def Create(self, runtime: XmlQueryRuntime) -> None: ...
    def MergeSequences(self) -> List[XPathNavigator]: ...


class DoubleAggregator(ValueType):
    def Average(self, value: float) -> None: ...
    def Create(self) -> None: ...
    @property
    def AverageResult(self) -> float: ...
    @property
    def IsEmpty(self) -> bool: ...
    @property
    def MaximumResult(self) -> float: ...
    @property
    def MinimumResult(self) -> float: ...
    @property
    def SumResult(self) -> float: ...
    def Maximum(self, value: float) -> None: ...
    def Minimum(self, value: float) -> None: ...
    def Sum(self, value: float) -> None: ...


class ElementContentIterator(ValueType):
    def Create(self, context: XPathNavigator, localName: str, ns: str) -> None: ...
    @property
    def Current(self) -> XPathNavigator: ...
    def MoveNext(self) -> bool: ...


class FollowingSiblingIterator(ValueType):
    def Create(self, context: XPathNavigator, filter: XmlNavigatorFilter) -> None: ...
    @property
    def Current(self) -> XPathNavigator: ...
    def MoveNext(self) -> bool: ...


class FollowingSiblingMergeIterator(ValueType):
    def Create(self, filter: XmlNavigatorFilter) -> None: ...
    @property
    def Current(self) -> XPathNavigator: ...
    def MoveNext(self, navigator: XPathNavigator) -> IteratorResult: ...


class IdIterator(ValueType):
    def Create(self, context: XPathNavigator, value: str) -> None: ...
    @property
    def Current(self) -> XPathNavigator: ...
    def MoveNext(self) -> bool: ...


class Int32Aggregator(ValueType):
    def Average(self, value: int) -> None: ...
    def Create(self) -> None: ...
    @property
    def AverageResult(self) -> int: ...
    @property
    def IsEmpty(self) -> bool: ...
    @property
    def MaximumResult(self) -> int: ...
    @property
    def MinimumResult(self) -> int: ...
    @property
    def SumResult(self) -> int: ...
    def Maximum(self, value: int) -> None: ...
    def Minimum(self, value: int) -> None: ...
    def Sum(self, value: int) -> None: ...


class Int64Aggregator(ValueType):
    def Average(self, value: Int64) -> None: ...
    def Create(self) -> None: ...
    @property
    def AverageResult(self) -> Int64: ...
    @property
    def IsEmpty(self) -> bool: ...
    @property
    def MaximumResult(self) -> Int64: ...
    @property
    def MinimumResult(self) -> Int64: ...
    @property
    def SumResult(self) -> Int64: ...
    def Maximum(self, value: Int64) -> None: ...
    def Minimum(self, value: Int64) -> None: ...
    def Sum(self, value: Int64) -> None: ...


class IntersectIterator(ValueType):
    def Create(self, runtime: XmlQueryRuntime) -> None: ...
    @property
    def Current(self) -> XPathNavigator: ...
    def MoveNext(self, nestedNavigator: XPathNavigator) -> SetIteratorResult: ...


class IteratorResult:
    NoMoreNodes = 0
    NeedInputNode = 1
    HaveCurrentNode = 2


class NamespaceIterator(ValueType):
    def Create(self, context: XPathNavigator) -> None: ...
    @property
    def Current(self) -> XPathNavigator: ...
    def MoveNext(self) -> bool: ...


class NodeKindContentIterator(ValueType):
    def Create(self, context: XPathNavigator, nodeType: XPathNodeType) -> None: ...
    @property
    def Current(self) -> XPathNavigator: ...
    def MoveNext(self) -> bool: ...


class NodeRangeIterator(ValueType):
    def Create(self, start: XPathNavigator, filter: XmlNavigatorFilter, end: XPathNavigator) -> None: ...
    @property
    def Current(self) -> XPathNavigator: ...
    def MoveNext(self) -> bool: ...


class ParentIterator(ValueType):
    def Create(self, context: XPathNavigator, filter: XmlNavigatorFilter) -> None: ...
    @property
    def Current(self) -> XPathNavigator: ...
    def MoveNext(self) -> bool: ...


class PrecedingIterator(ValueType):
    def Create(self, context: XPathNavigator, filter: XmlNavigatorFilter) -> None: ...
    @property
    def Current(self) -> XPathNavigator: ...
    def MoveNext(self) -> bool: ...


class PrecedingSiblingDocOrderIterator(ValueType):
    def Create(self, context: XPathNavigator, filter: XmlNavigatorFilter) -> None: ...
    @property
    def Current(self) -> XPathNavigator: ...
    def MoveNext(self) -> bool: ...


class PrecedingSiblingIterator(ValueType):
    def Create(self, context: XPathNavigator, filter: XmlNavigatorFilter) -> None: ...
    @property
    def Current(self) -> XPathNavigator: ...
    def MoveNext(self) -> bool: ...


class SetIteratorResult:
    NoMoreNodes = 0
    InitRightIterator = 1
    NeedLeftNode = 2
    NeedRightNode = 3
    HaveCurrentNode = 4


class StringConcat(ValueType):
    def Clear(self) -> None: ...
    def Concat(self, value: str) -> None: ...
    @property
    def Delimiter(self) -> str: ...
    def GetResult(self) -> str: ...
    @Delimiter.setter
    def Delimiter(self, value: str) -> None: ...


class UnionIterator(ValueType):
    def Create(self, runtime: XmlQueryRuntime) -> None: ...
    @property
    def Current(self) -> XPathNavigator: ...
    def MoveNext(self, nestedNavigator: XPathNavigator) -> SetIteratorResult: ...


class XmlCollation(Object):
    def Equals(self, obj: Object) -> bool: ...
    def GetHashCode(self) -> int: ...


class XmlILIndex(Object):
    def Add(self, key: str, navigator: XPathNavigator) -> None: ...
    def Lookup(self, key: str) -> XmlQueryNodeSequence: ...


class XmlILStorageConverter(Object):
    def BooleanToAtomicValue(value: bool, index: int, runtime: XmlQueryRuntime) -> XmlAtomicValue: ...
    def BytesToAtomicValue(value: Set(Byte), index: int, runtime: XmlQueryRuntime) -> XmlAtomicValue: ...
    def DateTimeToAtomicValue(value: DateTime, index: int, runtime: XmlQueryRuntime) -> XmlAtomicValue: ...
    def DecimalToAtomicValue(value: Decimal, index: int, runtime: XmlQueryRuntime) -> XmlAtomicValue: ...
    def DoubleToAtomicValue(value: float, index: int, runtime: XmlQueryRuntime) -> XmlAtomicValue: ...
    def Int32ToAtomicValue(value: int, index: int, runtime: XmlQueryRuntime) -> XmlAtomicValue: ...
    def Int64ToAtomicValue(value: Int64, index: int, runtime: XmlQueryRuntime) -> XmlAtomicValue: ...
    def ItemsToNavigators(listItems: List[XPathItem]) -> List[XPathNavigator]: ...
    def NavigatorsToItems(listNavigators: List[XPathNavigator]) -> List[XPathItem]: ...
    def SingleToAtomicValue(value: Single, index: int, runtime: XmlQueryRuntime) -> XmlAtomicValue: ...
    def StringToAtomicValue(value: str, index: int, runtime: XmlQueryRuntime) -> XmlAtomicValue: ...
    def TimeSpanToAtomicValue(value: TimeSpan, index: int, runtime: XmlQueryRuntime) -> XmlAtomicValue: ...
    def XmlQualifiedNameToAtomicValue(value: XmlQualifiedName, index: int, runtime: XmlQueryRuntime) -> XmlAtomicValue: ...


class XmlNavigatorFilter(Object):
    def IsFiltered(self, navigator: XPathNavigator) -> bool: ...
    def MoveToContent(self, navigator: XPathNavigator) -> bool: ...
    def MoveToFollowing(self, navigator: XPathNavigator, navigatorEnd: XPathNavigator) -> bool: ...
    def MoveToFollowingSibling(self, navigator: XPathNavigator) -> bool: ...
    def MoveToNextContent(self, navigator: XPathNavigator) -> bool: ...
    def MoveToPreviousSibling(self, navigator: XPathNavigator) -> bool: ...


class XmlQueryContext(Object):
    @property
    def DefaultDataSource(self) -> XPathNavigator: ...
    @property
    def DefaultNameTable(self) -> XmlNameTable: ...
    @property
    def QueryNameTable(self) -> XmlNameTable: ...
    def GetDataSource(self, uriRelative: str, uriBase: str) -> XPathNavigator: ...
    def GetLateBoundObject(self, namespaceUri: str) -> Object: ...
    def GetParameter(self, localName: str, namespaceUri: str) -> Object: ...
    def InvokeXsltLateBoundFunction(self, name: str, namespaceUri: str, args: List[XPathItem]) -> List[XPathItem]: ...
    def LateBoundFunctionExists(self, name: str, namespaceUri: str) -> bool: ...
    def OnXsltMessageEncountered(self, message: str) -> None: ...


class XmlQueryItemSequence:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, capacity: int): ...
    @overload
    def __init__(self, item: XPathItem): ...
    def AddClone(self, item: XPathItem) -> None: ...
    @overload
    def CreateOrReuse(seq: XmlQueryItemSequence) -> XmlQueryItemSequence: ...
    @overload
    def CreateOrReuse(seq: XmlQueryItemSequence, item: XPathItem) -> XmlQueryItemSequence: ...


class XmlQueryNodeSequence:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, capacity: int): ...
    @overload
    def __init__(self, list: List[XPathNavigator]): ...
    @overload
    def __init__(self, navigator: XPathNavigator): ...
    @overload
    def __init__(self, array: Set(XPathNavigator), size: int): ...
    def AddClone(self, navigator: XPathNavigator) -> None: ...
    @overload
    def CreateOrReuse(seq: XmlQueryNodeSequence) -> XmlQueryNodeSequence: ...
    @overload
    def CreateOrReuse(seq: XmlQueryNodeSequence, navigator: XPathNavigator) -> XmlQueryNodeSequence: ...
    def DocOrderDistinct(self, comparer: IComparer) -> XmlQueryNodeSequence: ...
    @property
    def IsDocOrderDistinct(self) -> bool: ...
    @IsDocOrderDistinct.setter
    def IsDocOrderDistinct(self, value: bool) -> None: ...


class XmlQueryOutput(XmlWriter):
    def Close(self) -> None: ...
    def EndCopy(self, navigator: XPathNavigator) -> None: ...
    def EndTree(self) -> None: ...
    def Flush(self) -> None: ...
    @property
    def WriteState(self) -> WriteState: ...
    @property
    def XmlLang(self) -> str: ...
    @property
    def XmlSpace(self) -> XmlSpace: ...
    def LookupPrefix(self, ns: str) -> str: ...
    def StartCopy(self, navigator: XPathNavigator) -> bool: ...
    def StartElementContentUnchecked(self) -> None: ...
    def StartTree(self, rootType: XPathNodeType) -> None: ...
    def WriteBase64(self, buffer: Set(Byte), index: int, count: int) -> None: ...
    def WriteCData(self, text: str) -> None: ...
    def WriteCharEntity(self, ch: Char) -> None: ...
    def WriteChars(self, buffer: Set(Char), index: int, count: int) -> None: ...
    def WriteComment(self, text: str) -> None: ...
    def WriteCommentString(self, text: str) -> None: ...
    def WriteDocType(self, name: str, pubid: str, sysid: str, subset: str) -> None: ...
    def WriteEndAttribute(self) -> None: ...
    def WriteEndAttributeUnchecked(self) -> None: ...
    def WriteEndComment(self) -> None: ...
    def WriteEndDocument(self) -> None: ...
    def WriteEndElement(self) -> None: ...
    @overload
    def WriteEndElementUnchecked(self, localName: str) -> None: ...
    @overload
    def WriteEndElementUnchecked(self, prefix: str, localName: str, ns: str) -> None: ...
    def WriteEndNamespace(self) -> None: ...
    def WriteEndProcessingInstruction(self) -> None: ...
    def WriteEndRoot(self) -> None: ...
    def WriteEntityRef(self, name: str) -> None: ...
    def WriteFullEndElement(self) -> None: ...
    def WriteItem(self, item: XPathItem) -> None: ...
    def WriteNamespaceDeclaration(self, prefix: str, ns: str) -> None: ...
    def WriteNamespaceDeclarationUnchecked(self, prefix: str, ns: str) -> None: ...
    def WriteNamespaceString(self, text: str) -> None: ...
    def WriteProcessingInstruction(self, target: str, text: str) -> None: ...
    def WriteProcessingInstructionString(self, text: str) -> None: ...
    @overload
    def WriteRaw(self, data: str) -> None: ...
    @overload
    def WriteRaw(self, buffer: Set(Char), index: int, count: int) -> None: ...
    def WriteRawUnchecked(self, text: str) -> None: ...
    @overload
    def WriteStartAttribute(self, prefix: str, localName: str, ns: str) -> None: ...
    @overload
    def WriteStartAttributeComputed(self, navigator: XPathNavigator) -> None: ...
    @overload
    def WriteStartAttributeComputed(self, name: XmlQualifiedName) -> None: ...
    @overload
    def WriteStartAttributeComputed(self, tagName: str, prefixMappingsIndex: int) -> None: ...
    @overload
    def WriteStartAttributeComputed(self, tagName: str, ns: str) -> None: ...
    def WriteStartAttributeLocalName(self, localName: str) -> None: ...
    @overload
    def WriteStartAttributeUnchecked(self, localName: str) -> None: ...
    @overload
    def WriteStartAttributeUnchecked(self, prefix: str, localName: str, ns: str) -> None: ...
    def WriteStartComment(self) -> None: ...
    @overload
    def WriteStartDocument(self) -> None: ...
    @overload
    def WriteStartDocument(self, standalone: bool) -> None: ...
    @overload
    def WriteStartElement(self, prefix: str, localName: str, ns: str) -> None: ...
    @overload
    def WriteStartElementComputed(self, navigator: XPathNavigator) -> None: ...
    @overload
    def WriteStartElementComputed(self, name: XmlQualifiedName) -> None: ...
    @overload
    def WriteStartElementComputed(self, tagName: str, prefixMappingsIndex: int) -> None: ...
    @overload
    def WriteStartElementComputed(self, tagName: str, ns: str) -> None: ...
    def WriteStartElementLocalName(self, localName: str) -> None: ...
    @overload
    def WriteStartElementUnchecked(self, localName: str) -> None: ...
    @overload
    def WriteStartElementUnchecked(self, prefix: str, localName: str, ns: str) -> None: ...
    def WriteStartNamespace(self, prefix: str) -> None: ...
    def WriteStartProcessingInstruction(self, target: str) -> None: ...
    def WriteStartRoot(self) -> None: ...
    def WriteString(self, text: str) -> None: ...
    def WriteStringUnchecked(self, text: str) -> None: ...
    def WriteSurrogateCharEntity(self, lowChar: Char, highChar: Char) -> None: ...
    def WriteWhitespace(self, ws: str) -> None: ...
    def XsltCopyOf(self, navigator: XPathNavigator) -> None: ...


class XmlQueryRuntime(Object):
    def AddNewIndex(self, context: XPathNavigator, indexId: int, index: XmlILIndex) -> None: ...
    def ChangeTypeXsltArgument(self, indexType: int, value: Object, destinationType: Type) -> Object: ...
    def ChangeTypeXsltResult(self, indexType: int, value: Object) -> Object: ...
    def ComparePosition(self, navigatorThis: XPathNavigator, navigatorThat: XPathNavigator) -> int: ...
    def CreateCollation(self, collation: str) -> XmlCollation: ...
    def DebugGetGlobalNames(self) -> Set(str): ...
    def DebugGetGlobalValue(self, name: str) -> IList: ...
    def DebugGetXsltValue(self, seq: IList) -> Object: ...
    def DebugSetGlobalValue(self, name: str, value: Object) -> None: ...
    def DocOrderDistinct(self, seq: List[XPathNavigator]) -> List[XPathNavigator]: ...
    def EarlyBoundFunctionExists(self, name: str, namespaceUri: str) -> bool: ...
    def EndRtfConstruction(self) -> Tuple[XPathNavigator, XmlQueryOutput]: ...
    def EndSequenceConstruction(self) -> Tuple[List[XPathItem], XmlQueryOutput]: ...
    def FindIndex(self, context: XPathNavigator, indexId: int) -> Tuple[bool, XmlILIndex]: ...
    def GenerateId(self, navigator: XPathNavigator) -> str: ...
    @property
    def ExternalContext(self) -> XmlQueryContext: ...
    @property
    def NameTable(self) -> XmlNameTable: ...
    @property
    def Output(self) -> XmlQueryOutput: ...
    @property
    def XsltFunctions(self) -> XsltLibrary: ...
    def GetAtomizedName(self, index: int) -> str: ...
    def GetCollation(self, index: int) -> XmlCollation: ...
    def GetEarlyBoundObject(self, index: int) -> Object: ...
    def GetGlobalValue(self, index: int) -> Object: ...
    def GetNameFilter(self, index: int) -> XmlNavigatorFilter: ...
    def GetTypeFilter(self, nodeType: XPathNodeType) -> XmlNavigatorFilter: ...
    def IsGlobalComputed(self, index: int) -> bool: ...
    @overload
    def IsQNameEqual(self, n1: XPathNavigator, n2: XPathNavigator) -> bool: ...
    @overload
    def IsQNameEqual(self, navigator: XPathNavigator, indexLocalName: int, indexNamespaceUri: int) -> bool: ...
    @overload
    def MatchesXmlType(self, seq: List[XPathItem], code: XmlTypeCode) -> bool: ...
    @overload
    def MatchesXmlType(self, item: XPathItem, code: XmlTypeCode) -> bool: ...
    @overload
    def MatchesXmlType(self, item: XPathItem, indexType: int) -> bool: ...
    @overload
    def MatchesXmlType(self, seq: List[XPathItem], indexType: int) -> bool: ...
    def OnCurrentNodeChanged(currentNode: XPathNavigator) -> int: ...
    @overload
    def ParseTagName(self, tagName: str, indexPrefixMappings: int) -> XmlQualifiedName: ...
    @overload
    def ParseTagName(self, tagName: str, ns: str) -> XmlQualifiedName: ...
    def SendMessage(self, message: str) -> None: ...
    def SetGlobalValue(self, index: int, value: Object) -> None: ...
    def StartRtfConstruction(self, baseUri: str) -> Tuple[XmlQueryOutput]: ...
    def StartSequenceConstruction(self) -> Tuple[XmlQueryOutput]: ...
    def TextRtfConstruction(self, text: str, baseUri: str) -> XPathNavigator: ...
    def ThrowException(self, text: str) -> None: ...




class XmlSortKeyAccumulator(ValueType):
    def AddDateTimeSortKey(self, collation: XmlCollation, value: DateTime) -> None: ...
    def AddDecimalSortKey(self, collation: XmlCollation, value: Decimal) -> None: ...
    def AddDoubleSortKey(self, collation: XmlCollation, value: float) -> None: ...
    def AddEmptySortKey(self, collation: XmlCollation) -> None: ...
    def AddIntegerSortKey(self, collation: XmlCollation, value: Int64) -> None: ...
    def AddIntSortKey(self, collation: XmlCollation, value: int) -> None: ...
    def AddStringSortKey(self, collation: XmlCollation, value: str) -> None: ...
    def Create(self) -> None: ...
    def FinishSortKeys(self) -> None: ...
    @property
    def Keys(self) -> Array: ...


class XPathFollowingIterator(ValueType):
    def Create(self, input: XPathNavigator, filter: XmlNavigatorFilter) -> None: ...
    @property
    def Current(self) -> XPathNavigator: ...
    def MoveNext(self) -> bool: ...


class XPathFollowingMergeIterator(ValueType):
    def Create(self, filter: XmlNavigatorFilter) -> None: ...
    @property
    def Current(self) -> XPathNavigator: ...
    def MoveNext(self, input: XPathNavigator) -> IteratorResult: ...


class XPathPrecedingDocOrderIterator(ValueType):
    def Create(self, input: XPathNavigator, filter: XmlNavigatorFilter) -> None: ...
    @property
    def Current(self) -> XPathNavigator: ...
    def MoveNext(self) -> bool: ...


class XPathPrecedingIterator(ValueType):
    def Create(self, context: XPathNavigator, filter: XmlNavigatorFilter) -> None: ...
    @property
    def Current(self) -> XPathNavigator: ...
    def MoveNext(self) -> bool: ...


class XPathPrecedingMergeIterator(ValueType):
    def Create(self, filter: XmlNavigatorFilter) -> None: ...
    @property
    def Current(self) -> XPathNavigator: ...
    def MoveNext(self, input: XPathNavigator) -> IteratorResult: ...


class XsltConvert(Object):
    def EnsureNodeSet(listItems: List[XPathItem]) -> List[XPathNavigator]: ...
    @overload
    def ToBoolean(item: XPathItem) -> bool: ...
    @overload
    def ToBoolean(listItems: List[XPathItem]) -> bool: ...
    def ToDateTime(value: str) -> DateTime: ...
    def ToDecimal(value: float) -> Decimal: ...
    @overload
    def ToDouble(value: int) -> float: ...
    @overload
    def ToDouble(value: str) -> float: ...
    @overload
    def ToDouble(item: XPathItem) -> float: ...
    @overload
    def ToDouble(value: Decimal) -> float: ...
    @overload
    def ToDouble(listItems: List[XPathItem]) -> float: ...
    @overload
    def ToDouble(value: Int64) -> float: ...
    def ToInt(value: float) -> int: ...
    def ToLong(value: float) -> Int64: ...
    @overload
    def ToNode(item: XPathItem) -> XPathNavigator: ...
    @overload
    def ToNode(listItems: List[XPathItem]) -> XPathNavigator: ...
    @overload
    def ToNodeSet(listItems: List[XPathItem]) -> List[XPathNavigator]: ...
    @overload
    def ToNodeSet(item: XPathItem) -> List[XPathNavigator]: ...
    @overload
    def ToString(item: XPathItem) -> str: ...
    @overload
    def ToString(value: float) -> str: ...
    @overload
    def ToString(listItems: List[XPathItem]) -> str: ...
    @overload
    def ToString(value: DateTime) -> str: ...


class XsltFunctions(Object):
    def BaseUri(navigator: XPathNavigator) -> str: ...
    def Contains(s1: str, s2: str) -> bool: ...
    def EXslObjectType(value: List[XPathItem]) -> str: ...
    def Lang(value: str, context: XPathNavigator) -> bool: ...
    def MSFormatDateTime(dateTime: str, format: str, lang: str, isDate: bool) -> str: ...
    def MSLocalName(name: str) -> str: ...
    def MSNamespaceUri(name: str, currentNode: XPathNavigator) -> str: ...
    def MSNumber(value: List[XPathItem]) -> float: ...
    def MSStringCompare(s1: str, s2: str, lang: str, options: str) -> float: ...
    def MSUtc(dateTime: str) -> str: ...
    def NormalizeSpace(value: str) -> str: ...
    def OuterXml(navigator: XPathNavigator) -> str: ...
    def Round(value: float) -> float: ...
    def StartsWith(s1: str, s2: str) -> bool: ...
    @overload
    def Substring(value: str, startIndex: float) -> str: ...
    @overload
    def Substring(value: str, startIndex: float, length: float) -> str: ...
    def SubstringAfter(s1: str, s2: str) -> str: ...
    def SubstringBefore(s1: str, s2: str) -> str: ...
    def SystemProperty(name: XmlQualifiedName) -> XPathItem: ...
    def Translate(arg: str, mapString: str, transString: str) -> str: ...


class XsltLibrary(Object):
    def CheckScriptNamespace(self, nsUri: str) -> int: ...
    def ElementAvailable(self, name: XmlQualifiedName) -> bool: ...
    def EqualityOperator(self, opCode: float, left: List[XPathItem], right: List[XPathItem]) -> bool: ...
    def FormatMessage(self, res: str, args: List[str]) -> str: ...
    def FormatNumberDynamic(self, value: float, formatPicture: str, decimalFormatName: XmlQualifiedName, errorMessageName: str) -> str: ...
    def FormatNumberStatic(self, value: float, decimalFormatterIndex: float) -> str: ...
    def FunctionAvailable(self, name: XmlQualifiedName) -> bool: ...
    def IsSameNodeSort(self, nav1: XPathNavigator, nav2: XPathNavigator) -> bool: ...
    def LangToLcid(self, lang: str, forwardCompatibility: bool) -> int: ...
    def NumberFormat(self, value: List[XPathItem], formatString: str, lang: float, letterValue: str, groupingSeparator: str, groupingSize: float) -> str: ...
    def RegisterDecimalFormat(self, name: XmlQualifiedName, infinitySymbol: str, nanSymbol: str, characters: str) -> int: ...
    def RegisterDecimalFormatter(self, formatPicture: str, infinitySymbol: str, nanSymbol: str, characters: str) -> float: ...
    def RelationalOperator(self, opCode: float, left: List[XPathItem], right: List[XPathItem]) -> bool: ...
