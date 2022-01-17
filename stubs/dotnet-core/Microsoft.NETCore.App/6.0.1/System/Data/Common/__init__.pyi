from typing import Tuple, Set, Iterable, List


class CatalogLocation:
    Start = 1
    End = 2


class DataAdapter(Component):
    def add_FillError(self, value: FillErrorEventHandler) -> None: ...
    def Fill(self, dataSet: DataSet) -> int: ...
    def FillSchema(self, dataSet: DataSet, schemaType: SchemaType) -> Set(DataTable): ...
    @property
    def AcceptChangesDuringFill(self) -> bool: ...
    @property
    def AcceptChangesDuringUpdate(self) -> bool: ...
    @property
    def ContinueUpdateOnError(self) -> bool: ...
    @property
    def FillLoadOption(self) -> LoadOption: ...
    @property
    def MissingMappingAction(self) -> MissingMappingAction: ...
    @property
    def MissingSchemaAction(self) -> MissingSchemaAction: ...
    @property
    def ReturnProviderSpecificTypes(self) -> bool: ...
    @property
    def TableMappings(self) -> DataTableMappingCollection: ...
    def GetFillParameters(self) -> Set(IDataParameter): ...
    def remove_FillError(self, value: FillErrorEventHandler) -> None: ...
    def ResetFillLoadOption(self) -> None: ...
    @AcceptChangesDuringFill.setter
    def AcceptChangesDuringFill(self, value: bool) -> None: ...
    @AcceptChangesDuringUpdate.setter
    def AcceptChangesDuringUpdate(self, value: bool) -> None: ...
    @ContinueUpdateOnError.setter
    def ContinueUpdateOnError(self, value: bool) -> None: ...
    @FillLoadOption.setter
    def FillLoadOption(self, value: LoadOption) -> None: ...
    @MissingMappingAction.setter
    def MissingMappingAction(self, value: MissingMappingAction) -> None: ...
    @MissingSchemaAction.setter
    def MissingSchemaAction(self, value: MissingSchemaAction) -> None: ...
    @ReturnProviderSpecificTypes.setter
    def ReturnProviderSpecificTypes(self, value: bool) -> None: ...
    def ShouldSerializeAcceptChangesDuringFill(self) -> bool: ...
    def ShouldSerializeFillLoadOption(self) -> bool: ...
    def Update(self, dataSet: DataSet) -> int: ...


class DataColumnMapping(MarshalByRefObject):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, sourceColumn: str, dataSetColumn: str): ...
    @property
    def DataSetColumn(self) -> str: ...
    @property
    def SourceColumn(self) -> str: ...
    @overload
    def GetDataColumnBySchemaAction(self, dataTable: DataTable, dataType: Type, schemaAction: MissingSchemaAction) -> DataColumn: ...
    @overload
    def GetDataColumnBySchemaAction(sourceColumn: str, dataSetColumn: str, dataTable: DataTable, dataType: Type, schemaAction: MissingSchemaAction) -> DataColumn: ...
    @DataSetColumn.setter
    def DataSetColumn(self, value: str) -> None: ...
    @SourceColumn.setter
    def SourceColumn(self, value: str) -> None: ...
    def ToString(self) -> str: ...


class DataColumnMappingCollection(MarshalByRefObject):
    def __init__(self): ...
    @overload
    def Add(self, value: Object) -> int: ...
    @overload
    def Add(self, sourceColumn: str, dataSetColumn: str) -> DataColumnMapping: ...
    @overload
    def AddRange(self, values: Array) -> None: ...
    @overload
    def AddRange(self, values: Set(DataColumnMapping)) -> None: ...
    def Clear(self) -> None: ...
    @overload
    def Contains(self, value: Object) -> bool: ...
    @overload
    def Contains(self, value: str) -> bool: ...
    @overload
    def CopyTo(self, array: Set(DataColumnMapping), index: int) -> None: ...
    @overload
    def CopyTo(self, array: Array, index: int) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, sourceColumn: str) -> DataColumnMapping: ...
    @property
    def Item(self, index: int) -> DataColumnMapping: ...
    def GetByDataSetColumn(self, value: str) -> DataColumnMapping: ...
    def GetColumnMappingBySchemaAction(columnMappings: DataColumnMappingCollection, sourceColumn: str, mappingAction: MissingMappingAction) -> DataColumnMapping: ...
    def GetDataColumn(columnMappings: DataColumnMappingCollection, sourceColumn: str, dataType: Type, dataTable: DataTable, mappingAction: MissingMappingAction, schemaAction: MissingSchemaAction) -> DataColumn: ...
    def GetEnumerator(self) -> IEnumerator: ...
    @overload
    def IndexOf(self, sourceColumn: str) -> int: ...
    @overload
    def IndexOf(self, value: Object) -> int: ...
    def IndexOfDataSetColumn(self, dataSetColumn: str) -> int: ...
    @overload
    def Insert(self, index: int, value: Object) -> None: ...
    @overload
    def Insert(self, index: int, value: DataColumnMapping) -> None: ...
    @overload
    def Remove(self, value: Object) -> None: ...
    @overload
    def Remove(self, value: DataColumnMapping) -> None: ...
    @overload
    def RemoveAt(self, index: int) -> None: ...
    @overload
    def RemoveAt(self, sourceColumn: str) -> None: ...
    @Item.setter
    def Item(self, sourceColumn: str, value: DataColumnMapping) -> None: ...
    @Item.setter
    def Item(self, index: int, value: DataColumnMapping) -> None: ...


