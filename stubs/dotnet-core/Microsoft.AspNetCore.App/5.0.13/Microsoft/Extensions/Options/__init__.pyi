from typing import Tuple, Set, Iterable, List




































class Options:
    def Create(options: TOptions) -> IOptions: ...












class OptionsMonitorExtensions:
    def OnChange(monitor: IOptionsMonitor, listener: Action) -> IDisposable: ...


class OptionsValidationException:
    def __init__(self, optionsName: str, optionsType: Type, failureMessages: Iterable[str]): ...
    @property
    def Failures(self) -> Iterable[str]: ...
    @property
    def Message(self) -> str: ...
    @property
    def OptionsName(self) -> str: ...
    @property
    def OptionsType(self) -> Type: ...




























class ValidateOptionsResult:
    def __init__(self): ...
    @overload
    def Fail(failureMessage: str) -> ValidateOptionsResult: ...
    @overload
    def Fail(failures: Iterable[str]) -> ValidateOptionsResult: ...
    @property
    def Failed(self) -> bool: ...
    @property
    def FailureMessage(self) -> str: ...
    @property
    def Failures(self) -> Iterable[str]: ...
    @property
    def Skipped(self) -> bool: ...
    @property
    def Succeeded(self) -> bool: ...
