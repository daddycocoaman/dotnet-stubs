__all__ = ['CompilerServices','FileIO']
from typing import Tuple, Set, Iterable, List


class AppWinStyle:
    Hide = 0
    NormalFocus = 1
    MinimizedFocus = 2
    MaximizedFocus = 3
    NormalNoFocus = 4
    MinimizedNoFocus = 6


class CallType:
    Method = 1
    Get = 2
    Let = 4
    Set = 8


class Collection:
    def __init__(self): ...
    def Add(self, Item: Object, Key: str, Before: Object, After: Object) -> None: ...
    def Clear(self) -> None: ...
    def Contains(self, Key: str) -> bool: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, Index: int) -> Object: ...
    @property
    def Item(self, Key: str) -> Object: ...
    @property
    def Item(self, Index: Object) -> Object: ...
    def GetEnumerator(self) -> IEnumerator: ...
    @overload
    def Remove(self, Key: str) -> None: ...
    @overload
    def Remove(self, Index: int) -> None: ...


class ComClassAttribute:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, _ClassID: str): ...
    @overload
    def __init__(self, _ClassID: str, _InterfaceID: str): ...
    @overload
    def __init__(self, _ClassID: str, _InterfaceID: str, _EventId: str): ...
    @property
    def ClassID(self) -> str: ...
    @property
    def EventID(self) -> str: ...
    @property
    def InterfaceID(self) -> str: ...
    @property
    def InterfaceShadows(self) -> bool: ...
    @InterfaceShadows.setter
    def InterfaceShadows(self, AutoPropertyValue: bool) -> None: ...


class CompareMethod:
    Binary = 0
    Text = 1


class Constants:
    pass


class ControlChars:
    def __init__(self): ...


class Conversion:
    @overload
    def CTypeDynamic(Expression: Object) -> TargetType: ...
    @overload
    def CTypeDynamic(Expression: Object, TargetType: Type) -> Object: ...
    @overload
    def ErrorToString() -> str: ...
    @overload
    def ErrorToString(ErrorNumber: int) -> str: ...
    @overload
    def Fix(Number: Int16) -> Int16: ...
    @overload
    def Fix(Number: int) -> int: ...
    @overload
    def Fix(Number: Int64) -> Int64: ...
    @overload
    def Fix(Number: float) -> float: ...
    @overload
    def Fix(Number: Single) -> Single: ...
    @overload
    def Fix(Number: Decimal) -> Decimal: ...
    @overload
    def Fix(Number: Object) -> Object: ...
    @overload
    def Hex(Number: UInt32) -> str: ...
    @overload
    def Hex(Number: SByte) -> str: ...
    @overload
    def Hex(Number: Byte) -> str: ...
    @overload
    def Hex(Number: Int16) -> str: ...
    @overload
    def Hex(Number: UInt16) -> str: ...
    @overload
    def Hex(Number: int) -> str: ...
    @overload
    def Hex(Number: Int64) -> str: ...
    @overload
    def Hex(Number: UInt64) -> str: ...
    @overload
    def Hex(Number: Object) -> str: ...
    @overload
    def Int(Number: Int16) -> Int16: ...
    @overload
    def Int(Number: int) -> int: ...
    @overload
    def Int(Number: float) -> float: ...
    @overload
    def Int(Number: Single) -> Single: ...
    @overload
    def Int(Number: Decimal) -> Decimal: ...
    @overload
    def Int(Number: Object) -> Object: ...
    @overload
    def Int(Number: Int64) -> Int64: ...
    @overload
    def Oct(Number: Int16) -> str: ...
    @overload
    def Oct(Number: Byte) -> str: ...
    @overload
    def Oct(Number: Object) -> str: ...
    @overload
    def Oct(Number: UInt16) -> str: ...
    @overload
    def Oct(Number: Int64) -> str: ...
    @overload
    def Oct(Number: UInt32) -> str: ...
    @overload
    def Oct(Number: int) -> str: ...
    @overload
    def Oct(Number: SByte) -> str: ...
    @overload
    def Oct(Number: UInt64) -> str: ...
    def Str(Number: Object) -> str: ...
    @overload
    def Val(Expression: Char) -> int: ...
    @overload
    def Val(Expression: Object) -> float: ...
    @overload
    def Val(InputStr: str) -> float: ...


