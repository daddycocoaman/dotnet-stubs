from typing import Tuple, Set, Iterable, List


class CodeCompiler(CodeGenerator):
    pass


class CodeDomProvider(Component):
    def CompileAssemblyFromDom(self, options: CompilerParameters, compilationUnits: Set(CodeCompileUnit)) -> CompilerResults: ...
    def CompileAssemblyFromFile(self, options: CompilerParameters, fileNames: Set(str)) -> CompilerResults: ...
    def CompileAssemblyFromSource(self, options: CompilerParameters, sources: Set(str)) -> CompilerResults: ...
    def CreateEscapedIdentifier(self, value: str) -> str: ...
    @overload
    def CreateGenerator(self, output: TextWriter) -> ICodeGenerator: ...
    @overload
    def CreateGenerator(self, fileName: str) -> ICodeGenerator: ...
    @overload
    def CreateProvider(language: str) -> CodeDomProvider: ...
    @overload
    def CreateProvider(language: str, providerOptions: IDictionary) -> CodeDomProvider: ...
    def CreateValidIdentifier(self, value: str) -> str: ...
    def GenerateCodeFromCompileUnit(self, compileUnit: CodeCompileUnit, writer: TextWriter, options: CodeGeneratorOptions) -> None: ...
    def GenerateCodeFromExpression(self, expression: CodeExpression, writer: TextWriter, options: CodeGeneratorOptions) -> None: ...
    def GenerateCodeFromMember(self, member: CodeTypeMember, writer: TextWriter, options: CodeGeneratorOptions) -> None: ...
    def GenerateCodeFromNamespace(self, codeNamespace: CodeNamespace, writer: TextWriter, options: CodeGeneratorOptions) -> None: ...
    def GenerateCodeFromStatement(self, statement: CodeStatement, writer: TextWriter, options: CodeGeneratorOptions) -> None: ...
    def GenerateCodeFromType(self, codeType: CodeTypeDeclaration, writer: TextWriter, options: CodeGeneratorOptions) -> None: ...
    @property
    def FileExtension(self) -> str: ...
    @property
    def LanguageOptions(self) -> LanguageOptions: ...
    def GetAllCompilerInfo() -> Set(CompilerInfo): ...
    def GetCompilerInfo(language: str) -> CompilerInfo: ...
    def GetConverter(self, type: Type) -> TypeConverter: ...
    def GetLanguageFromExtension(extension: str) -> str: ...
    def GetTypeOutput(self, type: CodeTypeReference) -> str: ...
    def IsDefinedExtension(extension: str) -> bool: ...
    def IsDefinedLanguage(language: str) -> bool: ...
    def IsValidIdentifier(self, value: str) -> bool: ...
    def Parse(self, codeStream: TextReader) -> CodeCompileUnit: ...
    def Supports(self, generatorSupport: GeneratorSupport) -> bool: ...


class CodeGenerator(Object):
    def GenerateCodeFromMember(self, member: CodeTypeMember, writer: TextWriter, options: CodeGeneratorOptions) -> None: ...
    def IsValidLanguageIndependentIdentifier(value: str) -> bool: ...
    def ValidateIdentifiers(e: CodeObject) -> None: ...


class CodeGeneratorOptions(Object):
    def __init__(self): ...
    @property
    def BlankLinesBetweenMembers(self) -> bool: ...
    @property
    def BracingStyle(self) -> str: ...
    @property
    def ElseOnClosing(self) -> bool: ...
    @property
    def IndentString(self) -> str: ...
    @property
    def Item(self, index: str) -> Object: ...
    @property
    def VerbatimOrder(self) -> bool: ...
    @BlankLinesBetweenMembers.setter
    def BlankLinesBetweenMembers(self, value: bool) -> None: ...
    @BracingStyle.setter
    def BracingStyle(self, value: str) -> None: ...
    @ElseOnClosing.setter
    def ElseOnClosing(self, value: bool) -> None: ...
    @IndentString.setter
    def IndentString(self, value: str) -> None: ...
    @Item.setter
    def Item(self, index: str, value: Object) -> None: ...
    @VerbatimOrder.setter
    def VerbatimOrder(self, value: bool) -> None: ...


class CodeParser(Object):
    def Parse(self, codeStream: TextReader) -> CodeCompileUnit: ...


class CompilerError(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, fileName: str, line: int, column: int, errorNumber: str, errorText: str): ...
    @property
    def Column(self) -> int: ...
    @property
    def ErrorNumber(self) -> str: ...
    @property
    def ErrorText(self) -> str: ...
    @property
    def FileName(self) -> str: ...
    @property
    def IsWarning(self) -> bool: ...
    @property
    def Line(self) -> int: ...
    @Column.setter
    def Column(self, value: int) -> None: ...
    @ErrorNumber.setter
    def ErrorNumber(self, value: str) -> None: ...
    @ErrorText.setter
    def ErrorText(self, value: str) -> None: ...
    @FileName.setter
    def FileName(self, value: str) -> None: ...
    @IsWarning.setter
    def IsWarning(self, value: bool) -> None: ...
    @Line.setter
    def Line(self, value: int) -> None: ...
    def ToString(self) -> str: ...


