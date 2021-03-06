__all__ = ['Mapping','SqlClient']
from typing import Tuple, Set, Iterable, List


class Binary(Object):
    def __init__(self, value: Set(Byte)): ...
    @overload
    def Equals(self, other: Binary) -> bool: ...
    @overload
    def Equals(self, obj: Object) -> bool: ...
    @property
    def Length(self) -> int: ...
    def GetHashCode(self) -> int: ...
    def op_Equality(binary1: Binary, binary2: Binary) -> bool: ...
    def op_Implicit(value: Set(Byte)) -> Binary: ...
    def op_Inequality(binary1: Binary, binary2: Binary) -> bool: ...
    def ToArray(self) -> Set(Byte): ...
    def ToString(self) -> str: ...


class ChangeAction:
    #None = 0
    Delete = 1
    Insert = 2
    Update = 3


class ChangeConflictCollection(Object):
    def Clear(self) -> None: ...
    def Contains(self, item: ObjectChangeConflict) -> bool: ...
    def CopyTo(self, array: Set(ObjectChangeConflict), arrayIndex: int) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, index: int) -> ObjectChangeConflict: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def Remove(self, item: ObjectChangeConflict) -> bool: ...
    @overload
    def ResolveAll(self, mode: RefreshMode) -> None: ...
    @overload
    def ResolveAll(self, mode: RefreshMode, autoResolveDeletes: bool) -> None: ...


class ChangeConflictException(Exception):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class ChangeSet(Object):
    @property
    def Deletes(self) -> List[Object]: ...
    @property
    def Inserts(self) -> List[Object]: ...
    @property
    def Updates(self) -> List[Object]: ...
    def ToString(self) -> str: ...


