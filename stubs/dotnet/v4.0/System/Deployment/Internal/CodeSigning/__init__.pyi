from typing import Tuple, Set, Iterable, List


class RSAPKCS1SHA256SignatureDescription(SignatureDescription):
    def __init__(self): ...
    def CreateDeformatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureDeformatter: ...
    def CreateFormatter(self, key: AsymmetricAlgorithm) -> AsymmetricSignatureFormatter: ...
