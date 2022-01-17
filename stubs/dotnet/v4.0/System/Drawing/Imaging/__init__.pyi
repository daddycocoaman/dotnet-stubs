from typing import Tuple, Set, Iterable, List


class BitmapData(Object):
    def __init__(self): ...
    @property
    def Height(self) -> int: ...
    @property
    def PixelFormat(self) -> PixelFormat: ...
    @property
    def Reserved(self) -> int: ...
    @property
    def Scan0(self) -> IntPtr: ...
    @property
    def Stride(self) -> int: ...
    @property
    def Width(self) -> int: ...
    @Height.setter
    def Height(self, value: int) -> None: ...
    @PixelFormat.setter
    def PixelFormat(self, value: PixelFormat) -> None: ...
    @Reserved.setter
    def Reserved(self, value: int) -> None: ...
    @Scan0.setter
    def Scan0(self, value: IntPtr) -> None: ...
    @Stride.setter
    def Stride(self, value: int) -> None: ...
    @Width.setter
    def Width(self, value: int) -> None: ...


class ColorAdjustType:
    Default = 0
    Bitmap = 1
    Brush = 2
    Pen = 3
    Text = 4
    Count = 5
    Any = 6


class ColorChannelFlag:
    ColorChannelC = 0
    ColorChannelM = 1
    ColorChannelY = 2
    ColorChannelK = 3
    ColorChannelLast = 4


class ColorMap(Object):
    def __init__(self): ...
    @property
    def NewColor(self) -> Color: ...
    @property
    def OldColor(self) -> Color: ...
    @NewColor.setter
    def NewColor(self, value: Color) -> None: ...
    @OldColor.setter
    def OldColor(self, value: Color) -> None: ...


class ColorMapType:
    Default = 0
    Brush = 1


class ColorMatrix(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, newColorMatrix: Set(Set(Single))): ...
    @property
    def Item(self, row: int, column: int) -> Single: ...
    @property
    def Matrix00(self) -> Single: ...
    @property
    def Matrix01(self) -> Single: ...
    @property
    def Matrix02(self) -> Single: ...
    @property
    def Matrix03(self) -> Single: ...
    @property
    def Matrix04(self) -> Single: ...
    @property
    def Matrix10(self) -> Single: ...
    @property
    def Matrix11(self) -> Single: ...
    @property
    def Matrix12(self) -> Single: ...
    @property
    def Matrix13(self) -> Single: ...
    @property
    def Matrix14(self) -> Single: ...
    @property
    def Matrix20(self) -> Single: ...
    @property
    def Matrix21(self) -> Single: ...
    @property
    def Matrix22(self) -> Single: ...
    @property
    def Matrix23(self) -> Single: ...
    @property
    def Matrix24(self) -> Single: ...
    @property
    def Matrix30(self) -> Single: ...
    @property
    def Matrix31(self) -> Single: ...
    @property
    def Matrix32(self) -> Single: ...
    @property
    def Matrix33(self) -> Single: ...
    @property
    def Matrix34(self) -> Single: ...
    @property
    def Matrix40(self) -> Single: ...
    @property
    def Matrix41(self) -> Single: ...
    @property
    def Matrix42(self) -> Single: ...
    @property
    def Matrix43(self) -> Single: ...
    @property
    def Matrix44(self) -> Single: ...
    @Item.setter
    def Item(self, row: int, column: int, value: Single) -> None: ...
    @Matrix00.setter
    def Matrix00(self, value: Single) -> None: ...
    @Matrix01.setter
    def Matrix01(self, value: Single) -> None: ...
    @Matrix02.setter
    def Matrix02(self, value: Single) -> None: ...
    @Matrix03.setter
    def Matrix03(self, value: Single) -> None: ...
    @Matrix04.setter
    def Matrix04(self, value: Single) -> None: ...
    @Matrix10.setter
    def Matrix10(self, value: Single) -> None: ...
    @Matrix11.setter
    def Matrix11(self, value: Single) -> None: ...
    @Matrix12.setter
    def Matrix12(self, value: Single) -> None: ...
    @Matrix13.setter
    def Matrix13(self, value: Single) -> None: ...
    @Matrix14.setter
    def Matrix14(self, value: Single) -> None: ...
    @Matrix20.setter
    def Matrix20(self, value: Single) -> None: ...
    @Matrix21.setter
    def Matrix21(self, value: Single) -> None: ...
    @Matrix22.setter
    def Matrix22(self, value: Single) -> None: ...
    @Matrix23.setter
    def Matrix23(self, value: Single) -> None: ...
    @Matrix24.setter
    def Matrix24(self, value: Single) -> None: ...
    @Matrix30.setter
    def Matrix30(self, value: Single) -> None: ...
    @Matrix31.setter
    def Matrix31(self, value: Single) -> None: ...
    @Matrix32.setter
    def Matrix32(self, value: Single) -> None: ...
    @Matrix33.setter
    def Matrix33(self, value: Single) -> None: ...
    @Matrix34.setter
    def Matrix34(self, value: Single) -> None: ...
    @Matrix40.setter
    def Matrix40(self, value: Single) -> None: ...
    @Matrix41.setter
    def Matrix41(self, value: Single) -> None: ...
    @Matrix42.setter
    def Matrix42(self, value: Single) -> None: ...
    @Matrix43.setter
    def Matrix43(self, value: Single) -> None: ...
    @Matrix44.setter
    def Matrix44(self, value: Single) -> None: ...


