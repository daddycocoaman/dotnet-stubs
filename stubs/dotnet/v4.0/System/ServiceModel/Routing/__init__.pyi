__all__ = ['Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration']
from typing import Tuple, Set, Iterable, List


class SoapProcessingBehavior(Object):
    def __init__(self): ...
    def AddBindingParameters(self, endpoint: ServiceEndpoint, bindingParameters: BindingParameterCollection) -> None: ...
    def ApplyClientBehavior(self, endpoint: ServiceEndpoint, clientRuntime: ClientRuntime) -> None: ...
    def ApplyDispatchBehavior(self, endpoint: ServiceEndpoint, endpointDispatcher: EndpointDispatcher) -> None: ...
    @property
    def ProcessMessages(self) -> bool: ...
    @ProcessMessages.setter
    def ProcessMessages(self, value: bool) -> None: ...
    def Validate(self, endpoint: ServiceEndpoint) -> None: ...