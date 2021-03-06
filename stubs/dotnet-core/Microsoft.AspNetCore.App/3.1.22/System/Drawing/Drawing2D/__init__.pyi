from typing import Tuple, Set, Iterable, List


class AdjustableArrowCap(CustomLineCap):
    @overload
    def __init__(self, width: Single, height: Single): ...
    @overload
    def __init__(self, width: Single, height: Single, isFilled: bool): ...
    @property
    def Filled(self) -> bool: ...
    @property
    def Height(self) -> Single: ...
    @property
    def MiddleInset(self) -> Single: ...
    @property
    def Width(self) -> Single: ...
    @Filled.setter
    def Filled(self, value: bool) -> None: ...
    @Height.setter
    def Height(self, value: Single) -> None: ...
    @MiddleInset.setter
    def MiddleInset(self, value: Single) -> None: ...
    @Width.setter
    def Width(self, value: Single) -> None: ...


class Blend(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, count: int): ...
    @property
    def Factors(self) -> Set(Single): ...
    @property
    def Positions(self) -> Set(Single): ...
    @Factors.setter
    def Factors(self, value: Set(Single)) -> None: ...
    @Positions.setter
    def Positions(self, value: Set(Single)) -> None: ...


class ColorBlend(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, count: int): ...
    @property
    def Colors(self) -> Set(Color): ...
    @property
    def Positions(self) -> Set(Single): ...
    @Colors.setter
    def Colors(self, value: Set(Color)) -> None: ...
    @Positions.setter
    def Positions(self, value: Set(Single)) -> None: ...


class CombineMode:
    Replace = 0
    Intersect = 1
    Union = 2
    Xor = 3
    Exclude = 4
    Complement = 5


class CompositingMode:
    SourceOver = 0
    SourceCopy = 1


class CompositingQuality:
    Default = 0
    HighSpeed = 1
    HighQuality = 2
    GammaCorrected = 3
    AssumeLinear = 4
    Invalid = -1


class CoordinateSpace:
    World = 0
    Page = 1
    Device = 2


class CustomLineCap(MarshalByRefObject):
    @overload
    def __init__(self, fillPath: GraphicsPath, strokePath: GraphicsPath): ...
    @overload
    def __init__(self, fillPath: GraphicsPath, strokePath: GraphicsPath, baseCap: LineCap): ...
    @overload
    def __init__(self, fillPath: GraphicsPath, strokePath: GraphicsPath, baseCap: LineCap, baseInset: Single): ...
    def Clone(self) -> Object: ...
    def Dispose(self) -> None: ...
    @property
    def BaseCap(self) -> LineCap: ...
    @property
    def BaseInset(self) -> Single: ...
    @property
    def StrokeJoin(self) -> LineJoin: ...
    @property
    def WidthScale(self) -> Single: ...
    def GetStrokeCaps(self) -> Tuple[LineCap, LineCap]: ...
    @BaseCap.setter
    def BaseCap(self, value: LineCap) -> None: ...
    @BaseInset.setter
    def BaseInset(self, value: Single) -> None: ...
    @StrokeJoin.setter
    def StrokeJoin(self, value: LineJoin) -> None: ...
    @WidthScale.setter
    def WidthScale(self, value: Single) -> None: ...
    def SetStrokeCaps(self, startCap: LineCap, endCap: LineCap) -> None: ...


class DashCap:
    Flat = 0
    Round = 2
    Triangle = 3


class DashStyle:
    Solid = 0
    Dash = 1
    Dot = 2
    DashDot = 3
    DashDotDot = 4
    Custom = 5


class FillMode:
    Alternate = 0
    Winding = 1


class FlushIntention:
    Flush = 0
    Sync = 1


class GraphicsContainer(MarshalByRefObject):
    pass


