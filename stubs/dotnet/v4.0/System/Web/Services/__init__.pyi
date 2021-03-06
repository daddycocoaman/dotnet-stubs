__all__ = ['Configuration','Description','Discovery','Protocols']
from typing import Tuple, Set, Iterable, List


class WebMethodAttribute(Attribute):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, enableSession: bool): ...
    @overload
    def __init__(self, enableSession: bool, transactionOption: TransactionOption): ...
    @overload
    def __init__(self, enableSession: bool, transactionOption: TransactionOption, cacheDuration: int): ...
    @overload
    def __init__(self, enableSession: bool, transactionOption: TransactionOption, cacheDuration: int, bufferResponse: bool): ...
    @property
    def BufferResponse(self) -> bool: ...
    @property
    def CacheDuration(self) -> int: ...
    @property
    def Description(self) -> str: ...
    @property
    def EnableSession(self) -> bool: ...
    @property
    def MessageName(self) -> str: ...
    @property
    def TransactionOption(self) -> TransactionOption: ...
    @BufferResponse.setter
    def BufferResponse(self, value: bool) -> None: ...
    @CacheDuration.setter
    def CacheDuration(self, value: int) -> None: ...
    @Description.setter
    def Description(self, value: str) -> None: ...
    @EnableSession.setter
    def EnableSession(self, value: bool) -> None: ...
    @MessageName.setter
    def MessageName(self, value: str) -> None: ...
    @TransactionOption.setter
    def TransactionOption(self, value: TransactionOption) -> None: ...


class WebService(MarshalByValueComponent):
    def __init__(self): ...
    @property
    def Application(self) -> HttpApplicationState: ...
    @property
    def Context(self) -> HttpContext: ...
    @property
    def Server(self) -> HttpServerUtility: ...
    @property
    def Session(self) -> HttpSessionState: ...
    @property
    def SoapVersion(self) -> SoapProtocolVersion: ...
    @property
    def User(self) -> IPrincipal: ...


class WebServiceAttribute(Attribute):
    def __init__(self): ...
    @property
    def Description(self) -> str: ...
    @property
    def Name(self) -> str: ...
    @property
    def Namespace(self) -> str: ...
    @Description.setter
    def Description(self, value: str) -> None: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    @Namespace.setter
    def Namespace(self, value: str) -> None: ...


class WebServiceBindingAttribute(Attribute):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, name: str): ...
    @overload
    def __init__(self, name: str, ns: str): ...
    @overload
    def __init__(self, name: str, ns: str, location: str): ...
    @property
    def ConformsTo(self) -> WsiProfiles: ...
    @property
    def EmitConformanceClaims(self) -> bool: ...
    @property
    def Location(self) -> str: ...
    @property
    def Name(self) -> str: ...
    @property
    def Namespace(self) -> str: ...
    @ConformsTo.setter
    def ConformsTo(self, value: WsiProfiles) -> None: ...
    @EmitConformanceClaims.setter
    def EmitConformanceClaims(self, value: bool) -> None: ...
    @Location.setter
    def Location(self, value: str) -> None: ...
    @Name.setter
    def Name(self, value: str) -> None: ...
    @Namespace.setter
    def Namespace(self, value: str) -> None: ...


class WsiProfiles:
    #None = 0
    BasicProfile1_1 = 1
