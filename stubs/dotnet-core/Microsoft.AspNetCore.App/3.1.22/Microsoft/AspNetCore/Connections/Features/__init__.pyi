from typing import Tuple, Set, Iterable, List


class ITransferFormatFeature:
    @property
    def ActiveFormat(self) -> TransferFormat: ...
    @property
    def SupportedFormats(self) -> TransferFormat: ...
    @ActiveFormat.setter
    def ActiveFormat(self, value: TransferFormat) -> None: ...
