__all__ = ['Eventing','Eventing','Eventing','Eventing','PerformanceData','PerformanceData','PerformanceData','PerformanceData','PerformanceData','PerformanceData']
from typing import Tuple, Set, Iterable, List


class UnescapedXmlDiagnosticData(Object):
    def __init__(self, xmlPayload: str): ...
    @property
    def UnescapedXml(self) -> str: ...
    @UnescapedXml.setter
    def UnescapedXml(self, value: str) -> None: ...
    def ToString(self) -> str: ...