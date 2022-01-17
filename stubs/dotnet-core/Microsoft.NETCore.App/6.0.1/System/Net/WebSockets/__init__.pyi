from typing import Tuple, Set, Iterable, List


class WebSocketReceiveResult(Object):
    @overload
    def __init__(self, count: int, messageType: WebSocketMessageType, endOfMessage: bool): ...
    @overload
    def __init__(self, count: int, messageType: WebSocketMessageType, endOfMessage: bool, closeStatus: Nullable, closeStatusDescription: str): ...
    @property
    def CloseStatus(self) -> Nullable: ...
    @property
    def CloseStatusDescription(self) -> str: ...
    @property
    def Count(self) -> int: ...
    @property
    def EndOfMessage(self) -> bool: ...
    @property
    def MessageType(self) -> WebSocketMessageType: ...