class GraphicsPath(MarshalByRefObject):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, fillMode: FillMode): ...
    @overload
    def __init__(self, pts: Set(PointF), types: Set(Byte)): ...
    @overload
    def __init__(self, pts: Set(Point), types: Set(Byte)): ...
    @overload
    def __init__(self, pts: Set(PointF), types: Set(Byte), fillMode: FillMode): ...
    @overload
    def __init__(self, pts: Set(Point), types: Set(Byte), fillMode: FillMode): ...
    @overload
    def AddArc(self, rect: Rectangle, startAngle: Single, sweepAngle: Single) -> None: ...
    @overload
    def AddArc(self, rect: RectangleF, startAngle: Single, sweepAngle: Single) -> None: ...
    @overload
    def AddArc(self, x: int, y: int, width: int, height: int, startAngle: Single, sweepAngle: Single) -> None: ...
    @overload
    def AddArc(self, x: Single, y: Single, width: Single, height: Single, startAngle: Single, sweepAngle: Single) -> None: ...
    @overload
    def AddBezier(self, pt1: Point, pt2: Point, pt3: Point, pt4: Point) -> None: ...
    @overload
    def AddBezier(self, pt1: PointF, pt2: PointF, pt3: PointF, pt4: PointF) -> None: ...
    @overload
    def AddBezier(self, x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, x4: int, y4: int) -> None: ...
    @overload
    def AddBezier(self, x1: Single, y1: Single, x2: Single, y2: Single, x3: Single, y3: Single, x4: Single, y4: Single) -> None: ...
    @overload
    def AddBeziers(self, points: Set(PointF)) -> None: ...
    @overload
    def AddBeziers(self, points: Set(Point)) -> None: ...
    @overload
    def AddClosedCurve(self, points: Set(Point)) -> None: ...
    @overload
    def AddClosedCurve(self, points: Set(PointF)) -> None: ...
    @overload
    def AddClosedCurve(self, points: Set(Point), tension: Single) -> None: ...
    @overload
    def AddClosedCurve(self, points: Set(PointF), tension: Single) -> None: ...
    @overload
    def AddCurve(self, points: Set(PointF)) -> None: ...
    @overload
    def AddCurve(self, points: Set(Point)) -> None: ...
    @overload
    def AddCurve(self, points: Set(PointF), tension: Single) -> None: ...
    @overload
    def AddCurve(self, points: Set(Point), tension: Single) -> None: ...
    @overload
    def AddCurve(self, points: Set(PointF), offset: int, numberOfSegments: int, tension: Single) -> None: ...
    @overload
    def AddCurve(self, points: Set(Point), offset: int, numberOfSegments: int, tension: Single) -> None: ...
    @overload
    def AddEllipse(self, rect: Rectangle) -> None: ...
    @overload
    def AddEllipse(self, rect: RectangleF) -> None: ...
    @overload
    def AddEllipse(self, x: int, y: int, width: int, height: int) -> None: ...
    @overload
    def AddEllipse(self, x: Single, y: Single, width: Single, height: Single) -> None: ...
    @overload
    def AddLine(self, pt1: PointF, pt2: PointF) -> None: ...
    @overload
    def AddLine(self, pt1: Point, pt2: Point) -> None: ...
    @overload
    def AddLine(self, x1: int, y1: int, x2: int, y2: int) -> None: ...
    @overload
    def AddLine(self, x1: Single, y1: Single, x2: Single, y2: Single) -> None: ...
    @overload
    def AddLines(self, points: Set(Point)) -> None: ...
    @overload
    def AddLines(self, points: Set(PointF)) -> None: ...
    def AddPath(self, addingPath: GraphicsPath, connect: bool) -> None: ...
    @overload
    def AddPie(self, rect: Rectangle, startAngle: Single, sweepAngle: Single) -> None: ...
    @overload
    def AddPie(self, x: int, y: int, width: int, height: int, startAngle: Single, sweepAngle: Single) -> None: ...
    @overload
    def AddPie(self, x: Single, y: Single, width: Single, height: Single, startAngle: Single, sweepAngle: Single) -> None: ...
    @overload
    def AddPolygon(self, points: Set(PointF)) -> None: ...
    @overload
    def AddPolygon(self, points: Set(Point)) -> None: ...
    @overload
    def AddRectangle(self, rect: Rectangle) -> None: ...
    @overload
    def AddRectangle(self, rect: RectangleF) -> None: ...
    @overload
    def AddRectangles(self, rects: Set(Rectangle)) -> None: ...
    @overload
    def AddRectangles(self, rects: Set(RectangleF)) -> None: ...
    @overload
    def AddString(self, s: str, family: FontFamily, style: int, emSize: Single, layoutRect: RectangleF, format: StringFormat) -> None: ...
    @overload
    def AddString(self, s: str, family: FontFamily, style: int, emSize: Single, origin: Point, format: StringFormat) -> None: ...
    @overload
    def AddString(self, s: str, family: FontFamily, style: int, emSize: Single, origin: PointF, format: StringFormat) -> None: ...
    @overload
    def AddString(self, s: str, family: FontFamily, style: int, emSize: Single, layoutRect: Rectangle, format: StringFormat) -> None: ...
    def ClearMarkers(self) -> None: ...
    def Clone(self) -> Object: ...
    def CloseAllFigures(self) -> None: ...
    def CloseFigure(self) -> None: ...
    def Dispose(self) -> None: ...
    @overload
    def Flatten(self) -> None: ...
    @overload
    def Flatten(self, matrix: Matrix) -> None: ...
    @overload
    def Flatten(self, matrix: Matrix, flatness: Single) -> None: ...
    @property
    def FillMode(self) -> FillMode: ...
    @property
    def PathData(self) -> PathData: ...
    @property
    def PathPoints(self) -> Set(PointF): ...
    @property
    def PathTypes(self) -> Set(Byte): ...
    @property
    def PointCount(self) -> int: ...
    @overload
    def GetBounds(self) -> RectangleF: ...
    @overload
    def GetBounds(self, matrix: Matrix) -> RectangleF: ...
    @overload
    def GetBounds(self, matrix: Matrix, pen: Pen) -> RectangleF: ...
    def GetLastPoint(self) -> PointF: ...
    @overload
    def IsOutlineVisible(self, point: Point, pen: Pen) -> bool: ...
    @overload
    def IsOutlineVisible(self, point: PointF, pen: Pen) -> bool: ...
    @overload
    def IsOutlineVisible(self, x: int, y: int, pen: Pen) -> bool: ...
    @overload
    def IsOutlineVisible(self, pt: PointF, pen: Pen, graphics: Graphics) -> bool: ...
    @overload
    def IsOutlineVisible(self, x: Single, y: Single, pen: Pen) -> bool: ...
    @overload
    def IsOutlineVisible(self, pt: Point, pen: Pen, graphics: Graphics) -> bool: ...
    @overload
    def IsOutlineVisible(self, x: int, y: int, pen: Pen, graphics: Graphics) -> bool: ...
    @overload
    def IsOutlineVisible(self, x: Single, y: Single, pen: Pen, graphics: Graphics) -> bool: ...
    @overload
    def IsVisible(self, point: PointF) -> bool: ...
    @overload
    def IsVisible(self, point: Point) -> bool: ...
    @overload
    def IsVisible(self, x: Single, y: Single) -> bool: ...
    @overload
    def IsVisible(self, x: int, y: int) -> bool: ...
    @overload
    def IsVisible(self, pt: Point, graphics: Graphics) -> bool: ...
    @overload
    def IsVisible(self, pt: PointF, graphics: Graphics) -> bool: ...
    @overload
    def IsVisible(self, x: Single, y: Single, graphics: Graphics) -> bool: ...
    @overload
    def IsVisible(self, x: int, y: int, graphics: Graphics) -> bool: ...
    def Reset(self) -> None: ...
    def Reverse(self) -> None: ...
    @FillMode.setter
    def FillMode(self, value: FillMode) -> None: ...
    def SetMarkers(self) -> None: ...
    def StartFigure(self) -> None: ...
    def Transform(self, matrix: Matrix) -> None: ...
    @overload
    def Warp(self, destPoints: Set(PointF), srcRect: RectangleF) -> None: ...
    @overload
    def Warp(self, destPoints: Set(PointF), srcRect: RectangleF, matrix: Matrix) -> None: ...
    @overload
    def Warp(self, destPoints: Set(PointF), srcRect: RectangleF, matrix: Matrix, warpMode: WarpMode) -> None: ...
    @overload
    def Warp(self, destPoints: Set(PointF), srcRect: RectangleF, matrix: Matrix, warpMode: WarpMode, flatness: Single) -> None: ...
    @overload
    def Widen(self, pen: Pen) -> None: ...
    @overload
    def Widen(self, pen: Pen, matrix: Matrix) -> None: ...
    @overload
    def Widen(self, pen: Pen, matrix: Matrix, flatness: Single) -> None: ...


