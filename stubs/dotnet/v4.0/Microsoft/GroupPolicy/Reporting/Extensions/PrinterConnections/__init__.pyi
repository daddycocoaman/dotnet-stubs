from typing import Tuple, Set, Iterable, List


class PrinterConnectionSettings(GPOExtension):
    def __init__(self): ...
    @property
    def PrinterConnection(self) -> ArrayList: ...
    def Initialize(self, context: ReportingContext) -> None: ...
    @PrinterConnection.setter
    def PrinterConnection(self, value: ArrayList) -> None: ...