class ColorMatrixFlag:
    Default = 0
    SkipGrays = 1
    AltGrays = 2


class ColorMode:
    Argb32Mode = 0
    Argb64Mode = 1


class ColorPalette(Object):
    @property
    def Entries(self) -> Set(Color): ...
    @property
    def Flags(self) -> int: ...


class EmfPlusRecordType:
    EmfMin = 1
    EmfHeader = 1
    EmfPolyBezier = 2
    EmfPolygon = 3
    EmfPolyline = 4
    EmfPolyBezierTo = 5
    EmfPolyLineTo = 6
    EmfPolyPolyline = 7
    EmfPolyPolygon = 8
    EmfSetWindowExtEx = 9
    EmfSetWindowOrgEx = 10
    EmfSetViewportExtEx = 11
    EmfSetViewportOrgEx = 12
    EmfSetBrushOrgEx = 13
    EmfEof = 14
    EmfSetPixelV = 15
    EmfSetMapperFlags = 16
    EmfSetMapMode = 17
    EmfSetBkMode = 18
    EmfSetPolyFillMode = 19
    EmfSetROP2 = 20
    EmfSetStretchBltMode = 21
    EmfSetTextAlign = 22
    EmfSetColorAdjustment = 23
    EmfSetTextColor = 24
    EmfSetBkColor = 25
    EmfOffsetClipRgn = 26
    EmfMoveToEx = 27
    EmfSetMetaRgn = 28
    EmfExcludeClipRect = 29
    EmfIntersectClipRect = 30
    EmfScaleViewportExtEx = 31
    EmfScaleWindowExtEx = 32
    EmfSaveDC = 33
    EmfRestoreDC = 34
    EmfSetWorldTransform = 35
    EmfModifyWorldTransform = 36
    EmfSelectObject = 37
    EmfCreatePen = 38
    EmfCreateBrushIndirect = 39
    EmfDeleteObject = 40
    EmfAngleArc = 41
    EmfEllipse = 42
    EmfRectangle = 43
    EmfRoundRect = 44
    EmfRoundArc = 45
    EmfChord = 46
    EmfPie = 47
    EmfSelectPalette = 48
    EmfCreatePalette = 49
    EmfSetPaletteEntries = 50
    EmfResizePalette = 51
    EmfRealizePalette = 52
    EmfExtFloodFill = 53
    EmfLineTo = 54
    EmfArcTo = 55
    EmfPolyDraw = 56
    EmfSetArcDirection = 57
    EmfSetMiterLimit = 58
    EmfBeginPath = 59
    EmfEndPath = 60
    EmfCloseFigure = 61
    EmfFillPath = 62
    EmfStrokeAndFillPath = 63
    EmfStrokePath = 64
    EmfFlattenPath = 65
    EmfWidenPath = 66
    EmfSelectClipPath = 67
    EmfAbortPath = 68
    EmfReserved069 = 69
    EmfGdiComment = 70
    EmfFillRgn = 71
    EmfFrameRgn = 72
    EmfInvertRgn = 73
    EmfPaintRgn = 74
    EmfExtSelectClipRgn = 75
    EmfBitBlt = 76
    EmfStretchBlt = 77
    EmfMaskBlt = 78
    EmfPlgBlt = 79
    EmfSetDIBitsToDevice = 80
    EmfStretchDIBits = 81
    EmfExtCreateFontIndirect = 82
    EmfExtTextOutA = 83
    EmfExtTextOutW = 84
    EmfPolyBezier16 = 85
    EmfPolygon16 = 86
    EmfPolyline16 = 87
    EmfPolyBezierTo16 = 88
    EmfPolylineTo16 = 89
    EmfPolyPolyline16 = 90
    EmfPolyPolygon16 = 91
    EmfPolyDraw16 = 92
    EmfCreateMonoBrush = 93
    EmfCreateDibPatternBrushPt = 94
    EmfExtCreatePen = 95
    EmfPolyTextOutA = 96
    EmfPolyTextOutW = 97
    EmfSetIcmMode = 98
    EmfCreateColorSpace = 99
    EmfSetColorSpace = 100
    EmfDeleteColorSpace = 101
    EmfGlsRecord = 102
    EmfGlsBoundedRecord = 103
    EmfPixelFormat = 104
    EmfDrawEscape = 105
    EmfExtEscape = 106
    EmfStartDoc = 107
    EmfSmallTextOut = 108
    EmfForceUfiMapping = 109
    EmfNamedEscpae = 110
    EmfColorCorrectPalette = 111
    EmfSetIcmProfileA = 112
    EmfSetIcmProfileW = 113
    EmfAlphaBlend = 114
    EmfSetLayout = 115
    EmfTransparentBlt = 116
    EmfReserved117 = 117
    EmfGradientFill = 118
    EmfSetLinkedUfis = 119
    EmfSetTextJustification = 120
    EmfColorMatchToTargetW = 121
    EmfCreateColorSpaceW = 122
    EmfMax = 122
    Invalid = 16384
    EmfPlusRecordBase = 16384
    Header = 16385
    Min = 16385
    EndOfFile = 16386
    Comment = 16387
    GetDC = 16388
    MultiFormatStart = 16389
    MultiFormatSection = 16390
    MultiFormatEnd = 16391
    Object = 16392
    Clear = 16393
    FillRects = 16394
    DrawRects = 16395
    FillPolygon = 16396
    DrawLines = 16397
    FillEllipse = 16398
    DrawEllipse = 16399
    FillPie = 16400
    DrawPie = 16401
    DrawArc = 16402
    FillRegion = 16403
    FillPath = 16404
    DrawPath = 16405
    FillClosedCurve = 16406
    DrawClosedCurve = 16407
    DrawCurve = 16408
    DrawBeziers = 16409
    DrawImage = 16410
    DrawImagePoints = 16411
    DrawString = 16412
    SetRenderingOrigin = 16413
    SetAntiAliasMode = 16414
    SetTextRenderingHint = 16415
    SetTextContrast = 16416
    SetInterpolationMode = 16417
    SetPixelOffsetMode = 16418
    SetCompositingMode = 16419
    SetCompositingQuality = 16420
    Save = 16421
    Restore = 16422
    BeginContainer = 16423
    BeginContainerNoParams = 16424
    EndContainer = 16425
    SetWorldTransform = 16426
    ResetWorldTransform = 16427
    MultiplyWorldTransform = 16428
    TranslateWorldTransform = 16429
    ScaleWorldTransform = 16430
    RotateWorldTransform = 16431
    SetPageTransform = 16432
    ResetClip = 16433
    SetClipRect = 16434
    SetClipPath = 16435
    SetClipRegion = 16436
    OffsetClip = 16437
    Max = 16438
    DrawDriverString = 16438
    Total = 16439
    WmfRecordBase = 65536
    WmfSaveDC = 65566
    WmfRealizePalette = 65589
    WmfSetPalEntries = 65591
    WmfCreatePalette = 65783
    WmfSetBkMode = 65794
    WmfSetMapMode = 65795
    WmfSetROP2 = 65796
    WmfSetRelAbs = 65797
    WmfSetPolyFillMode = 65798
    WmfSetStretchBltMode = 65799
    WmfSetTextCharExtra = 65800
    WmfRestoreDC = 65831
    WmfInvertRegion = 65834
    WmfPaintRegion = 65835
    WmfSelectClipRegion = 65836
    WmfSelectObject = 65837
    WmfSetTextAlign = 65838
    WmfResizePalette = 65849
    WmfDibCreatePatternBrush = 65858
    WmfSetLayout = 65865
    WmfDeleteObject = 66032
    WmfCreatePatternBrush = 66041
    WmfSetBkColor = 66049
    WmfSetTextColor = 66057
    WmfSetTextJustification = 66058
    WmfSetWindowOrg = 66059
    WmfSetWindowExt = 66060
    WmfSetViewportOrg = 66061
    WmfSetViewportExt = 66062
    WmfOffsetWindowOrg = 66063
    WmfOffsetViewportOrg = 66065
    WmfLineTo = 66067
    WmfMoveTo = 66068
    WmfOffsetCilpRgn = 66080
    WmfFillRegion = 66088
    WmfSetMapperFlags = 66097
    WmfSelectPalette = 66100
    WmfCreatePenIndirect = 66298
    WmfCreateFontIndirect = 66299
    WmfCreateBrushIndirect = 66300
    WmfPolygon = 66340
    WmfPolyline = 66341
    WmfScaleWindowExt = 66576
    WmfScaleViewportExt = 66578
    WmfExcludeClipRect = 66581
    WmfIntersectClipRect = 66582
    WmfEllipse = 66584
    WmfFloodFill = 66585
    WmfRectangle = 66587
    WmfSetPixel = 66591
    WmfFrameRegion = 66601
    WmfAnimatePalette = 66614
    WmfTextOut = 66849
    WmfPolyPolygon = 66872
    WmfExtFloodFill = 66888
    WmfRoundRect = 67100
    WmfPatBlt = 67101
    WmfEscape = 67110
    WmfCreateRegion = 67327
    WmfArc = 67607
    WmfPie = 67610
    WmfChord = 67632
    WmfBitBlt = 67874
    WmfDibBitBlt = 67904
    WmfExtTextOut = 68146
    WmfStretchBlt = 68387
    WmfDibStretchBlt = 68417
    WmfSetDibToDev = 68915
    WmfStretchDib = 69443