class GraphicsPathIterator(MarshalByRefObject):
    def __init__(self, path: GraphicsPath): ...
    def CopyData(self, points: Set(PointF), types: Set(Byte), startIndex: int, endIndex: int) -> Tuple[int, Set(PointF), Set(Byte)]: ...
    def Dispose(self) -> None: ...
    def Enumerate(self, points: Set(PointF), types: Set(Byte)) -> Tuple[int, Set(PointF), Set(Byte)]: ...
    @property
    def Count(self) -> int: ...
    @property
    def SubpathCount(self) -> int: ...
    def HasCurve(self) -> bool: ...
    @overload
    def NextMarker(self, path: GraphicsPath) -> int: ...
    @overload
    def NextMarker(self) -> Tuple[int, int, int]: ...
    def NextPathType(self) -> Tuple[int, Byte, int, int]: ...
    @overload
    def NextSubpath(self, path: GraphicsPath) -> Tuple[int, bool]: ...
    @overload
    def NextSubpath(self) -> Tuple[int, int, int, bool]: ...
    def Rewind(self) -> None: ...


class GraphicsState(MarshalByRefObject):
    pass


class HatchBrush(Brush):
    @overload
    def __init__(self, hatchstyle: HatchStyle, foreColor: Color): ...
    @overload
    def __init__(self, hatchstyle: HatchStyle, foreColor: Color, backColor: Color): ...
    def Clone(self) -> Object: ...
    @property
    def BackgroundColor(self) -> Color: ...
    @property
    def ForegroundColor(self) -> Color: ...
    @property
    def HatchStyle(self) -> HatchStyle: ...


