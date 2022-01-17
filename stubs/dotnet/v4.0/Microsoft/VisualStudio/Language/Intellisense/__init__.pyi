__all__ = ['Implementation','Implementation']
from typing import Tuple, Set, Iterable, List


class SelectedSignatureChangedEventArgs:
    def __init__(self, previousSelectedSignature: ISignature, newSelectedSignature: ISignature): ...
    @property
    def NewSelectedSignature(self) -> ISignature: ...
    @property
    def PreviousSelectedSignature(self) -> ISignature: ...