class DataTableMapping(MarshalByRefObject):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, sourceTable: str, dataSetTable: str): ...
    @overload
    def __init__(self, sourceTable: str, dataSetTable: str, columnMappings: Set(DataColumnMapping)): ...
    @property
    def ColumnMappings(self) -> DataColumnMappingCollection: ...
    @property
    def DataSetTable(self) -> str: ...
    @property
    def SourceTable(self) -> str: ...
    def GetColumnMappingBySchemaAction(self, sourceColumn: str, mappingAction: MissingMappingAction) -> DataColumnMapping: ...
    def GetDataColumn(self, sourceColumn: str, dataType: Type, dataTable: DataTable, mappingAction: MissingMappingAction, schemaAction: MissingSchemaAction) -> DataColumn: ...
    def GetDataTableBySchemaAction(self, dataSet: DataSet, schemaAction: MissingSchemaAction) -> DataTable: ...
    @DataSetTable.setter
    def DataSetTable(self, value: str) -> None: ...
    @SourceTable.setter
    def SourceTable(self, value: str) -> None: ...
    def ToString(self) -> str: ...


class DataTableMappingCollection(MarshalByRefObject):
    def __init__(self): ...
    @overload
    def Add(self, value: Object) -> int: ...
    @overload
    def Add(self, sourceTable: str, dataSetTable: str) -> DataTableMapping: ...
    @overload
    def AddRange(self, values: Set(DataTableMapping)) -> None: ...
    @overload
    def AddRange(self, values: Array) -> None: ...
    def Clear(self) -> None: ...
    @overload
    def Contains(self, value: str) -> bool: ...
    @overload
    def Contains(self, value: Object) -> bool: ...
    @overload
    def CopyTo(self, array: Array, index: int) -> None: ...
    @overload
    def CopyTo(self, array: Set(DataTableMapping), index: int) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self, index: int) -> DataTableMapping: ...
    @property
    def Item(self, sourceTable: str) -> DataTableMapping: ...
    def GetByDataSetTable(self, dataSetTable: str) -> DataTableMapping: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def GetTableMappingBySchemaAction(tableMappings: DataTableMappingCollection, sourceTable: str, dataSetTable: str, mappingAction: MissingMappingAction) -> DataTableMapping: ...
    @overload
    def IndexOf(self, value: Object) -> int: ...
    @overload
    def IndexOf(self, sourceTable: str) -> int: ...
    def IndexOfDataSetTable(self, dataSetTable: str) -> int: ...
    @overload
    def Insert(self, index: int, value: Object) -> None: ...
    @overload
    def Insert(self, index: int, value: DataTableMapping) -> None: ...
    @overload
    def Remove(self, value: Object) -> None: ...
    @overload
    def Remove(self, value: DataTableMapping) -> None: ...
    @overload
    def RemoveAt(self, sourceTable: str) -> None: ...
    @overload
    def RemoveAt(self, index: int) -> None: ...
    @Item.setter
    def Item(self, sourceTable: str, value: DataTableMapping) -> None: ...
    @Item.setter
    def Item(self, index: int, value: DataTableMapping) -> None: ...


class DbBatch(Object):
    def Cancel(self) -> None: ...
    def CreateBatchCommand(self) -> DbBatchCommand: ...
    def Dispose(self) -> None: ...
    def DisposeAsync(self) -> ValueTask: ...
    def ExecuteNonQuery(self) -> int: ...
    def ExecuteNonQueryAsync(self, cancellationToken: CancellationToken) -> Task: ...
    def ExecuteReader(self, behavior: CommandBehavior) -> DbDataReader: ...
    @overload
    def ExecuteReaderAsync(self, cancellationToken: CancellationToken) -> Task: ...
    @overload
    def ExecuteReaderAsync(self, behavior: CommandBehavior, cancellationToken: CancellationToken) -> Task: ...
    def ExecuteScalar(self) -> Object: ...
    def ExecuteScalarAsync(self, cancellationToken: CancellationToken) -> Task: ...
    @property
    def BatchCommands(self) -> DbBatchCommandCollection: ...
    @property
    def Connection(self) -> DbConnection: ...
    @property
    def Timeout(self) -> int: ...
    @property
    def Transaction(self) -> DbTransaction: ...
    def Prepare(self) -> None: ...
    def PrepareAsync(self, cancellationToken: CancellationToken) -> Task: ...
    @Connection.setter
    def Connection(self, value: DbConnection) -> None: ...
    @Timeout.setter
    def Timeout(self, value: int) -> None: ...
    @Transaction.setter
    def Transaction(self, value: DbTransaction) -> None: ...