class EmfType:
    EmfOnly = 3
    EmfPlusOnly = 4
    EmfPlusDual = 5


class Encoder(Object):
    def __init__(self, guid: Guid): ...
    @property
    def Guid(self) -> Guid: ...


class EncoderParameter(Object):
    @overload
    def __init__(self, encoder: Encoder, value: Byte): ...
    @overload
    def __init__(self, encoder: Encoder, value: Set(Int64)): ...
    @overload
    def __init__(self, encoder: Encoder, value: Set(Int16)): ...
    @overload
    def __init__(self, encoder: Encoder, value: str): ...
    @overload
    def __init__(self, encoder: Encoder, value: Set(Byte)): ...
    @overload
    def __init__(self, encoder: Encoder, value: Int64): ...
    @overload
    def __init__(self, encoder: Encoder, value: Int16): ...
    @overload
    def __init__(self, encoder: Encoder, rangebegin: Int64, rangeend: Int64): ...
    @overload
    def __init__(self, encoder: Encoder, value: Set(Byte), undefined: bool): ...
    @overload
    def __init__(self, encoder: Encoder, value: Byte, undefined: bool): ...
    @overload
    def __init__(self, encoder: Encoder, numerator: Set(int), denominator: Set(int)): ...
    @overload
    def __init__(self, encoder: Encoder, rangebegin: Set(Int64), rangeend: Set(Int64)): ...
    @overload
    def __init__(self, encoder: Encoder, numerator: int, denominator: int): ...
    @overload
    def __init__(self, encoder: Encoder, NumberOfValues: int, Type: int, Value: int): ...
    @overload
    def __init__(self, encoder: Encoder, numberValues: int, type: EncoderParameterValueType, value: IntPtr): ...
    @overload
    def __init__(self, encoder: Encoder, numerator1: int, demoninator1: int, numerator2: int, demoninator2: int): ...
    @overload
    def __init__(self, encoder: Encoder, numerator1: Set(int), denominator1: Set(int), numerator2: Set(int), denominator2: Set(int)): ...
    def Dispose(self) -> None: ...
    @property
    def Encoder(self) -> Encoder: ...
    @property
    def NumberOfValues(self) -> int: ...
    @property
    def Type(self) -> EncoderParameterValueType: ...
    @property
    def ValueType(self) -> EncoderParameterValueType: ...
    @Encoder.setter
    def Encoder(self, value: Encoder) -> None: ...


