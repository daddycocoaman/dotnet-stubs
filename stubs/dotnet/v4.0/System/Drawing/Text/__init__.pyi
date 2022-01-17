from typing import Tuple, Set, Iterable, List


class FontCollection(Object):
    def Dispose(self) -> None: ...
    @property
    def Families(self) -> Set(FontFamily): ...


class GenericFontFamilies:
    Serif = 0
    SansSerif = 1
    Monospace = 2


class HotkeyPrefix:
    #None = 0
    Show = 1
    Hide = 2


class InstalledFontCollection(FontCollection):
    def __init__(self): ...


class PrivateFontCollection(FontCollection):
    def __init__(self): ...
    def AddFontFile(self, filename: str) -> None: ...
    def AddMemoryFont(self, memory: IntPtr, length: int) -> None: ...


class TextRenderingHint:
    SystemDefault = 0
    SingleBitPerPixelGridFit = 1
    SingleBitPerPixel = 2
    AntiAliasGridFit = 3
    AntiAlias = 4
    ClearTypeGridFit = 5
