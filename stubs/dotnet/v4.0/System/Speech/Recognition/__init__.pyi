__all__ = ['SrgsGrammar']
from typing import Tuple, Set, Iterable, List


class AudioLevelUpdatedEventArgs(EventArgs):
    @property
    def AudioLevel(self) -> int: ...


class AudioSignalProblem:
    #None = 0
    TooNoisy = 1
    NoSignal = 2
    TooLoud = 3
    TooSoft = 4
    TooFast = 5
    TooSlow = 6


class AudioSignalProblemOccurredEventArgs(EventArgs):
    @property
    def AudioLevel(self) -> int: ...
    @property
    def AudioPosition(self) -> TimeSpan: ...
    @property
    def AudioSignalProblem(self) -> AudioSignalProblem: ...
    @property
    def RecognizerAudioPosition(self) -> TimeSpan: ...


class AudioState:
    Stopped = 0
    Silence = 1
    Speech = 2


class AudioStateChangedEventArgs(EventArgs):
    @property
    def AudioState(self) -> AudioState: ...


class Choices(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, phrases: Set(str)): ...
    @overload
    def __init__(self, alternateChoices: Set(GrammarBuilder)): ...
    @overload
    def Add(self, phrases: Set(str)) -> None: ...
    @overload
    def Add(self, alternateChoices: Set(GrammarBuilder)) -> None: ...
    def ToGrammarBuilder(self) -> GrammarBuilder: ...


class DictationGrammar(Grammar):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, topic: str): ...
    def SetDictationContext(self, precedingText: str, subsequentText: str) -> None: ...


class DisplayAttributes:
    #None = 0
    ZeroTrailingSpaces = 2
    OneTrailingSpace = 4
    TwoTrailingSpaces = 8
    ConsumeLeadingSpaces = 16


class EmulateRecognizeCompletedEventArgs(AsyncCompletedEventArgs):
    @property
    def Result(self) -> RecognitionResult: ...


class Grammar(Object):
    @overload
    def __init__(self, path: str): ...
    @overload
    def __init__(self, srgsDocument: SrgsDocument): ...
    @overload
    def __init__(self, stream: Stream): ...
    @overload
    def __init__(self, builder: GrammarBuilder): ...
    @overload
    def __init__(self, path: str, ruleName: str): ...
    @overload
    def __init__(self, srgsDocument: SrgsDocument, ruleName: str): ...
    @overload
    def __init__(self, stream: Stream, ruleName: str): ...
    @overload
    def __init__(self, path: str, ruleName: str, parameters: Set(Object)): ...
    @overload
    def __init__(self, srgsDocument: SrgsDocument, ruleName: str, parameters: Set(Object)): ...
    @overload
    def __init__(self, srgsDocument: SrgsDocument, ruleName: str, baseUri: Uri): ...
    @overload
    def __init__(self, stream: Stream, ruleName: str, parameters: Set(Object)): ...
    @overload
    def __init__(self, stream: Stream, ruleName: str, baseUri: Uri): ...
    @overload
    def __init__(self, srgsDocument: SrgsDocument, ruleName: str, baseUri: Uri, parameters: Set(Object)): ...
    @overload
    def __init__(self, stream: Stream, ruleName: str, baseUri: Uri, parameters: Set(Object)): ...
    def add_SpeechRecognized(self, value: EventHandler) -> None: ...
    @property
    def Enabled(self) -> bool: ...
    @property
    def Loaded(self) -> bool: ...
    @property
    def Name(self) -> str: ...
    @property
    def Priority(self) -> int: ...
    @property
    def RuleName(self) -> str: ...
    @property
    def Weight(self) -> Single: ...
    def LoadLocalizedGrammarFromType(type: Type, onInitParameters: Set(Object)) -> Grammar: ...
    def remove_SpeechRecognized(self, value: EventHandler) -> None: ...
    @Enabled.setter
    def Enabled(self, value: bool) -> None: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    @Priority.setter
    def Priority(self, value: int) -> None: ...
    @Weight.setter
    def Weight(self, value: Single) -> None: ...