class DbBatchCommand(Object):
    @property
    def CommandText(self) -> str: ...
    @property
    def CommandType(self) -> CommandType: ...
    @property
    def Parameters(self) -> DbParameterCollection: ...
    @property
    def RecordsAffected(self) -> int: ...
    @CommandText.setter
    def CommandText(self, value: str) -> None: ...
    @CommandType.setter
    def CommandType(self, value: CommandType) -> None: ...


class DbBatchCommandCollection(Object):
    def Add(self, item: DbBatchCommand) -> None: ...
    def Clear(self) -> None: ...
    def Contains(self, item: DbBatchCommand) -> bool: ...
    def CopyTo(self, array: Set(DbBatchCommand), arrayIndex: int) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsReadOnly(self) -> bool: ...
    @property
    def Item(self, index: int) -> DbBatchCommand: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def IndexOf(self, item: DbBatchCommand) -> int: ...
    def Insert(self, index: int, item: DbBatchCommand) -> None: ...
    def Remove(self, item: DbBatchCommand) -> bool: ...
    def RemoveAt(self, index: int) -> None: ...
    @Item.setter
    def Item(self, index: int, value: DbBatchCommand) -> None: ...


class DbColumn(Object):
    @property
    def AllowDBNull(self) -> Nullable: ...
    @property
    def BaseCatalogName(self) -> str: ...
    @property
    def BaseColumnName(self) -> str: ...
    @property
    def BaseSchemaName(self) -> str: ...
    @property
    def BaseServerName(self) -> str: ...
    @property
    def BaseTableName(self) -> str: ...
    @property
    def ColumnName(self) -> str: ...
    @property
    def ColumnOrdinal(self) -> Nullable: ...
    @property
    def ColumnSize(self) -> Nullable: ...
    @property
    def DataType(self) -> Type: ...
    @property
    def DataTypeName(self) -> str: ...
    @property
    def IsAliased(self) -> Nullable: ...
    @property
    def IsAutoIncrement(self) -> Nullable: ...
    @property
    def IsExpression(self) -> Nullable: ...
    @property
    def IsHidden(self) -> Nullable: ...
    @property
    def IsIdentity(self) -> Nullable: ...
    @property
    def IsKey(self) -> Nullable: ...
    @property
    def IsLong(self) -> Nullable: ...
    @property
    def IsReadOnly(self) -> Nullable: ...
    @property
    def IsUnique(self) -> Nullable: ...
    @property
    def Item(self, property: str) -> Object: ...
    @property
    def NumericPrecision(self) -> Nullable: ...
    @property
    def NumericScale(self) -> Nullable: ...
    @property
    def UdtAssemblyQualifiedName(self) -> str: ...


class DbCommand(Component):
    def Cancel(self) -> None: ...
    def CreateParameter(self) -> DbParameter: ...
    def DisposeAsync(self) -> ValueTask: ...
    def ExecuteNonQuery(self) -> int: ...
    @overload
    def ExecuteNonQueryAsync(self) -> Task: ...
    @overload
    def ExecuteNonQueryAsync(self, cancellationToken: CancellationToken) -> Task: ...
    @overload
    def ExecuteReader(self) -> DbDataReader: ...
    @overload
    def ExecuteReader(self, behavior: CommandBehavior) -> DbDataReader: ...
    @overload
    def ExecuteReaderAsync(self) -> Task: ...
    @overload
    def ExecuteReaderAsync(self, cancellationToken: CancellationToken) -> Task: ...
    @overload
    def ExecuteReaderAsync(self, behavior: CommandBehavior) -> Task: ...
    @overload
    def ExecuteReaderAsync(self, behavior: CommandBehavior, cancellationToken: CancellationToken) -> Task: ...
    def ExecuteScalar(self) -> Object: ...
    @overload
    def ExecuteScalarAsync(self) -> Task: ...
    @overload
    def ExecuteScalarAsync(self, cancellationToken: CancellationToken) -> Task: ...
    @property
    def CommandText(self) -> str: ...
    @property
    def CommandTimeout(self) -> int: ...
    @property
    def CommandType(self) -> CommandType: ...
    @property
    def Connection(self) -> DbConnection: ...
    @property
    def DesignTimeVisible(self) -> bool: ...
    @property
    def Parameters(self) -> DbParameterCollection: ...
    @property
    def Transaction(self) -> DbTransaction: ...
    @property
    def UpdatedRowSource(self) -> UpdateRowSource: ...
    def Prepare(self) -> None: ...
    def PrepareAsync(self, cancellationToken: CancellationToken) -> Task: ...
    @CommandText.setter
    def CommandText(self, value: str) -> None: ...
    @CommandTimeout.setter
    def CommandTimeout(self, value: int) -> None: ...
    @CommandType.setter
    def CommandType(self, value: CommandType) -> None: ...
    @Connection.setter
    def Connection(self, value: DbConnection) -> None: ...
    @DesignTimeVisible.setter
    def DesignTimeVisible(self, value: bool) -> None: ...
    @Transaction.setter
    def Transaction(self, value: DbTransaction) -> None: ...
    @UpdatedRowSource.setter
    def UpdatedRowSource(self, value: UpdateRowSource) -> None: ...