class EncoderParameters(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, count: int): ...
    def Dispose(self) -> None: ...
    @property
    def Param(self) -> Set(EncoderParameter): ...
    @Param.setter
    def Param(self, value: Set(EncoderParameter)) -> None: ...


class EncoderParameterValueType:
    ValueTypeByte = 1
    ValueTypeAscii = 2
    ValueTypeShort = 3
    ValueTypeLong = 4
    ValueTypeRational = 5
    ValueTypeLongRange = 6
    ValueTypeUndefined = 7
    ValueTypeRationalRange = 8


class EncoderValue:
    ColorTypeCMYK = 0
    ColorTypeYCCK = 1
    CompressionLZW = 2
    CompressionCCITT3 = 3
    CompressionCCITT4 = 4
    CompressionRle = 5
    CompressionNone = 6
    ScanMethodInterlaced = 7
    ScanMethodNonInterlaced = 8
    VersionGif87 = 9
    VersionGif89 = 10
    RenderProgressive = 11
    RenderNonProgressive = 12
    TransformRotate90 = 13
    TransformRotate180 = 14
    TransformRotate270 = 15
    TransformFlipHorizontal = 16
    TransformFlipVertical = 17
    MultiFrame = 18
    LastFrame = 19
    Flush = 20
    FrameDimensionTime = 21
    FrameDimensionResolution = 22
    FrameDimensionPage = 23