class CompilerErrorCollection(CollectionBase):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, value: CompilerErrorCollection): ...
    @overload
    def __init__(self, value: Set(CompilerError)): ...
    def Add(self, value: CompilerError) -> int: ...
    @overload
    def AddRange(self, value: Set(CompilerError)) -> None: ...
    @overload
    def AddRange(self, value: CompilerErrorCollection) -> None: ...
    def Contains(self, value: CompilerError) -> bool: ...
    def CopyTo(self, array: Set(CompilerError), index: int) -> None: ...
    @property
    def HasErrors(self) -> bool: ...
    @property
    def HasWarnings(self) -> bool: ...
    @property
    def Item(self, index: int) -> CompilerError: ...
    def IndexOf(self, value: CompilerError) -> int: ...
    def Insert(self, index: int, value: CompilerError) -> None: ...
    def Remove(self, value: CompilerError) -> None: ...
    @Item.setter
    def Item(self, index: int, value: CompilerError) -> None: ...


class CompilerInfo(Object):
    def CreateDefaultCompilerParameters(self) -> CompilerParameters: ...
    @overload
    def CreateProvider(self) -> CodeDomProvider: ...
    @overload
    def CreateProvider(self, providerOptions: IDictionary) -> CodeDomProvider: ...
    def Equals(self, o: Object) -> bool: ...
    @property
    def CodeDomProviderType(self) -> Type: ...
    @property
    def IsCodeDomProviderTypeValid(self) -> bool: ...
    def GetExtensions(self) -> Set(str): ...
    def GetHashCode(self) -> int: ...
    def GetLanguages(self) -> Set(str): ...


class CompilerParameters(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, assemblyNames: Set(str)): ...
    @overload
    def __init__(self, assemblyNames: Set(str), outputName: str): ...
    @overload
    def __init__(self, assemblyNames: Set(str), outputName: str, includeDebugInformation: bool): ...
    @property
    def CompilerOptions(self) -> str: ...
    @property
    def CoreAssemblyFileName(self) -> str: ...
    @property
    def EmbeddedResources(self) -> StringCollection: ...
    @property
    def GenerateExecutable(self) -> bool: ...
    @property
    def GenerateInMemory(self) -> bool: ...
    @property
    def IncludeDebugInformation(self) -> bool: ...
    @property
    def LinkedResources(self) -> StringCollection: ...
    @property
    def MainClass(self) -> str: ...
    @property
    def OutputAssembly(self) -> str: ...
    @property
    def ReferencedAssemblies(self) -> StringCollection: ...
    @property
    def TempFiles(self) -> TempFileCollection: ...
    @property
    def TreatWarningsAsErrors(self) -> bool: ...
    @property
    def UserToken(self) -> IntPtr: ...
    @property
    def WarningLevel(self) -> int: ...
    @property
    def Win32Resource(self) -> str: ...
    @CompilerOptions.setter
    def CompilerOptions(self, value: str) -> None: ...
    @CoreAssemblyFileName.setter
    def CoreAssemblyFileName(self, value: str) -> None: ...
    @GenerateExecutable.setter
    def GenerateExecutable(self, value: bool) -> None: ...
    @GenerateInMemory.setter
    def GenerateInMemory(self, value: bool) -> None: ...
    @IncludeDebugInformation.setter
    def IncludeDebugInformation(self, value: bool) -> None: ...
    @MainClass.setter
    def MainClass(self, value: str) -> None: ...
    @OutputAssembly.setter
    def OutputAssembly(self, value: str) -> None: ...
    @TempFiles.setter
    def TempFiles(self, value: TempFileCollection) -> None: ...
    @TreatWarningsAsErrors.setter
    def TreatWarningsAsErrors(self, value: bool) -> None: ...
    @UserToken.setter
    def UserToken(self, value: IntPtr) -> None: ...
    @WarningLevel.setter
    def WarningLevel(self, value: int) -> None: ...
    @Win32Resource.setter
    def Win32Resource(self, value: str) -> None: ...


class CompilerResults(Object):
    def __init__(self, tempFiles: TempFileCollection): ...
    @property
    def CompiledAssembly(self) -> Assembly: ...
    @property
    def Errors(self) -> CompilerErrorCollection: ...
    @property
    def NativeCompilerReturnValue(self) -> int: ...
    @property
    def Output(self) -> StringCollection: ...
    @property
    def PathToAssembly(self) -> str: ...
    @property
    def TempFiles(self) -> TempFileCollection: ...
    @CompiledAssembly.setter
    def CompiledAssembly(self, value: Assembly) -> None: ...
    @NativeCompilerReturnValue.setter
    def NativeCompilerReturnValue(self, value: int) -> None: ...
    @PathToAssembly.setter
    def PathToAssembly(self, value: str) -> None: ...
    @TempFiles.setter
    def TempFiles(self, value: TempFileCollection) -> None: ...