class HatchStyle:
    Horizontal = 0
    Min = 0
    Vertical = 1
    ForwardDiagonal = 2
    BackwardDiagonal = 3
    Cross = 4
    LargeGrid = 4
    Max = 4
    DiagonalCross = 5
    Percent05 = 6
    Percent10 = 7
    Percent20 = 8
    Percent25 = 9
    Percent30 = 10
    Percent40 = 11
    Percent50 = 12
    Percent60 = 13
    Percent70 = 14
    Percent75 = 15
    Percent80 = 16
    Percent90 = 17
    LightDownwardDiagonal = 18
    LightUpwardDiagonal = 19
    DarkDownwardDiagonal = 20
    DarkUpwardDiagonal = 21
    WideDownwardDiagonal = 22
    WideUpwardDiagonal = 23
    LightVertical = 24
    LightHorizontal = 25
    NarrowVertical = 26
    NarrowHorizontal = 27
    DarkVertical = 28
    DarkHorizontal = 29
    DashedDownwardDiagonal = 30
    DashedUpwardDiagonal = 31
    DashedHorizontal = 32
    DashedVertical = 33
    SmallConfetti = 34
    LargeConfetti = 35
    ZigZag = 36
    Wave = 37
    DiagonalBrick = 38
    HorizontalBrick = 39
    Weave = 40
    Plaid = 41
    Divot = 42
    DottedGrid = 43
    DottedDiamond = 44
    Shingle = 45
    Trellis = 46
    Sphere = 47
    SmallGrid = 48
    SmallCheckerBoard = 49
    LargeCheckerBoard = 50
    OutlinedDiamond = 51
    SolidDiamond = 52


