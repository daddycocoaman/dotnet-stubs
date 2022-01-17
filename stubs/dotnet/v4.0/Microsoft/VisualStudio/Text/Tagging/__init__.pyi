from typing import Tuple, Set, Iterable, List


class BatchedTagsChangedEventArgs:
    def __init__(self, spans: List[IMappingSpan]): ...
    @property
    def Spans(self) -> ReadOnlyCollection: ...


class ClassificationTag:
    def __init__(self, type: IClassificationType): ...
    @property
    def ClassificationType(self) -> IClassificationType: ...


class ErrorTag:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, errorType: str): ...
    @overload
    def __init__(self, errorType: str, toolTipContent: Object): ...
    @property
    def ErrorType(self) -> str: ...
    @property
    def ToolTipContent(self) -> Object: ...


class IBufferTagAggregatorFactoryService:
    @overload
    def CreateTagAggregator(self, textBuffer: ITextBuffer) -> ITagAggregator: ...
    @overload
    def CreateTagAggregator(self, textBuffer: ITextBuffer, options: TagAggregatorOptions) -> ITagAggregator: ...


class IClassificationTag:
    @property
    def ClassificationType(self) -> IClassificationType: ...


class IElisionTag:
    pass


class IErrorTag:
    @property
    def ErrorType(self) -> str: ...
    @property
    def ToolTipContent(self) -> Object: ...




class IOutliningRegionTag:
    @property
    def CollapsedForm(self) -> Object: ...
    @property
    def CollapsedHintForm(self) -> Object: ...
    @property
    def IsDefaultCollapsed(self) -> bool: ...
    @property
    def IsImplementation(self) -> bool: ...


class ITag:
    pass






class ITaggerMetadata:
    @property
    def ContentTypes(self) -> Iterable[str]: ...
    @property
    def TagTypes(self) -> Iterable[Type]: ...


class ITaggerProvider:
    def CreateTagger(self, buffer: ITextBuffer) -> ITagger: ...




class ITextMarkerTag:
    @property
    def Type(self) -> str: ...


class IUrlTag:
    @property
    def Url(self) -> Uri: ...


class IViewTagAggregatorFactoryService:
    @overload
    def CreateTagAggregator(self, textView: ITextView) -> ITagAggregator: ...
    @overload
    def CreateTagAggregator(self, textView: ITextView, options: TagAggregatorOptions) -> ITagAggregator: ...


class IViewTaggerProvider:
    def CreateTagger(self, textView: ITextView, buffer: ITextBuffer) -> ITagger: ...




class OutliningRegionTag:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, collapsedForm: Object, collapsedHintForm: Object): ...
    @overload
    def __init__(self, isDefaultCollapsed: bool, isImplementation: bool, collapsedForm: Object, collapsedHintForm: Object): ...
    @property
    def CollapsedForm(self) -> Object: ...
    @property
    def CollapsedHintForm(self) -> Object: ...
    @property
    def IsDefaultCollapsed(self) -> bool: ...
    @property
    def IsImplementation(self) -> bool: ...




class SpaceNegotiatingAdornmentTag:
    def __init__(self, width: float, topSpace: float, baseline: float, textHeight: float, bottomSpace: float, affinity: PositionAffinity, identityTag: Object, providerTag: Object): ...
    @property
    def Affinity(self) -> PositionAffinity: ...
    @property
    def Baseline(self) -> float: ...
    @property
    def BottomSpace(self) -> float: ...
    @property
    def IdentityTag(self) -> Object: ...
    @property
    def ProviderTag(self) -> Object: ...
    @property
    def TextHeight(self) -> float: ...
    @property
    def TopSpace(self) -> float: ...
    @property
    def Width(self) -> float: ...


class TagAggregatorOptions:
    #None = 0
    MapByContentType = 1


class TagsChangedEventArgs:
    def __init__(self, span: IMappingSpan): ...
    @property
    def Span(self) -> IMappingSpan: ...




class TagTypeAttribute(MultipleBaseMetadataAttribute):
    def __init__(self, tagType: Type): ...
    @property
    def TagTypes(self) -> Type: ...


class TextMarkerTag:
    def __init__(self, type: str): ...
    @property
    def Type(self) -> str: ...




class UrlTag:
    def __init__(self, url: Uri): ...
    @property
    def Url(self) -> Uri: ...
