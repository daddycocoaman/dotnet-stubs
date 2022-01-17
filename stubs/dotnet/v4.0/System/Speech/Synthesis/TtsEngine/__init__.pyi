from typing import Tuple, Set, Iterable, List


class ContourPoint(ValueType):
    def __init__(self, start: Single, change: Single, changeType: ContourPointChangeType): ...
    @overload
    def Equals(self, other: ContourPoint) -> bool: ...
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @property
    def Change(self) -> Single: ...
    @property
    def ChangeType(self) -> ContourPointChangeType: ...
    @property
    def Start(self) -> Single: ...
    def GetHashCode(self) -> int: ...
    def op_Equality(point1: ContourPoint, point2: ContourPoint) -> bool: ...
    def op_Inequality(point1: ContourPoint, point2: ContourPoint) -> bool: ...


class ContourPointChangeType:
    Hz = 0
    Percentage = 1


class EmphasisBreak:
    Default = -7
    ExtraStrong = -6
    Strong = -5
    Medium = -4
    Weak = -3
    ExtraWeak = -2
    #None = -1


class EmphasisWord:
    Default = 0
    Strong = 1
    Moderate = 2
    #None = 3
    Reduced = 4


class EventParameterType:
    Undefined = 0
    Token = 1
    Object = 2
    Pointer = 3
    String = 4


class FragmentState(ValueType):
    def __init__(self, action: TtsEngineAction, langId: int, emphasis: int, duration: int, sayAs: SayAs, prosody: Prosody, phonemes: Set(Char)): ...
    @overload
    def Equals(self, other: FragmentState) -> bool: ...
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @property
    def Action(self) -> TtsEngineAction: ...
    @property
    def Duration(self) -> int: ...
    @property
    def Emphasis(self) -> int: ...
    @property
    def LangId(self) -> int: ...
    @property
    def Phoneme(self) -> Set(Char): ...
    @property
    def Prosody(self) -> Prosody: ...
    @property
    def SayAs(self) -> SayAs: ...
    def GetHashCode(self) -> int: ...
    def op_Equality(state1: FragmentState, state2: FragmentState) -> bool: ...
    def op_Inequality(state1: FragmentState, state2: FragmentState) -> bool: ...


class ITtsEngineSite:
    def AddEvents(self, events: Set(SpeechEventInfo), count: int) -> None: ...
    def CompleteSkip(self, skipped: int) -> None: ...
    @property
    def Actions(self) -> int: ...
    @property
    def EventInterest(self) -> int: ...
    @property
    def Rate(self) -> int: ...
    @property
    def Volume(self) -> int: ...
    def GetSkipInfo(self) -> SkipInfo: ...
    def LoadResource(self, uri: Uri, mediaType: str) -> Stream: ...
    def Write(self, data: IntPtr, count: int) -> int: ...


class Prosody(Object):
    def __init__(self): ...
    @property
    def Duration(self) -> int: ...
    @property
    def Pitch(self) -> ProsodyNumber: ...
    @property
    def Range(self) -> ProsodyNumber: ...
    @property
    def Rate(self) -> ProsodyNumber: ...
    @property
    def Volume(self) -> ProsodyNumber: ...
    def GetContourPoints(self) -> Set(ContourPoint): ...
    @Duration.setter
    def Duration(self, value: int) -> None: ...
    @Pitch.setter
    def Pitch(self, value: ProsodyNumber) -> None: ...
    @Range.setter
    def Range(self, value: ProsodyNumber) -> None: ...
    @Rate.setter
    def Rate(self, value: ProsodyNumber) -> None: ...
    @Volume.setter
    def Volume(self, value: ProsodyNumber) -> None: ...
    def SetContourPoints(self, points: Set(ContourPoint)) -> None: ...


class ProsodyNumber(ValueType):
    @overload
    def __init__(self, ssmlAttributeId: int): ...
    @overload
    def __init__(self, number: Single): ...
    @overload
    def Equals(self, other: ProsodyNumber) -> bool: ...
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @property
    def IsNumberPercent(self) -> bool: ...
    @property
    def Number(self) -> Single: ...
    @property
    def SsmlAttributeId(self) -> int: ...
    @property
    def Unit(self) -> ProsodyUnit: ...
    def GetHashCode(self) -> int: ...
    def op_Equality(prosodyNumber1: ProsodyNumber, prosodyNumber2: ProsodyNumber) -> bool: ...
    def op_Inequality(prosodyNumber1: ProsodyNumber, prosodyNumber2: ProsodyNumber) -> bool: ...


