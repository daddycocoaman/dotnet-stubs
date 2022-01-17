from typing import Tuple, Set, Iterable, List


class ResolveCriteria11(Object):
    def FromResolveCriteria(resolveCriteria: ResolveCriteria) -> ResolveCriteria11: ...
    @overload
    def GetSchema(self) -> XmlSchema: ...
    @overload
    def GetSchema(schemaSet: XmlSchemaSet) -> XmlQualifiedName: ...
    def ReadXml(self, reader: XmlReader) -> None: ...
    def ToResolveCriteria(self) -> ResolveCriteria: ...
    def WriteXml(self, writer: XmlWriter) -> None: ...