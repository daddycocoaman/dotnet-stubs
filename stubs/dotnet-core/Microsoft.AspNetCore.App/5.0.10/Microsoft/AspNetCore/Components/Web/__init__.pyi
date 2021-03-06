__all__ = ['Virtualization']
from typing import Tuple, Set, Iterable, List


class BindAttributes:
    pass


class ClipboardEventArgs:
    def __init__(self): ...
    @property
    def Type(self) -> str: ...
    @Type.setter
    def Type(self, value: str) -> None: ...


class DataTransfer:
    def __init__(self): ...
    @property
    def DropEffect(self) -> str: ...
    @property
    def EffectAllowed(self) -> str: ...
    @property
    def Files(self) -> Set(str): ...
    @property
    def Items(self) -> Set(DataTransferItem): ...
    @property
    def Types(self) -> Set(str): ...
    @DropEffect.setter
    def DropEffect(self, value: str) -> None: ...
    @EffectAllowed.setter
    def EffectAllowed(self, value: str) -> None: ...
    @Files.setter
    def Files(self, value: Set(str)) -> None: ...
    @Items.setter
    def Items(self, value: Set(DataTransferItem)) -> None: ...
    @Types.setter
    def Types(self, value: Set(str)) -> None: ...


class DataTransferItem:
    def __init__(self): ...
    @property
    def Kind(self) -> str: ...
    @property
    def Type(self) -> str: ...
    @Kind.setter
    def Kind(self, value: str) -> None: ...
    @Type.setter
    def Type(self, value: str) -> None: ...


class DragEventArgs(MouseEventArgs):
    def __init__(self): ...
    @property
    def DataTransfer(self) -> DataTransfer: ...
    @DataTransfer.setter
    def DataTransfer(self, value: DataTransfer) -> None: ...


class ErrorEventArgs:
    def __init__(self): ...
    @property
    def Colno(self) -> int: ...
    @property
    def Filename(self) -> str: ...
    @property
    def Lineno(self) -> int: ...
    @property
    def Message(self) -> str: ...
    @property
    def Type(self) -> str: ...
    @Colno.setter
    def Colno(self, value: int) -> None: ...
    @Filename.setter
    def Filename(self, value: str) -> None: ...
    @Lineno.setter
    def Lineno(self, value: int) -> None: ...
    @Message.setter
    def Message(self, value: str) -> None: ...
    @Type.setter
    def Type(self, value: str) -> None: ...


class EventHandlers:
    pass


class FocusEventArgs:
    def __init__(self): ...
    @property
    def Type(self) -> str: ...
    @Type.setter
    def Type(self, value: str) -> None: ...


class KeyboardEventArgs:
    def __init__(self): ...
    @property
    def AltKey(self) -> bool: ...
    @property
    def Code(self) -> str: ...
    @property
    def CtrlKey(self) -> bool: ...
    @property
    def Key(self) -> str: ...
    @property
    def Location(self) -> Single: ...
    @property
    def MetaKey(self) -> bool: ...
    @property
    def Repeat(self) -> bool: ...
    @property
    def ShiftKey(self) -> bool: ...
    @property
    def Type(self) -> str: ...
    @AltKey.setter
    def AltKey(self, value: bool) -> None: ...
    @Code.setter
    def Code(self, value: str) -> None: ...
    @CtrlKey.setter
    def CtrlKey(self, value: bool) -> None: ...
    @Key.setter
    def Key(self, value: str) -> None: ...
    @Location.setter
    def Location(self, value: Single) -> None: ...
    @MetaKey.setter
    def MetaKey(self, value: bool) -> None: ...
    @Repeat.setter
    def Repeat(self, value: bool) -> None: ...
    @ShiftKey.setter
    def ShiftKey(self, value: bool) -> None: ...
    @Type.setter
    def Type(self, value: str) -> None: ...