class Executor(Object):
    def ExecWait(cmd: str, tempFiles: TempFileCollection) -> None: ...
    @overload
    def ExecWaitWithCapture(cmd: str, tempFiles: TempFileCollection, outputName: str, errorName: str) -> Tuple[int, str, str]: ...
    @overload
    def ExecWaitWithCapture(userToken: IntPtr, cmd: str, tempFiles: TempFileCollection, outputName: str, errorName: str) -> Tuple[int, str, str]: ...
    @overload
    def ExecWaitWithCapture(cmd: str, currentDir: str, tempFiles: TempFileCollection, outputName: str, errorName: str) -> Tuple[int, str, str]: ...
    @overload
    def ExecWaitWithCapture(userToken: IntPtr, cmd: str, currentDir: str, tempFiles: TempFileCollection, outputName: str, errorName: str) -> Tuple[int, str, str]: ...


class GeneratorSupport:
    ArraysOfArrays = 1
    EntryPointMethod = 2
    GotoStatements = 4
    MultidimensionalArrays = 8
    StaticConstructors = 16
    TryCatchStatements = 32
    ReturnTypeAttributes = 64
    DeclareValueTypes = 128
    DeclareEnums = 256
    DeclareDelegates = 512
    DeclareInterfaces = 1024
    DeclareEvents = 2048
    AssemblyAttributes = 4096
    ParameterAttributes = 8192
    ReferenceParameters = 16384
    ChainedConstructorArguments = 32768
    NestedTypes = 65536
    MultipleInterfaceMembers = 131072
    PublicStaticMembers = 262144
    ComplexExpressions = 524288
    Win32Resources = 1048576
    Resources = 2097152
    PartialTypes = 4194304
    GenericTypeReference = 8388608
    GenericTypeDeclaration = 16777216
    DeclareIndexerProperties = 33554432


class ICodeCompiler:
    def CompileAssemblyFromDom(self, options: CompilerParameters, compilationUnit: CodeCompileUnit) -> CompilerResults: ...
    def CompileAssemblyFromDomBatch(self, options: CompilerParameters, compilationUnits: Set(CodeCompileUnit)) -> CompilerResults: ...
    def CompileAssemblyFromFile(self, options: CompilerParameters, fileName: str) -> CompilerResults: ...
    def CompileAssemblyFromFileBatch(self, options: CompilerParameters, fileNames: Set(str)) -> CompilerResults: ...
    def CompileAssemblyFromSource(self, options: CompilerParameters, source: str) -> CompilerResults: ...
    def CompileAssemblyFromSourceBatch(self, options: CompilerParameters, sources: Set(str)) -> CompilerResults: ...


class ICodeGenerator:
    def CreateEscapedIdentifier(self, value: str) -> str: ...
    def CreateValidIdentifier(self, value: str) -> str: ...
    def GenerateCodeFromCompileUnit(self, e: CodeCompileUnit, w: TextWriter, o: CodeGeneratorOptions) -> None: ...
    def GenerateCodeFromExpression(self, e: CodeExpression, w: TextWriter, o: CodeGeneratorOptions) -> None: ...
    def GenerateCodeFromNamespace(self, e: CodeNamespace, w: TextWriter, o: CodeGeneratorOptions) -> None: ...
    def GenerateCodeFromStatement(self, e: CodeStatement, w: TextWriter, o: CodeGeneratorOptions) -> None: ...
    def GenerateCodeFromType(self, e: CodeTypeDeclaration, w: TextWriter, o: CodeGeneratorOptions) -> None: ...
    def GetTypeOutput(self, type: CodeTypeReference) -> str: ...
    def IsValidIdentifier(self, value: str) -> bool: ...
    def Supports(self, supports: GeneratorSupport) -> bool: ...
    def ValidateIdentifier(self, value: str) -> None: ...


class ICodeParser:
    def Parse(self, codeStream: TextReader) -> CodeCompileUnit: ...


class LanguageOptions:
    #None = 0
    CaseInsensitive = 1


class TempFileCollection(Object):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, tempDir: str): ...
    @overload
    def __init__(self, tempDir: str, keepFiles: bool): ...
    @overload
    def AddExtension(self, fileExtension: str) -> str: ...
    @overload
    def AddExtension(self, fileExtension: str, keepFile: bool) -> str: ...
    def AddFile(self, fileName: str, keepFile: bool) -> None: ...
    def CopyTo(self, fileNames: Set(str), start: int) -> None: ...
    def Delete(self) -> None: ...
    @property
    def BasePath(self) -> str: ...
    @property
    def Count(self) -> int: ...
    @property
    def KeepFiles(self) -> bool: ...
    @property
    def TempDir(self) -> str: ...
    def GetEnumerator(self) -> IEnumerator: ...
    @KeepFiles.setter
    def KeepFiles(self, value: bool) -> None: ...