class InterpolationMode:
    Default = 0
    Low = 1
    High = 2
    Bilinear = 3
    Bicubic = 4
    NearestNeighbor = 5
    HighQualityBilinear = 6
    HighQualityBicubic = 7
    Invalid = -1


class LinearGradientBrush(Brush):
    @overload
    def __init__(self, point1: PointF, point2: PointF, color1: Color, color2: Color): ...
    @overload
    def __init__(self, point1: Point, point2: Point, color1: Color, color2: Color): ...
    @overload
    def __init__(self, rect: RectangleF, color1: Color, color2: Color, linearGradientMode: LinearGradientMode): ...
    @overload
    def __init__(self, rect: Rectangle, color1: Color, color2: Color, linearGradientMode: LinearGradientMode): ...
    @overload
    def __init__(self, rect: RectangleF, color1: Color, color2: Color, angle: Single): ...
    @overload
    def __init__(self, rect: Rectangle, color1: Color, color2: Color, angle: Single): ...
    @overload
    def __init__(self, rect: RectangleF, color1: Color, color2: Color, angle: Single, isAngleScaleable: bool): ...
    @overload
    def __init__(self, rect: Rectangle, color1: Color, color2: Color, angle: Single, isAngleScaleable: bool): ...
    def Clone(self) -> Object: ...
    @property
    def Blend(self) -> Blend: ...
    @property
    def GammaCorrection(self) -> bool: ...
    @property
    def InterpolationColors(self) -> ColorBlend: ...
    @property
    def LinearColors(self) -> Set(Color): ...
    @property
    def Rectangle(self) -> RectangleF: ...
    @property
    def Transform(self) -> Matrix: ...
    @property
    def WrapMode(self) -> WrapMode: ...
    @overload
    def MultiplyTransform(self, matrix: Matrix) -> None: ...
    @overload
    def MultiplyTransform(self, matrix: Matrix, order: MatrixOrder) -> None: ...
    def ResetTransform(self) -> None: ...
    @overload
    def RotateTransform(self, angle: Single) -> None: ...
    @overload
    def RotateTransform(self, angle: Single, order: MatrixOrder) -> None: ...
    @overload
    def ScaleTransform(self, sx: Single, sy: Single) -> None: ...
    @overload
    def ScaleTransform(self, sx: Single, sy: Single, order: MatrixOrder) -> None: ...
    @Blend.setter
    def Blend(self, value: Blend) -> None: ...
    @GammaCorrection.setter
    def GammaCorrection(self, value: bool) -> None: ...
    @InterpolationColors.setter
    def InterpolationColors(self, value: ColorBlend) -> None: ...
    @LinearColors.setter
    def LinearColors(self, value: Set(Color)) -> None: ...
    @Transform.setter
    def Transform(self, value: Matrix) -> None: ...
    @WrapMode.setter
    def WrapMode(self, value: WrapMode) -> None: ...
    @overload
    def SetBlendTriangularShape(self, focus: Single) -> None: ...
    @overload
    def SetBlendTriangularShape(self, focus: Single, scale: Single) -> None: ...
    @overload
    def SetSigmaBellShape(self, focus: Single) -> None: ...
    @overload
    def SetSigmaBellShape(self, focus: Single, scale: Single) -> None: ...
    @overload
    def TranslateTransform(self, dx: Single, dy: Single) -> None: ...
    @overload
    def TranslateTransform(self, dx: Single, dy: Single, order: MatrixOrder) -> None: ...