class MouseEventArgs:
    def __init__(self): ...
    @property
    def AltKey(self) -> bool: ...
    @property
    def Button(self) -> Int64: ...
    @property
    def Buttons(self) -> Int64: ...
    @property
    def ClientX(self) -> float: ...
    @property
    def ClientY(self) -> float: ...
    @property
    def CtrlKey(self) -> bool: ...
    @property
    def Detail(self) -> Int64: ...
    @property
    def MetaKey(self) -> bool: ...
    @property
    def OffsetX(self) -> float: ...
    @property
    def OffsetY(self) -> float: ...
    @property
    def ScreenX(self) -> float: ...
    @property
    def ScreenY(self) -> float: ...
    @property
    def ShiftKey(self) -> bool: ...
    @property
    def Type(self) -> str: ...
    @AltKey.setter
    def AltKey(self, value: bool) -> None: ...
    @Button.setter
    def Button(self, value: Int64) -> None: ...
    @Buttons.setter
    def Buttons(self, value: Int64) -> None: ...
    @ClientX.setter
    def ClientX(self, value: float) -> None: ...
    @ClientY.setter
    def ClientY(self, value: float) -> None: ...
    @CtrlKey.setter
    def CtrlKey(self, value: bool) -> None: ...
    @Detail.setter
    def Detail(self, value: Int64) -> None: ...
    @MetaKey.setter
    def MetaKey(self, value: bool) -> None: ...
    @OffsetX.setter
    def OffsetX(self, value: float) -> None: ...
    @OffsetY.setter
    def OffsetY(self, value: float) -> None: ...
    @ScreenX.setter
    def ScreenX(self, value: float) -> None: ...
    @ScreenY.setter
    def ScreenY(self, value: float) -> None: ...
    @ShiftKey.setter
    def ShiftKey(self, value: bool) -> None: ...
    @Type.setter
    def Type(self, value: str) -> None: ...


class PointerEventArgs(MouseEventArgs):
    def __init__(self): ...
    @property
    def Height(self) -> Single: ...
    @property
    def IsPrimary(self) -> bool: ...
    @property
    def PointerId(self) -> Int64: ...
    @property
    def PointerType(self) -> str: ...
    @property
    def Pressure(self) -> Single: ...
    @property
    def TiltX(self) -> Single: ...
    @property
    def TiltY(self) -> Single: ...
    @property
    def Width(self) -> Single: ...
    @Height.setter
    def Height(self, value: Single) -> None: ...
    @IsPrimary.setter
    def IsPrimary(self, value: bool) -> None: ...
    @PointerId.setter
    def PointerId(self, value: Int64) -> None: ...
    @PointerType.setter
    def PointerType(self, value: str) -> None: ...
    @Pressure.setter
    def Pressure(self, value: Single) -> None: ...
    @TiltX.setter
    def TiltX(self, value: Single) -> None: ...
    @TiltY.setter
    def TiltY(self, value: Single) -> None: ...
    @Width.setter
    def Width(self, value: Single) -> None: ...


class ProgressEventArgs:
    def __init__(self): ...
    @property
    def LengthComputable(self) -> bool: ...
    @property
    def Loaded(self) -> Int64: ...
    @property
    def Total(self) -> Int64: ...
    @property
    def Type(self) -> str: ...
    @LengthComputable.setter
    def LengthComputable(self, value: bool) -> None: ...
    @Loaded.setter
    def Loaded(self, value: Int64) -> None: ...
    @Total.setter
    def Total(self, value: Int64) -> None: ...
    @Type.setter
    def Type(self, value: str) -> None: ...


class TouchEventArgs:
    def __init__(self): ...
    @property
    def AltKey(self) -> bool: ...
    @property
    def ChangedTouches(self) -> Set(TouchPoint): ...
    @property
    def CtrlKey(self) -> bool: ...
    @property
    def Detail(self) -> Int64: ...
    @property
    def MetaKey(self) -> bool: ...
    @property
    def ShiftKey(self) -> bool: ...
    @property
    def TargetTouches(self) -> Set(TouchPoint): ...
    @property
    def Touches(self) -> Set(TouchPoint): ...
    @property
    def Type(self) -> str: ...
    @AltKey.setter
    def AltKey(self, value: bool) -> None: ...
    @ChangedTouches.setter
    def ChangedTouches(self, value: Set(TouchPoint)) -> None: ...
    @CtrlKey.setter
    def CtrlKey(self, value: bool) -> None: ...
    @Detail.setter
    def Detail(self, value: Int64) -> None: ...
    @MetaKey.setter
    def MetaKey(self, value: bool) -> None: ...
    @ShiftKey.setter
    def ShiftKey(self, value: bool) -> None: ...
    @TargetTouches.setter
    def TargetTouches(self, value: Set(TouchPoint)) -> None: ...
    @Touches.setter
    def Touches(self, value: Set(TouchPoint)) -> None: ...
    @Type.setter
    def Type(self, value: str) -> None: ...


