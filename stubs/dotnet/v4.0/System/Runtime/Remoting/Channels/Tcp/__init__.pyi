from typing import Tuple, Set, Iterable, List


class TcpServerChannel(Object):
    @overload
    def __init__(self, port: int): ...
    @overload
    def __init__(self, name: str, port: int): ...
    @overload
    def __init__(self, properties: IDictionary, sinkProvider: IServerChannelSinkProvider): ...
    @overload
    def __init__(self, name: str, port: int, sinkProvider: IServerChannelSinkProvider): ...
    @overload
    def __init__(self, properties: IDictionary, sinkProvider: IServerChannelSinkProvider, authorizeCallback: IAuthorizeRemotingConnection): ...
    @property
    def ChannelData(self) -> Object: ...
    @property
    def ChannelName(self) -> str: ...
    @property
    def ChannelPriority(self) -> int: ...
    @property
    def IsSecured(self) -> bool: ...
    def GetChannelUri(self) -> str: ...
    def GetUrlsForUri(self, objectUri: str) -> Set(str): ...
    def Parse(self, url: str) -> Tuple[str, str]: ...
    @IsSecured.setter
    def IsSecured(self, value: bool) -> None: ...
    def StartListening(self, data: Object) -> None: ...
    def StopListening(self, data: Object) -> None: ...