class GrammarBuilder(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, phrase: str): ...
    @overload
    def __init__(self, alternateChoices: Choices): ...
    @overload
    def __init__(self, key: SemanticResultKey): ...
    @overload
    def __init__(self, value: SemanticResultValue): ...
    @overload
    def __init__(self, phrase: str, subsetMatchingCriteria: SubsetMatchingMode): ...
    @overload
    def __init__(self, phrase: str, minRepeat: int, maxRepeat: int): ...
    @overload
    def __init__(self, builder: GrammarBuilder, minRepeat: int, maxRepeat: int): ...
    @overload
    def Add(builder: GrammarBuilder, choices: Choices) -> GrammarBuilder: ...
    @overload
    def Add(choices: Choices, builder: GrammarBuilder) -> GrammarBuilder: ...
    @overload
    def Add(builder1: GrammarBuilder, builder2: GrammarBuilder) -> GrammarBuilder: ...
    @overload
    def Add(builder: GrammarBuilder, phrase: str) -> GrammarBuilder: ...
    @overload
    def Add(phrase: str, builder: GrammarBuilder) -> GrammarBuilder: ...
    @overload
    def Append(self, value: SemanticResultValue) -> None: ...
    @overload
    def Append(self, phrase: str) -> None: ...
    @overload
    def Append(self, builder: GrammarBuilder) -> None: ...
    @overload
    def Append(self, alternateChoices: Choices) -> None: ...
    @overload
    def Append(self, key: SemanticResultKey) -> None: ...
    @overload
    def Append(self, phrase: str, subsetMatchingCriteria: SubsetMatchingMode) -> None: ...
    @overload
    def Append(self, builder: GrammarBuilder, minRepeat: int, maxRepeat: int) -> None: ...
    @overload
    def Append(self, phrase: str, minRepeat: int, maxRepeat: int) -> None: ...
    @overload
    def AppendDictation(self) -> None: ...
    @overload
    def AppendDictation(self, category: str) -> None: ...
    @overload
    def AppendRuleReference(self, path: str) -> None: ...
    @overload
    def AppendRuleReference(self, path: str, rule: str) -> None: ...
    def AppendWildcard(self) -> None: ...
    @property
    def Culture(self) -> CultureInfo: ...
    @property
    def DebugShowPhrases(self) -> str: ...
    @overload
    def op_Addition(builder1: GrammarBuilder, builder2: GrammarBuilder) -> GrammarBuilder: ...
    @overload
    def op_Addition(phrase: str, builder: GrammarBuilder) -> GrammarBuilder: ...
    @overload
    def op_Addition(choices: Choices, builder: GrammarBuilder) -> GrammarBuilder: ...
    @overload
    def op_Addition(builder: GrammarBuilder, phrase: str) -> GrammarBuilder: ...
    @overload
    def op_Addition(builder: GrammarBuilder, choices: Choices) -> GrammarBuilder: ...
    @overload
    def op_Implicit(phrase: str) -> GrammarBuilder: ...
    @overload
    def op_Implicit(choices: Choices) -> GrammarBuilder: ...
    @overload
    def op_Implicit(semanticKey: SemanticResultKey) -> GrammarBuilder: ...
    @overload
    def op_Implicit(semanticValue: SemanticResultValue) -> GrammarBuilder: ...
    @Culture.setter
    def Culture(self, value: CultureInfo) -> None: ...


class LoadGrammarCompletedEventArgs(AsyncCompletedEventArgs):
    @property
    def Grammar(self) -> Grammar: ...


class RecognitionEventArgs(EventArgs):
    @property
    def Result(self) -> RecognitionResult: ...


class RecognitionResult(RecognizedPhrase):
    @property
    def Alternates(self) -> ReadOnlyCollection: ...
    @property
    def Audio(self) -> RecognizedAudio: ...
    def GetAudioForWordRange(self, firstWord: RecognizedWordUnit, lastWord: RecognizedWordUnit) -> RecognizedAudio: ...