class TouchPoint:
    def __init__(self): ...
    @property
    def ClientX(self) -> float: ...
    @property
    def ClientY(self) -> float: ...
    @property
    def Identifier(self) -> Int64: ...
    @property
    def PageX(self) -> float: ...
    @property
    def PageY(self) -> float: ...
    @property
    def ScreenX(self) -> float: ...
    @property
    def ScreenY(self) -> float: ...
    @ClientX.setter
    def ClientX(self, value: float) -> None: ...
    @ClientY.setter
    def ClientY(self, value: float) -> None: ...
    @Identifier.setter
    def Identifier(self, value: Int64) -> None: ...
    @PageX.setter
    def PageX(self, value: float) -> None: ...
    @PageY.setter
    def PageY(self, value: float) -> None: ...
    @ScreenX.setter
    def ScreenX(self, value: float) -> None: ...
    @ScreenY.setter
    def ScreenY(self, value: float) -> None: ...


class WebEventCallbackFactoryEventArgsExtensions:
    @overload
    def Create(factory: EventCallbackFactory, receiver: Object, callback: Action) -> EventCallback: ...
    @overload
    def Create(factory: EventCallbackFactory, receiver: Object, callback: Func) -> EventCallback: ...
    @overload
    def Create(factory: EventCallbackFactory, receiver: Object, callback: Action) -> EventCallback: ...
    @overload
    def Create(factory: EventCallbackFactory, receiver: Object, callback: Func) -> EventCallback: ...
    @overload
    def Create(factory: EventCallbackFactory, receiver: Object, callback: Action) -> EventCallback: ...
    @overload
    def Create(factory: EventCallbackFactory, receiver: Object, callback: Func) -> EventCallback: ...
    @overload
    def Create(factory: EventCallbackFactory, receiver: Object, callback: Action) -> EventCallback: ...
    @overload
    def Create(factory: EventCallbackFactory, receiver: Object, callback: Func) -> EventCallback: ...
    @overload
    def Create(factory: EventCallbackFactory, receiver: Object, callback: Action) -> EventCallback: ...
    @overload
    def Create(factory: EventCallbackFactory, receiver: Object, callback: Action) -> EventCallback: ...
    @overload
    def Create(factory: EventCallbackFactory, receiver: Object, callback: Func) -> EventCallback: ...
    @overload
    def Create(factory: EventCallbackFactory, receiver: Object, callback: Action) -> EventCallback: ...
    @overload
    def Create(factory: EventCallbackFactory, receiver: Object, callback: Func) -> EventCallback: ...
    @overload
    def Create(factory: EventCallbackFactory, receiver: Object, callback: Action) -> EventCallback: ...
    @overload
    def Create(factory: EventCallbackFactory, receiver: Object, callback: Func) -> EventCallback: ...
    @overload
    def Create(factory: EventCallbackFactory, receiver: Object, callback: Action) -> EventCallback: ...
    @overload
    def Create(factory: EventCallbackFactory, receiver: Object, callback: Func) -> EventCallback: ...
    @overload
    def Create(factory: EventCallbackFactory, receiver: Object, callback: Action) -> EventCallback: ...
    @overload
    def Create(factory: EventCallbackFactory, receiver: Object, callback: Func) -> EventCallback: ...
    @overload
    def Create(factory: EventCallbackFactory, receiver: Object, callback: Func) -> EventCallback: ...


class WebRenderTreeBuilderExtensions:
    def AddEventPreventDefaultAttribute(builder: RenderTreeBuilder, sequence: int, eventName: str, value: bool) -> None: ...
    def AddEventStopPropagationAttribute(builder: RenderTreeBuilder, sequence: int, eventName: str, value: bool) -> None: ...


class WheelEventArgs(MouseEventArgs):
    def __init__(self): ...
    @property
    def DeltaMode(self) -> Int64: ...
    @property
    def DeltaX(self) -> float: ...
    @property
    def DeltaY(self) -> float: ...
    @property
    def DeltaZ(self) -> float: ...
    @DeltaMode.setter
    def DeltaMode(self, value: Int64) -> None: ...
    @DeltaX.setter
    def DeltaX(self, value: float) -> None: ...
    @DeltaY.setter
    def DeltaY(self, value: float) -> None: ...
    @DeltaZ.setter
    def DeltaZ(self, value: float) -> None: ...