class DbCommandBuilder(Component):
    @property
    def CatalogLocation(self) -> CatalogLocation: ...
    @property
    def CatalogSeparator(self) -> str: ...
    @property
    def ConflictOption(self) -> ConflictOption: ...
    @property
    def DataAdapter(self) -> DbDataAdapter: ...
    @property
    def QuotePrefix(self) -> str: ...
    @property
    def QuoteSuffix(self) -> str: ...
    @property
    def SchemaSeparator(self) -> str: ...
    @property
    def SetAllValues(self) -> bool: ...
    @overload
    def GetDeleteCommand(self) -> DbCommand: ...
    @overload
    def GetDeleteCommand(self, useColumnsForParameterNames: bool) -> DbCommand: ...
    @overload
    def GetInsertCommand(self) -> DbCommand: ...
    @overload
    def GetInsertCommand(self, useColumnsForParameterNames: bool) -> DbCommand: ...
    @overload
    def GetUpdateCommand(self) -> DbCommand: ...
    @overload
    def GetUpdateCommand(self, useColumnsForParameterNames: bool) -> DbCommand: ...
    def QuoteIdentifier(self, unquotedIdentifier: str) -> str: ...
    def RefreshSchema(self) -> None: ...
    @CatalogLocation.setter
    def CatalogLocation(self, value: CatalogLocation) -> None: ...
    @CatalogSeparator.setter
    def CatalogSeparator(self, value: str) -> None: ...
    @ConflictOption.setter
    def ConflictOption(self, value: ConflictOption) -> None: ...
    @DataAdapter.setter
    def DataAdapter(self, value: DbDataAdapter) -> None: ...
    @QuotePrefix.setter
    def QuotePrefix(self, value: str) -> None: ...
    @QuoteSuffix.setter
    def QuoteSuffix(self, value: str) -> None: ...
    @SchemaSeparator.setter
    def SchemaSeparator(self, value: str) -> None: ...
    @SetAllValues.setter
    def SetAllValues(self, value: bool) -> None: ...
    def UnquoteIdentifier(self, quotedIdentifier: str) -> str: ...


class DbConnection(Component):
    def add_StateChange(self, value: StateChangeEventHandler) -> None: ...
    @overload
    def BeginTransaction(self) -> DbTransaction: ...
    @overload
    def BeginTransaction(self, isolationLevel: IsolationLevel) -> DbTransaction: ...
    @overload
    def BeginTransactionAsync(self, cancellationToken: CancellationToken) -> ValueTask: ...
    @overload
    def BeginTransactionAsync(self, isolationLevel: IsolationLevel, cancellationToken: CancellationToken) -> ValueTask: ...
    def ChangeDatabase(self, databaseName: str) -> None: ...
    def ChangeDatabaseAsync(self, databaseName: str, cancellationToken: CancellationToken) -> Task: ...
    def Close(self) -> None: ...
    def CloseAsync(self) -> Task: ...
    def CreateBatch(self) -> DbBatch: ...
    def CreateCommand(self) -> DbCommand: ...
    def DisposeAsync(self) -> ValueTask: ...
    def EnlistTransaction(self, transaction: Transaction) -> None: ...
    @property
    def CanCreateBatch(self) -> bool: ...
    @property
    def ConnectionString(self) -> str: ...
    @property
    def ConnectionTimeout(self) -> int: ...
    @property
    def Database(self) -> str: ...
    @property
    def DataSource(self) -> str: ...
    @property
    def ServerVersion(self) -> str: ...
    @property
    def State(self) -> ConnectionState: ...
    @overload
    def GetSchema(self) -> DataTable: ...
    @overload
    def GetSchema(self, collectionName: str) -> DataTable: ...
    @overload
    def GetSchema(self, collectionName: str, restrictionValues: Set(str)) -> DataTable: ...
    @overload
    def GetSchemaAsync(self, cancellationToken: CancellationToken) -> Task: ...
    @overload
    def GetSchemaAsync(self, collectionName: str, cancellationToken: CancellationToken) -> Task: ...
    @overload
    def GetSchemaAsync(self, collectionName: str, restrictionValues: Set(str), cancellationToken: CancellationToken) -> Task: ...
    def Open(self) -> None: ...
    @overload
    def OpenAsync(self) -> Task: ...
    @overload
    def OpenAsync(self, cancellationToken: CancellationToken) -> Task: ...
    def remove_StateChange(self, value: StateChangeEventHandler) -> None: ...
    @ConnectionString.setter
    def ConnectionString(self, value: str) -> None: ...