class ProsodyPitch:
    Default = 0
    ExtraLow = 1
    Low = 2
    Medium = 3
    High = 4
    ExtraHigh = 5


class ProsodyRange:
    Default = 0
    ExtraLow = 1
    Low = 2
    Medium = 3
    High = 4
    ExtraHigh = 5


class ProsodyRate:
    Default = 0
    ExtraSlow = 1
    Slow = 2
    Medium = 3
    Fast = 4
    ExtraFast = 5


class ProsodyUnit:
    Default = 0
    Hz = 1
    Semitone = 2


class ProsodyVolume:
    ExtraLoud = -7
    Loud = -6
    Medium = -5
    Soft = -4
    ExtraSoft = -3
    Silent = -2
    Default = -1


class SayAs(Object):
    def __init__(self): ...
    @property
    def Detail(self) -> str: ...
    @property
    def Format(self) -> str: ...
    @property
    def InterpretAs(self) -> str: ...
    @Detail.setter
    def Detail(self, value: str) -> None: ...
    @Format.setter
    def Format(self, value: str) -> None: ...
    @InterpretAs.setter
    def InterpretAs(self, value: str) -> None: ...


class SkipInfo(Object):
    def __init__(self): ...
    @property
    def Count(self) -> int: ...
    @property
    def Type(self) -> int: ...
    @Count.setter
    def Count(self, value: int) -> None: ...
    @Type.setter
    def Type(self, value: int) -> None: ...


class SpeakOutputFormat:
    WaveFormat = 0
    Text = 1


class SpeechEventInfo(ValueType):
    def __init__(self, eventId: Int16, parameterType: Int16, param1: int, param2: IntPtr): ...
    @overload
    def Equals(self, other: SpeechEventInfo) -> bool: ...
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @property
    def EventId(self) -> Int16: ...
    @property
    def Param1(self) -> int: ...
    @property
    def Param2(self) -> IntPtr: ...
    @property
    def ParameterType(self) -> Int16: ...
    def GetHashCode(self) -> int: ...
    def op_Equality(event1: SpeechEventInfo, event2: SpeechEventInfo) -> bool: ...
    def op_Inequality(event1: SpeechEventInfo, event2: SpeechEventInfo) -> bool: ...


class TextFragment(Object):
    def __init__(self): ...
    @property
    def State(self) -> FragmentState: ...
    @property
    def TextLength(self) -> int: ...
    @property
    def TextOffset(self) -> int: ...
    @property
    def TextToSpeak(self) -> str: ...
    @State.setter
    def State(self, value: FragmentState) -> None: ...
    @TextLength.setter
    def TextLength(self, value: int) -> None: ...
    @TextOffset.setter
    def TextOffset(self, value: int) -> None: ...
    @TextToSpeak.setter
    def TextToSpeak(self, value: str) -> None: ...


class TtsEngineAction:
    Speak = 0
    Silence = 1
    Pronounce = 2
    Bookmark = 3
    SpellOut = 4
    StartSentence = 5
    StartParagraph = 6
    ParseUnknownTag = 7


class TtsEngineSsml(Object):
    def AddLexicon(self, uri: Uri, mediaType: str, site: ITtsEngineSite) -> None: ...
    def GetOutputFormat(self, speakOutputFormat: SpeakOutputFormat, targetWaveFormat: IntPtr) -> IntPtr: ...
    def RemoveLexicon(self, uri: Uri, site: ITtsEngineSite) -> None: ...
    def Speak(self, fragment: Set(TextFragment), waveHeader: IntPtr, site: ITtsEngineSite) -> None: ...


class TtsEventId:
    StartInputStream = 1
    EndInputStream = 2
    VoiceChange = 3
    Bookmark = 4
    WordBoundary = 5
    Phoneme = 6
    SentenceBoundary = 7
    Viseme = 8
    AudioLevel = 9
