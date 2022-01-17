from typing import Tuple, Set, Iterable, List


class X509SecurityTokenParameters(SecurityTokenParameters):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, x509ReferenceStyle: X509KeyIdentifierClauseType): ...
    @overload
    def __init__(self, x509ReferenceStyle: X509KeyIdentifierClauseType, inclusionMode: SecurityTokenInclusionMode): ...
    @property
    def X509ReferenceStyle(self) -> X509KeyIdentifierClauseType: ...
    @X509ReferenceStyle.setter
    def X509ReferenceStyle(self, value: X509KeyIdentifierClauseType) -> None: ...
    def ToString(self) -> str: ...