class DbConnectionStringBuilder(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, useOdbcRules: bool): ...
    def Add(self, keyword: str, value: Object) -> None: ...
    @overload
    def AppendKeyValuePair(builder: StringBuilder, keyword: str, value: str) -> None: ...
    @overload
    def AppendKeyValuePair(builder: StringBuilder, keyword: str, value: str, useOdbcRules: bool) -> None: ...
    def Clear(self) -> None: ...
    def ContainsKey(self, keyword: str) -> bool: ...
    def EquivalentTo(self, connectionStringBuilder: DbConnectionStringBuilder) -> bool: ...
    @property
    def BrowsableConnectionString(self) -> bool: ...
    @property
    def ConnectionString(self) -> str: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsFixedSize(self) -> bool: ...
    @property
    def IsReadOnly(self) -> bool: ...
    @property
    def Item(self, keyword: str) -> Object: ...
    @property
    def Keys(self) -> ICollection: ...
    @property
    def Values(self) -> ICollection: ...
    def Remove(self, keyword: str) -> bool: ...
    @BrowsableConnectionString.setter
    def BrowsableConnectionString(self, value: bool) -> None: ...
    @ConnectionString.setter
    def ConnectionString(self, value: str) -> None: ...
    @Item.setter
    def Item(self, keyword: str, value: Object) -> None: ...
    def ShouldSerialize(self, keyword: str) -> bool: ...
    def ToString(self) -> str: ...
    def TryGetValue(self, keyword: str) -> Tuple[bool, Object]: ...


class DbDataAdapter(DataAdapter):
    @overload
    def Fill(self, dataTable: DataTable) -> int: ...
    @overload
    def Fill(self, dataSet: DataSet) -> int: ...
    @overload
    def Fill(self, dataSet: DataSet, srcTable: str) -> int: ...
    @overload
    def Fill(self, startRecord: int, maxRecords: int, dataTables: Set(DataTable)) -> int: ...
    @overload
    def Fill(self, dataSet: DataSet, startRecord: int, maxRecords: int, srcTable: str) -> int: ...
    @overload
    def FillSchema(self, dataTable: DataTable, schemaType: SchemaType) -> DataTable: ...
    @overload
    def FillSchema(self, dataSet: DataSet, schemaType: SchemaType) -> Set(DataTable): ...
    @overload
    def FillSchema(self, dataSet: DataSet, schemaType: SchemaType, srcTable: str) -> Set(DataTable): ...
    @property
    def DeleteCommand(self) -> DbCommand: ...
    @property
    def InsertCommand(self) -> DbCommand: ...
    @property
    def SelectCommand(self) -> DbCommand: ...
    @property
    def UpdateBatchSize(self) -> int: ...
    @property
    def UpdateCommand(self) -> DbCommand: ...
    def GetFillParameters(self) -> Set(IDataParameter): ...
    @DeleteCommand.setter
    def DeleteCommand(self, value: DbCommand) -> None: ...
    @InsertCommand.setter
    def InsertCommand(self, value: DbCommand) -> None: ...
    @SelectCommand.setter
    def SelectCommand(self, value: DbCommand) -> None: ...
    @UpdateBatchSize.setter
    def UpdateBatchSize(self, value: int) -> None: ...
    @UpdateCommand.setter
    def UpdateCommand(self, value: DbCommand) -> None: ...
    @overload
    def Update(self, dataSet: DataSet) -> int: ...
    @overload
    def Update(self, dataTable: DataTable) -> int: ...
    @overload
    def Update(self, dataRows: Set(DataRow)) -> int: ...
    @overload
    def Update(self, dataSet: DataSet, srcTable: str) -> int: ...