class FrameDimension(Object):
    def __init__(self, guid: Guid): ...
    def Equals(self, o: Object) -> bool: ...
    @property
    def Guid(self) -> Guid: ...
    @property
    def Page() -> FrameDimension: ...
    @property
    def Resolution() -> FrameDimension: ...
    @property
    def Time() -> FrameDimension: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...


class ImageAttributes(Object):
    def __init__(self): ...
    def ClearBrushRemapTable(self) -> None: ...
    @overload
    def ClearColorKey(self) -> None: ...
    @overload
    def ClearColorKey(self, type: ColorAdjustType) -> None: ...
    @overload
    def ClearColorMatrix(self) -> None: ...
    @overload
    def ClearColorMatrix(self, type: ColorAdjustType) -> None: ...
    @overload
    def ClearGamma(self) -> None: ...
    @overload
    def ClearGamma(self, type: ColorAdjustType) -> None: ...
    @overload
    def ClearNoOp(self) -> None: ...
    @overload
    def ClearNoOp(self, type: ColorAdjustType) -> None: ...
    @overload
    def ClearOutputChannel(self) -> None: ...
    @overload
    def ClearOutputChannel(self, type: ColorAdjustType) -> None: ...
    @overload
    def ClearOutputChannelColorProfile(self) -> None: ...
    @overload
    def ClearOutputChannelColorProfile(self, type: ColorAdjustType) -> None: ...
    @overload
    def ClearRemapTable(self) -> None: ...
    @overload
    def ClearRemapTable(self, type: ColorAdjustType) -> None: ...
    @overload
    def ClearThreshold(self) -> None: ...
    @overload
    def ClearThreshold(self, type: ColorAdjustType) -> None: ...
    def Clone(self) -> Object: ...
    def Dispose(self) -> None: ...
    def GetAdjustedPalette(self, palette: ColorPalette, type: ColorAdjustType) -> None: ...
    def SetBrushRemapTable(self, map: Set(ColorMap)) -> None: ...
    @overload
    def SetColorKey(self, colorLow: Color, colorHigh: Color) -> None: ...
    @overload
    def SetColorKey(self, colorLow: Color, colorHigh: Color, type: ColorAdjustType) -> None: ...
    @overload
    def SetColorMatrices(self, newColorMatrix: ColorMatrix, grayMatrix: ColorMatrix) -> None: ...
    @overload
    def SetColorMatrices(self, newColorMatrix: ColorMatrix, grayMatrix: ColorMatrix, flags: ColorMatrixFlag) -> None: ...
    @overload
    def SetColorMatrices(self, newColorMatrix: ColorMatrix, grayMatrix: ColorMatrix, mode: ColorMatrixFlag, type: ColorAdjustType) -> None: ...
    @overload
    def SetColorMatrix(self, newColorMatrix: ColorMatrix) -> None: ...
    @overload
    def SetColorMatrix(self, newColorMatrix: ColorMatrix, flags: ColorMatrixFlag) -> None: ...
    @overload
    def SetColorMatrix(self, newColorMatrix: ColorMatrix, mode: ColorMatrixFlag, type: ColorAdjustType) -> None: ...
    @overload
    def SetGamma(self, gamma: Single) -> None: ...
    @overload
    def SetGamma(self, gamma: Single, type: ColorAdjustType) -> None: ...
    @overload
    def SetNoOp(self) -> None: ...
    @overload
    def SetNoOp(self, type: ColorAdjustType) -> None: ...
    @overload
    def SetOutputChannel(self, flags: ColorChannelFlag) -> None: ...
    @overload
    def SetOutputChannel(self, flags: ColorChannelFlag, type: ColorAdjustType) -> None: ...
    @overload
    def SetOutputChannelColorProfile(self, colorProfileFilename: str) -> None: ...
    @overload
    def SetOutputChannelColorProfile(self, colorProfileFilename: str, type: ColorAdjustType) -> None: ...
    @overload
    def SetRemapTable(self, map: Set(ColorMap)) -> None: ...
    @overload
    def SetRemapTable(self, map: Set(ColorMap), type: ColorAdjustType) -> None: ...
    @overload
    def SetThreshold(self, threshold: Single) -> None: ...
    @overload
    def SetThreshold(self, threshold: Single, type: ColorAdjustType) -> None: ...
    @overload
    def SetWrapMode(self, mode: WrapMode) -> None: ...
    @overload
    def SetWrapMode(self, mode: WrapMode, color: Color) -> None: ...
    @overload
    def SetWrapMode(self, mode: WrapMode, color: Color, clamp: bool) -> None: ...