class RecognizeCompletedEventArgs(AsyncCompletedEventArgs):
    @property
    def AudioPosition(self) -> TimeSpan: ...
    @property
    def BabbleTimeout(self) -> bool: ...
    @property
    def InitialSilenceTimeout(self) -> bool: ...
    @property
    def InputStreamEnded(self) -> bool: ...
    @property
    def Result(self) -> RecognitionResult: ...


class RecognizedAudio(Object):
    @property
    def AudioPosition(self) -> TimeSpan: ...
    @property
    def Duration(self) -> TimeSpan: ...
    @property
    def Format(self) -> SpeechAudioFormatInfo: ...
    @property
    def StartTime(self) -> DateTime: ...
    def GetRange(self, audioPosition: TimeSpan, duration: TimeSpan) -> RecognizedAudio: ...
    def WriteToAudioStream(self, outputStream: Stream) -> None: ...
    def WriteToWaveStream(self, outputStream: Stream) -> None: ...


class RecognizedPhrase(Object):
    def ConstructSmlFromSemantics(self) -> IXPathNavigable: ...
    @property
    def Confidence(self) -> Single: ...
    @property
    def Grammar(self) -> Grammar: ...
    @property
    def HomophoneGroupId(self) -> int: ...
    @property
    def Homophones(self) -> ReadOnlyCollection: ...
    @property
    def ReplacementWordUnits(self) -> Collection: ...
    @property
    def Semantics(self) -> SemanticValue: ...
    @property
    def Text(self) -> str: ...
    @property
    def Words(self) -> ReadOnlyCollection: ...


class RecognizedWordUnit(Object):
    def __init__(self, text: str, confidence: Single, pronunciation: str, lexicalForm: str, displayAttributes: DisplayAttributes, audioPosition: TimeSpan, audioDuration: TimeSpan): ...
    @property
    def Confidence(self) -> Single: ...
    @property
    def DisplayAttributes(self) -> DisplayAttributes: ...
    @property
    def LexicalForm(self) -> str: ...
    @property
    def Pronunciation(self) -> str: ...
    @property
    def Text(self) -> str: ...


class RecognizeMode:
    Single = 0
    Multiple = 1


class RecognizerInfo(Object):
    def Dispose(self) -> None: ...
    @property
    def AdditionalInfo(self) -> IDictionary: ...
    @property
    def Culture(self) -> CultureInfo: ...
    @property
    def Description(self) -> str: ...
    @property
    def Id(self) -> str: ...
    @property
    def Name(self) -> str: ...
    @property
    def SupportedAudioFormats(self) -> ReadOnlyCollection: ...


class RecognizerState:
    Stopped = 0
    Listening = 1


class RecognizerUpdateReachedEventArgs(EventArgs):
    @property
    def AudioPosition(self) -> TimeSpan: ...
    @property
    def UserToken(self) -> Object: ...


class ReplacementText(Object):
    @property
    def CountOfWords(self) -> int: ...
    @property
    def DisplayAttributes(self) -> DisplayAttributes: ...
    @property
    def FirstWordIndex(self) -> int: ...
    @property
    def Text(self) -> str: ...


class SemanticResultKey(Object):
    @overload
    def __init__(self, semanticResultKey: str, phrases: Set(str)): ...
    @overload
    def __init__(self, semanticResultKey: str, builders: Set(GrammarBuilder)): ...
    def ToGrammarBuilder(self) -> GrammarBuilder: ...


class SemanticResultValue(Object):
    @overload
    def __init__(self, value: Object): ...
    @overload
    def __init__(self, phrase: str, value: Object): ...
    @overload
    def __init__(self, builder: GrammarBuilder, value: Object): ...
    def ToGrammarBuilder(self) -> GrammarBuilder: ...