class DbDataReader(MarshalByRefObject):
    def Close(self) -> None: ...
    def CloseAsync(self) -> Task: ...
    def Dispose(self) -> None: ...
    def DisposeAsync(self) -> ValueTask: ...
    @property
    def Depth(self) -> int: ...
    @property
    def FieldCount(self) -> int: ...
    @property
    def HasRows(self) -> bool: ...
    @property
    def IsClosed(self) -> bool: ...
    @property
    def Item(self, ordinal: int) -> Object: ...
    @property
    def Item(self, name: str) -> Object: ...
    @property
    def RecordsAffected(self) -> int: ...
    @property
    def VisibleFieldCount(self) -> int: ...
    def GetBoolean(self, ordinal: int) -> bool: ...
    def GetByte(self, ordinal: int) -> Byte: ...
    def GetBytes(self, ordinal: int, dataOffset: Int64, buffer: Set(Byte), bufferOffset: int, length: int) -> Int64: ...
    def GetChar(self, ordinal: int) -> Char: ...
    def GetChars(self, ordinal: int, dataOffset: Int64, buffer: Set(Char), bufferOffset: int, length: int) -> Int64: ...
    def GetColumnSchemaAsync(self, cancellationToken: CancellationToken) -> Task: ...
    def GetData(self, ordinal: int) -> DbDataReader: ...
    def GetDataTypeName(self, ordinal: int) -> str: ...
    def GetDateTime(self, ordinal: int) -> DateTime: ...
    def GetDecimal(self, ordinal: int) -> Decimal: ...
    def GetDouble(self, ordinal: int) -> float: ...
    def GetEnumerator(self) -> IEnumerator: ...
    def GetFieldType(self, ordinal: int) -> Type: ...
    def GetFieldValue(self, ordinal: int) -> T: ...
    @overload
    def GetFieldValueAsync(self, ordinal: int) -> Task: ...
    @overload
    def GetFieldValueAsync(self, ordinal: int, cancellationToken: CancellationToken) -> Task: ...
    def GetFloat(self, ordinal: int) -> Single: ...
    def GetGuid(self, ordinal: int) -> Guid: ...
    def GetInt16(self, ordinal: int) -> Int16: ...
    def GetInt32(self, ordinal: int) -> int: ...
    def GetInt64(self, ordinal: int) -> Int64: ...
    def GetName(self, ordinal: int) -> str: ...
    def GetOrdinal(self, name: str) -> int: ...
    def GetProviderSpecificFieldType(self, ordinal: int) -> Type: ...
    def GetProviderSpecificValue(self, ordinal: int) -> Object: ...
    def GetProviderSpecificValues(self, values: Set(Object)) -> int: ...
    def GetSchemaTable(self) -> DataTable: ...
    def GetSchemaTableAsync(self, cancellationToken: CancellationToken) -> Task: ...
    def GetStream(self, ordinal: int) -> Stream: ...
    def GetString(self, ordinal: int) -> str: ...
    def GetTextReader(self, ordinal: int) -> TextReader: ...
    def GetValue(self, ordinal: int) -> Object: ...
    def GetValues(self, values: Set(Object)) -> int: ...
    def IsDBNull(self, ordinal: int) -> bool: ...
    @overload
    def IsDBNullAsync(self, ordinal: int) -> Task: ...
    @overload
    def IsDBNullAsync(self, ordinal: int, cancellationToken: CancellationToken) -> Task: ...
    def NextResult(self) -> bool: ...
    @overload
    def NextResultAsync(self) -> Task: ...
    @overload
    def NextResultAsync(self, cancellationToken: CancellationToken) -> Task: ...
    def Read(self) -> bool: ...
    @overload
    def ReadAsync(self) -> Task: ...
    @overload
    def ReadAsync(self, cancellationToken: CancellationToken) -> Task: ...


class DbDataReaderExtensions(Object):
    def CanGetColumnSchema(reader: DbDataReader) -> bool: ...
    def GetColumnSchema(reader: DbDataReader) -> ReadOnlyCollection: ...


class DbDataRecord(Object):
    @property
    def FieldCount(self) -> int: ...
    @property
    def Item(self, i: int) -> Object: ...
    @property
    def Item(self, name: str) -> Object: ...
    def GetBoolean(self, i: int) -> bool: ...
    def GetByte(self, i: int) -> Byte: ...
    def GetBytes(self, i: int, dataIndex: Int64, buffer: Set(Byte), bufferIndex: int, length: int) -> Int64: ...
    def GetChar(self, i: int) -> Char: ...
    def GetChars(self, i: int, dataIndex: Int64, buffer: Set(Char), bufferIndex: int, length: int) -> Int64: ...
    def GetData(self, i: int) -> IDataReader: ...
    def GetDataTypeName(self, i: int) -> str: ...
    def GetDateTime(self, i: int) -> DateTime: ...
    def GetDecimal(self, i: int) -> Decimal: ...
    def GetDouble(self, i: int) -> float: ...
    def GetFieldType(self, i: int) -> Type: ...
    def GetFloat(self, i: int) -> Single: ...
    def GetGuid(self, i: int) -> Guid: ...
    def GetInt16(self, i: int) -> Int16: ...
    def GetInt32(self, i: int) -> int: ...
    def GetInt64(self, i: int) -> Int64: ...
    def GetName(self, i: int) -> str: ...
    def GetOrdinal(self, name: str) -> int: ...
    def GetString(self, i: int) -> str: ...
    def GetValue(self, i: int) -> Object: ...
    def GetValues(self, values: Set(Object)) -> int: ...
    def IsDBNull(self, i: int) -> bool: ...


