from typing import Tuple, Set, Iterable, List


class ErrorTypeDefinition:
    def __init__(self): ...


class IErrorProviderFactory:
    def GetErrorTagger(self, textBuffer: ITextBuffer) -> SimpleTagger: ...


class ITextMarkerProviderFactory:
    def GetTextMarkerTagger(self, textBuffer: ITextBuffer) -> SimpleTagger: ...


class IToolTipProvider:
    def ClearToolTip(self) -> None: ...
    @overload
    def ShowToolTip(self, span: ITrackingSpan, toolTipContent: Object) -> None: ...
    @overload
    def ShowToolTip(self, span: ITrackingSpan, toolTipContent: Object, style: PopupStyles) -> None: ...


class IToolTipProviderFactory:
    def GetToolTipProvider(self, textView: ITextView) -> IToolTipProvider: ...


class PopupStyles:
    #None = 0
    DismissOnMouseLeaveText = 4
    DismissOnMouseLeaveTextOrContent = 8
    PositionLeftOrRight = 16
    PreferLeftOrTopPosition = 32
    RightOrBottomJustify = 64
    PositionClosest = 128


class PredefinedErrorTypeNames:
    pass
