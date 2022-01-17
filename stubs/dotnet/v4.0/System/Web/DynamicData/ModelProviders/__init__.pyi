from typing import Tuple, Set, Iterable, List


class TableProvider(Object):
    def CanDelete(self, principal: IPrincipal) -> bool: ...
    def CanInsert(self, principal: IPrincipal) -> bool: ...
    def CanRead(self, principal: IPrincipal) -> bool: ...
    def CanUpdate(self, principal: IPrincipal) -> bool: ...
    def EvaluateForeignKey(self, row: Object, foreignKeyName: str) -> Object: ...
    @property
    def Attributes(self) -> AttributeCollection: ...
    @property
    def Columns(self) -> ReadOnlyCollection: ...
    @property
    def DataContextPropertyName(self) -> str: ...
    @property
    def DataModel(self) -> DataModelProvider: ...
    @property
    def EntityType(self) -> Type: ...
    @property
    def Name(self) -> str: ...
    @property
    def ParentEntityType(self) -> Type: ...
    @property
    def RootEntityType(self) -> Type: ...
    def GetQuery(self, context: Object) -> IQueryable: ...
    def GetTypeDescriptor(self) -> ICustomTypeDescriptor: ...
    def ToString(self) -> str: ...