class DbDataSourceEnumerator(Object):
    def GetDataSources(self) -> DataTable: ...


class DbEnumerator(Object):
    @overload
    def __init__(self, reader: IDataReader): ...
    @overload
    def __init__(self, reader: DbDataReader): ...
    @overload
    def __init__(self, reader: IDataReader, closeReader: bool): ...
    @overload
    def __init__(self, reader: DbDataReader, closeReader: bool): ...
    @property
    def Current(self) -> Object: ...
    def MoveNext(self) -> bool: ...
    def Reset(self) -> None: ...


class DbException(ExternalException):
    @property
    def BatchCommand(self) -> DbBatchCommand: ...
    @property
    def IsTransient(self) -> bool: ...
    @property
    def SqlState(self) -> str: ...


class DbMetaDataCollectionNames(Object):
    pass


class DbMetaDataColumnNames(Object):
    pass


class DbParameter(MarshalByRefObject):
    @property
    def DbType(self) -> DbType: ...
    @property
    def Direction(self) -> ParameterDirection: ...
    @property
    def IsNullable(self) -> bool: ...
    @property
    def ParameterName(self) -> str: ...
    @property
    def Precision(self) -> Byte: ...
    @property
    def Scale(self) -> Byte: ...
    @property
    def Size(self) -> int: ...
    @property
    def SourceColumn(self) -> str: ...
    @property
    def SourceColumnNullMapping(self) -> bool: ...
    @property
    def SourceVersion(self) -> DataRowVersion: ...
    @property
    def Value(self) -> Object: ...
    def ResetDbType(self) -> None: ...
    @DbType.setter
    def DbType(self, value: DbType) -> None: ...
    @Direction.setter
    def Direction(self, value: ParameterDirection) -> None: ...
    @IsNullable.setter
    def IsNullable(self, value: bool) -> None: ...
    @ParameterName.setter
    def ParameterName(self, value: str) -> None: ...
    @Precision.setter
    def Precision(self, value: Byte) -> None: ...
    @Scale.setter
    def Scale(self, value: Byte) -> None: ...
    @Size.setter
    def Size(self, value: int) -> None: ...
    @SourceColumn.setter
    def SourceColumn(self, value: str) -> None: ...
    @SourceColumnNullMapping.setter
    def SourceColumnNullMapping(self, value: bool) -> None: ...
    @SourceVersion.setter
    def SourceVersion(self, value: DataRowVersion) -> None: ...
    @Value.setter
    def Value(self, value: Object) -> None: ...


class DbParameterCollection(MarshalByRefObject):
    def Add(self, value: Object) -> int: ...
    def AddRange(self, values: Array) -> None: ...
    def Clear(self) -> None: ...
    @overload
    def Contains(self, value: str) -> bool: ...
    @overload
    def Contains(self, value: Object) -> bool: ...
    def CopyTo(self, array: Array, index: int) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def IsFixedSize(self) -> bool: ...
    @property
    def IsReadOnly(self) -> bool: ...
    @property
    def IsSynchronized(self) -> bool: ...
    @property
    def Item(self, index: int) -> DbParameter: ...
    @property
    def Item(self, parameterName: str) -> DbParameter: ...
    @property
    def SyncRoot(self) -> Object: ...
    def GetEnumerator(self) -> IEnumerator: ...
    @overload
    def IndexOf(self, parameterName: str) -> int: ...
    @overload
    def IndexOf(self, value: Object) -> int: ...
    def Insert(self, index: int, value: Object) -> None: ...
    def Remove(self, value: Object) -> None: ...
    @overload
    def RemoveAt(self, index: int) -> None: ...
    @overload
    def RemoveAt(self, parameterName: str) -> None: ...
    @Item.setter
    def Item(self, index: int, value: DbParameter) -> None: ...
    @Item.setter
    def Item(self, parameterName: str, value: DbParameter) -> None: ...


class DbProviderFactories(Object):
    @overload
    def GetFactory(providerInvariantName: str) -> DbProviderFactory: ...
    @overload
    def GetFactory(providerRow: DataRow) -> DbProviderFactory: ...
    @overload
    def GetFactory(connection: DbConnection) -> DbProviderFactory: ...
    def GetFactoryClasses() -> DataTable: ...
    def GetProviderInvariantNames() -> Iterable[str]: ...
    @overload
    def RegisterFactory(providerInvariantName: str, factoryTypeAssemblyQualifiedName: str) -> None: ...
    @overload
    def RegisterFactory(providerInvariantName: str, providerFactoryClass: Type) -> None: ...
    @overload
    def RegisterFactory(providerInvariantName: str, factory: DbProviderFactory) -> None: ...
    def TryGetFactory(providerInvariantName: str) -> Tuple[bool, DbProviderFactory]: ...
    def UnregisterFactory(providerInvariantName: str) -> bool: ...


