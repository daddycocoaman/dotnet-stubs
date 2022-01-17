from typing import Tuple, Set, Iterable, List


class ValidationSettings(Object):
    def __init__(self): ...
    @property
    def AdditionalConstraints(self) -> IDictionary: ...
    @property
    def CancellationToken(self) -> CancellationToken: ...
    @property
    def Environment(self) -> LocationReferenceEnvironment: ...
    @property
    def OnlyUseAdditionalConstraints(self) -> bool: ...
    @property
    def PrepareForRuntime(self) -> bool: ...
    @property
    def SingleLevel(self) -> bool: ...
    @property
    def SkipValidatingRootConfiguration(self) -> bool: ...
    @CancellationToken.setter
    def CancellationToken(self, value: CancellationToken) -> None: ...
    @Environment.setter
    def Environment(self, value: LocationReferenceEnvironment) -> None: ...
    @OnlyUseAdditionalConstraints.setter
    def OnlyUseAdditionalConstraints(self, value: bool) -> None: ...
    @PrepareForRuntime.setter
    def PrepareForRuntime(self, value: bool) -> None: ...
    @SingleLevel.setter
    def SingleLevel(self, value: bool) -> None: ...
    @SkipValidatingRootConfiguration.setter
    def SkipValidatingRootConfiguration(self, value: bool) -> None: ...
