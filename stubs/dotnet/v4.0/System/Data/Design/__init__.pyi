from typing import Tuple, Set, Iterable, List


class GenerateOption:
    #None = 0
    HierarchicalUpdate = 1
    LinqOverTypedDatasets = 2


class MethodSignatureGenerator(Object):
    def __init__(self): ...
    def GenerateMethod(self) -> CodeMemberMethod: ...
    def GenerateMethodSignature(self) -> str: ...
    def GenerateUpdatingMethods(self) -> CodeTypeDeclaration: ...
    @property
    def CodeProvider(self) -> CodeDomProvider: ...
    @property
    def ContainerParameterType(self) -> Type: ...
    @property
    def DataSetClassName(self) -> str: ...
    @property
    def IsGetMethod(self) -> bool: ...
    @property
    def PagingMethod(self) -> bool: ...
    @property
    def ParameterOption(self) -> ParameterGenerationOption: ...
    @property
    def TableClassName(self) -> str: ...
    @CodeProvider.setter
    def CodeProvider(self, value: CodeDomProvider) -> None: ...
    @ContainerParameterType.setter
    def ContainerParameterType(self, value: Type) -> None: ...
    @DataSetClassName.setter
    def DataSetClassName(self, value: str) -> None: ...
    @IsGetMethod.setter
    def IsGetMethod(self, value: bool) -> None: ...
    @PagingMethod.setter
    def PagingMethod(self, value: bool) -> None: ...
    @ParameterOption.setter
    def ParameterOption(self, value: ParameterGenerationOption) -> None: ...
    @TableClassName.setter
    def TableClassName(self, value: str) -> None: ...
    def SetDesignTableContent(self, designTableContent: str) -> None: ...
    def SetMethodSourceContent(self, methodSourceContent: str) -> None: ...


class ParameterGenerationOption:
    ClrTypes = 0
    SqlTypes = 1
    Objects = 2


class TypedDataSetGenerator(Object):
    @overload
    def Generate(dataSet: DataSet, codeNamespace: CodeNamespace, codeProvider: CodeDomProvider) -> str: ...
    @overload
    def Generate(inputFileContent: str, compileUnit: CodeCompileUnit, mainNamespace: CodeNamespace, codeProvider: CodeDomProvider) -> str: ...
    @overload
    def Generate(inputFileContent: str, compileUnit: CodeCompileUnit, mainNamespace: CodeNamespace, codeProvider: CodeDomProvider, specifiedFactory: DbProviderFactory) -> None: ...
    @overload
    def Generate(inputFileContent: str, compileUnit: CodeCompileUnit, mainNamespace: CodeNamespace, codeProvider: CodeDomProvider, customDBProviders: Hashtable) -> None: ...
    @overload
    def Generate(inputFileContent: str, compileUnit: CodeCompileUnit, mainNamespace: CodeNamespace, codeProvider: CodeDomProvider, option: GenerateOption) -> str: ...
    @overload
    def Generate(inputFileContent: str, compileUnit: CodeCompileUnit, mainNamespace: CodeNamespace, codeProvider: CodeDomProvider, customDBProviders: Hashtable, option: GenerateOption) -> None: ...
    @overload
    def Generate(inputFileContent: str, compileUnit: CodeCompileUnit, mainNamespace: CodeNamespace, codeProvider: CodeDomProvider, option: GenerateOption, dataSetNamespace: str) -> str: ...
    @overload
    def Generate(inputFileContent: str, compileUnit: CodeCompileUnit, mainNamespace: CodeNamespace, codeProvider: CodeDomProvider, option: GenerateOption, dataSetNamespace: str, basePath: str) -> str: ...
    @overload
    def Generate(inputFileContent: str, compileUnit: CodeCompileUnit, mainNamespace: CodeNamespace, codeProvider: CodeDomProvider, customDBProviders: Hashtable, option: GenerateOption, dataSetNamespace: str) -> None: ...
    @overload
    def Generate(inputFileContent: str, compileUnit: CodeCompileUnit, mainNamespace: CodeNamespace, codeProvider: CodeDomProvider, customDBProviders: Hashtable, option: GenerateOption, dataSetNamespace: str, basePath: str) -> None: ...
    @property
    def ReferencedAssemblies() -> ICollection: ...
    @overload
    def GetProviderName(inputFileContent: str) -> str: ...
    @overload
    def GetProviderName(inputFileContent: str, tableName: str) -> str: ...


class TypedDataSetGeneratorException(DataException):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, message: str): ...
    @overload
    def __init__(self, list: IList): ...
    @overload
    def __init__(self, message: str, innerException: Exception): ...
    @property
    def ErrorList(self) -> IList: ...
    def GetObjectData(self, info: SerializationInfo, context: StreamingContext) -> None: ...


class TypedDataSetSchemaImporterExtension(SchemaImporterExtension):
    def __init__(self): ...
    @overload
    def ImportSchemaType(self, type: XmlSchemaType, context: XmlSchemaObject, schemas: XmlSchemas, importer: XmlSchemaImporter, compileUnit: CodeCompileUnit, mainNamespace: CodeNamespace, options: CodeGenerationOptions, codeProvider: CodeDomProvider) -> str: ...
    @overload
    def ImportSchemaType(self, name: str, namespaceName: str, context: XmlSchemaObject, schemas: XmlSchemas, importer: XmlSchemaImporter, compileUnit: CodeCompileUnit, mainNamespace: CodeNamespace, options: CodeGenerationOptions, codeProvider: CodeDomProvider) -> str: ...


class TypedDataSetSchemaImporterExtensionFx35(TypedDataSetSchemaImporterExtension):
    def __init__(self): ...
