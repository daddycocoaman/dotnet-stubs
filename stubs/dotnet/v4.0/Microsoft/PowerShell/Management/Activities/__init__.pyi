from typing import Tuple, Set, Iterable, List


class RestartComputer(PSActivity):
    def __init__(self): ...
    @property
    def DcomAuthentication(self) -> InArgument: ...
    @property
    def Delay(self) -> InArgument: ...
    @property
    def DisableSelfRestart() -> bool: ...
    @property
    def For(self) -> InArgument: ...
    @property
    def Force(self) -> InArgument: ...
    @property
    def Impersonation(self) -> InArgument: ...
    @property
    def Protocol(self) -> InArgument: ...
    @property
    def PSCommandName(self) -> str: ...
    @property
    def PSComputerName(self) -> InArgument: ...
    @property
    def PSCredential(self) -> InArgument: ...
    @property
    def ThrottleLimit(self) -> InArgument: ...
    @property
    def Timeout(self) -> InArgument: ...
    @property
    def Wait(self) -> InArgument: ...
    @property
    def WsmanAuthentication(self) -> InArgument: ...
    @DcomAuthentication.setter
    def DcomAuthentication(self, value: InArgument) -> None: ...
    @Delay.setter
    def Delay(self, value: InArgument) -> None: ...
    @DisableSelfRestart.setter
    def DisableSelfRestart(value: bool) -> None: ...
    @For.setter
    def For(self, value: InArgument) -> None: ...
    @Force.setter
    def Force(self, value: InArgument) -> None: ...
    @Impersonation.setter
    def Impersonation(self, value: InArgument) -> None: ...
    @Protocol.setter
    def Protocol(self, value: InArgument) -> None: ...
    @PSComputerName.setter
    def PSComputerName(self, value: InArgument) -> None: ...
    @PSCredential.setter
    def PSCredential(self, value: InArgument) -> None: ...
    @ThrottleLimit.setter
    def ThrottleLimit(self, value: InArgument) -> None: ...
    @Timeout.setter
    def Timeout(self, value: InArgument) -> None: ...
    @Wait.setter
    def Wait(self, value: InArgument) -> None: ...
    @WsmanAuthentication.setter
    def WsmanAuthentication(self, value: InArgument) -> None: ...