__all__ = ['Tokens','Tokens','Tokens','Tokens','Tokens','Tokens','Tokens','Tokens','Tokens','Tokens','Tokens','Tokens','Tokens','Tokens','Tokens','Tokens','Tokens','Tokens','Tokens','Tokens','Tokens','Tokens','Tokens','Tokens','Tokens','Tokens','Tokens','Tokens']
from typing import Tuple, Set, Iterable, List


class WSTrustServiceHost(ServiceHost):
    @overload
    def __init__(self, securityTokenServiceConfiguration: SecurityTokenServiceConfiguration, baseAddresses: Set(Uri)): ...
    @overload
    def __init__(self, serviceContract: WSTrustServiceContract, baseAddresses: Set(Uri)): ...
    @property
    def SecurityTokenServiceConfiguration(self) -> SecurityTokenServiceConfiguration: ...
    @property
    def ServiceContract(self) -> WSTrustServiceContract: ...
