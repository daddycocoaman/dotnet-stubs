from typing import Tuple, Set, Iterable, List


class AudioBitsPerSample:
    Eight = 8
    Sixteen = 16


class AudioChannel:
    Mono = 1
    Stereo = 2


class EncodingFormat:
    Pcm = 1
    ALaw = 6
    ULaw = 7


class SpeechAudioFormatInfo(Object):
    @overload
    def __init__(self, samplesPerSecond: int, bitsPerSample: AudioBitsPerSample, channel: AudioChannel): ...
    @overload
    def __init__(self, encodingFormat: EncodingFormat, samplesPerSecond: int, bitsPerSample: int, channelCount: int, averageBytesPerSecond: int, blockAlign: int, formatSpecificData: Set(Byte)): ...
    def Equals(self, obj: Object) -> bool: ...
    def FormatSpecificData(self) -> Set(Byte): ...
    @property
    def AverageBytesPerSecond(self) -> int: ...
    @property
    def BitsPerSample(self) -> int: ...
    @property
    def BlockAlign(self) -> int: ...
    @property
    def ChannelCount(self) -> int: ...
    @property
    def EncodingFormat(self) -> EncodingFormat: ...
    @property
    def SamplesPerSecond(self) -> int: ...
    def GetHashCode(self) -> int: ...
