from typing import Tuple, Set, Iterable, List




class IAttributeAdapter:
    def GetErrorMessage(self, validationContext: ModelValidationContextBase) -> str: ...


class IValidationAttributeAdapterProvider:
    def GetAttributeAdapter(self, attribute: ValidationAttribute, stringLocalizer: IStringLocalizer) -> IAttributeAdapter: ...


class MvcDataAnnotationsLocalizationOptions:
    def __init__(self): ...


class RequiredAttributeAdapter:
    def __init__(self, attribute: RequiredAttribute, stringLocalizer: IStringLocalizer): ...
    def AddValidation(self, context: ClientModelValidationContext) -> None: ...
    def GetErrorMessage(self, validationContext: ModelValidationContextBase) -> str: ...




class ValidationAttributeAdapterProvider:
    def __init__(self): ...
    def GetAttributeAdapter(self, attribute: ValidationAttribute, stringLocalizer: IStringLocalizer) -> IAttributeAdapter: ...


class ValidationProviderAttribute:
    def GetValidationAttributes(self) -> Iterable[ValidationAttribute]: ...
