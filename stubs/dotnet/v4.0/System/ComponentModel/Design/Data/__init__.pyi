from typing import Tuple, Set, Iterable, List


class IDesignerDataSchema:
    def GetSchemaItems(self, schemaClass: DesignerDataSchemaClass) -> ICollection: ...
    def SupportsSchemaClass(self, schemaClass: DesignerDataSchemaClass) -> bool: ...
