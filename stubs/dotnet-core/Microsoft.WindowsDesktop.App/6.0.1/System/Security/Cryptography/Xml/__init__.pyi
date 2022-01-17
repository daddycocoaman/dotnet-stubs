from typing import Tuple, Set, Iterable, List


class XmlLicenseTransform(Transform):
    def __init__(self): ...
    @property
    def Decryptor(self) -> IRelDecryptor: ...
    @property
    def InputTypes(self) -> Set(Type): ...
    @property
    def OutputTypes(self) -> Set(Type): ...
    @overload
    def GetOutput(self) -> Object: ...
    @overload
    def GetOutput(self, type: Type) -> Object: ...
    def LoadInnerXml(self, nodeList: XmlNodeList) -> None: ...
    def LoadInput(self, obj: Object) -> None: ...
    @Decryptor.setter
    def Decryptor(self, value: IRelDecryptor) -> None: ...