class DateAndTime:
    @overload
    def DateAdd(Interval: DateInterval, Number: float, DateValue: DateTime) -> DateTime: ...
    @overload
    def DateAdd(Interval: str, Number: float, DateValue: Object) -> DateTime: ...
    @overload
    def DateDiff(Interval: DateInterval, Date1: DateTime, Date2: DateTime, DayOfWeek: FirstDayOfWeek, WeekOfYear: FirstWeekOfYear) -> Int64: ...
    @overload
    def DateDiff(Interval: str, Date1: Object, Date2: Object, DayOfWeek: FirstDayOfWeek, WeekOfYear: FirstWeekOfYear) -> Int64: ...
    @overload
    def DatePart(Interval: str, DateValue: Object, DayOfWeek: FirstDayOfWeek, WeekOfYear: FirstWeekOfYear) -> int: ...
    @overload
    def DatePart(Interval: DateInterval, DateValue: DateTime, FirstDayOfWeekValue: FirstDayOfWeek, FirstWeekOfYearValue: FirstWeekOfYear) -> int: ...
    def DateSerial(Year: int, Month: int, Day: int) -> DateTime: ...
    def DateValue(StringDate: str) -> DateTime: ...
    def Day(DateValue: DateTime) -> int: ...
    @property
    def DateString() -> str: ...
    @property
    def Now() -> DateTime: ...
    @property
    def TimeOfDay() -> DateTime: ...
    @property
    def Timer() -> float: ...
    @property
    def TimeString() -> str: ...
    @property
    def Today() -> DateTime: ...
    def Hour(TimeValue: DateTime) -> int: ...
    def Minute(TimeValue: DateTime) -> int: ...
    def Month(DateValue: DateTime) -> int: ...
    def MonthName(Month: int, Abbreviate: bool) -> str: ...
    def Second(TimeValue: DateTime) -> int: ...
    @DateString.setter
    def DateString(Value: str) -> None: ...
    @TimeOfDay.setter
    def TimeOfDay(Value: DateTime) -> None: ...
    @TimeString.setter
    def TimeString(Value: str) -> None: ...
    @Today.setter
    def Today(Value: DateTime) -> None: ...
    def TimeSerial(Hour: int, Minute: int, Second: int) -> DateTime: ...
    def TimeValue(StringTime: str) -> DateTime: ...
    def Weekday(DateValue: DateTime, DayOfWeek: FirstDayOfWeek) -> int: ...
    def WeekdayName(Weekday: int, Abbreviate: bool, FirstDayOfWeekValue: FirstDayOfWeek) -> str: ...
    def Year(DateValue: DateTime) -> int: ...


class DateFormat:
    GeneralDate = 0
    LongDate = 1
    ShortDate = 2
    LongTime = 3
    ShortTime = 4


class DateInterval:
    Year = 0
    Quarter = 1
    Month = 2
    DayOfYear = 3
    Day = 4
    WeekOfYear = 5
    Weekday = 6
    Hour = 7
    Minute = 8
    Second = 9


class DueDate:
    EndOfPeriod = 0
    BegOfPeriod = 1


class ErrObject:
    def Clear(self) -> None: ...
    @property
    def Description(self) -> str: ...
    @property
    def Erl(self) -> int: ...
    @property
    def HelpContext(self) -> int: ...
    @property
    def HelpFile(self) -> str: ...
    @property
    def LastDllError(self) -> int: ...
    @property
    def Number(self) -> int: ...
    @property
    def Source(self) -> str: ...
    def GetException(self) -> Exception: ...
    def Raise(self, Number: int, Source: Object, Description: Object, HelpFile: Object, HelpContext: Object) -> None: ...
    @Description.setter
    def Description(self, Value: str) -> None: ...
    @HelpContext.setter
    def HelpContext(self, Value: int) -> None: ...
    @HelpFile.setter
    def HelpFile(self, Value: str) -> None: ...
    @Number.setter
    def Number(self, Value: int) -> None: ...
    @Source.setter
    def Source(self, Value: str) -> None: ...


