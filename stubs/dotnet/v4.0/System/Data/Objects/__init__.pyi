__all__ = ['DataClasses','SqlClient']
from typing import Tuple, Set, Iterable, List


class CompiledQuery(Object):
    @overload
    def Compile(query: Expression) -> Func`17: ...
    @overload
    def Compile(query: Expression) -> Func: ...
    @overload
    def Compile(query: Expression) -> Func`3: ...
    @overload
    def Compile(query: Expression) -> Func`4: ...
    @overload
    def Compile(query: Expression) -> Func`5: ...
    @overload
    def Compile(query: Expression) -> Func`6: ...
    @overload
    def Compile(query: Expression) -> Func`7: ...
    @overload
    def Compile(query: Expression) -> Func`9: ...
    @overload
    def Compile(query: Expression) -> Func`8: ...
    @overload
    def Compile(query: Expression) -> Func`11: ...
    @overload
    def Compile(query: Expression) -> Func`12: ...
    @overload
    def Compile(query: Expression) -> Func`13: ...
    @overload
    def Compile(query: Expression) -> Func`14: ...
    @overload
    def Compile(query: Expression) -> Func`15: ...
    @overload
    def Compile(query: Expression) -> Func`16: ...
    @overload
    def Compile(query: Expression) -> Func`10: ...


class CurrentValueRecord(DbUpdatableDataRecord):
    pass


class DbUpdatableDataRecord(DbDataRecord):
    @property
    def DataRecordInfo(self) -> DataRecordInfo: ...
    @property
    def FieldCount(self) -> int: ...
    @property
    def Item(self, name: str) -> Object: ...
    @property
    def Item(self, ordinal: int) -> Object: ...
    def GetBoolean(self, ordinal: int) -> bool: ...
    def GetByte(self, ordinal: int) -> Byte: ...
    def GetBytes(self, ordinal: int, dataIndex: Int64, buffer: Set(Byte), bufferIndex: int, length: int) -> Int64: ...
    def GetChar(self, ordinal: int) -> Char: ...
    def GetChars(self, ordinal: int, dataIndex: Int64, buffer: Set(Char), bufferIndex: int, length: int) -> Int64: ...
    def GetDataReader(self, i: int) -> DbDataReader: ...
    def GetDataRecord(self, ordinal: int) -> DbDataRecord: ...
    def GetDataTypeName(self, ordinal: int) -> str: ...
    def GetDateTime(self, ordinal: int) -> DateTime: ...
    def GetDecimal(self, ordinal: int) -> Decimal: ...
    def GetDouble(self, ordinal: int) -> float: ...
    def GetFieldType(self, ordinal: int) -> Type: ...
    def GetFloat(self, ordinal: int) -> Single: ...
    def GetGuid(self, ordinal: int) -> Guid: ...
    def GetInt16(self, ordinal: int) -> Int16: ...
    def GetInt32(self, ordinal: int) -> int: ...
    def GetInt64(self, ordinal: int) -> Int64: ...
    def GetName(self, ordinal: int) -> str: ...
    def GetOrdinal(self, name: str) -> int: ...
    def GetString(self, ordinal: int) -> str: ...
    def GetValue(self, ordinal: int) -> Object: ...
    def GetValues(self, values: Set(Object)) -> int: ...
    def IsDBNull(self, ordinal: int) -> bool: ...
    def SetBoolean(self, ordinal: int, value: bool) -> None: ...
    def SetByte(self, ordinal: int, value: Byte) -> None: ...
    def SetChar(self, ordinal: int, value: Char) -> None: ...
    def SetDataRecord(self, ordinal: int, value: IDataRecord) -> None: ...
    def SetDateTime(self, ordinal: int, value: DateTime) -> None: ...
    def SetDBNull(self, ordinal: int) -> None: ...
    def SetDecimal(self, ordinal: int, value: Decimal) -> None: ...
    def SetDouble(self, ordinal: int, value: float) -> None: ...
    def SetFloat(self, ordinal: int, value: Single) -> None: ...
    def SetGuid(self, ordinal: int, value: Guid) -> None: ...
    def SetInt16(self, ordinal: int, value: Int16) -> None: ...
    def SetInt32(self, ordinal: int, value: int) -> None: ...
    def SetInt64(self, ordinal: int, value: Int64) -> None: ...
    def SetString(self, ordinal: int, value: str) -> None: ...
    def SetValue(self, ordinal: int, value: Object) -> None: ...
    def SetValues(self, values: Set(Object)) -> int: ...


class EntityFunctions(Object):
    @overload
    def AddDays(dateValue: Nullable, addValue: Nullable) -> Nullable: ...
    @overload
    def AddDays(dateValue: Nullable, addValue: Nullable) -> Nullable: ...
    @overload
    def AddHours(timeValue: Nullable, addValue: Nullable) -> Nullable: ...
    @overload
    def AddHours(timeValue: Nullable, addValue: Nullable) -> Nullable: ...
    @overload
    def AddHours(timeValue: Nullable, addValue: Nullable) -> Nullable: ...
    @overload
    def AddMicroseconds(timeValue: Nullable, addValue: Nullable) -> Nullable: ...
    @overload
    def AddMicroseconds(timeValue: Nullable, addValue: Nullable) -> Nullable: ...
    @overload
    def AddMicroseconds(timeValue: Nullable, addValue: Nullable) -> Nullable: ...
    @overload
    def AddMilliseconds(timeValue: Nullable, addValue: Nullable) -> Nullable: ...
    @overload
    def AddMilliseconds(timeValue: Nullable, addValue: Nullable) -> Nullable: ...
    @overload
    def AddMilliseconds(timeValue: Nullable, addValue: Nullable) -> Nullable: ...
    @overload
    def AddMinutes(timeValue: Nullable, addValue: Nullable) -> Nullable: ...
    @overload
    def AddMinutes(timeValue: Nullable, addValue: Nullable) -> Nullable: ...
    @overload
    def AddMinutes(timeValue: Nullable, addValue: Nullable) -> Nullable: ...
    @overload
    def AddMonths(dateValue: Nullable, addValue: Nullable) -> Nullable: ...
    @overload
    def AddMonths(dateValue: Nullable, addValue: Nullable) -> Nullable: ...
    @overload
    def AddNanoseconds(timeValue: Nullable, addValue: Nullable) -> Nullable: ...
    @overload
    def AddNanoseconds(timeValue: Nullable, addValue: Nullable) -> Nullable: ...
    @overload
    def AddNanoseconds(timeValue: Nullable, addValue: Nullable) -> Nullable: ...
    @overload
    def AddSeconds(timeValue: Nullable, addValue: Nullable) -> Nullable: ...
    @overload
    def AddSeconds(timeValue: Nullable, addValue: Nullable) -> Nullable: ...
    @overload
    def AddSeconds(timeValue: Nullable, addValue: Nullable) -> Nullable: ...
    @overload
    def AddYears(dateValue: Nullable, addValue: Nullable) -> Nullable: ...
    @overload
    def AddYears(dateValue: Nullable, addValue: Nullable) -> Nullable: ...
    def AsNonUnicode(value: str) -> str: ...
    def AsUnicode(value: str) -> str: ...
    def CreateDateTime(year: Nullable, month: Nullable, day: Nullable, hour: Nullable, minute: Nullable, second: Nullable) -> Nullable: ...
    def CreateDateTimeOffset(year: Nullable, month: Nullable, day: Nullable, hour: Nullable, minute: Nullable, second: Nullable, timeZoneOffset: Nullable) -> Nullable: ...
    def CreateTime(hour: Nullable, minute: Nullable, second: Nullable) -> Nullable: ...
    @overload
    def DiffDays(dateValue1: Nullable, dateValue2: Nullable) -> Nullable: ...
    @overload
    def DiffDays(dateValue1: Nullable, dateValue2: Nullable) -> Nullable: ...
    @overload
    def DiffHours(timeValue1: Nullable, timeValue2: Nullable) -> Nullable: ...
    @overload
    def DiffHours(timeValue1: Nullable, timeValue2: Nullable) -> Nullable: ...
    @overload
    def DiffHours(timeValue1: Nullable, timeValue2: Nullable) -> Nullable: ...
    @overload
    def DiffMicroseconds(timeValue1: Nullable, timeValue2: Nullable) -> Nullable: ...
    @overload
    def DiffMicroseconds(timeValue1: Nullable, timeValue2: Nullable) -> Nullable: ...
    @overload
    def DiffMicroseconds(timeValue1: Nullable, timeValue2: Nullable) -> Nullable: ...
    @overload
    def DiffMilliseconds(timeValue1: Nullable, timeValue2: Nullable) -> Nullable: ...
    @overload
    def DiffMilliseconds(timeValue1: Nullable, timeValue2: Nullable) -> Nullable: ...
    @overload
    def DiffMilliseconds(timeValue1: Nullable, timeValue2: Nullable) -> Nullable: ...
    @overload
    def DiffMinutes(timeValue1: Nullable, timeValue2: Nullable) -> Nullable: ...
    @overload
    def DiffMinutes(timeValue1: Nullable, timeValue2: Nullable) -> Nullable: ...
    @overload
    def DiffMinutes(timeValue1: Nullable, timeValue2: Nullable) -> Nullable: ...
    @overload
    def DiffMonths(dateValue1: Nullable, dateValue2: Nullable) -> Nullable: ...
    @overload
    def DiffMonths(dateValue1: Nullable, dateValue2: Nullable) -> Nullable: ...
    @overload
    def DiffNanoseconds(timeValue1: Nullable, timeValue2: Nullable) -> Nullable: ...
    @overload
    def DiffNanoseconds(timeValue1: Nullable, timeValue2: Nullable) -> Nullable: ...
    @overload
    def DiffNanoseconds(timeValue1: Nullable, timeValue2: Nullable) -> Nullable: ...
    @overload
    def DiffSeconds(timeValue1: Nullable, timeValue2: Nullable) -> Nullable: ...
    @overload
    def DiffSeconds(timeValue1: Nullable, timeValue2: Nullable) -> Nullable: ...
    @overload
    def DiffSeconds(timeValue1: Nullable, timeValue2: Nullable) -> Nullable: ...
    @overload
    def DiffYears(dateValue1: Nullable, dateValue2: Nullable) -> Nullable: ...
    @overload
    def DiffYears(dateValue1: Nullable, dateValue2: Nullable) -> Nullable: ...
    def GetTotalOffsetMinutes(dateTimeOffsetArgument: Nullable) -> Nullable: ...
    def Left(stringArgument: str, length: Nullable) -> str: ...
    def Reverse(stringArgument: str) -> str: ...
    def Right(stringArgument: str, length: Nullable) -> str: ...
    @overload
    def StandardDeviation(collection: Iterable[Nullable]) -> Nullable: ...
    @overload
    def StandardDeviation(collection: Iterable[Decimal]) -> Nullable: ...
    @overload
    def StandardDeviation(collection: Iterable[float]) -> Nullable: ...
    @overload
    def StandardDeviation(collection: Iterable[Nullable]) -> Nullable: ...
    @overload
    def StandardDeviation(collection: Iterable[int]) -> Nullable: ...
    @overload
    def StandardDeviation(collection: Iterable[Int64]) -> Nullable: ...
    @overload
    def StandardDeviation(collection: Iterable[Nullable]) -> Nullable: ...
    @overload
    def StandardDeviation(collection: Iterable[Nullable]) -> Nullable: ...
    @overload
    def StandardDeviationP(collection: Iterable[Decimal]) -> Nullable: ...
    @overload
    def StandardDeviationP(collection: Iterable[Nullable]) -> Nullable: ...
    @overload
    def StandardDeviationP(collection: Iterable[float]) -> Nullable: ...
    @overload
    def StandardDeviationP(collection: Iterable[Nullable]) -> Nullable: ...
    @overload
    def StandardDeviationP(collection: Iterable[int]) -> Nullable: ...
    @overload
    def StandardDeviationP(collection: Iterable[Nullable]) -> Nullable: ...
    @overload
    def StandardDeviationP(collection: Iterable[Int64]) -> Nullable: ...
    @overload
    def StandardDeviationP(collection: Iterable[Nullable]) -> Nullable: ...
    @overload
    def Truncate(value: Nullable, digits: Nullable) -> Nullable: ...
    @overload
    def Truncate(value: Nullable, digits: Nullable) -> Nullable: ...
    @overload
    def TruncateTime(dateValue: Nullable) -> Nullable: ...
    @overload
    def TruncateTime(dateValue: Nullable) -> Nullable: ...
    @overload
    def Var(collection: Iterable[Decimal]) -> Nullable: ...
    @overload
    def Var(collection: Iterable[Nullable]) -> Nullable: ...
    @overload
    def Var(collection: Iterable[float]) -> Nullable: ...
    @overload
    def Var(collection: Iterable[Nullable]) -> Nullable: ...
    @overload
    def Var(collection: Iterable[int]) -> Nullable: ...
    @overload
    def Var(collection: Iterable[Nullable]) -> Nullable: ...
    @overload
    def Var(collection: Iterable[Int64]) -> Nullable: ...
    @overload
    def Var(collection: Iterable[Nullable]) -> Nullable: ...
    @overload
    def VarP(collection: Iterable[Nullable]) -> Nullable: ...
    @overload
    def VarP(collection: Iterable[float]) -> Nullable: ...
    @overload
    def VarP(collection: Iterable[Nullable]) -> Nullable: ...
    @overload
    def VarP(collection: Iterable[int]) -> Nullable: ...
    @overload
    def VarP(collection: Iterable[Nullable]) -> Nullable: ...
    @overload
    def VarP(collection: Iterable[Int64]) -> Nullable: ...
    @overload
    def VarP(collection: Iterable[Nullable]) -> Nullable: ...
    @overload
    def VarP(collection: Iterable[Decimal]) -> Nullable: ...




class MergeOption:
    AppendOnly = 0
    OverwriteChanges = 1
    PreserveChanges = 2
    NoTracking = 3


class ObjectContext(Object):
    @overload
    def __init__(self, connection: EntityConnection): ...
    @overload
    def __init__(self, connectionString: str): ...
    def AcceptAllChanges(self) -> None: ...
    def add_ObjectMaterialized(self, value: ObjectMaterializedEventHandler) -> None: ...
    def add_SavingChanges(self, value: EventHandler) -> None: ...
    def AddObject(self, entitySetName: str, entity: Object) -> None: ...
    def ApplyCurrentValues(self, entitySetName: str, currentEntity: TEntity) -> TEntity: ...
    def ApplyOriginalValues(self, entitySetName: str, originalEntity: TEntity) -> TEntity: ...
    def Attach(self, entity: IEntityWithKey) -> None: ...
    def AttachTo(self, entitySetName: str, entity: Object) -> None: ...
    def CreateDatabase(self) -> None: ...
    def CreateDatabaseScript(self) -> str: ...
    def CreateEntityKey(self, entitySetName: str, entity: Object) -> EntityKey: ...
    def CreateObject(self) -> T: ...
    @overload
    def CreateObjectSet(self) -> ObjectSet: ...
    @overload
    def CreateObjectSet(self, entitySetName: str) -> ObjectSet: ...
    def CreateProxyTypes(self, types: Iterable[Type]) -> None: ...
    def CreateQuery(self, queryString: str, parameters: Set(ObjectParameter)) -> ObjectQuery: ...
    def DatabaseExists(self) -> bool: ...
    def DeleteDatabase(self) -> None: ...
    def DeleteObject(self, entity: Object) -> None: ...
    def Detach(self, entity: Object) -> None: ...
    def DetectChanges(self) -> None: ...
    def Dispose(self) -> None: ...
    @overload
    def ExecuteFunction(self, functionName: str, parameters: Set(ObjectParameter)) -> int: ...
    @overload
    def ExecuteFunction(self, functionName: str, parameters: Set(ObjectParameter)) -> ObjectResult: ...
    @overload
    def ExecuteFunction(self, functionName: str, mergeOption: MergeOption, parameters: Set(ObjectParameter)) -> ObjectResult: ...
    def ExecuteStoreCommand(self, commandText: str, parameters: Set(Object)) -> int: ...
    @overload
    def ExecuteStoreQuery(self, commandText: str, parameters: Set(Object)) -> ObjectResult: ...
    @overload
    def ExecuteStoreQuery(self, commandText: str, entitySetName: str, mergeOption: MergeOption, parameters: Set(Object)) -> ObjectResult: ...
    @property
    def CommandTimeout(self) -> Nullable: ...
    @property
    def Connection(self) -> DbConnection: ...
    @property
    def ContextOptions(self) -> ObjectContextOptions: ...
    @property
    def DefaultContainerName(self) -> str: ...
    @property
    def MetadataWorkspace(self) -> MetadataWorkspace: ...
    @property
    def ObjectStateManager(self) -> ObjectStateManager: ...
    def GetKnownProxyTypes() -> Iterable[Type]: ...
    def GetObjectByKey(self, key: EntityKey) -> Object: ...
    def GetObjectType(type: Type) -> Type: ...
    @overload
    def LoadProperty(self, entity: Object, navigationProperty: str) -> None: ...
    @overload
    def LoadProperty(self, entity: TEntity, selector: Expression) -> None: ...
    @overload
    def LoadProperty(self, entity: TEntity, selector: Expression, mergeOption: MergeOption) -> None: ...
    @overload
    def LoadProperty(self, entity: Object, navigationProperty: str, mergeOption: MergeOption) -> None: ...
    @overload
    def Refresh(self, refreshMode: RefreshMode, entity: Object) -> None: ...
    @overload
    def Refresh(self, refreshMode: RefreshMode, collection: IEnumerable) -> None: ...
    def remove_ObjectMaterialized(self, value: ObjectMaterializedEventHandler) -> None: ...
    def remove_SavingChanges(self, value: EventHandler) -> None: ...
    @overload
    def SaveChanges(self) -> int: ...
    @overload
    def SaveChanges(self, options: SaveOptions) -> int: ...
    @CommandTimeout.setter
    def CommandTimeout(self, value: Nullable) -> None: ...
    @DefaultContainerName.setter
    def DefaultContainerName(self, value: str) -> None: ...
    @overload
    def Translate(self, reader: DbDataReader) -> ObjectResult: ...
    @overload
    def Translate(self, reader: DbDataReader, entitySetName: str, mergeOption: MergeOption) -> ObjectResult: ...
    def TryGetObjectByKey(self, key: EntityKey) -> Tuple[bool, Object]: ...


class ObjectContextOptions(Object):
    @property
    def LazyLoadingEnabled(self) -> bool: ...
    @property
    def ProxyCreationEnabled(self) -> bool: ...
    @property
    def UseConsistentNullReferenceBehavior(self) -> bool: ...
    @property
    def UseCSharpNullComparisonBehavior(self) -> bool: ...
    @property
    def UseLegacyPreserveChangesBehavior(self) -> bool: ...
    @LazyLoadingEnabled.setter
    def LazyLoadingEnabled(self, value: bool) -> None: ...
    @ProxyCreationEnabled.setter
    def ProxyCreationEnabled(self, value: bool) -> None: ...
    @UseConsistentNullReferenceBehavior.setter
    def UseConsistentNullReferenceBehavior(self, value: bool) -> None: ...
    @UseCSharpNullComparisonBehavior.setter
    def UseCSharpNullComparisonBehavior(self, value: bool) -> None: ...
    @UseLegacyPreserveChangesBehavior.setter
    def UseLegacyPreserveChangesBehavior(self, value: bool) -> None: ...


class ObjectMaterializedEventArgs(EventArgs):
    @property
    def Entity(self) -> Object: ...


class ObjectMaterializedEventHandler(MulticastDelegate):
    def __init__(self, object: Object, method: IntPtr): ...
    def BeginInvoke(self, sender: Object, e: ObjectMaterializedEventArgs, callback: AsyncCallback, object: Object) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> None: ...
    def Invoke(self, sender: Object, e: ObjectMaterializedEventArgs) -> None: ...


class ObjectParameter(Object):
    @overload
    def __init__(self, name: str, type: Type): ...
    @overload
    def __init__(self, name: str, value: Object): ...
    @property
    def Name(self) -> str: ...
    @property
    def ParameterType(self) -> Type: ...
    @property
    def Value(self) -> Object: ...
    @Value.setter
    def Value(self, value: Object) -> None: ...


class ObjectParameterCollection(Object):
    def Add(self, parameter: ObjectParameter) -> None: ...
    def Clear(self) -> None: ...
    @overload
    def Contains(self, parameter: ObjectParameter) -> bool: ...
    @overload
    def Contains(self, name: str) -> bool: ...
    def CopyTo(self, array: Set(ObjectParameter), index: int) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, name: str) -> ObjectParameter: ...
    def Remove(self, parameter: ObjectParameter) -> bool: ...


class ObjectQuery(Object):
    def Execute(self, mergeOption: MergeOption) -> ObjectResult: ...
    @property
    def CommandText(self) -> str: ...
    @property
    def Context(self) -> ObjectContext: ...
    @property
    def EnablePlanCaching(self) -> bool: ...
    @property
    def MergeOption(self) -> MergeOption: ...
    @property
    def Parameters(self) -> ObjectParameterCollection: ...
    def GetResultType(self) -> TypeUsage: ...
    @EnablePlanCaching.setter
    def EnablePlanCaching(self, value: bool) -> None: ...
    @MergeOption.setter
    def MergeOption(self, value: MergeOption) -> None: ...
    def ToTraceString(self) -> str: ...




class ObjectResult(Object):
    def Dispose(self) -> None: ...
    @property
    def ElementType(self) -> Type: ...
    def GetNextResult(self) -> ObjectResult: ...






class ObjectStateEntry(Object):
    def AcceptChanges(self) -> None: ...
    def ApplyCurrentValues(self, currentEntity: Object) -> None: ...
    def ApplyOriginalValues(self, originalEntity: Object) -> None: ...
    def ChangeState(self, state: EntityState) -> None: ...
    def Delete(self) -> None: ...
    @property
    def CurrentValues(self) -> CurrentValueRecord: ...
    @property
    def Entity(self) -> Object: ...
    @property
    def EntityKey(self) -> EntityKey: ...
    @property
    def EntitySet(self) -> EntitySetBase: ...
    @property
    def IsRelationship(self) -> bool: ...
    @property
    def ObjectStateManager(self) -> ObjectStateManager: ...
    @property
    def OriginalValues(self) -> DbDataRecord: ...
    @property
    def RelationshipManager(self) -> RelationshipManager: ...
    @property
    def State(self) -> EntityState: ...
    def GetModifiedProperties(self) -> Iterable[str]: ...
    def GetUpdatableOriginalValues(self) -> OriginalValueRecord: ...
    def IsPropertyChanged(self, propertyName: str) -> bool: ...
    def RejectPropertyChanges(self, propertyName: str) -> None: ...
    def SetModified(self) -> None: ...
    def SetModifiedProperty(self, propertyName: str) -> None: ...


class ObjectStateManager(Object):
    def __init__(self, metadataWorkspace: MetadataWorkspace): ...
    def add_ObjectStateManagerChanged(self, value: CollectionChangeEventHandler) -> None: ...
    def ChangeObjectState(self, entity: Object, entityState: EntityState) -> ObjectStateEntry: ...
    @overload
    def ChangeRelationshipState(self, sourceEntity: Object, targetEntity: Object, navigationProperty: str, relationshipState: EntityState) -> ObjectStateEntry: ...
    @overload
    def ChangeRelationshipState(self, sourceEntity: TEntity, targetEntity: Object, navigationPropertySelector: Expression, relationshipState: EntityState) -> ObjectStateEntry: ...
    @overload
    def ChangeRelationshipState(self, sourceEntity: Object, targetEntity: Object, relationshipName: str, targetRoleName: str, relationshipState: EntityState) -> ObjectStateEntry: ...
    @property
    def MetadataWorkspace(self) -> MetadataWorkspace: ...
    def GetObjectStateEntries(self, state: EntityState) -> Iterable[ObjectStateEntry]: ...
    @overload
    def GetObjectStateEntry(self, key: EntityKey) -> ObjectStateEntry: ...
    @overload
    def GetObjectStateEntry(self, entity: Object) -> ObjectStateEntry: ...
    def GetRelationshipManager(self, entity: Object) -> RelationshipManager: ...
    def remove_ObjectStateManagerChanged(self, value: CollectionChangeEventHandler) -> None: ...
    @overload
    def TryGetObjectStateEntry(self, entity: Object) -> Tuple[bool, ObjectStateEntry]: ...
    @overload
    def TryGetObjectStateEntry(self, key: EntityKey) -> Tuple[bool, ObjectStateEntry]: ...
    def TryGetRelationshipManager(self, entity: Object) -> Tuple[bool, RelationshipManager]: ...


class OriginalValueRecord(DbUpdatableDataRecord):
    pass


class ProxyDataContractResolver(DataContractResolver):
    def __init__(self): ...
    def ResolveName(self, typeName: str, typeNamespace: str, declaredType: Type, knownTypeResolver: DataContractResolver) -> Type: ...
    def TryResolveType(self, dataContractType: Type, declaredType: Type, knownTypeResolver: DataContractResolver) -> Tuple[bool, XmlDictionaryString, XmlDictionaryString]: ...


class RefreshMode:
    StoreWins = 1
    ClientWins = 2


class SaveOptions:
    #None = 0
    AcceptAllChangesAfterSave = 1
    DetectChangesBeforeSave = 2
