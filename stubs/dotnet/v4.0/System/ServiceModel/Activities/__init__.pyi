__all__ = ['Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Configuration','Description','Description','Description','Description','Description','Description','Description','Description','Tracking','Tracking']
from typing import Tuple, Set, Iterable, List


class SendSettings(Object):
    def __init__(self): ...
    @property
    def Endpoint(self) -> Endpoint: ...
    @property
    def EndpointAddress(self) -> Uri: ...
    @property
    def EndpointConfigurationName(self) -> str: ...
    @property
    def IsOneWay(self) -> bool: ...
    @property
    def OwnerDisplayName(self) -> str: ...
    @property
    def ProtectionLevel(self) -> Nullable: ...
    @property
    def RequirePersistBeforeSend(self) -> bool: ...
    @property
    def TokenImpersonationLevel(self) -> TokenImpersonationLevel: ...
    @Endpoint.setter
    def Endpoint(self, value: Endpoint) -> None: ...
    @EndpointAddress.setter
    def EndpointAddress(self, value: Uri) -> None: ...
    @EndpointConfigurationName.setter
    def EndpointConfigurationName(self, value: str) -> None: ...
    @IsOneWay.setter
    def IsOneWay(self, value: bool) -> None: ...
    @OwnerDisplayName.setter
    def OwnerDisplayName(self, value: str) -> None: ...
    @ProtectionLevel.setter
    def ProtectionLevel(self, value: Nullable) -> None: ...
    @RequirePersistBeforeSend.setter
    def RequirePersistBeforeSend(self, value: bool) -> None: ...
    @TokenImpersonationLevel.setter
    def TokenImpersonationLevel(self, value: TokenImpersonationLevel) -> None: ...