from typing import Tuple, Set, Iterable, List


class ResumeJob(PSRemotingActivity):
    def __init__(self): ...
    @property
    def Filter(self) -> InArgument: ...
    @property
    def InstanceId(self) -> InArgument: ...
    @property
    def Job(self) -> InArgument: ...
    @property
    def JobId(self) -> InArgument: ...
    @property
    def Name(self) -> InArgument: ...
    @property
    def PSCommandName(self) -> str: ...
    @property
    def State(self) -> InArgument: ...
    @property
    def Wait(self) -> InArgument: ...
    @Filter.setter
    def Filter(self, value: InArgument) -> None: ...
    @InstanceId.setter
    def InstanceId(self, value: InArgument) -> None: ...
    @Job.setter
    def Job(self, value: InArgument) -> None: ...
    @JobId.setter
    def JobId(self, value: InArgument) -> None: ...
    @Name.setter
    def Name(self, value: InArgument) -> None: ...
    @State.setter
    def State(self, value: InArgument) -> None: ...
    @Wait.setter
    def Wait(self, value: InArgument) -> None: ...