class SemanticValue(Object):
    @overload
    def __init__(self, value: Object): ...
    @overload
    def __init__(self, keyName: str, value: Object, confidence: Single): ...
    def Contains(self, item: KeyValuePair) -> bool: ...
    def ContainsKey(self, key: str) -> bool: ...
    def Equals(self, obj: Object) -> bool: ...
    @property
    def Confidence(self) -> Single: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, key: str) -> SemanticValue: ...
    @property
    def Value(self) -> Object: ...
    def GetHashCode(self) -> int: ...
    @Item.setter
    def Item(self, key: str, value: SemanticValue) -> None: ...


class SpeechDetectedEventArgs(EventArgs):
    @property
    def AudioPosition(self) -> TimeSpan: ...


class SpeechHypothesizedEventArgs(RecognitionEventArgs):
    pass


class SpeechRecognitionEngine(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, culture: CultureInfo): ...
    @overload
    def __init__(self, recognizerId: str): ...
    @overload
    def __init__(self, recognizerInfo: RecognizerInfo): ...
    def add_AudioLevelUpdated(self, value: EventHandler) -> None: ...
    def add_AudioSignalProblemOccurred(self, value: EventHandler) -> None: ...
    def add_AudioStateChanged(self, value: EventHandler) -> None: ...
    def add_EmulateRecognizeCompleted(self, value: EventHandler) -> None: ...
    def add_LoadGrammarCompleted(self, value: EventHandler) -> None: ...
    def add_RecognizeCompleted(self, value: EventHandler) -> None: ...
    def add_RecognizerUpdateReached(self, value: EventHandler) -> None: ...
    def add_SpeechDetected(self, value: EventHandler) -> None: ...
    def add_SpeechHypothesized(self, value: EventHandler) -> None: ...
    def add_SpeechRecognitionRejected(self, value: EventHandler) -> None: ...
    def add_SpeechRecognized(self, value: EventHandler) -> None: ...
    def Dispose(self) -> None: ...
    @overload
    def EmulateRecognize(self, inputText: str) -> RecognitionResult: ...
    @overload
    def EmulateRecognize(self, wordUnits: Set(RecognizedWordUnit), compareOptions: CompareOptions) -> RecognitionResult: ...
    @overload
    def EmulateRecognize(self, inputText: str, compareOptions: CompareOptions) -> RecognitionResult: ...
    @overload
    def EmulateRecognizeAsync(self, inputText: str) -> None: ...
    @overload
    def EmulateRecognizeAsync(self, wordUnits: Set(RecognizedWordUnit), compareOptions: CompareOptions) -> None: ...
    @overload
    def EmulateRecognizeAsync(self, inputText: str, compareOptions: CompareOptions) -> None: ...
    @property
    def AudioFormat(self) -> SpeechAudioFormatInfo: ...
    @property
    def AudioLevel(self) -> int: ...
    @property
    def AudioPosition(self) -> TimeSpan: ...
    @property
    def AudioState(self) -> AudioState: ...
    @property
    def BabbleTimeout(self) -> TimeSpan: ...
    @property
    def EndSilenceTimeout(self) -> TimeSpan: ...
    @property
    def EndSilenceTimeoutAmbiguous(self) -> TimeSpan: ...
    @property
    def Grammars(self) -> ReadOnlyCollection: ...
    @property
    def InitialSilenceTimeout(self) -> TimeSpan: ...
    @property
    def MaxAlternates(self) -> int: ...
    @property
    def RecognizerAudioPosition(self) -> TimeSpan: ...
    @property
    def RecognizerInfo(self) -> RecognizerInfo: ...
    def InstalledRecognizers() -> ReadOnlyCollection: ...
    def LoadGrammar(self, grammar: Grammar) -> None: ...
    def LoadGrammarAsync(self, grammar: Grammar) -> None: ...
    def QueryRecognizerSetting(self, settingName: str) -> Object: ...
    @overload
    def Recognize(self) -> RecognitionResult: ...
    @overload
    def Recognize(self, initialSilenceTimeout: TimeSpan) -> RecognitionResult: ...
    @overload
    def RecognizeAsync(self) -> None: ...
    @overload
    def RecognizeAsync(self, mode: RecognizeMode) -> None: ...
    def RecognizeAsyncCancel(self) -> None: ...
    def RecognizeAsyncStop(self) -> None: ...
    def remove_AudioLevelUpdated(self, value: EventHandler) -> None: ...
    def remove_AudioSignalProblemOccurred(self, value: EventHandler) -> None: ...
    def remove_AudioStateChanged(self, value: EventHandler) -> None: ...
    def remove_EmulateRecognizeCompleted(self, value: EventHandler) -> None: ...
    def remove_LoadGrammarCompleted(self, value: EventHandler) -> None: ...
    def remove_RecognizeCompleted(self, value: EventHandler) -> None: ...
    def remove_RecognizerUpdateReached(self, value: EventHandler) -> None: ...
    def remove_SpeechDetected(self, value: EventHandler) -> None: ...
    def remove_SpeechHypothesized(self, value: EventHandler) -> None: ...
    def remove_SpeechRecognitionRejected(self, value: EventHandler) -> None: ...
    def remove_SpeechRecognized(self, value: EventHandler) -> None: ...
    @overload
    def RequestRecognizerUpdate(self) -> None: ...
    @overload
    def RequestRecognizerUpdate(self, userToken: Object) -> None: ...
    @overload
    def RequestRecognizerUpdate(self, userToken: Object, audioPositionAheadToRaiseUpdate: TimeSpan) -> None: ...
    @BabbleTimeout.setter
    def BabbleTimeout(self, value: TimeSpan) -> None: ...
    @EndSilenceTimeout.setter
    def EndSilenceTimeout(self, value: TimeSpan) -> None: ...
    @EndSilenceTimeoutAmbiguous.setter
    def EndSilenceTimeoutAmbiguous(self, value: TimeSpan) -> None: ...
    @InitialSilenceTimeout.setter
    def InitialSilenceTimeout(self, value: TimeSpan) -> None: ...
    @MaxAlternates.setter
    def MaxAlternates(self, value: int) -> None: ...
    def SetInputToAudioStream(self, audioSource: Stream, audioFormat: SpeechAudioFormatInfo) -> None: ...
    def SetInputToDefaultAudioDevice(self) -> None: ...
    def SetInputToNull(self) -> None: ...
    def SetInputToWaveFile(self, path: str) -> None: ...
    def SetInputToWaveStream(self, audioSource: Stream) -> None: ...
    def UnloadAllGrammars(self) -> None: ...
    def UnloadGrammar(self, grammar: Grammar) -> None: ...
    @overload
    def UpdateRecognizerSetting(self, settingName: str, updatedValue: int) -> None: ...
    @overload
    def UpdateRecognizerSetting(self, settingName: str, updatedValue: str) -> None: ...


