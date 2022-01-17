from typing import Tuple, Set, Iterable, List


class ValidationProviderAttribute:
    def GetValidationAttributes(self) -> Iterable[ValidationAttribute]: ...