class FileAttribute:
    Normal = 0
    ReadOnly = 1
    Hidden = 2
    System = 4
    Volume = 8
    Directory = 16
    Archive = 32


class FileSystem:
    def ChDir(Path: str) -> None: ...
    @overload
    def ChDrive(Drive: Char) -> None: ...
    @overload
    def ChDrive(Drive: str) -> None: ...
    @overload
    def CurDir() -> str: ...
    @overload
    def CurDir(Drive: Char) -> str: ...
    @overload
    def Dir() -> str: ...
    @overload
    def Dir(PathName: str, Attributes: FileAttribute) -> str: ...
    def EOF(FileNumber: int) -> bool: ...
    def FileAttr(FileNumber: int) -> OpenMode: ...
    def FileClose(FileNumbers: Set(int)) -> None: ...
    def FileCopy(Source: str, Destination: str) -> None: ...
    def FileDateTime(PathName: str) -> DateTime: ...
    @overload
    def FileGet(FileNumber: int, Value: Int64, RecordNumber: Int64) -> Tuple[Int64]: ...
    @overload
    def FileGet(FileNumber: int, Value: Char, RecordNumber: Int64) -> Tuple[Char]: ...
    @overload
    def FileGet(FileNumber: int, Value: int, RecordNumber: Int64) -> Tuple[int]: ...
    @overload
    def FileGet(FileNumber: int, Value: Int16, RecordNumber: Int64) -> Tuple[Int16]: ...
    @overload
    def FileGet(FileNumber: int, Value: Byte, RecordNumber: Int64) -> Tuple[Byte]: ...
    @overload
    def FileGet(FileNumber: int, Value: bool, RecordNumber: Int64) -> Tuple[bool]: ...
    @overload
    def FileGet(FileNumber: int, Value: ValueType, RecordNumber: Int64) -> Tuple[ValueType]: ...
    @overload
    def FileGet(FileNumber: int, Value: Decimal, RecordNumber: Int64) -> Tuple[Decimal]: ...
    @overload
    def FileGet(FileNumber: int, Value: float, RecordNumber: Int64) -> Tuple[float]: ...
    @overload
    def FileGet(FileNumber: int, Value: DateTime, RecordNumber: Int64) -> Tuple[DateTime]: ...
    @overload
    def FileGet(FileNumber: int, Value: Single, RecordNumber: Int64) -> Tuple[Single]: ...
    @overload
    def FileGet(FileNumber: int, Value: str, RecordNumber: Int64, StringIsFixedLength: bool) -> Tuple[str]: ...
    @overload
    def FileGet(FileNumber: int, Value: Array, RecordNumber: Int64, ArrayIsDynamic: bool, StringIsFixedLength: bool) -> Tuple[Array]: ...
    def FileGetObject(FileNumber: int, Value: Object, RecordNumber: Int64) -> Tuple[Object]: ...
    def FileLen(PathName: str) -> Int64: ...
    def FileOpen(FileNumber: int, FileName: str, Mode: OpenMode, Access: OpenAccess, Share: OpenShare, RecordLength: int) -> None: ...
    @overload
    def FilePut(FileNumber: int, Value: ValueType, RecordNumber: Int64) -> None: ...
    @overload
    def FilePut(FileNumber: int, Value: bool, RecordNumber: Int64) -> None: ...
    @overload
    def FilePut(FileNumber: int, Value: Byte, RecordNumber: Int64) -> None: ...
    @overload
    def FilePut(FileNumber: int, Value: int, RecordNumber: Int64) -> None: ...
    @overload
    def FilePut(FileNumber: int, Value: Int16, RecordNumber: Int64) -> None: ...
    @overload
    def FilePut(FileNumber: int, Value: Single, RecordNumber: Int64) -> None: ...
    @overload
    def FilePut(FileNumber: int, Value: float, RecordNumber: Int64) -> None: ...
    @overload
    def FilePut(FileNumber: int, Value: Decimal, RecordNumber: Int64) -> None: ...
    @overload
    def FilePut(FileNumber: int, Value: DateTime, RecordNumber: Int64) -> None: ...
    @overload
    def FilePut(FileNumber: int, Value: Int64, RecordNumber: Int64) -> None: ...
    @overload
    def FilePut(FileNumber: int, Value: Char, RecordNumber: Int64) -> None: ...
    @overload
    def FilePut(FileNumber: int, Value: str, RecordNumber: Int64, StringIsFixedLength: bool) -> None: ...
    @overload
    def FilePut(FileNumber: int, Value: Array, RecordNumber: Int64, ArrayIsDynamic: bool, StringIsFixedLength: bool) -> None: ...
    def FilePutObject(FileNumber: int, Value: Object, RecordNumber: Int64) -> None: ...
    def FileWidth(FileNumber: int, RecordWidth: int) -> None: ...
    def FreeFile() -> int: ...
    def GetAttr(PathName: str) -> FileAttribute: ...
    @overload
    def Input(FileNumber: int, Value: Decimal) -> Tuple[Decimal]: ...
    @overload
    def Input(FileNumber: int, Value: DateTime) -> Tuple[DateTime]: ...
    @overload
    def Input(FileNumber: int, Value: str) -> Tuple[str]: ...
    @overload
    def Input(FileNumber: int, Value: float) -> Tuple[float]: ...
    @overload
    def Input(FileNumber: int, Value: Object) -> Tuple[Object]: ...
    @overload
    def Input(FileNumber: int, Value: bool) -> Tuple[bool]: ...
    @overload
    def Input(FileNumber: int, Value: Byte) -> Tuple[Byte]: ...
    @overload
    def Input(FileNumber: int, Value: Int16) -> Tuple[Int16]: ...
    @overload
    def Input(FileNumber: int, Value: int) -> Tuple[int]: ...
    @overload
    def Input(FileNumber: int, Value: Int64) -> Tuple[Int64]: ...
    @overload
    def Input(FileNumber: int, Value: Char) -> Tuple[Char]: ...
    @overload
    def Input(FileNumber: int, Value: Single) -> Tuple[Single]: ...
    def InputString(FileNumber: int, CharCount: int) -> str: ...
    def Kill(PathName: str) -> None: ...
    def LineInput(FileNumber: int) -> str: ...
    def Loc(FileNumber: int) -> Int64: ...
    @overload
    def Lock(FileNumber: int) -> None: ...
    @overload
    def Lock(FileNumber: int, Record: Int64) -> None: ...
    @overload
    def Lock(FileNumber: int, FromRecord: Int64, ToRecord: Int64) -> None: ...
    def LOF(FileNumber: int) -> Int64: ...
    def MkDir(Path: str) -> None: ...
    def Print(FileNumber: int, Output: Set(Object)) -> None: ...
    def PrintLine(FileNumber: int, Output: Set(Object)) -> None: ...
    def Rename(OldPath: str, NewPath: str) -> None: ...
    def Reset() -> None: ...
    def RmDir(Path: str) -> None: ...
    @overload
    def Seek(FileNumber: int) -> Int64: ...
    @overload
    def Seek(FileNumber: int, Position: Int64) -> None: ...
    def SetAttr(PathName: str, Attributes: FileAttribute) -> None: ...
    def SPC(Count: Int16) -> SpcInfo: ...
    @overload
    def TAB() -> TabInfo: ...
    @overload
    def TAB(Column: Int16) -> TabInfo: ...
    @overload
    def Unlock(FileNumber: int) -> None: ...
    @overload
    def Unlock(FileNumber: int, Record: Int64) -> None: ...
    @overload
    def Unlock(FileNumber: int, FromRecord: Int64, ToRecord: Int64) -> None: ...
    def Write(FileNumber: int, Output: Set(Object)) -> None: ...
    def WriteLine(FileNumber: int, Output: Set(Object)) -> None: ...


