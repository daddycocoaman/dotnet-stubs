__all__ = ['Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration']
from typing import Tuple, Set, Iterable, List


class SendMessageRecord(CustomTrackingRecord):
    def __init__(self, name: str): ...
    @property
    def E2EActivityId(self) -> Guid: ...
    @E2EActivityId.setter
    def E2EActivityId(self, value: Guid) -> None: ...
