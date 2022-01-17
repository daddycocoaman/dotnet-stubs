from typing import Tuple, Set, Iterable, List


class AtomPub10CategoriesDocumentFormatter(CategoriesDocumentFormatter):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, documentToWrite: CategoriesDocument): ...
    @overload
    def __init__(self, inlineDocumentType: Type, referencedDocumentType: Type): ...
    def CanRead(self, reader: XmlReader) -> bool: ...
    @property
    def Version(self) -> str: ...
    def ReadFrom(self, reader: XmlReader) -> None: ...
    def WriteTo(self, writer: XmlWriter) -> None: ...