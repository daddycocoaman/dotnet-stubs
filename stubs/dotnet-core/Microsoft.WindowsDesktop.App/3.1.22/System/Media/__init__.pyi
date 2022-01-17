from typing import Tuple, Set, Iterable, List


class SoundPlayer(Component):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, soundLocation: str): ...
    @overload
    def __init__(self, stream: Stream): ...
    def add_LoadCompleted(self, value: AsyncCompletedEventHandler) -> None: ...
    def add_SoundLocationChanged(self, value: EventHandler) -> None: ...
    def add_StreamChanged(self, value: EventHandler) -> None: ...
    @property
    def IsLoadCompleted(self) -> bool: ...
    @property
    def LoadTimeout(self) -> int: ...
    @property
    def SoundLocation(self) -> str: ...
    @property
    def Stream(self) -> Stream: ...
    @property
    def Tag(self) -> Object: ...
    def Load(self) -> None: ...
    def LoadAsync(self) -> None: ...
    def Play(self) -> None: ...
    def PlayLooping(self) -> None: ...
    def PlaySync(self) -> None: ...
    def remove_LoadCompleted(self, value: AsyncCompletedEventHandler) -> None: ...
    def remove_SoundLocationChanged(self, value: EventHandler) -> None: ...
    def remove_StreamChanged(self, value: EventHandler) -> None: ...
    @LoadTimeout.setter
    def LoadTimeout(self, value: int) -> None: ...
    @SoundLocation.setter
    def SoundLocation(self, value: str) -> None: ...
    @Stream.setter
    def Stream(self, value: Stream) -> None: ...
    @Tag.setter
    def Tag(self, value: Object) -> None: ...
    def Stop(self) -> None: ...


class SystemSound(Object):
    def Play(self) -> None: ...


class SystemSounds(Object):
    @property
    def Asterisk() -> SystemSound: ...
    @property
    def Beep() -> SystemSound: ...
    @property
    def Exclamation() -> SystemSound: ...
    @property
    def Hand() -> SystemSound: ...
    @property
    def Question() -> SystemSound: ...