class LinearGradientMode:
    Horizontal = 0
    Vertical = 1
    ForwardDiagonal = 2
    BackwardDiagonal = 3


class LineCap:
    Flat = 0
    Square = 1
    Round = 2
    Triangle = 3
    NoAnchor = 16
    SquareAnchor = 17
    RoundAnchor = 18
    DiamondAnchor = 19
    ArrowAnchor = 20
    AnchorMask = 240
    Custom = 255


class LineJoin:
    Miter = 0
    Bevel = 1
    Round = 2
    MiterClipped = 3


class Matrix(MarshalByRefObject):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, rect: RectangleF, plgpts: Set(PointF)): ...
    @overload
    def __init__(self, rect: Rectangle, plgpts: Set(Point)): ...
    @overload
    def __init__(self, m11: Single, m12: Single, m21: Single, m22: Single, dx: Single, dy: Single): ...
    def Clone(self) -> Matrix: ...
    def Dispose(self) -> None: ...
    def Equals(self, obj: Object) -> bool: ...
    @property
    def Elements(self) -> Set(Single): ...
    @property
    def IsIdentity(self) -> bool: ...
    @property
    def IsInvertible(self) -> bool: ...
    @property
    def OffsetX(self) -> Single: ...
    @property
    def OffsetY(self) -> Single: ...
    def GetHashCode(self) -> int: ...
    def Invert(self) -> None: ...
    @overload
    def Multiply(self, matrix: Matrix) -> None: ...
    @overload
    def Multiply(self, matrix: Matrix, order: MatrixOrder) -> None: ...
    def Reset(self) -> None: ...
    @overload
    def Rotate(self, angle: Single) -> None: ...
    @overload
    def Rotate(self, angle: Single, order: MatrixOrder) -> None: ...
    @overload
    def RotateAt(self, angle: Single, point: PointF) -> None: ...
    @overload
    def RotateAt(self, angle: Single, point: PointF, order: MatrixOrder) -> None: ...
    @overload
    def Scale(self, scaleX: Single, scaleY: Single) -> None: ...
    @overload
    def Scale(self, scaleX: Single, scaleY: Single, order: MatrixOrder) -> None: ...
    @overload
    def Shear(self, shearX: Single, shearY: Single) -> None: ...
    @overload
    def Shear(self, shearX: Single, shearY: Single, order: MatrixOrder) -> None: ...
    @overload
    def TransformPoints(self, pts: Set(Point)) -> None: ...
    @overload
    def TransformPoints(self, pts: Set(PointF)) -> None: ...
    @overload
    def TransformVectors(self, pts: Set(PointF)) -> None: ...
    @overload
    def TransformVectors(self, pts: Set(Point)) -> None: ...
    @overload
    def Translate(self, offsetX: Single, offsetY: Single) -> None: ...
    @overload
    def Translate(self, offsetX: Single, offsetY: Single, order: MatrixOrder) -> None: ...
    def VectorTransformPoints(self, pts: Set(Point)) -> None: ...


class MatrixOrder:
    Prepend = 0
    Append = 1


class PathData(Object):
    def __init__(self): ...
    @property
    def Points(self) -> Set(PointF): ...
    @property
    def Types(self) -> Set(Byte): ...
    @Points.setter
    def Points(self, value: Set(PointF)) -> None: ...
    @Types.setter
    def Types(self, value: Set(Byte)) -> None: ...