class Financial:
    def DDB(Cost: float, Salvage: float, Life: float, Period: float, Factor: float) -> float: ...
    def FV(Rate: float, NPer: float, Pmt: float, PV: float, Due: DueDate) -> float: ...
    def IPmt(Rate: float, Per: float, NPer: float, PV: float, FV: float, Due: DueDate) -> float: ...
    def IRR(ValueArray: Set(float), Guess: float) -> Tuple[float, Set(float)]: ...
    def MIRR(ValueArray: Set(float), FinanceRate: float, ReinvestRate: float) -> Tuple[float, Set(float)]: ...
    def NPer(Rate: float, Pmt: float, PV: float, FV: float, Due: DueDate) -> float: ...
    def NPV(Rate: float, ValueArray: Set(float)) -> Tuple[float, Set(float)]: ...
    def Pmt(Rate: float, NPer: float, PV: float, FV: float, Due: DueDate) -> float: ...
    def PPmt(Rate: float, Per: float, NPer: float, PV: float, FV: float, Due: DueDate) -> float: ...
    def PV(Rate: float, NPer: float, Pmt: float, FV: float, Due: DueDate) -> float: ...
    def Rate(NPer: float, Pmt: float, PV: float, FV: float, Due: DueDate, Guess: float) -> float: ...
    def SLN(Cost: float, Salvage: float, Life: float) -> float: ...
    def SYD(Cost: float, Salvage: float, Life: float, Period: float) -> float: ...


