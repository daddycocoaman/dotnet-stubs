from typing import Tuple, Set, Iterable, List


class ResolveCriteriaApril2005(Object):
    def FromResolveCriteria(resolveCriteria: ResolveCriteria) -> ResolveCriteriaApril2005: ...
    @overload
    def GetSchema(self) -> XmlSchema: ...
    @overload
    def GetSchema(schemaSet: XmlSchemaSet) -> XmlQualifiedName: ...
    def ReadXml(self, reader: XmlReader) -> None: ...
    def ToResolveCriteria(self) -> ResolveCriteria: ...
    def WriteXml(self, writer: XmlWriter) -> None: ...
