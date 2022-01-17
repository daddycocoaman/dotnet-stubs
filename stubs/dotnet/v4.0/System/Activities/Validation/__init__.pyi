from typing import Tuple, Set, Iterable, List


class ActivityValidationServices(Object):
    def Resolve(root: Activity, id: str) -> Activity: ...
    @overload
    def Validate(toValidate: Activity) -> ValidationResults: ...
    @overload
    def Validate(toValidate: Activity, settings: ValidationSettings) -> ValidationResults: ...


class AddValidationError(NativeActivity):
    def __init__(self): ...
    @property
    def IsWarning(self) -> InArgument: ...
    @property
    def Message(self) -> InArgument: ...
    @property
    def PropertyName(self) -> InArgument: ...
    @IsWarning.setter
    def IsWarning(self, value: InArgument) -> None: ...
    @Message.setter
    def Message(self, value: InArgument) -> None: ...
    @PropertyName.setter
    def PropertyName(self, value: InArgument) -> None: ...


class AssertValidation(NativeActivity):
    def __init__(self): ...
    @property
    def Assertion(self) -> InArgument: ...
    @property
    def IsWarning(self) -> InArgument: ...
    @property
    def Message(self) -> InArgument: ...
    @property
    def PropertyName(self) -> InArgument: ...
    @Assertion.setter
    def Assertion(self, value: InArgument) -> None: ...
    @IsWarning.setter
    def IsWarning(self, value: InArgument) -> None: ...
    @Message.setter
    def Message(self, value: InArgument) -> None: ...
    @PropertyName.setter
    def PropertyName(self, value: InArgument) -> None: ...


class Constraint(NativeActivity):
    def AddValidationError(context: NativeActivityContext, error: ValidationError) -> None: ...




class GetChildSubtree:
    def __init__(self): ...
    @property
    def ValidationContext(self) -> InArgument: ...
    @ValidationContext.setter
    def ValidationContext(self, value: InArgument) -> None: ...


class GetParentChain:
    def __init__(self): ...
    @property
    def ValidationContext(self) -> InArgument: ...
    @ValidationContext.setter
    def ValidationContext(self, value: InArgument) -> None: ...


class GetWorkflowTree:
    def __init__(self): ...
    @property
    def ValidationContext(self) -> InArgument: ...
    @ValidationContext.setter
    def ValidationContext(self, value: InArgument) -> None: ...


class ValidationContext(Object):
    pass


class ValidationError(Object):
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, isWarning: bool): ...
    @overload
    def __init__(self, message: str, isWarning: bool, propertyName: str): ...
    @overload
    def __init__(self, message: str, isWarning: bool, propertyName: str, sourceDetail: Object): ...
    @property
    def Id(self) -> str: ...
    @property
    def IsWarning(self) -> bool: ...
    @property
    def Message(self) -> str: ...
    @property
    def PropertyName(self) -> str: ...
    @property
    def Source(self) -> Activity: ...
    @property
    def SourceDetail(self) -> Object: ...
    def ToString(self) -> str: ...


class ValidationResults(Object):
    def __init__(self, allValidationErrors: List[ValidationError]): ...
    @property
    def Errors(self) -> ReadOnlyCollection: ...
    @property
    def Warnings(self) -> ReadOnlyCollection: ...


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
