__all__ = ['Commands','Commands']
from typing import Tuple, Set, Iterable, List


class DiagCallback:
    def __init__(self, ui: PSHostUserInterface): ...
    def AddPackage(self, package: DiagPack) -> None: ...
    def ClearConsole(self) -> None: ...
    def HandleInteraction(self, interaction: DiagInteraction, generatingAnswerFile: bool) -> Tuple[Set(str)]: ...
    def Interact(self, interactionXml: str) -> Tuple[Set(str)]: ...
    def Progress(self, activity: str, status: str, progressValue: int, color: int) -> None: ...
    def Telemetry(self, Property: str, Value: str) -> None: ...