class ImageCodecFlags:
    Encoder = 1
    Decoder = 2
    SupportBitmap = 4
    SupportVector = 8
    SeekableEncode = 16
    BlockingDecode = 32
    Builtin = 65536
    System = 131072
    User = 262144


class ImageCodecInfo(Object):
    @property
    def Clsid(self) -> Guid: ...
    @property
    def CodecName(self) -> str: ...
    @property
    def DllName(self) -> str: ...
    @property
    def FilenameExtension(self) -> str: ...
    @property
    def Flags(self) -> ImageCodecFlags: ...
    @property
    def FormatDescription(self) -> str: ...
    @property
    def FormatID(self) -> Guid: ...
    @property
    def MimeType(self) -> str: ...
    @property
    def SignatureMasks(self) -> Set(Set(Byte)): ...
    @property
    def SignaturePatterns(self) -> Set(Set(Byte)): ...
    @property
    def Version(self) -> int: ...
    def GetImageDecoders() -> Set(ImageCodecInfo): ...
    def GetImageEncoders() -> Set(ImageCodecInfo): ...
    @Clsid.setter
    def Clsid(self, value: Guid) -> None: ...
    @CodecName.setter
    def CodecName(self, value: str) -> None: ...
    @DllName.setter
    def DllName(self, value: str) -> None: ...
    @FilenameExtension.setter
    def FilenameExtension(self, value: str) -> None: ...
    @Flags.setter
    def Flags(self, value: ImageCodecFlags) -> None: ...
    @FormatDescription.setter
    def FormatDescription(self, value: str) -> None: ...
    @FormatID.setter
    def FormatID(self, value: Guid) -> None: ...
    @MimeType.setter
    def MimeType(self, value: str) -> None: ...
    @SignatureMasks.setter
    def SignatureMasks(self, value: Set(Set(Byte))) -> None: ...
    @SignaturePatterns.setter
    def SignaturePatterns(self, value: Set(Set(Byte))) -> None: ...
    @Version.setter
    def Version(self, value: int) -> None: ...


class ImageFlags:
    #None = 0
    Scalable = 1
    HasAlpha = 2
    HasTranslucent = 4
    PartiallyScalable = 8
    ColorSpaceRgb = 16
    ColorSpaceCmyk = 32
    ColorSpaceGray = 64
    ColorSpaceYcbcr = 128
    ColorSpaceYcck = 256
    HasRealDpi = 4096
    HasRealPixelSize = 8192
    ReadOnly = 65536
    Caching = 131072


class ImageFormat(Object):
    def __init__(self, guid: Guid): ...
    def Equals(self, o: Object) -> bool: ...
    @property
    def Bmp() -> ImageFormat: ...
    @property
    def Emf() -> ImageFormat: ...
    @property
    def Exif() -> ImageFormat: ...
    @property
    def Gif() -> ImageFormat: ...
    @property
    def Guid(self) -> Guid: ...
    @property
    def Icon() -> ImageFormat: ...
    @property
    def Jpeg() -> ImageFormat: ...
    @property
    def MemoryBmp() -> ImageFormat: ...
    @property
    def Png() -> ImageFormat: ...
    @property
    def Tiff() -> ImageFormat: ...
    @property
    def Wmf() -> ImageFormat: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...


class ImageLockMode:
    ReadOnly = 1
    WriteOnly = 2
    ReadWrite = 3
    UserInputBuffer = 4