class FirstDayOfWeek:
    System = 0
    Sunday = 1
    Monday = 2
    Tuesday = 3
    Wednesday = 4
    Thursday = 5
    Friday = 6
    Saturday = 7


class FirstWeekOfYear:
    System = 0
    Jan1 = 1
    FirstFourDays = 2
    FirstFullWeek = 3


class HideModuleNameAttribute:
    def __init__(self): ...


class Information:
    def Erl() -> int: ...
    def Err() -> ErrObject: ...
    def IsArray(VarName: Object) -> bool: ...
    def IsDate(Expression: Object) -> bool: ...
    def IsDBNull(Expression: Object) -> bool: ...
    def IsError(Expression: Object) -> bool: ...
    def IsNothing(Expression: Object) -> bool: ...
    def IsNumeric(Expression: Object) -> bool: ...
    def IsReference(Expression: Object) -> bool: ...
    def LBound(Array: Array, Rank: int) -> int: ...
    def QBColor(Color: int) -> int: ...
    def RGB(Red: int, Green: int, Blue: int) -> int: ...
    def SystemTypeName(VbName: str) -> str: ...
    def TypeName(VarName: Object) -> str: ...
    def UBound(Array: Array, Rank: int) -> int: ...
    def VarType(VarName: Object) -> VariantType: ...
    def VbTypeName(UrtName: str) -> str: ...


class Interaction:
    @overload
    def AppActivate(ProcessId: int) -> None: ...
    @overload
    def AppActivate(Title: str) -> None: ...
    def Beep() -> None: ...
    def CallByName(ObjectRef: Object, ProcName: str, UseCallType: CallType, Args: Set(Object)) -> Object: ...
    def Choose(Index: float, Choice: Set(Object)) -> Object: ...
    def Command() -> str: ...
    def CreateObject(ProgId: str, ServerName: str) -> Object: ...
    def DeleteSetting(AppName: str, Section: str, Key: str) -> None: ...
    @overload
    def Environ(Expression: int) -> str: ...
    @overload
    def Environ(Expression: str) -> str: ...
    def GetAllSettings(AppName: str, Section: str) -> String[,]: ...
    def GetObject(PathName: str, Class: str) -> Object: ...
    def GetSetting(AppName: str, Section: str, Key: str, Default: str) -> str: ...
    def IIf(Expression: bool, TruePart: Object, FalsePart: Object) -> Object: ...
    def InputBox(Prompt: str, Title: str, DefaultResponse: str, XPos: int, YPos: int) -> str: ...
    def MsgBox(Prompt: Object, Buttons: MsgBoxStyle, Title: Object) -> MsgBoxResult: ...
    def Partition(Number: Int64, Start: Int64, Stop: Int64, Interval: Int64) -> str: ...
    def SaveSetting(AppName: str, Section: str, Key: str, Setting: str) -> None: ...
    def Shell(PathName: str, Style: AppWinStyle, Wait: bool, Timeout: int) -> int: ...
    def Switch(VarExpr: Set(Object)) -> Object: ...