class PathGradientBrush(Brush):
    @overload
    def __init__(self, points: Set(PointF)): ...
    @overload
    def __init__(self, points: Set(Point)): ...
    @overload
    def __init__(self, path: GraphicsPath): ...
    @overload
    def __init__(self, points: Set(PointF), wrapMode: WrapMode): ...
    @overload
    def __init__(self, points: Set(Point), wrapMode: WrapMode): ...
    def Clone(self) -> Object: ...
    @property
    def Blend(self) -> Blend: ...
    @property
    def CenterColor(self) -> Color: ...
    @property
    def CenterPoint(self) -> PointF: ...
    @property
    def FocusScales(self) -> PointF: ...
    @property
    def InterpolationColors(self) -> ColorBlend: ...
    @property
    def Rectangle(self) -> RectangleF: ...
    @property
    def SurroundColors(self) -> Set(Color): ...
    @property
    def Transform(self) -> Matrix: ...
    @property
    def WrapMode(self) -> WrapMode: ...
    @overload
    def MultiplyTransform(self, matrix: Matrix) -> None: ...
    @overload
    def MultiplyTransform(self, matrix: Matrix, order: MatrixOrder) -> None: ...
    def ResetTransform(self) -> None: ...
    @overload
    def RotateTransform(self, angle: Single) -> None: ...
    @overload
    def RotateTransform(self, angle: Single, order: MatrixOrder) -> None: ...
    @overload
    def ScaleTransform(self, sx: Single, sy: Single) -> None: ...
    @overload
    def ScaleTransform(self, sx: Single, sy: Single, order: MatrixOrder) -> None: ...
    @Blend.setter
    def Blend(self, value: Blend) -> None: ...
    @CenterColor.setter
    def CenterColor(self, value: Color) -> None: ...
    @CenterPoint.setter
    def CenterPoint(self, value: PointF) -> None: ...
    @FocusScales.setter
    def FocusScales(self, value: PointF) -> None: ...
    @InterpolationColors.setter
    def InterpolationColors(self, value: ColorBlend) -> None: ...
    @SurroundColors.setter
    def SurroundColors(self, value: Set(Color)) -> None: ...
    @Transform.setter
    def Transform(self, value: Matrix) -> None: ...
    @WrapMode.setter
    def WrapMode(self, value: WrapMode) -> None: ...
    @overload
    def SetBlendTriangularShape(self, focus: Single) -> None: ...
    @overload
    def SetBlendTriangularShape(self, focus: Single, scale: Single) -> None: ...
    @overload
    def SetSigmaBellShape(self, focus: Single) -> None: ...
    @overload
    def SetSigmaBellShape(self, focus: Single, scale: Single) -> None: ...
    @overload
    def TranslateTransform(self, dx: Single, dy: Single) -> None: ...
    @overload
    def TranslateTransform(self, dx: Single, dy: Single, order: MatrixOrder) -> None: ...


class PathPointType:
    Start = 0
    Line = 1
    Bezier = 3
    Bezier3 = 3
    PathTypeMask = 7
    DashMode = 16
    PathMarker = 32
    CloseSubpath = 128


class PenAlignment:
    Center = 0
    Inset = 1
    Outset = 2
    Left = 3
    Right = 4


class PenType:
    SolidColor = 0
    HatchFill = 1
    TextureFill = 2
    PathGradient = 3
    LinearGradient = 4


class PixelOffsetMode:
    Default = 0
    HighSpeed = 1
    HighQuality = 2
    #None = 3
    Half = 4
    Invalid = -1


class QualityMode:
    Default = 0
    Low = 1
    High = 2
    Invalid = -1


class RegionData(Object):
    @property
    def Data(self) -> Set(Byte): ...
    @Data.setter
    def Data(self, value: Set(Byte)) -> None: ...


class SmoothingMode:
    Default = 0
    HighSpeed = 1
    HighQuality = 2
    #None = 3
    AntiAlias = 4
    Invalid = -1


class WarpMode:
    Perspective = 0
    Bilinear = 1


class WrapMode:
    Tile = 0
    TileFlipX = 1
    TileFlipY = 2
    TileFlipXY = 3
    Clamp = 4
