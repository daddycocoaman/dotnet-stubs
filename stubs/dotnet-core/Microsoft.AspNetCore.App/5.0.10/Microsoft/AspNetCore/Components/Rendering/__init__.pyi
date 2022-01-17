from typing import Tuple, Set, Iterable, List


class RenderTreeBuilder:
    def __init__(self): ...
    @overload
    def AddAttribute(self, sequence: int, frame: RenderTreeFrame) -> None: ...
    @overload
    def AddAttribute(self, sequence: int, name: str) -> None: ...
    @overload
    def AddAttribute(self, sequence: int, name: str, value: Object) -> None: ...
    @overload
    def AddAttribute(self, sequence: int, name: str, value: EventCallback) -> None: ...
    @overload
    def AddAttribute(self, sequence: int, name: str, value: EventCallback) -> None: ...
    @overload
    def AddAttribute(self, sequence: int, name: str, value: str) -> None: ...
    @overload
    def AddAttribute(self, sequence: int, name: str, value: bool) -> None: ...
    @overload
    def AddAttribute(self, sequence: int, name: str, value: MulticastDelegate) -> None: ...
    def AddComponentReferenceCapture(self, sequence: int, componentReferenceCaptureAction: Action) -> None: ...
    @overload
    def AddContent(self, sequence: int, markupContent: MarkupString) -> None: ...
    @overload
    def AddContent(self, sequence: int, fragment: RenderFragment) -> None: ...
    @overload
    def AddContent(self, sequence: int, textContent: str) -> None: ...
    @overload
    def AddContent(self, sequence: int, textContent: Object) -> None: ...
    @overload
    def AddContent(self, sequence: int, fragment: RenderFragment, value: TValue) -> None: ...
    def AddElementReferenceCapture(self, sequence: int, elementReferenceCaptureAction: Action) -> None: ...
    def AddMarkupContent(self, sequence: int, markupContent: str) -> None: ...
    def AddMultipleAttributes(self, sequence: int, attributes: Iterable[KeyValuePair]) -> None: ...
    def Clear(self) -> None: ...
    def CloseComponent(self) -> None: ...
    def CloseElement(self) -> None: ...
    def CloseRegion(self) -> None: ...
    def GetFrames(self) -> ArrayRange: ...
    @overload
    def OpenComponent(self, sequence: int) -> None: ...
    @overload
    def OpenComponent(self, sequence: int, componentType: Type) -> None: ...
    def OpenElement(self, sequence: int, elementName: str) -> None: ...
    def OpenRegion(self, sequence: int) -> None: ...
    def SetKey(self, value: Object) -> None: ...
    def SetUpdatesAttributeName(self, updatesAttributeName: str) -> None: ...