class Metafile(Image):
    @overload
    def __init__(self, filename: str): ...
    @overload
    def __init__(self, stream: Stream): ...
    @overload
    def __init__(self, hmetafile: IntPtr, wmfHeader: WmfPlaceableFileHeader): ...
    @overload
    def __init__(self, stream: Stream, referenceHdc: IntPtr): ...
    @overload
    def __init__(self, fileName: str, referenceHdc: IntPtr): ...
    @overload
    def __init__(self, referenceHdc: IntPtr, frameRect: RectangleF): ...
    @overload
    def __init__(self, referenceHdc: IntPtr, frameRect: Rectangle): ...
    @overload
    def __init__(self, referenceHdc: IntPtr, emfType: EmfType): ...
    @overload
    def __init__(self, henhmetafile: IntPtr, deleteEmf: bool): ...
    @overload
    def __init__(self, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit): ...
    @overload
    def __init__(self, stream: Stream, referenceHdc: IntPtr, frameRect: Rectangle): ...
    @overload
    def __init__(self, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit): ...
    @overload
    def __init__(self, stream: Stream, referenceHdc: IntPtr, frameRect: RectangleF): ...
    @overload
    def __init__(self, fileName: str, referenceHdc: IntPtr, type: EmfType): ...
    @overload
    def __init__(self, fileName: str, referenceHdc: IntPtr, frameRect: RectangleF): ...
    @overload
    def __init__(self, stream: Stream, referenceHdc: IntPtr, type: EmfType): ...
    @overload
    def __init__(self, hmetafile: IntPtr, wmfHeader: WmfPlaceableFileHeader, deleteWmf: bool): ...
    @overload
    def __init__(self, referenceHdc: IntPtr, emfType: EmfType, description: str): ...
    @overload
    def __init__(self, fileName: str, referenceHdc: IntPtr, frameRect: Rectangle): ...
    @overload
    def __init__(self, stream: Stream, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit): ...
    @overload
    def __init__(self, fileName: str, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit): ...
    @overload
    def __init__(self, stream: Stream, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit): ...
    @overload
    def __init__(self, stream: Stream, referenceHdc: IntPtr, type: EmfType, description: str): ...
    @overload
    def __init__(self, fileName: str, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit): ...
    @overload
    def __init__(self, fileName: str, referenceHdc: IntPtr, type: EmfType, description: str): ...
    @overload
    def __init__(self, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, type: EmfType): ...
    @overload
    def __init__(self, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, type: EmfType): ...
    @overload
    def __init__(self, fileName: str, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, desc: str): ...
    @overload
    def __init__(self, fileName: str, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, type: EmfType): ...
    @overload
    def __init__(self, fileName: str, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, description: str): ...
    @overload
    def __init__(self, fileName: str, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, type: EmfType): ...
    @overload
    def __init__(self, stream: Stream, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, type: EmfType): ...
    @overload
    def __init__(self, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, type: EmfType, desc: str): ...
    @overload
    def __init__(self, stream: Stream, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, type: EmfType): ...
    @overload
    def __init__(self, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, type: EmfType, description: str): ...
    @overload
    def __init__(self, fileName: str, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, type: EmfType, description: str): ...
    @overload
    def __init__(self, stream: Stream, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, type: EmfType, description: str): ...
    @overload
    def __init__(self, fileName: str, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, type: EmfType, description: str): ...
    @overload
    def __init__(self, stream: Stream, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, type: EmfType, description: str): ...
    def GetHenhmetafile(self) -> IntPtr: ...
    @overload
    def GetMetafileHeader(self) -> MetafileHeader: ...
    @overload
    def GetMetafileHeader(henhmetafile: IntPtr) -> MetafileHeader: ...
    @overload
    def GetMetafileHeader(fileName: str) -> MetafileHeader: ...
    @overload
    def GetMetafileHeader(stream: Stream) -> MetafileHeader: ...
    @overload
    def GetMetafileHeader(hmetafile: IntPtr, wmfHeader: WmfPlaceableFileHeader) -> MetafileHeader: ...
    def PlayRecord(self, recordType: EmfPlusRecordType, flags: int, dataSize: int, data: Set(Byte)) -> None: ...


class MetafileFrameUnit:
    Pixel = 2
    Point = 3
    Inch = 4
    Document = 5
    Millimeter = 6
    GdiCompatible = 7


class MetafileHeader(Object):
    @property
    def Bounds(self) -> Rectangle: ...
    @property
    def DpiX(self) -> Single: ...
    @property
    def DpiY(self) -> Single: ...
    @property
    def EmfPlusHeaderSize(self) -> int: ...
    @property
    def LogicalDpiX(self) -> int: ...
    @property
    def LogicalDpiY(self) -> int: ...
    @property
    def MetafileSize(self) -> int: ...
    @property
    def Type(self) -> MetafileType: ...
    @property
    def Version(self) -> int: ...
    @property
    def WmfHeader(self) -> MetaHeader: ...
    def IsDisplay(self) -> bool: ...
    def IsEmf(self) -> bool: ...
    def IsEmfOrEmfPlus(self) -> bool: ...
    def IsEmfPlus(self) -> bool: ...
    def IsEmfPlusDual(self) -> bool: ...
    def IsEmfPlusOnly(self) -> bool: ...
    def IsWmf(self) -> bool: ...
    def IsWmfPlaceable(self) -> bool: ...