class MsgBoxResult:
    Ok = 1
    Cancel = 2
    Abort = 3
    Retry = 4
    Ignore = 5
    Yes = 6
    No = 7


class MsgBoxStyle:
    ApplicationModal = 0
    DefaultButton1 = 0
    OkOnly = 0
    OkCancel = 1
    AbortRetryIgnore = 2
    YesNoCancel = 3
    YesNo = 4
    RetryCancel = 5
    Critical = 16
    Question = 32
    Exclamation = 48
    Information = 64
    DefaultButton2 = 256
    DefaultButton3 = 512
    SystemModal = 4096
    MsgBoxHelp = 16384
    MsgBoxSetForeground = 65536
    MsgBoxRight = 524288
    MsgBoxRtlReading = 1048576


class MyGroupCollectionAttribute:
    def __init__(self, typeToCollect: str, createInstanceMethodName: str, disposeInstanceMethodName: str, defaultInstanceAlias: str): ...
    @property
    def CreateMethod(self) -> str: ...
    @property
    def DefaultInstanceAlias(self) -> str: ...
    @property
    def DisposeMethod(self) -> str: ...
    @property
    def MyGroupName(self) -> str: ...


class OpenAccess:
    Read = 1
    Write = 2
    ReadWrite = 3
    Default = -1


class OpenMode:
    Input = 1
    Output = 2
    Random = 4
    Append = 8
    Binary = 32


class OpenShare:
    LockReadWrite = 0
    LockWrite = 1
    LockRead = 2
    Shared = 3
    Default = -1


class SpcInfo:
    pass