class SpeechRecognitionRejectedEventArgs(RecognitionEventArgs):
    pass


class SpeechRecognizedEventArgs(RecognitionEventArgs):
    pass


class SpeechRecognizer(Object):
    def __init__(self): ...
    def add_AudioLevelUpdated(self, value: EventHandler) -> None: ...
    def add_AudioSignalProblemOccurred(self, value: EventHandler) -> None: ...
    def add_AudioStateChanged(self, value: EventHandler) -> None: ...
    def add_EmulateRecognizeCompleted(self, value: EventHandler) -> None: ...
    def add_LoadGrammarCompleted(self, value: EventHandler) -> None: ...
    def add_RecognizerUpdateReached(self, value: EventHandler) -> None: ...
    def add_SpeechDetected(self, value: EventHandler) -> None: ...
    def add_SpeechHypothesized(self, value: EventHandler) -> None: ...
    def add_SpeechRecognitionRejected(self, value: EventHandler) -> None: ...
    def add_SpeechRecognized(self, value: EventHandler) -> None: ...
    def add_StateChanged(self, value: EventHandler) -> None: ...
    def Dispose(self) -> None: ...
    @overload
    def EmulateRecognize(self, inputText: str) -> RecognitionResult: ...
    @overload
    def EmulateRecognize(self, wordUnits: Set(RecognizedWordUnit), compareOptions: CompareOptions) -> RecognitionResult: ...
    @overload
    def EmulateRecognize(self, inputText: str, compareOptions: CompareOptions) -> RecognitionResult: ...
    @overload
    def EmulateRecognizeAsync(self, inputText: str) -> None: ...
    @overload
    def EmulateRecognizeAsync(self, wordUnits: Set(RecognizedWordUnit), compareOptions: CompareOptions) -> None: ...
    @overload
    def EmulateRecognizeAsync(self, inputText: str, compareOptions: CompareOptions) -> None: ...
    @property
    def AudioFormat(self) -> SpeechAudioFormatInfo: ...
    @property
    def AudioLevel(self) -> int: ...
    @property
    def AudioPosition(self) -> TimeSpan: ...
    @property
    def AudioState(self) -> AudioState: ...
    @property
    def Enabled(self) -> bool: ...
    @property
    def Grammars(self) -> ReadOnlyCollection: ...
    @property
    def MaxAlternates(self) -> int: ...
    @property
    def PauseRecognizerOnRecognition(self) -> bool: ...
    @property
    def RecognizerAudioPosition(self) -> TimeSpan: ...
    @property
    def RecognizerInfo(self) -> RecognizerInfo: ...
    @property
    def State(self) -> RecognizerState: ...
    def LoadGrammar(self, grammar: Grammar) -> None: ...
    def LoadGrammarAsync(self, grammar: Grammar) -> None: ...
    def remove_AudioLevelUpdated(self, value: EventHandler) -> None: ...
    def remove_AudioSignalProblemOccurred(self, value: EventHandler) -> None: ...
    def remove_AudioStateChanged(self, value: EventHandler) -> None: ...
    def remove_EmulateRecognizeCompleted(self, value: EventHandler) -> None: ...
    def remove_LoadGrammarCompleted(self, value: EventHandler) -> None: ...
    def remove_RecognizerUpdateReached(self, value: EventHandler) -> None: ...
    def remove_SpeechDetected(self, value: EventHandler) -> None: ...
    def remove_SpeechHypothesized(self, value: EventHandler) -> None: ...
    def remove_SpeechRecognitionRejected(self, value: EventHandler) -> None: ...
    def remove_SpeechRecognized(self, value: EventHandler) -> None: ...
    def remove_StateChanged(self, value: EventHandler) -> None: ...
    @overload
    def RequestRecognizerUpdate(self) -> None: ...
    @overload
    def RequestRecognizerUpdate(self, userToken: Object) -> None: ...
    @overload
    def RequestRecognizerUpdate(self, userToken: Object, audioPositionAheadToRaiseUpdate: TimeSpan) -> None: ...
    @Enabled.setter
    def Enabled(self, value: bool) -> None: ...
    @MaxAlternates.setter
    def MaxAlternates(self, value: int) -> None: ...
    @PauseRecognizerOnRecognition.setter
    def PauseRecognizerOnRecognition(self, value: bool) -> None: ...
    def UnloadAllGrammars(self) -> None: ...
    def UnloadGrammar(self, grammar: Grammar) -> None: ...


class SpeechUI(Object):
    def SendTextFeedback(result: RecognitionResult, feedback: str, isSuccessfulAction: bool) -> bool: ...


class StateChangedEventArgs(EventArgs):
    @property
    def RecognizerState(self) -> RecognizerState: ...


class SubsetMatchingMode:
    Subsequence = 0
    OrderedSubset = 1
    SubsequenceContentRequired = 2
    OrderedSubsetContentRequired = 3
