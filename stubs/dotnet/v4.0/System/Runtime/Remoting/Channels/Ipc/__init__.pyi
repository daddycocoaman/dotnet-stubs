from typing import Tuple, Set, Iterable, List


class IpcClientChannel(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, name: str, sinkProvider: IClientChannelSinkProvider): ...
    @overload
    def __init__(self, properties: IDictionary, sinkProvider: IClientChannelSinkProvider): ...
    def CreateMessageSink(self, url: str, remoteChannelData: Object) -> Tuple[IMessageSink, str]: ...
    @property
    def ChannelName(self) -> str: ...
    @property
    def ChannelPriority(self) -> int: ...
    @property
    def IsSecured(self) -> bool: ...
    def Parse(self, url: str) -> Tuple[str, str]: ...
    @IsSecured.setter
    def IsSecured(self, value: bool) -> None: ...