class MetafileType:
    Invalid = 0
    Wmf = 1
    WmfPlaceable = 2
    Emf = 3
    EmfPlusOnly = 4
    EmfPlusDual = 5


class MetaHeader(Object):
    def __init__(self): ...
    @property
    def HeaderSize(self) -> Int16: ...
    @property
    def MaxRecord(self) -> int: ...
    @property
    def NoObjects(self) -> Int16: ...
    @property
    def NoParameters(self) -> Int16: ...
    @property
    def Size(self) -> int: ...
    @property
    def Type(self) -> Int16: ...
    @property
    def Version(self) -> Int16: ...
    @HeaderSize.setter
    def HeaderSize(self, value: Int16) -> None: ...
    @MaxRecord.setter
    def MaxRecord(self, value: int) -> None: ...
    @NoObjects.setter
    def NoObjects(self, value: Int16) -> None: ...
    @NoParameters.setter
    def NoParameters(self, value: Int16) -> None: ...
    @Size.setter
    def Size(self, value: int) -> None: ...
    @Type.setter
    def Type(self, value: Int16) -> None: ...
    @Version.setter
    def Version(self, value: Int16) -> None: ...


class PaletteFlags:
    HasAlpha = 1
    GrayScale = 2
    Halftone = 4


class PixelFormat:
    DontCare = 0
    Undefined = 0
    Max = 15
    Indexed = 65536
    Gdi = 131072
    Format16bppRgb555 = 135173
    Format16bppRgb565 = 135174
    Format24bppRgb = 137224
    Format32bppRgb = 139273
    Format1bppIndexed = 196865
    Format4bppIndexed = 197634
    Format8bppIndexed = 198659
    Alpha = 262144
    Format16bppArgb1555 = 397319
    PAlpha = 524288
    Format32bppPArgb = 925707
    Extended = 1048576
    Format16bppGrayScale = 1052676
    Format48bppRgb = 1060876
    Format64bppPArgb = 1851406
    Canonical = 2097152
    Format32bppArgb = 2498570
    Format64bppArgb = 3424269


class PlayRecordCallback(MulticastDelegate):
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, recordType: EmfPlusRecordType, flags: int, dataSize: int, recordData: IntPtr, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, recordType: EmfPlusRecordType, flags: int, dataSize: int, recordData: IntPtr) -> None: ...


class PropertyItem(Object):
    @property
    def Id(self) -> int: ...
    @property
    def Len(self) -> int: ...
    @property
    def Type(self) -> Int16: ...
    @property
    def Value(self) -> Set(Byte): ...
    @Id.setter
    def Id(self, value: int) -> None: ...
    @Len.setter
    def Len(self, value: int) -> None: ...
    @Type.setter
    def Type(self, value: Int16) -> None: ...
    @Value.setter
    def Value(self, value: Set(Byte)) -> None: ...


class WmfPlaceableFileHeader(Object):
    def __init__(self): ...
    @property
    def BboxBottom(self) -> Int16: ...
    @property
    def BboxLeft(self) -> Int16: ...
    @property
    def BboxRight(self) -> Int16: ...
    @property
    def BboxTop(self) -> Int16: ...
    @property
    def Checksum(self) -> Int16: ...
    @property
    def Hmf(self) -> Int16: ...
    @property
    def Inch(self) -> Int16: ...
    @property
    def Key(self) -> int: ...
    @property
    def Reserved(self) -> int: ...
    @BboxBottom.setter
    def BboxBottom(self, value: Int16) -> None: ...
    @BboxLeft.setter
    def BboxLeft(self, value: Int16) -> None: ...
    @BboxRight.setter
    def BboxRight(self, value: Int16) -> None: ...
    @BboxTop.setter
    def BboxTop(self, value: Int16) -> None: ...
    @Checksum.setter
    def Checksum(self, value: Int16) -> None: ...
    @Hmf.setter
    def Hmf(self, value: Int16) -> None: ...
    @Inch.setter
    def Inch(self, value: Int16) -> None: ...
    @Key.setter
    def Key(self, value: int) -> None: ...
    @Reserved.setter
    def Reserved(self, value: int) -> None: ...
