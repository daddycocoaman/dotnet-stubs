from typing import Tuple, Set, Iterable, List


class ITargetAwareCodeDomProvider:
    def SupportsProperty(self, type: Type, propertyName: str, isWritable: bool) -> bool: ...


class StronglyTypedResourceBuilder(Object):
    @overload
    def Create(resourceList: IDictionary, baseName: str, generatedCodeNamespace: str, codeProvider: CodeDomProvider, internalClass: bool) -> Tuple[CodeCompileUnit, Set(str)]: ...
    @overload
    def Create(resxFile: str, baseName: str, generatedCodeNamespace: str, codeProvider: CodeDomProvider, internalClass: bool) -> Tuple[CodeCompileUnit, Set(str)]: ...
    @overload
    def Create(resourceList: IDictionary, baseName: str, generatedCodeNamespace: str, resourcesNamespace: str, codeProvider: CodeDomProvider, internalClass: bool) -> Tuple[CodeCompileUnit, Set(str)]: ...
    @overload
    def Create(resxFile: str, baseName: str, generatedCodeNamespace: str, resourcesNamespace: str, codeProvider: CodeDomProvider, internalClass: bool) -> Tuple[CodeCompileUnit, Set(str)]: ...
    def VerifyResourceName(key: str, provider: CodeDomProvider) -> str: ...