class CompiledQuery(Object):
    @overload
    def Compile(query: Expression) -> Func`11: ...
    @overload
    def Compile(query: Expression) -> Func`15: ...
    @overload
    def Compile(query: Expression) -> Func`14: ...
    @overload
    def Compile(query: Expression) -> Func`13: ...
    @overload
    def Compile(query: Expression) -> Func`12: ...
    @overload
    def Compile(query: Expression) -> Func`10: ...
    @overload
    def Compile(query: Expression) -> Func`16: ...
    @overload
    def Compile(query: Expression) -> Func`9: ...
    @overload
    def Compile(query: Expression) -> Func`7: ...
    @overload
    def Compile(query: Expression) -> Func`6: ...
    @overload
    def Compile(query: Expression) -> Func`5: ...
    @overload
    def Compile(query: Expression) -> Func`4: ...
    @overload
    def Compile(query: Expression) -> Func`3: ...
    @overload
    def Compile(query: Expression) -> Func: ...
    @overload
    def Compile(query: Expression) -> Func`8: ...
    @overload
    def Compile(query: Expression) -> Func`17: ...
    @property
    def Expression(self) -> LambdaExpression: ...


class ConflictMode:
    FailOnFirstConflict = 0
    ContinueOnConflict = 1


class DataContext(Object):
    @overload
    def __init__(self, fileOrServerOrConnection: str): ...
    @overload
    def __init__(self, connection: IDbConnection): ...
    @overload
    def __init__(self, fileOrServerOrConnection: str, mapping: MappingSource): ...
    @overload
    def __init__(self, connection: IDbConnection, mapping: MappingSource): ...
    def CreateDatabase(self) -> None: ...
    def DatabaseExists(self) -> bool: ...
    def DeleteDatabase(self) -> None: ...
    def Dispose(self) -> None: ...
    def ExecuteCommand(self, command: str, parameters: Set(Object)) -> int: ...
    @overload
    def ExecuteQuery(self, query: str, parameters: Set(Object)) -> Iterable[TResult]: ...
    @overload
    def ExecuteQuery(self, elementType: Type, query: str, parameters: Set(Object)) -> IEnumerable: ...
    @property
    def ChangeConflicts(self) -> ChangeConflictCollection: ...
    @property
    def CommandTimeout(self) -> int: ...
    @property
    def Connection(self) -> DbConnection: ...
    @property
    def DeferredLoadingEnabled(self) -> bool: ...
    @property
    def LoadOptions(self) -> DataLoadOptions: ...
    @property
    def Log(self) -> TextWriter: ...
    @property
    def Mapping(self) -> MetaModel: ...
    @property
    def ObjectTrackingEnabled(self) -> bool: ...
    @property
    def Transaction(self) -> DbTransaction: ...
    def GetChangeSet(self) -> ChangeSet: ...
    def GetCommand(self, query: IQueryable) -> DbCommand: ...
    @overload
    def GetTable(self) -> Table: ...
    @overload
    def GetTable(self, type: Type) -> ITable: ...
    @overload
    def Refresh(self, mode: RefreshMode, entities: Set(Object)) -> None: ...
    @overload
    def Refresh(self, mode: RefreshMode, entity: Object) -> None: ...
    @overload
    def Refresh(self, mode: RefreshMode, entities: IEnumerable) -> None: ...
    @CommandTimeout.setter
    def CommandTimeout(self, value: int) -> None: ...
    @DeferredLoadingEnabled.setter
    def DeferredLoadingEnabled(self, value: bool) -> None: ...
    @LoadOptions.setter
    def LoadOptions(self, value: DataLoadOptions) -> None: ...
    @Log.setter
    def Log(self, value: TextWriter) -> None: ...
    @ObjectTrackingEnabled.setter
    def ObjectTrackingEnabled(self, value: bool) -> None: ...
    @Transaction.setter
    def Transaction(self, value: DbTransaction) -> None: ...
    @overload
    def SubmitChanges(self) -> None: ...
    @overload
    def SubmitChanges(self, failureMode: ConflictMode) -> None: ...
    @overload
    def Translate(self, reader: DbDataReader) -> Iterable[TResult]: ...
    @overload
    def Translate(self, reader: DbDataReader) -> IMultipleResults: ...
    @overload
    def Translate(self, elementType: Type, reader: DbDataReader) -> IEnumerable: ...


class DataLoadOptions(Object):
    def __init__(self): ...
    @overload
    def AssociateWith(self, expression: Expression) -> None: ...
    @overload
    def AssociateWith(self, expression: LambdaExpression) -> None: ...
    @overload
    def LoadWith(self, expression: Expression) -> None: ...
    @overload
    def LoadWith(self, expression: LambdaExpression) -> None: ...


class DBConvert(Object):
    @overload
    def ChangeType(value: Object) -> T: ...
    @overload
    def ChangeType(value: Object, type: Type) -> Object: ...


class DuplicateKeyException(InvalidOperationException):
    @overload
    def __init__(self, duplicate: Object): ...
    @overload
    def __init__(self, duplicate: Object, message: str): ...
    @overload
    def __init__(self, duplicate: Object, message: str, innerException: Exception): ...
    @property
    def Object(self) -> Object: ...






class ForeignKeyReferenceAlreadyHasValueException(InvalidOperationException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...


class IExecuteResult:
    @property
    def ReturnValue(self) -> Object: ...
    def GetParameterValue(self, parameterIndex: int) -> Object: ...


class IFunctionResult:
    @property
    def ReturnValue(self) -> Object: ...


class IMultipleResults:
    def GetResult(self) -> Iterable[TElement]: ...




class ITable:
    @overload
    def Attach(self, entity: Object) -> None: ...
    @overload
    def Attach(self, entity: Object, asModified: bool) -> None: ...
    @overload
    def Attach(self, entity: Object, original: Object) -> None: ...
    @overload
    def AttachAll(self, entities: IEnumerable) -> None: ...
    @overload
    def AttachAll(self, entities: IEnumerable, asModified: bool) -> None: ...
    def DeleteAllOnSubmit(self, entities: IEnumerable) -> None: ...
    def DeleteOnSubmit(self, entity: Object) -> None: ...
    @property
    def Context(self) -> DataContext: ...
    @property
    def IsReadOnly(self) -> bool: ...
    def GetModifiedMembers(self, entity: Object) -> Set(ModifiedMemberInfo): ...
    def GetOriginalEntityState(self, entity: Object) -> Object: ...
    def InsertAllOnSubmit(self, entities: IEnumerable) -> None: ...
    def InsertOnSubmit(self, entity: Object) -> None: ...






class MemberChangeConflict(Object):
    @property
    def CurrentValue(self) -> Object: ...
    @property
    def DatabaseValue(self) -> Object: ...
    @property
    def IsModified(self) -> bool: ...
    @property
    def IsResolved(self) -> bool: ...
    @property
    def Member(self) -> MemberInfo: ...
    @property
    def OriginalValue(self) -> Object: ...
    @overload
    def Resolve(self, value: Object) -> None: ...
    @overload
    def Resolve(self, refreshMode: RefreshMode) -> None: ...


class ModifiedMemberInfo(ValueType):
    @property
    def CurrentValue(self) -> Object: ...
    @property
    def Member(self) -> MemberInfo: ...
    @property
    def OriginalValue(self) -> Object: ...


class ObjectChangeConflict(Object):
    @property
    def IsDeleted(self) -> bool: ...
    @property
    def IsResolved(self) -> bool: ...
    @property
    def MemberConflicts(self) -> ReadOnlyCollection: ...
    @property
    def Object(self) -> Object: ...
    @overload
    def Resolve(self) -> None: ...
    @overload
    def Resolve(self, refreshMode: RefreshMode) -> None: ...
    @overload
    def Resolve(self, refreshMode: RefreshMode, autoResolveDeletes: bool) -> None: ...


class RefreshMode:
    KeepCurrentValues = 0
    KeepChanges = 1
    OverwriteCurrentValues = 2


