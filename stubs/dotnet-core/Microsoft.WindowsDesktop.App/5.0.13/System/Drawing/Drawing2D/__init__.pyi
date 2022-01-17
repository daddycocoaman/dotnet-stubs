from typing import Tuple, Set, Iterable, List


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
