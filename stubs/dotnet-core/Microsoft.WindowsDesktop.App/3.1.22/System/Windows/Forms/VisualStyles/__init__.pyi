from typing import Tuple, Set, Iterable, List


class AnimateBackground(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class ArrowButton(Object):
    @property
    def DownDisabled() -> VisualStyleElement: ...
    @property
    def DownHot() -> VisualStyleElement: ...
    @property
    def DownNormal() -> VisualStyleElement: ...
    @property
    def DownPressed() -> VisualStyleElement: ...
    @property
    def LeftDisabled() -> VisualStyleElement: ...
    @property
    def LeftHot() -> VisualStyleElement: ...
    @property
    def LeftNormal() -> VisualStyleElement: ...
    @property
    def LeftPressed() -> VisualStyleElement: ...
    @property
    def RightDisabled() -> VisualStyleElement: ...
    @property
    def RightHot() -> VisualStyleElement: ...
    @property
    def RightNormal() -> VisualStyleElement: ...
    @property
    def RightPressed() -> VisualStyleElement: ...
    @property
    def UpDisabled() -> VisualStyleElement: ...
    @property
    def UpHot() -> VisualStyleElement: ...
    @property
    def UpNormal() -> VisualStyleElement: ...
    @property
    def UpPressed() -> VisualStyleElement: ...


class Background(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class BackgroundBottom(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class BackgroundLeft(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class BackgroundRight(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class BackgroundTop(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class BackgroundType:
    ImageFile = 0
    BorderFill = 1
    #None = 2


class Balloon(Object):
    @property
    def Link() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...


class BalloonTitle(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class Band(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class Bar(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class Bar(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class BarDropDown(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class BarItem(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class BarVertical(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class Body(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class BooleanProperty:
    Transparent = 2201
    AutoSize = 2202
    BorderOnly = 2203
    Composited = 2204
    BackgroundFill = 2205
    GlyphTransparent = 2206
    GlyphOnly = 2207
    AlwaysShowSizingBar = 2208
    MirrorImage = 2209
    UniformSizing = 2210
    IntegralSizing = 2211
    SourceGrow = 2212
    SourceShrink = 2213


class BorderType:
    Rectangle = 0
    RoundedRectangle = 1
    Ellipse = 2


class Branch(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class Button(Object):
    @property
    def Checked() -> VisualStyleElement: ...
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def HotChecked() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class Button(Object):
    pass


class Caption(Object):
    @property
    def Active() -> VisualStyleElement: ...
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Inactive() -> VisualStyleElement: ...


class CaptionSizingTemplate(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class Caret(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class CheckBox(Object):
    @property
    def CheckedDisabled() -> VisualStyleElement: ...
    @property
    def CheckedHot() -> VisualStyleElement: ...
    @property
    def CheckedNormal() -> VisualStyleElement: ...
    @property
    def CheckedPressed() -> VisualStyleElement: ...
    @property
    def MixedDisabled() -> VisualStyleElement: ...
    @property
    def MixedHot() -> VisualStyleElement: ...
    @property
    def MixedNormal() -> VisualStyleElement: ...
    @property
    def MixedPressed() -> VisualStyleElement: ...
    @property
    def UncheckedDisabled() -> VisualStyleElement: ...
    @property
    def UncheckedHot() -> VisualStyleElement: ...
    @property
    def UncheckedNormal() -> VisualStyleElement: ...
    @property
    def UncheckedPressed() -> VisualStyleElement: ...


class CheckBoxState:
    UncheckedNormal = 1
    UncheckedHot = 2
    UncheckedPressed = 3
    UncheckedDisabled = 4
    CheckedNormal = 5
    CheckedHot = 6
    CheckedPressed = 7
    CheckedDisabled = 8
    MixedNormal = 9
    MixedHot = 10
    MixedPressed = 11
    MixedDisabled = 12


class Chevron(Object):
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class Chevron(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class ChevronVertical(Object):
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class Chunk(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class ChunkVertical(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class Close(Object):
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class CloseButton(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class ColorProperty:
    BorderColor = 3801
    FillColor = 3802
    TextColor = 3803
    EdgeLightColor = 3804
    EdgeHighlightColor = 3805
    EdgeShadowColor = 3806
    EdgeDarkShadowColor = 3807
    EdgeFillColor = 3808
    TransparentColor = 3809
    GradientColor1 = 3810
    GradientColor2 = 3811
    GradientColor3 = 3812
    GradientColor4 = 3813
    GradientColor5 = 3814
    ShadowColor = 3815
    GlowColor = 3816
    TextBorderColor = 3817
    TextShadowColor = 3818
    GlyphTextColor = 3819
    GlyphTransparentColor = 3820
    FillColorHint = 3821
    BorderColorHint = 3822
    AccentColorHint = 3823


class ComboBox(Object):
    pass


class ComboBoxState:
    Normal = 1
    Hot = 2
    Pressed = 3
    Disabled = 4


class ContentAlignment:
    Left = 0
    Center = 1
    Right = 2


class Detail(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class Dialog(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class Down(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class Down(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class DownHorizontal(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class DownHorizontal(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class DropDown(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class DropDownButton(Object):
    @property
    def Checked() -> VisualStyleElement: ...
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def HotChecked() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class DropDownButton(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class EdgeEffects:
    #None = 0
    FillInterior = 2048
    Flat = 4096
    Soft = 16384
    Mono = 32768


class Edges:
    Left = 1
    Top = 2
    Right = 4
    Bottom = 8
    Diagonal = 16


class EdgeStyle:
    Raised = 5
    Etched = 6
    Bump = 9
    Sunken = 10


class EmptyText(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class EnumProperty:
    BackgroundType = 4001
    BorderType = 4002
    FillType = 4003
    SizingType = 4004
    HorizontalAlignment = 4005
    ContentAlignment = 4006
    VerticalAlignment = 4007
    OffsetType = 4008
    IconEffect = 4009
    TextShadowType = 4010
    ImageLayout = 4011
    GlyphType = 4012
    ImageSelectType = 4013
    GlyphFontSizingType = 4014
    TrueSizeScalingType = 4015


class ExplorerBar(Object):
    pass


class FilenameProperty:
    ImageFile = 3001
    ImageFile1 = 3002
    ImageFile2 = 3003
    ImageFile3 = 3004
    ImageFile4 = 3005
    ImageFile5 = 3006
    StockImageFile = 3007
    GlyphImageFile = 3008


class FillType:
    Solid = 0
    VerticalGradient = 1
    HorizontalGradient = 2
    RadialGradient = 3
    TileImage = 4


class FlashButton(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class FlashButtonGroupMenu(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class FontProperty:
    GlyphFont = 2601


class FrameBottom(Object):
    @property
    def Active() -> VisualStyleElement: ...
    @property
    def Inactive() -> VisualStyleElement: ...


class FrameBottomSizingTemplate(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class FrameLeft(Object):
    @property
    def Active() -> VisualStyleElement: ...
    @property
    def Inactive() -> VisualStyleElement: ...


class FrameLeftSizingTemplate(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class FrameRight(Object):
    @property
    def Active() -> VisualStyleElement: ...
    @property
    def Inactive() -> VisualStyleElement: ...


class FrameRightSizingTemplate(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class Glyph(Object):
    @property
    def Closed() -> VisualStyleElement: ...
    @property
    def Opened() -> VisualStyleElement: ...


class GlyphFontSizingType:
    #None = 0
    Size = 1
    Dpi = 2


class GlyphType:
    #None = 0
    ImageGlyph = 1
    FontGlyph = 2


class Gripper(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class Gripper(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class GripperHorizontal(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class GripperPane(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class GripperVertical(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class GripperVertical(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class Group(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class GroupBox(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...


class GroupBoxState:
    Normal = 1
    Disabled = 2


class GroupCount(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class Header(Object):
    pass


class HeaderBackground(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class HeaderClose(Object):
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class HeaderPin(Object):
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...
    @property
    def SelectedHot() -> VisualStyleElement: ...
    @property
    def SelectedNormal() -> VisualStyleElement: ...
    @property
    def SelectedPressed() -> VisualStyleElement: ...


class HelpButton(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class HitTestCode:
    Nowhere = 0
    Client = 1
    Left = 10
    Right = 11
    Top = 12
    TopLeft = 13
    TopRight = 14
    Bottom = 15
    BottomLeft = 16
    BottomRight = 17


class HitTestOptions:
    BackgroundSegment = 0
    FixedBorder = 2
    Caption = 4
    ResizingBorderLeft = 16
    ResizingBorderTop = 32
    ResizingBorderRight = 64
    ResizingBorderBottom = 128
    ResizingBorder = 240
    SizingTemplate = 256
    SystemSizingMargins = 512


class HorizontalAlign:
    Left = 0
    Center = 1
    Right = 2


class HorizontalScroll(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class HorizontalThumb(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class IconEffect:
    #None = 0
    Glow = 1
    Shadow = 2
    Pulse = 3
    Alpha = 4


class IEBarMenu(Object):
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class ImageOrientation:
    Vertical = 0
    Horizontal = 1


class ImageSelectType:
    #None = 0
    Size = 1
    Dpi = 2


class IntegerProperty:
    ImageCount = 2401
    AlphaLevel = 2402
    BorderSize = 2403
    RoundCornerWidth = 2404
    RoundCornerHeight = 2405
    GradientRatio1 = 2406
    GradientRatio2 = 2407
    GradientRatio3 = 2408
    GradientRatio4 = 2409
    GradientRatio5 = 2410
    ProgressChunkSize = 2411
    ProgressSpaceSize = 2412
    Saturation = 2413
    TextBorderSize = 2414
    AlphaThreshold = 2415
    Width = 2416
    Height = 2417
    GlyphIndex = 2418
    TrueSizeStretchMark = 2419
    MinDpi1 = 2420
    MinDpi2 = 2421
    MinDpi3 = 2422
    MinDpi4 = 2423
    MinDpi5 = 2424


class Item(Object):
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class Item(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Selected() -> VisualStyleElement: ...
    @property
    def SelectedNotFocus() -> VisualStyleElement: ...


class Item(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Selected() -> VisualStyleElement: ...
    @property
    def SelectedNotFocus() -> VisualStyleElement: ...


class Item(Object):
    @property
    def Demoted() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Selected() -> VisualStyleElement: ...


class ItemLeft(Object):
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class ItemRight(Object):
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class LeftTrackHorizontal(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class ListView(Object):
    pass


class LogOff(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class LogOffButtons(Object):
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class LowerTrackVertical(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class MarginProperty:
    SizingMargins = 3601
    ContentMargins = 3602
    CaptionMargins = 3603


class MaxButton(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class MaxCaption(Object):
    @property
    def Active() -> VisualStyleElement: ...
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Inactive() -> VisualStyleElement: ...


class MdiCloseButton(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class MdiHelpButton(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class MdiMinButton(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class MdiRestoreButton(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class MdiSysButton(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class Menu(Object):
    pass


class MenuBand(Object):
    pass


class MinButton(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class MinCaption(Object):
    @property
    def Active() -> VisualStyleElement: ...
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Inactive() -> VisualStyleElement: ...


class MorePrograms(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class MoreProgramsArrow(Object):
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class NewApplicationButton(Object):
    @property
    def Checked() -> VisualStyleElement: ...
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def HotChecked() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class NormalGroupBackground(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class NormalGroupCollapse(Object):
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class NormalGroupExpand(Object):
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class NormalGroupHead(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class OffsetType:
    TopLeft = 0
    TopRight = 1
    TopMiddle = 2
    BottomLeft = 3
    BottomRight = 4
    BottomMiddle = 5
    MiddleLeft = 6
    MiddleRight = 7
    LeftOfCaption = 8
    RightOfCaption = 9
    LeftOfLastButton = 10
    RightOfLastButton = 11
    AboveLastButton = 12
    BelowLastButton = 13


class Page(Object):
    pass


class Pane(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class Pane(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class PlaceList(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class PlaceListSeparator(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class PointProperty:
    Offset = 3401
    TextShadowOffset = 3402
    MinSize = 3403
    MinSize1 = 3404
    MinSize2 = 3405
    MinSize3 = 3406
    MinSize4 = 3407
    MinSize5 = 3408


class Preview(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class ProgList(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class ProgListSeparator(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class ProgressBar(Object):
    pass


class PushButton(Object):
    @property
    def Default() -> VisualStyleElement: ...
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class PushButtonState:
    Normal = 1
    Hot = 2
    Pressed = 3
    Disabled = 4
    Default = 5


class RadioButton(Object):
    @property
    def CheckedDisabled() -> VisualStyleElement: ...
    @property
    def CheckedHot() -> VisualStyleElement: ...
    @property
    def CheckedNormal() -> VisualStyleElement: ...
    @property
    def CheckedPressed() -> VisualStyleElement: ...
    @property
    def UncheckedDisabled() -> VisualStyleElement: ...
    @property
    def UncheckedHot() -> VisualStyleElement: ...
    @property
    def UncheckedNormal() -> VisualStyleElement: ...
    @property
    def UncheckedPressed() -> VisualStyleElement: ...


class RadioButtonState:
    UncheckedNormal = 1
    UncheckedHot = 2
    UncheckedPressed = 3
    UncheckedDisabled = 4
    CheckedNormal = 5
    CheckedHot = 6
    CheckedPressed = 7
    CheckedDisabled = 8


class Rebar(Object):
    pass


class RestoreButton(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class RightTrackHorizontal(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class ScrollBar(Object):
    pass


class ScrollBarArrowButtonState:
    UpNormal = 1
    UpHot = 2
    UpPressed = 3
    UpDisabled = 4
    DownNormal = 5
    DownHot = 6
    DownPressed = 7
    DownDisabled = 8
    LeftNormal = 9
    LeftHot = 10
    LeftPressed = 11
    LeftDisabled = 12
    RightNormal = 13
    RightHot = 14
    RightPressed = 15
    RightDisabled = 16


class ScrollBarSizeBoxState:
    RightAlign = 1
    LeftAlign = 2


class ScrollBarState:
    Normal = 1
    Hot = 2
    Pressed = 3
    Disabled = 4


class Separator(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class Separator(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class SeparatorHorizontal(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class SeparatorVertical(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class SizeBox(Object):
    @property
    def LeftAlign() -> VisualStyleElement: ...
    @property
    def RightAlign() -> VisualStyleElement: ...


class SizingBarBottom(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class SizingBarLeft(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class SizingBarRight(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class SizingBarTop(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class SizingType:
    FixedSize = 0
    Stretch = 1
    Tile = 2


class SmallCaption(Object):
    @property
    def Active() -> VisualStyleElement: ...
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Inactive() -> VisualStyleElement: ...


class SmallCaptionSizingTemplate(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class SmallCloseButton(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class SmallFrameBottom(Object):
    @property
    def Active() -> VisualStyleElement: ...
    @property
    def Inactive() -> VisualStyleElement: ...


class SmallFrameBottomSizingTemplate(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class SmallFrameLeft(Object):
    @property
    def Active() -> VisualStyleElement: ...
    @property
    def Inactive() -> VisualStyleElement: ...


class SmallFrameLeftSizingTemplate(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class SmallFrameRight(Object):
    @property
    def Active() -> VisualStyleElement: ...
    @property
    def Inactive() -> VisualStyleElement: ...


class SmallFrameRightSizingTemplate(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class SmallMaxCaption(Object):
    @property
    def Active() -> VisualStyleElement: ...
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Inactive() -> VisualStyleElement: ...


class SmallMinCaption(Object):
    @property
    def Active() -> VisualStyleElement: ...
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Inactive() -> VisualStyleElement: ...


class SortArrow(Object):
    @property
    def SortedDown() -> VisualStyleElement: ...
    @property
    def SortedUp() -> VisualStyleElement: ...


class SortedDetail(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class SpecialGroupBackground(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class SpecialGroupCollapse(Object):
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class SpecialGroupExpand(Object):
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class SpecialGroupHead(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class Spin(Object):
    pass


class SplitButton(Object):
    @property
    def Checked() -> VisualStyleElement: ...
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def HotChecked() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class SplitButtonDropDown(Object):
    @property
    def Checked() -> VisualStyleElement: ...
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def HotChecked() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class Standard(Object):
    @property
    def Link() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...


class StandardTitle(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class StartPanel(Object):
    pass


class Status(Object):
    pass


class StringProperty:
    Text = 3201


class SysButton(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class Tab(Object):
    pass


class TabItem(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class TabItemBothEdges(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class TabItemLeftEdge(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class TabItemRightEdge(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class TabItemState:
    Normal = 1
    Hot = 2
    Selected = 3
    Disabled = 4


class TaskBand(Object):
    pass


class Taskbar(Object):
    pass


class TaskbarClock(Object):
    pass


class TextBox(Object):
    pass


class TextBoxState:
    Normal = 1
    Hot = 2
    Selected = 3
    Disabled = 4
    Readonly = 6
    Assist = 7


class TextEdit(Object):
    @property
    def Assist() -> VisualStyleElement: ...
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Focused() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def ReadOnly() -> VisualStyleElement: ...
    @property
    def Selected() -> VisualStyleElement: ...


class TextMetrics(ValueType):
    @property
    def Ascent(self) -> int: ...
    @property
    def AverageCharWidth(self) -> int: ...
    @property
    def BreakChar(self) -> Char: ...
    @property
    def CharSet(self) -> TextMetricsCharacterSet: ...
    @property
    def DefaultChar(self) -> Char: ...
    @property
    def Descent(self) -> int: ...
    @property
    def DigitizedAspectX(self) -> int: ...
    @property
    def DigitizedAspectY(self) -> int: ...
    @property
    def ExternalLeading(self) -> int: ...
    @property
    def FirstChar(self) -> Char: ...
    @property
    def Height(self) -> int: ...
    @property
    def InternalLeading(self) -> int: ...
    @property
    def Italic(self) -> bool: ...
    @property
    def LastChar(self) -> Char: ...
    @property
    def MaxCharWidth(self) -> int: ...
    @property
    def Overhang(self) -> int: ...
    @property
    def PitchAndFamily(self) -> TextMetricsPitchAndFamilyValues: ...
    @property
    def StruckOut(self) -> bool: ...
    @property
    def Underlined(self) -> bool: ...
    @property
    def Weight(self) -> int: ...
    @Ascent.setter
    def Ascent(self, value: int) -> None: ...
    @AverageCharWidth.setter
    def AverageCharWidth(self, value: int) -> None: ...
    @BreakChar.setter
    def BreakChar(self, value: Char) -> None: ...
    @CharSet.setter
    def CharSet(self, value: TextMetricsCharacterSet) -> None: ...
    @DefaultChar.setter
    def DefaultChar(self, value: Char) -> None: ...
    @Descent.setter
    def Descent(self, value: int) -> None: ...
    @DigitizedAspectX.setter
    def DigitizedAspectX(self, value: int) -> None: ...
    @DigitizedAspectY.setter
    def DigitizedAspectY(self, value: int) -> None: ...
    @ExternalLeading.setter
    def ExternalLeading(self, value: int) -> None: ...
    @FirstChar.setter
    def FirstChar(self, value: Char) -> None: ...
    @Height.setter
    def Height(self, value: int) -> None: ...
    @InternalLeading.setter
    def InternalLeading(self, value: int) -> None: ...
    @Italic.setter
    def Italic(self, value: bool) -> None: ...
    @LastChar.setter
    def LastChar(self, value: Char) -> None: ...
    @MaxCharWidth.setter
    def MaxCharWidth(self, value: int) -> None: ...
    @Overhang.setter
    def Overhang(self, value: int) -> None: ...
    @PitchAndFamily.setter
    def PitchAndFamily(self, value: TextMetricsPitchAndFamilyValues) -> None: ...
    @StruckOut.setter
    def StruckOut(self, value: bool) -> None: ...
    @Underlined.setter
    def Underlined(self, value: bool) -> None: ...
    @Weight.setter
    def Weight(self, value: int) -> None: ...


class TextMetricsCharacterSet:
    Ansi = 0
    Default = 1
    Symbol = 2
    Mac = 77
    ShiftJis = 128
    Hangul = 129
    Johab = 130
    Gb2312 = 134
    ChineseBig5 = 136
    Greek = 161
    Turkish = 162
    Vietnamese = 163
    Hebrew = 177
    Arabic = 178
    Baltic = 186
    Russian = 204
    Thai = 222
    EastEurope = 238
    Oem = 255


class TextMetricsPitchAndFamilyValues:
    FixedPitch = 1
    Vector = 2
    TrueType = 4
    Device = 8


class TextShadowType:
    #None = 0
    Single = 1
    Continuous = 2


class ThemeSizeType:
    Minimum = 0
    True = 1
    Draw = 2


class Thumb(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Focused() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class ThumbBottom(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Focused() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class ThumbButtonHorizontal(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class ThumbButtonVertical(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class ThumbLeft(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Focused() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class ThumbRight(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Focused() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class ThumbTop(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Focused() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class ThumbVertical(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Focused() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class Ticks(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class TicksVertical(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class Time(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class ToolBar(Object):
    pass


class ToolBarState:
    Normal = 1
    Hot = 2
    Pressed = 3
    Disabled = 4
    Checked = 5
    HotChecked = 6


class ToolTip(Object):
    pass


class TopTabItem(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class TopTabItemBothEdges(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class TopTabItemLeftEdge(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class TopTabItemRightEdge(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class Track(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class TrackBar(Object):
    pass


class TrackBarThumbState:
    Normal = 1
    Hot = 2
    Pressed = 3
    Disabled = 5


class TrackVertical(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class TrayNotify(Object):
    pass


class TreeView(Object):
    pass


class TrueSizeScalingType:
    #None = 0
    Size = 1
    Dpi = 2


class Up(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class Up(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class UpHorizontal(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class UpHorizontal(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class UpperTrackVertical(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class UserButton(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class UserPane(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class UserPicture(Object):
    @property
    def Normal() -> VisualStyleElement: ...


class VerticalAlignment:
    Top = 0
    Center = 1
    Bottom = 2


class VerticalScroll(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class VerticalThumb(Object):
    @property
    def Disabled() -> VisualStyleElement: ...
    @property
    def Hot() -> VisualStyleElement: ...
    @property
    def Normal() -> VisualStyleElement: ...
    @property
    def Pressed() -> VisualStyleElement: ...


class VisualStyleElement(Object):
    def CreateElement(className: str, part: int, state: int) -> VisualStyleElement: ...
    @property
    def ClassName(self) -> str: ...
    @property
    def Part(self) -> int: ...
    @property
    def State(self) -> int: ...


class VisualStyleInformation(Object):
    @property
    def Author() -> str: ...
    @property
    def ColorScheme() -> str: ...
    @property
    def Company() -> str: ...
    @property
    def ControlHighlightHot() -> Color: ...
    @property
    def Copyright() -> str: ...
    @property
    def Description() -> str: ...
    @property
    def DisplayName() -> str: ...
    @property
    def IsEnabledByUser() -> bool: ...
    @property
    def IsSupportedByOS() -> bool: ...
    @property
    def MinimumColorDepth() -> int: ...
    @property
    def Size() -> str: ...
    @property
    def SupportsFlatMenus() -> bool: ...
    @property
    def TextControlBorder() -> Color: ...
    @property
    def Url() -> str: ...
    @property
    def Version() -> str: ...


class VisualStyleRenderer(Object):
    @overload
    def __init__(self, element: VisualStyleElement): ...
    @overload
    def __init__(self, className: str, part: int, state: int): ...
    @overload
    def DrawBackground(self, dc: IDeviceContext, bounds: Rectangle) -> None: ...
    @overload
    def DrawBackground(self, dc: IDeviceContext, bounds: Rectangle, clipRectangle: Rectangle) -> None: ...
    def DrawEdge(self, dc: IDeviceContext, bounds: Rectangle, edges: Edges, style: EdgeStyle, effects: EdgeEffects) -> Rectangle: ...
    @overload
    def DrawImage(self, g: Graphics, bounds: Rectangle, image: Image) -> None: ...
    @overload
    def DrawImage(self, g: Graphics, bounds: Rectangle, imageList: ImageList, imageIndex: int) -> None: ...
    def DrawParentBackground(self, dc: IDeviceContext, bounds: Rectangle, childControl: Control) -> None: ...
    @overload
    def DrawText(self, dc: IDeviceContext, bounds: Rectangle, textToDraw: str) -> None: ...
    @overload
    def DrawText(self, dc: IDeviceContext, bounds: Rectangle, textToDraw: str, drawDisabled: bool) -> None: ...
    @overload
    def DrawText(self, dc: IDeviceContext, bounds: Rectangle, textToDraw: str, drawDisabled: bool, flags: TextFormatFlags) -> None: ...
    @property
    def Class(self) -> str: ...
    @property
    def Handle(self) -> IntPtr: ...
    @property
    def IsSupported() -> bool: ...
    @property
    def LastHResult(self) -> int: ...
    @property
    def Part(self) -> int: ...
    @property
    def State(self) -> int: ...
    def GetBackgroundContentRectangle(self, dc: IDeviceContext, bounds: Rectangle) -> Rectangle: ...
    def GetBackgroundExtent(self, dc: IDeviceContext, contentBounds: Rectangle) -> Rectangle: ...
    def GetBackgroundRegion(self, dc: IDeviceContext, bounds: Rectangle) -> Region: ...
    def GetBoolean(self, prop: BooleanProperty) -> bool: ...
    def GetColor(self, prop: ColorProperty) -> Color: ...
    def GetEnumValue(self, prop: EnumProperty) -> int: ...
    def GetFilename(self, prop: FilenameProperty) -> str: ...
    def GetFont(self, dc: IDeviceContext, prop: FontProperty) -> Font: ...
    def GetInteger(self, prop: IntegerProperty) -> int: ...
    def GetMargins(self, dc: IDeviceContext, prop: MarginProperty) -> Padding: ...
    @overload
    def GetPartSize(self, dc: IDeviceContext, type: ThemeSizeType) -> Size: ...
    @overload
    def GetPartSize(self, dc: IDeviceContext, bounds: Rectangle, type: ThemeSizeType) -> Size: ...
    def GetPoint(self, prop: PointProperty) -> Point: ...
    def GetString(self, prop: StringProperty) -> str: ...
    @overload
    def GetTextExtent(self, dc: IDeviceContext, textToDraw: str, flags: TextFormatFlags) -> Rectangle: ...
    @overload
    def GetTextExtent(self, dc: IDeviceContext, bounds: Rectangle, textToDraw: str, flags: TextFormatFlags) -> Rectangle: ...
    def GetTextMetrics(self, dc: IDeviceContext) -> TextMetrics: ...
    @overload
    def HitTestBackground(self, dc: IDeviceContext, backgroundRectangle: Rectangle, pt: Point, options: HitTestOptions) -> HitTestCode: ...
    @overload
    def HitTestBackground(self, g: Graphics, backgroundRectangle: Rectangle, region: Region, pt: Point, options: HitTestOptions) -> HitTestCode: ...
    @overload
    def HitTestBackground(self, dc: IDeviceContext, backgroundRectangle: Rectangle, hRgn: IntPtr, pt: Point, options: HitTestOptions) -> HitTestCode: ...
    def IsBackgroundPartiallyTransparent(self) -> bool: ...
    def IsElementDefined(element: VisualStyleElement) -> bool: ...
    @overload
    def SetParameters(self, element: VisualStyleElement) -> None: ...
    @overload
    def SetParameters(self, className: str, part: int, state: int) -> None: ...


class VisualStyleState:
    NoneEnabled = 0
    NonClientAreaEnabled = 1
    ClientAreaEnabled = 2
    ClientAndNonClientAreasEnabled = 3


class Window(Object):
    pass