class DbProviderFactory(Object):
    def CreateBatch(self) -> DbBatch: ...
    def CreateBatchCommand(self) -> DbBatchCommand: ...
    def CreateCommand(self) -> DbCommand: ...
    def CreateCommandBuilder(self) -> DbCommandBuilder: ...
    def CreateConnection(self) -> DbConnection: ...
    def CreateConnectionStringBuilder(self) -> DbConnectionStringBuilder: ...
    def CreateDataAdapter(self) -> DbDataAdapter: ...
    def CreateDataSourceEnumerator(self) -> DbDataSourceEnumerator: ...
    def CreateParameter(self) -> DbParameter: ...
    @property
    def CanCreateBatch(self) -> bool: ...
    @property
    def CanCreateCommandBuilder(self) -> bool: ...
    @property
    def CanCreateDataAdapter(self) -> bool: ...
    @property
    def CanCreateDataSourceEnumerator(self) -> bool: ...


class DbProviderSpecificTypePropertyAttribute(Attribute):
    def __init__(self, isProviderSpecificTypeProperty: bool): ...
    @property
    def IsProviderSpecificTypeProperty(self) -> bool: ...


class DbTransaction(MarshalByRefObject):
    def Commit(self) -> None: ...
    def CommitAsync(self, cancellationToken: CancellationToken) -> Task: ...
    def Dispose(self) -> None: ...
    def DisposeAsync(self) -> ValueTask: ...
    @property
    def Connection(self) -> DbConnection: ...
    @property
    def IsolationLevel(self) -> IsolationLevel: ...
    @property
    def SupportsSavepoints(self) -> bool: ...
    def Release(self, savepointName: str) -> None: ...
    def ReleaseAsync(self, savepointName: str, cancellationToken: CancellationToken) -> Task: ...
    @overload
    def Rollback(self) -> None: ...
    @overload
    def Rollback(self, savepointName: str) -> None: ...
    @overload
    def RollbackAsync(self, cancellationToken: CancellationToken) -> Task: ...
    @overload
    def RollbackAsync(self, savepointName: str, cancellationToken: CancellationToken) -> Task: ...
    def Save(self, savepointName: str) -> None: ...
    def SaveAsync(self, savepointName: str, cancellationToken: CancellationToken) -> Task: ...


class GroupByBehavior:
    Unknown = 0
    NotSupported = 1
    Unrelated = 2
    MustContainAll = 3
    ExactMatch = 4


class IDbColumnSchemaGenerator:
    def GetColumnSchema(self) -> ReadOnlyCollection: ...


class IdentifierCase:
    Unknown = 0
    Insensitive = 1
    Sensitive = 2


class RowUpdatedEventArgs(EventArgs):
    def __init__(self, dataRow: DataRow, command: IDbCommand, statementType: StatementType, tableMapping: DataTableMapping): ...
    @overload
    def CopyToRows(self, array: Set(DataRow)) -> None: ...
    @overload
    def CopyToRows(self, array: Set(DataRow), arrayIndex: int) -> None: ...
    @property
    def Command(self) -> IDbCommand: ...
    @property
    def Errors(self) -> Exception: ...
    @property
    def RecordsAffected(self) -> int: ...
    @property
    def Row(self) -> DataRow: ...
    @property
    def RowCount(self) -> int: ...
    @property
    def StatementType(self) -> StatementType: ...
    @property
    def Status(self) -> UpdateStatus: ...
    @property
    def TableMapping(self) -> DataTableMapping: ...
    @Errors.setter
    def Errors(self, value: Exception) -> None: ...
    @Status.setter
    def Status(self, value: UpdateStatus) -> None: ...


class RowUpdatingEventArgs(EventArgs):
    def __init__(self, dataRow: DataRow, command: IDbCommand, statementType: StatementType, tableMapping: DataTableMapping): ...
    @property
    def Command(self) -> IDbCommand: ...
    @property
    def Errors(self) -> Exception: ...
    @property
    def Row(self) -> DataRow: ...
    @property
    def StatementType(self) -> StatementType: ...
    @property
    def Status(self) -> UpdateStatus: ...
    @property
    def TableMapping(self) -> DataTableMapping: ...
    @Command.setter
    def Command(self, value: IDbCommand) -> None: ...
    @Errors.setter
    def Errors(self, value: Exception) -> None: ...
    @Status.setter
    def Status(self, value: UpdateStatus) -> None: ...


class SchemaTableColumn(Object):
    pass


class SchemaTableOptionalColumn(Object):
    pass


class SupportedJoinOperators:
    #None = 0
    Inner = 1
    LeftOuter = 2
    RightOuter = 4
    FullOuter = 8