class Strings:
    @overload
    def Asc(String: Char) -> int: ...
    @overload
    def Asc(String: str) -> int: ...
    @overload
    def AscW(String: str) -> int: ...
    @overload
    def AscW(String: Char) -> int: ...
    def Chr(CharCode: int) -> Char: ...
    def ChrW(CharCode: int) -> Char: ...
    @overload
    def Filter(Source: Set(Object), Match: str, Include: bool, Compare: CompareMethod) -> Set(str): ...
    @overload
    def Filter(Source: Set(str), Match: str, Include: bool, Compare: CompareMethod) -> Set(str): ...
    def Format(Expression: Object, Style: str) -> str: ...
    def FormatCurrency(Expression: Object, NumDigitsAfterDecimal: int, IncludeLeadingDigit: TriState, UseParensForNegativeNumbers: TriState, GroupDigits: TriState) -> str: ...
    def FormatDateTime(Expression: DateTime, NamedFormat: DateFormat) -> str: ...
    def FormatNumber(Expression: Object, NumDigitsAfterDecimal: int, IncludeLeadingDigit: TriState, UseParensForNegativeNumbers: TriState, GroupDigits: TriState) -> str: ...
    def FormatPercent(Expression: Object, NumDigitsAfterDecimal: int, IncludeLeadingDigit: TriState, UseParensForNegativeNumbers: TriState, GroupDigits: TriState) -> str: ...
    def GetChar(str: str, Index: int) -> Char: ...
    @overload
    def InStr(String1: str, String2: str, Compare: CompareMethod) -> int: ...
    @overload
    def InStr(Start: int, String1: str, String2: str, Compare: CompareMethod) -> int: ...
    def InStrRev(StringCheck: str, StringMatch: str, Start: int, Compare: CompareMethod) -> int: ...
    @overload
    def Join(SourceArray: Set(Object), Delimiter: str) -> str: ...
    @overload
    def Join(SourceArray: Set(str), Delimiter: str) -> str: ...
    @overload
    def LCase(Value: str) -> str: ...
    @overload
    def LCase(Value: Char) -> Char: ...
    def Left(str: str, Length: int) -> str: ...
    @overload
    def Len(Expression: SByte) -> int: ...
    @overload
    def Len(Expression: bool) -> int: ...
    @overload
    def Len(Expression: str) -> int: ...
    @overload
    def Len(Expression: Object) -> int: ...
    @overload
    def Len(Expression: DateTime) -> int: ...
    @overload
    def Len(Expression: Byte) -> int: ...
    @overload
    def Len(Expression: Int16) -> int: ...
    @overload
    def Len(Expression: UInt16) -> int: ...
    @overload
    def Len(Expression: int) -> int: ...
    @overload
    def Len(Expression: UInt32) -> int: ...
    @overload
    def Len(Expression: Char) -> int: ...
    @overload
    def Len(Expression: UInt64) -> int: ...
    @overload
    def Len(Expression: Decimal) -> int: ...
    @overload
    def Len(Expression: Int64) -> int: ...
    @overload
    def Len(Expression: float) -> int: ...
    @overload
    def Len(Expression: Single) -> int: ...
    def LSet(Source: str, Length: int) -> str: ...
    def LTrim(str: str) -> str: ...
    @overload
    def Mid(str: str, Start: int) -> str: ...
    @overload
    def Mid(str: str, Start: int, Length: int) -> str: ...
    def Replace(Expression: str, Find: str, Replacement: str, Start: int, Count: int, Compare: CompareMethod) -> str: ...
    def Right(str: str, Length: int) -> str: ...
    def RSet(Source: str, Length: int) -> str: ...
    def RTrim(str: str) -> str: ...
    def Space(Number: int) -> str: ...
    def Split(Expression: str, Delimiter: str, Limit: int, Compare: CompareMethod) -> Set(str): ...
    def StrComp(String1: str, String2: str, Compare: CompareMethod) -> int: ...
    def StrConv(str: str, Conversion: VbStrConv, LocaleID: int) -> str: ...
    @overload
    def StrDup(Number: int, Character: str) -> str: ...
    @overload
    def StrDup(Number: int, Character: Char) -> str: ...
    @overload
    def StrDup(Number: int, Character: Object) -> Object: ...
    def StrReverse(Expression: str) -> str: ...
    def Trim(str: str) -> str: ...
    @overload
    def UCase(Value: Char) -> Char: ...
    @overload
    def UCase(Value: str) -> str: ...


class TabInfo:
    pass


class TriState:
    False = 0
    UseDefault = -2
    True = -1


class VariantType:
    Empty = 0
    Null = 1
    Short = 2
    Integer = 3
    Single = 4
    Double = 5
    Currency = 6
    Date = 7
    String = 8
    Object = 9
    Error = 10
    Boolean = 11
    Variant = 12
    DataObject = 13
    Decimal = 14
    Byte = 17
    Char = 18
    Long = 20
    UserDefinedType = 36
    Array = 8192


class VBFixedArrayAttribute:
    @overload
    def __init__(self, UpperBound1: int): ...
    @overload
    def __init__(self, UpperBound1: int, UpperBound2: int): ...
    @property
    def Bounds(self) -> Set(int): ...
    @property
    def Length(self) -> int: ...


class VBFixedStringAttribute:
    def __init__(self, Length: int): ...
    @property
    def Length(self) -> int: ...


class VBMath:
    @overload
    def Randomize() -> None: ...
    @overload
    def Randomize(Number: float) -> None: ...
    @overload
    def Rnd() -> Single: ...
    @overload
    def Rnd(Number: Single) -> Single: ...


class VbStrConv:
    #None = 0
    Uppercase = 1
    Lowercase = 2
    ProperCase = 3
    Wide = 4
    Narrow = 8
    Katakana = 16
    Hiragana = 32
    SimplifiedChinese = 256
    TraditionalChinese = 512
    LinguisticCasing = 1024
