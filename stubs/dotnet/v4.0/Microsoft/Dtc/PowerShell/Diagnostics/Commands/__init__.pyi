from typing import Tuple, Set, Iterable, List


class CompleteDtcDiagnosticTransactionCommand(DtcCmdletBase):
    def __init__(self): ...
    @property
    def Transaction(self) -> DtcDiagnosticTransaction: ...
    @Transaction.setter
    def Transaction(self, value: DtcDiagnosticTransaction) -> None: ...
