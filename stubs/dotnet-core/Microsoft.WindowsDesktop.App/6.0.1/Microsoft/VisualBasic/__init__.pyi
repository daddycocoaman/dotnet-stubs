from typing import Tuple, Set, Iterable, List


class VBCodeProvider:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, providerOptions: IDictionary): ...
    def GenerateCodeFromMember(self, member: CodeTypeMember, writer: TextWriter, options: CodeGeneratorOptions) -> None: ...
    @property
    def FileExtension(self) -> str: ...
    @property
    def LanguageOptions(self) -> LanguageOptions: ...
    def GetConverter(self, type: Type) -> TypeConverter: ...
